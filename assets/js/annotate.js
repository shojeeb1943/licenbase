/**
 * Local, dependency-free visual feedback tool for dev use only.
 * Click "Annotate" (bottom-right), then click any element on the page,
 * type a note, and it's copied to your clipboard as AI-ready markdown.
 * Gated to localhost/file:// so it never runs in production.
 */
(function () {
  var isDev = ['localhost', '127.0.0.1', ''].indexOf(location.hostname) !== -1 || location.protocol === 'file:';
  if (!isDev) return;

  var notes = [];
  var active = false;
  var hoverEl = null;

  var style = document.createElement('style');
  style.textContent =
    '#lb-annotate-toggle{position:fixed;bottom:16px;right:16px;z-index:99999;background:#111;color:#fff;' +
    'font:600 13px system-ui,sans-serif;padding:8px 14px;border-radius:999px;cursor:pointer;box-shadow:0 2px 10px rgba(0,0,0,.3);}' +
    '#lb-annotate-toggle.on{background:#e11d48;}' +
    '.lb-annotate-hover{outline:2px solid #e11d48!important;outline-offset:2px;cursor:crosshair!important;}' +
    '#lb-annotate-box{position:absolute;z-index:100000;background:#fff;border:1px solid #ccc;border-radius:8px;' +
    'box-shadow:0 4px 20px rgba(0,0,0,.25);padding:8px;width:260px;font:13px system-ui,sans-serif;}' +
    '#lb-annotate-box textarea{width:100%;height:60px;box-sizing:border-box;font:inherit;padding:6px;' +
    'border:1px solid #ddd;border-radius:6px;resize:vertical;}' +
    '#lb-annotate-box .lb-row{display:flex;gap:6px;margin-top:6px;justify-content:flex-end;}' +
    '#lb-annotate-box button{font:600 12px system-ui,sans-serif;padding:5px 10px;border-radius:6px;border:0;cursor:pointer;}' +
    '#lb-annotate-box .lb-save{background:#111;color:#fff;}' +
    '#lb-annotate-box .lb-cancel{background:#eee;}' +
    '#lb-annotate-toast{position:fixed;bottom:56px;right:16px;z-index:99999;background:#111;color:#fff;' +
    'font:13px system-ui,sans-serif;padding:6px 12px;border-radius:6px;opacity:0;transition:opacity .2s;}' +
    '#lb-annotate-toast.show{opacity:1;}';
  document.head.appendChild(style);

  var toggle = document.createElement('div');
  toggle.id = 'lb-annotate-toggle';
  toggle.textContent = 'Annotate (' + 0 + ')';
  document.body.appendChild(toggle);

  var toast = document.createElement('div');
  toast.id = 'lb-annotate-toast';
  document.body.appendChild(toast);

  function showToast(msg) {
    toast.textContent = msg;
    toast.className = 'show';
    setTimeout(function () { toast.className = ''; }, 1400);
  }

  function selectorFor(el) {
    if (el.id) return '#' + el.id;
    var parts = [];
    while (el && el.nodeType === 1 && el !== document.body) {
      var part = el.tagName.toLowerCase();
      if (el.className && typeof el.className === 'string') {
        part += '.' + el.className.trim().split(/\s+/).slice(0, 2).join('.');
      }
      var siblings = el.parentNode ? Array.prototype.indexOf.call(el.parentNode.children, el) + 1 : 1;
      part += ':nth-child(' + siblings + ')';
      parts.unshift(part);
      el = el.parentElement;
    }
    return parts.join(' > ');
  }

  function toMarkdown() {
    return notes.map(function (n, i) {
      return '### Annotation ' + (i + 1) + '\n' +
        '**Selector:** `' + n.selector + '`\n' +
        '**Element text:** ' + (n.text ? '"' + n.text + '"' : '(none)') + '\n' +
        '**Feedback:** ' + n.note + '\n';
    }).join('\n');
  }

  function copyAll() {
    if (!notes.length) return;
    var md = toMarkdown();
    navigator.clipboard.writeText(md).then(function () {
      showToast('Copied ' + notes.length + ' annotation(s)');
    });
  }

  function closeBox() {
    var box = document.getElementById('lb-annotate-box');
    if (box) box.remove();
  }

  function openBox(el, x, y) {
    closeBox();
    var box = document.createElement('div');
    box.id = 'lb-annotate-box';
    box.style.left = x + window.scrollX + 'px';
    box.style.top = y + window.scrollY + 'px';
    box.innerHTML =
      '<textarea placeholder="What should change here?"></textarea>' +
      '<div class="lb-row"><button class="lb-cancel">Cancel</button><button class="lb-save">Save</button></div>';
    document.body.appendChild(box);
    var textarea = box.querySelector('textarea');
    textarea.focus();

    box.querySelector('.lb-cancel').onclick = closeBox;
    box.querySelector('.lb-save').onclick = function () {
      var note = textarea.value.trim();
      if (!note) return closeBox();
      notes.push({
        selector: selectorFor(el),
        text: (el.textContent || '').trim().slice(0, 60),
        note: note,
      });
      toggle.textContent = 'Annotate (' + notes.length + ')';
      closeBox();
      copyAll();
    };
  }

  function onMouseOver(e) {
    if (hoverEl) hoverEl.classList.remove('lb-annotate-hover');
    hoverEl = e.target;
    hoverEl.classList.add('lb-annotate-hover');
  }

  function onClick(e) {
    if (e.target === toggle || e.target.closest('#lb-annotate-box')) return;
    e.preventDefault();
    e.stopPropagation();
    openBox(e.target, e.clientX, e.clientY);
  }

  toggle.onclick = function () {
    active = !active;
    toggle.classList.toggle('on', active);
    if (active) {
      document.addEventListener('mouseover', onMouseOver);
      document.addEventListener('click', onClick, true);
    } else {
      document.removeEventListener('mouseover', onMouseOver);
      document.removeEventListener('click', onClick, true);
      if (hoverEl) hoverEl.classList.remove('lb-annotate-hover');
      closeBox();
    }
  };
})();
