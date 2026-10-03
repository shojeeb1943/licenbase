(function(){
  var d=document;
  function closeAll(except){d.querySelectorAll('.lb-topbar .lb-drop').forEach(function(x){if(x!==except){x.classList.remove('is-open');var b=x.querySelector('[data-drop]');b&&b.setAttribute('aria-expanded','false')}})}
  d.addEventListener('click',function(e){
    var b=e.target.closest&&e.target.closest('.lb-topbar [data-drop]');
    if(!b){closeAll();return}
    var x=b.closest('.lb-drop'),o=x.classList.toggle('is-open');b.setAttribute('aria-expanded',o);closeAll(x);e.stopPropagation()});
  d.addEventListener('mouseover',function(e){
    var x=e.target.closest&&e.target.closest('.lb-topbar .lb-drop');
    if(x){x.classList.add('is-open');closeAll(x)}else if(e.target.closest&&e.target.closest('.lb-topbar'))closeAll()});
  d.addEventListener('keydown',function(e){e.key==='Escape'&&closeAll()});
  function size(){var t=d.querySelector('.lb-topbar');t&&d.documentElement.style.setProperty('--lb-hdr',t.getBoundingClientRect().height+'px')}
  var l=d.createElement('link');l.rel='stylesheet';l.href='/assets/css/tools-footer.css?v=2';d.head.appendChild(l);
  addEventListener('resize',size);addEventListener('load',size);size();
})();
