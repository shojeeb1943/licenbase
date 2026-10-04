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
  /* --lb-hdr = space above the app shell, so the shell fills exactly the rest of the viewport (one scrollbar) */
  function size(){var s=d.querySelector('div.bg-background.flex[class*="dvh"]'),t=d.querySelector('.lb-topbar'),h=s?s.getBoundingClientRect().top+scrollY:t&&t.getBoundingClientRect().height;h!=null&&d.documentElement.style.setProperty('--lb-hdr',h+'px')}
  var l=d.createElement('link');l.rel='stylesheet';l.href='/assets/css/tools-footer.css?v=2';d.head.appendChild(l);
  addEventListener('resize',size);addEventListener('load',size);size();
  var hd=d.getElementById('lb-tools-header');window.ResizeObserver&&hd&&new ResizeObserver(size).observe(hd);
  /* lazy Tawk live chat, same widget as the rest of the site (generate_pages.py) */
  function tawk(){if(window.tawkLoaded)return;window.tawkLoaded=true;window.Tawk_API=window.Tawk_API||{};window.Tawk_LoadStart=new Date();var s=d.createElement('script');s.async=true;s.src='https://embed.tawk.to/6aa54c1357bdd83448ee36a5/1k2ar2bta';s.charset='UTF-8';s.setAttribute('crossorigin','*');d.head.appendChild(s)}
  ['scroll','keydown','touchstart','mousemove','click'].forEach(function(e){addEventListener(e,tawk,{once:true,passive:true})});
  setTimeout(tawk,3500);
})();
