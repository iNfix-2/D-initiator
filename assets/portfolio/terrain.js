/* An isometric height field. Draw back-to-front so the near ridges occlude the far mesh. */
(function () {
  function terrain(seed) {
    let state = seed;
    function random() { state = (Math.imul(1664525, state) + 1013904223) >>> 0; return state / 4294967296; }
    const phase = random() * 6.28;
    const offset = random() * 0.32 - 0.16;
    const summits = [[-.43 + offset, .08, .87], [.11, -.16 + offset, 1.09], [.46, .01, .69], [-.03, .31, .64]];
    function height(x, y) {
      const points = summits.map(([a,b,h]) => h * Math.exp(-3.65 * Math.hypot(x-a,(y-b)*1.19)));
      const peak = Math.max(...points) + .155 * points.reduce((sum,p) => sum+p,0);
      const ridges = .09*Math.sin(10*x + 5*y + phase) + .065*Math.cos(17*y - 5*x) + .04*Math.sin(29*x + 16*y+phase) + .028*Math.cos(39*y - 8*x);
      const edge = Math.min(1, 4.8*(1-Math.max(Math.abs(x),Math.abs(y))));
      return Math.max(0, peak*(1+ridges*2.5) - .052) * edge;
    }
    const n = 62;
    const heights = Array.from({length:n+1}, (_,j)=>Array.from({length:n+1}, (_,i)=>height(i/n*2-1,j/n*2-1)));
    const scale = 162/Math.max(...heights.flat());
    const rows = Array.from({length:n+1},(_,j)=>Array.from({length:n+1},(_,i)=>{
      const x = i/n*2-1, y=j/n*2-1, h=heights[j][i];
      return [(280+x*153-y*93).toFixed(2),(208+x*31+y*56-h*scale).toFixed(2),h];
    }));
    let svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 324" fill="none">';
    for(let j=0;j<n;j++){
      const a=rows[j], b=rows[j+1], pt=p=>p[0]+','+p[1];
      const avg=a.reduce((s,p)=>s+p[2],0)/a.length;
      svg+='<path d="M'+a.map(pt).join(' L')+' L'+b.slice().reverse().map(pt).join(' L')+' Z" fill="#0b160e"/>';
      const opacity=(.52+Math.min(.46,avg*1.5)).toFixed(2);
      svg+='<path d="M'+a.map(pt).join(' L')+'" stroke="#c2ff79" stroke-width=".88" opacity="'+opacity+'"/>';
      let cross='';
      for(let i=0;i<=n;i++) cross+='M'+pt(a[i])+'L'+pt(b[i]);
      svg+='<path d="'+cross+'" stroke="#94e67b" stroke-width=".66" opacity="'+opacity+'"/>';
    }
    return svg+'<path d="M'+rows[n].map(p=>p[0]+','+p[1]).join(' L')+'" stroke="#baf38d" stroke-width=".9"/></svg>';
  }
  if(typeof module !== 'undefined' && module.exports) module.exports=terrain;
  else {
    const button=document.getElementById('regenerate');
    if(!button) return;
    const label=document.getElementById('seed');
    let seed=2408;
    button.hidden=false;
    button.addEventListener('click',()=>{
      seed=1000+(seed*1847+3943)%9000;
      document.getElementById('mesh').innerHTML=terrain(seed);
      label.textContent='SEED '+seed;
    });
  }
})();
