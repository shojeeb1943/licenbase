/* Cookie consent: Google Consent Mode v2 + Accept/Reject banner.
   Must load synchronously BEFORE the GTM snippet so the "denied" default is set first. */
(function () {
  var KEY = 'lb_consent';
  var w = window;
  w.dataLayer = w.dataLayer || [];
  function gtag() { w.dataLayer.push(arguments); }

  function get() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function set(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }
  function state(v) {
    return { ad_storage: v, analytics_storage: v, ad_user_data: v, ad_personalization: v };
  }

  var saved = get();
  var init = state(saved || 'denied');
  init.wait_for_update = 500;
  gtag('consent', 'default', init);

  function choose(v) {
    set(v);
    gtag('consent', 'update', state(v));
    var b = document.getElementById('lb-consent');
    if (b) b.remove();
  }

  function show() {
    if (document.getElementById('lb-consent')) return;
    var css = document.createElement('style');
    css.textContent =
      '#lb-consent{position:fixed;left:16px;right:16px;bottom:16px;z-index:2147483000;max-width:440px;' +
      'background:#fff;color:#111827;border:1px solid #e5e7eb;border-radius:12px;padding:16px 18px;' +
      'box-shadow:0 10px 30px rgba(17,24,39,.18);font:14px/1.5 system-ui,-apple-system,Segoe UI,Roboto,sans-serif}' +
      '#lb-consent p{margin:0 0 12px}#lb-consent a{color:#1E40AF;text-decoration:underline}' +
      '#lb-consent .lb-c-row{display:flex;gap:8px}' +
      '#lb-consent button{flex:1;cursor:pointer;border-radius:8px;padding:9px 12px;font:600 14px system-ui,sans-serif;' +
      'border:1px solid #1E40AF;background:#1E40AF;color:#fff}' +
      '#lb-consent button.lb-c-no{background:#fff;color:#1E40AF}' +
      '#lb-consent button:focus-visible{outline:2px solid #111827;outline-offset:2px}';
    document.head.appendChild(css);
    var d = document.createElement('div');
    d.id = 'lb-consent';
    d.setAttribute('role', 'dialog');
    d.setAttribute('aria-label', 'Cookie consent');
    d.innerHTML =
      '<p>We use cookies for analytics to improve LicenBase. You can accept or reject non-essential cookies. ' +
      '<a href="/privacy-policy#cookies">Learn more</a></p>' +
      '<div class="lb-c-row"><button type="button" class="lb-c-no">Reject</button>' +
      '<button type="button" class="lb-c-yes">Accept</button></div>';
    d.querySelector('.lb-c-yes').onclick = function () { choose('granted'); };
    d.querySelector('.lb-c-no').onclick = function () { choose('denied'); };
    document.body.appendChild(d);
  }

  // Footer links with data-cookie-settings (or #cookie-settings) re-open the banner.
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('[data-cookie-settings],a[href="#cookie-settings"]');
    if (!a) return;
    e.preventDefault();
    try { localStorage.removeItem(KEY); } catch (x) {}
    show();
  });

  function ready() { if (!saved) show(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', ready);
  else ready();
})();
