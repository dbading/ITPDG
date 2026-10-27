#!/usr/bin/env python3
"""Interaktive Fouriertransformation zu Tut2, Aufgaben 5, 7 und 8.

Einmal ausführen: python3 fouriertransformation_interaktiv.py
Ergebnis: fouriertransformation_interaktiv.html

Keine Webserver oder JavaScript-Bibliotheken nötig. Python berechnet die
Funktionswerte und exakten Fourier-Transformierten vor; der Slider ändert die
Frequenz und das HTML-Canvas zeigt Integrand sowie numerischen Integrationsweg.

Konvention: F[f](omega) = integral_R f(t) exp(-i*omega*t) dt.
"""

from pathlib import Path
import json
import numpy as np

N_TIME = 1401
N_FREQ = 641  # Frequenzen zwischen -12 und 12, bzw. -18 und 18
OUTPUT = Path(__file__).with_name("fouriertransformation_interaktiv.html")


def make_examples():
    sqrt_pi = np.sqrt(np.pi)
    # f(t) wird inklusive komplexem Anteil gesampelt. F(w) ist die analytische
    # Fourier-Transformierte aus den Lösungen von Tut2.pdf.
    return [
        dict(id="5a", task="Aufgabe 5 · 1", title="Einseitige Exponentialfunktion",
             function="f(t) = e<sup>−t</sup> · 1<sub>[0,∞)</sub>(t)",
             transform="f̂(ω) = 1 / (1 + iω)",
             note="Der exponentielle Abfall im Zeitbereich erzeugt ein komplexes, mit |ω| abklingendes Spektrum.",
             tlim=(-5, 9), wlim=(-12, 12),
             f=lambda t: np.exp(-np.maximum(t, 0)) * (t >= 0),
             F=lambda w: 1/(1+1j*w)),
        dict(id="5b", task="Aufgabe 5 · 2", title="Dreiecksfunktion",
             function="f(t) = max(1 − |t|, 0)",
             transform="f̂(ω) = 2(1 − cos ω) / ω², &nbsp; f̂(0) = 1",
             note="Gerade und reelle Funktion: Die Transformierte ist ebenfalls reell und gerade. Beobachte ihre Nullstellen.",
             tlim=(-3, 3), wlim=(-18, 18),
             f=lambda t: np.maximum(1 - np.abs(t), 0),
             F=lambda w: np.sinc(w/(2*np.pi))**2),
        dict(id="7a", task="Aufgabe 7 · 1", title="Zeitverschiebung um 3",
             function="f(t) = e<sup>−(t−3)</sup> · 1<sub>[3,∞)</sub>(t)",
             transform="f̂(ω) = e<sup>−3iω</sup> / (1 + iω)",
             note="Zeitverschiebung verändert die Phase der Transformierten, nicht aber ihren Betrag.",
             tlim=(-3, 12), wlim=(-12, 12),
             f=lambda t: np.exp(-np.maximum(t-3, 0)) * (t >= 3),
             F=lambda w: np.exp(-3j*w)/(1+1j*w)),
        dict(id="7b", task="Aufgabe 7 · 2", title="Modulation mit e⁻²ⁱᵗ",
             function="f(t) = e<sup>−(1+2i)t</sup> · 1<sub>[0,∞)</sub>(t)",
             transform="f̂(ω) = 1 / (1 + i(ω + 2))",
             note="Multiplikation mit e⁻²ⁱᵗ verschiebt das Spektrum um 2 nach links. Hier ist bereits f komplexwertig.",
             tlim=(-5, 9), wlim=(-12, 12),
             f=lambda t: np.exp(-(1+2j)*np.maximum(t, 0)) * (t >= 0),
             F=lambda w: 1/(1+1j*(w+2))),
        dict(id="7c", task="Aufgabe 7 · 3", title="Dilatation f(t) = g(2t)",
             function="f(t) = e<sup>−2t</sup> · 1<sub>[0,∞)</sub>(t)",
             transform="f̂(ω) = 1 / (2 + iω)",
             note="Schnellerer Abfall in t: Das Spektrum wird breiter und in der Höhe kleiner.",
             tlim=(-3, 6), wlim=(-14, 14),
             f=lambda t: np.exp(-2*np.maximum(t, 0)) * (t >= 0),
             F=lambda w: 1/(2+1j*w)),
        dict(id="7d", task="Aufgabe 7 · 4", title="Zweiseitige Exponentialfunktion",
             function="f(t) = e<sup>−|t|</sup>",
             transform="f̂(ω) = 2 / (1 + ω²)",
             note="Reell und gerade: Imaginärteil der Fourier-Transformierten ist überall null.",
             tlim=(-8, 8), wlim=(-12, 12),
             f=lambda t: np.exp(-np.abs(t)),
             F=lambda w: 2/(1+w*w)),
        dict(id="8a", task="Aufgabe 8 · 1", title="Verschobene Gaußfunktion",
             function="f(t) = e<sup>−2(t−2)²</sup>",
             transform="f̂(ω) = √(π/2) · e<sup>−ω²/8 − 2iω</sup>",
             note="Auch die Fourier-Transformierte einer Gaußfunktion ist gaußförmig; die Verschiebung erzeugt einen Phasenfaktor.",
             tlim=(-2, 6), wlim=(-10, 10),
             f=lambda t: np.exp(-2*(t-2)**2),
             F=lambda w: np.sqrt(np.pi/2)*np.exp(-w*w/8-2j*w)),
        dict(id="8b", task="Aufgabe 8 · 2", title="Gaußfunktion mal t",
             function="f(t) = t · e<sup>−t²</sup>",
             transform="f̂(ω) = −i(ω/2)√π · e<sup>−ω²/4</sup>",
             note="f ist reell und ungerade. Die Transformierte ist deshalb rein imaginär und ungerade.",
             tlim=(-4, 4), wlim=(-10, 10),
             f=lambda t: t*np.exp(-t*t),
             F=lambda w: -1j*(w/2)*sqrt_pi*np.exp(-w*w/4)),
        dict(id="8c", task="Aufgabe 8 · 3", title="Verschobener Vorfaktor",
             function="f(t) = (t − 1) · e<sup>−t²</sup>",
             transform="f̂(ω) = −√π(1 + iω/2) · e<sup>−ω²/4</sup>",
             note="Mit Linearität zerfällt die Transformierte in den Anteil von t·e⁻ᵗ² und den von −e⁻ᵗ².",
             tlim=(-4, 4), wlim=(-10, 10),
             f=lambda t: (t-1)*np.exp(-t*t),
             F=lambda w: -sqrt_pi*(1+1j*w/2)*np.exp(-w*w/4)),
    ]


def serialize():
    examples = []
    for d in make_examples():
        x = np.linspace(*d["tlim"], N_TIME)
        w = np.linspace(*d["wlim"], N_FREQ)
        f = np.asarray(d["f"](x), dtype=np.complex128)
        F = np.asarray(d["F"](w), dtype=np.complex128)
        # Gemeinsame Achsgrenzen sorgen für vergleichbare Frames während des Ziehens.
        f_peak = float(np.max(np.abs(f)))
        y_signal = max(f_peak*1.18, 0.08)
        spectrum_low = float(min(0, F.real.min(), F.imag.min()))
        spectrum_high = float(max(0, np.abs(F).max(), F.real.max(), F.imag.max()))
        span = max(spectrum_high-spectrum_low, 0.2)
        spectrum_low -= 0.09*span
        spectrum_high += 0.09*span
        dt = float(x[1] - x[0])
        L1 = float(np.trapezoid(np.abs(f), x))
        # Für jeden Frequenzwert kann der partielle Integrationspfad betragsmäßig
        # höchstens das L1-Integral erreichen.
        zbound = max(1.20*L1, 0.15)
        examples.append({
            "id":d["id"], "task":d["task"], "title":d["title"],
            "function":d["function"], "transform":d["transform"], "note":d["note"],
            "x":np.round(x, 7).tolist(), "fr":np.round(f.real, 7).tolist(),
            "fi":np.round(f.imag, 7).tolist(),
            "w":np.round(w, 7).tolist(), "Fr":np.round(F.real, 7).tolist(),
            "Fi":np.round(F.imag, 7).tolist(), "Fm":np.round(abs(F), 7).tolist(),
            "timeY": [-y_signal, y_signal],
            "freqY": [spectrum_low, spectrum_high],
            "zY": [-zbound, zbound], "dt":dt,
            "complexSignal":bool(np.max(np.abs(f.imag)) > 1e-10),
        })
    return examples


HTML = r'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light">
<title>Fouriertransformation · Interaktive Mathematik</title>
<style>
:root { --ink:#16233c; --muted:#637087; --line:#dfe5ee; --page:#f6f8fc; --surface:#fff;
        --accent:#355ed7; --teal:#138b86; --orange:#d17a3e; --purple:#7e58b8; --grid:#e8ecf2; }
*{ box-sizing:border-box; }
body{ margin:0; padding:clamp(12px,3vw,32px); color:var(--ink); background:var(--page);
      font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; line-height:1.5; }
main{max-width:1080px; margin:0 auto; }
header{ margin:0 0 20px; }
.eyebrow{color:var(--accent);font-size:12px;font-weight:800;letter-spacing:.13em;text-transform:uppercase;}
h1{font-size:clamp(25px,3.6vw,40px);line-height:1.14;letter-spacing:-.035em;margin:8px 0 10px;}
.lead{color:var(--muted);max-width:770px;margin:0;font-size:15px;}
.card{ background:var(--surface); border:1px solid var(--line); border-radius:17px;box-shadow:0 6px 24px rgba(37,54,85,.035); }
.control-card{ padding:clamp(14px,2.5vw,22px); margin-bottom:16px; }
.control-grid{display:grid;grid-template-columns:minmax(240px,1fr) minmax(260px,1.6fr) auto;gap:17px;align-items:end;}
label{font-size:13px;font-weight:750;display:block;margin-bottom:8px;}
select,button{ font:inherit; }
select{width:100%;border:1px solid var(--line);background:#fff;color:var(--ink);padding:11px 12px;
       border-radius:10px;min-height:46px;outline-offset:2px; }
.range-row{display:flex;align-items:center;gap:12px;min-height:46px;}
input[type=range]{width:100%;min-width:0;accent-color:var(--accent);cursor:pointer;}
.omega{width:76px;flex-shrink:0;text-align:right;font-variant-numeric:tabular-nums;font-size:17px;font-weight:800;color:var(--accent);}
button{border:1px solid var(--line);padding:10px 16px;min-height:46px;background:#fff;
       border-radius:10px;color:var(--ink);cursor:pointer;white-space:nowrap;}
button:hover{background:#edf2ff;border-color:#ccd7f6;}
.formula-row{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:17px;}
.formula{padding:12px 14px;border-radius:10px;background:#f7f9fd;min-height:76px;}
.formula span{display:block;font-size:11px;color:var(--muted);font-weight:800;letter-spacing:.07em;text-transform:uppercase;margin-bottom:5px;}
.formula .math{font-family:Georgia,"Times New Roman",serif;font-size:17px;line-height:1.8;overflow-wrap:anywhere;}
.note{font-size:13px;color:var(--muted);margin:13px 1px 0;}
.plots{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;}
.plot{padding:17px 15px 13px;min-width:0;}
.plot h2{font-size:16px;line-height:1.2;margin:0 0 3px;letter-spacing:-.015em;}
.plot .sub{font-size:12px;color:var(--muted);margin:0 0 9px;min-height:17px;}
canvas{display:block;width:100%;height:230px;touch-action:pan-y;}
.legend{display:flex;flex-wrap:wrap;justify-content:center;gap:13px;font-size:11px;color:var(--muted);margin-top:8px;}
.legend span{display:flex;align-items:center;gap:5px;}
.swatch{width:17px;height:3px;display:inline-block;border-radius:4px;}
.teal{background:var(--teal)}.orange{background:var(--orange)}.purple{background:var(--purple)}
.blue{background:var(--accent)}.grey{background:#9aa5b6}
.foot{margin:16px 1px 0;color:var(--muted);font-size:12px;line-height:1.65;}
.numeric{font-variant-numeric:tabular-nums;}
@media(max-width:850px){.control-grid{grid-template-columns:1fr 1fr;}.play-container{grid-column:1/-1;}button{width:100%;}}
@media(max-width:700px){.plots{grid-template-columns:1fr}.formula-row{grid-template-columns:1fr}}
@media(max-width:540px){.control-grid{grid-template-columns:1fr}.play-container{grid-column:auto}}
@media(prefers-reduced-motion:reduce){*{scroll-behavior:auto!important}}
</style>
</head>
<body>
<main>
  <header>
    <div class="eyebrow">TU Berlin · ITPDG · Tutorium 2 · Aufgaben 5, 7 und 8</div>
    <h1>Die Fouriertransformation erkunden</h1>
    <p class="lead">Wähle eine Funktion und verändere die Frequenz ω. Die Kurven zeigen, wie aus dem Schwingungsintegral ein Punkt der Fourier-Transformierten entsteht.</p>
  </header>
  <section class="card control-card" aria-label="Steuerung">
    <div class="control-grid">
      <div><label for="example">Funktion aus dem Aufgabenblatt</label><select id="example"></select></div>
      <div><label for="slider">Frequenz ω <span class="numeric" id="omega-description"></span></label>
           <div class="range-row"><input id="slider" type="range" step="1" aria-label="Frequenz">
             <output class="omega" id="omega">0,00</output></div></div>
      <div class="play-container"><button id="play" type="button" aria-label="Animation abspielen">▶ Abspielen</button></div>
    </div>
    <div class="formula-row">
      <div class="formula"><span>Ausgangsfunktion</span><div class="math" id="function"></div></div>
      <div class="formula"><span>Fourier-Transformierte</span><div class="math" id="transform"></div></div>
    </div>
    <p class="note" id="note"></p>
  </section>
  <section class="plots" aria-label="Interaktive Diagramme">
    <article class="card plot"><h2>1 · Funktion im Zeitbereich</h2><p class="sub">f(t)</p>
      <canvas id="time" aria-label="Graph der Ausgangsfunktion"></canvas>
      <div class="legend" id="time-legend"><span><i class="swatch teal"></i>Re f(t)</span><span class="im"><i class="swatch orange"></i>Im f(t)</span></div>
    </article>
    <article class="card plot"><h2>2 · Fourier-Spektrum</h2><p class="sub">Die senkrechte Linie markiert die gewählte Frequenz ω.</p>
      <canvas id="frequency" aria-label="Realteil, Imaginärteil und Betrag der Fourier-Transformierten"></canvas>
      <div class="legend"><span><i class="swatch teal"></i>Re f̂</span><span><i class="swatch orange"></i>Im f̂</span><span><i class="swatch purple"></i>|f̂|</span></div>
    </article>
    <article class="card plot"><h2>3 · Rotierender Integrand</h2><p class="sub">f(t) · e<sup>−iωt</sup> für die gewählte Frequenz</p>
      <canvas id="integrand" aria-label="Realteil und Imaginärteil des Fourier-Integranden"></canvas>
      <div class="legend"><span><i class="swatch teal"></i>Realteil</span><span><i class="swatch orange"></i>Imaginärteil</span></div>
    </article>
    <article class="card plot"><h2>4 · Aufbau des Fourier-Integrals</h2><p class="sub">Γ<sub>ω</sub>(T) = ∫<sub>tₘᵢₙ</sub><sup>T</sup> f(t)e<sup>−iωt</sup>dt</p>
      <canvas id="complex" aria-label="Partieller Integrationspfad in der komplexen Ebene"></canvas>
      <div class="legend" id="values"><span><i class="swatch blue"></i>Endpunkt des Integrals</span></div>
    </article>
  </section>
  <p class="foot">Verwendet wird die Konvention f̂(ω) = ∫<sub>−∞</sub><sup>∞</sup> f(t)e<sup>−iωt</sup>dt (ohne Normierungsfaktor). Das Spektrum zeigt die exakten Formeln aus dem Aufgabenblatt. Der Integrationsweg wird numerisch über einen endlichen Zeitbereich angenähert. Alle Daten werden von Python vorbereitet; die Seite funktioniert auch offline.</p>
</main>
<script>
'use strict';
const examples = __DATA__;
const el = id => document.getElementById(id);
const colors = {teal:'#138b86', orange:'#d17a3e', purple:'#7e58b8', blue:'#355ed7', grey:'#a4adbd', grid:'#e8ecf2', ink:'#536078'};
const sel = el('example'), slider = el('slider');
for (const d of examples) {
  const option = document.createElement('option');
  option.value = d.id; option.textContent = d.task + ' · ' + d.title; sel.appendChild(option);
}
let active=examples[0], playTimer=null;
const plotIds = ['time','frequency','integrand','complex'];
const fmt = v => Math.abs(v)<1e-9 ? '0' : (Math.abs(v)<10 ? v.toFixed(2) : v.toFixed(1)).replace('.',',');
function settings(canvas){
  const cssWidth = Math.max(200, canvas.getBoundingClientRect().width);
  const cssHeight = 230;
  const dpr = Math.min(window.devicePixelRatio||1, 2);
  canvas.width=Math.round(cssWidth*dpr);
  canvas.height=Math.round(cssHeight*dpr);
  const ctx=canvas.getContext('2d');
  ctx.setTransform(dpr,0,0,dpr,0,0);
  return {ctx, W:cssWidth, H:cssHeight, L:48, R:15, T:12, B:30};
}
function tickStep(x){
  const rough=x/4; const power=Math.pow(10,Math.floor(Math.log10(Math.max(rough,1e-12))));
  for(const k of [1,2,2.5,5,10]) if(k*power>=rough) return k*power;
  return 10*power;
}
function frame(canvas,x0,x1,y0,y1,xName='t',yName=''){
  const p=settings(canvas), {ctx,W,H,L,R,T,B}=p;
  const X=x => L+(x-x0)/(x1-x0)*(W-L-R);
  const Y=y => H-B-(y-y0)/(y1-y0)*(H-T-B);
  ctx.clearRect(0,0,W,H);
  ctx.lineWidth=1;ctx.font='11px system-ui,sans-serif';
  const dx=tickStep(x1-x0), dy=tickStep(y1-y0);
  let count=0;
  for(let x=Math.ceil((x0-1e-10)/dx)*dx; x<=x1+1e-8 && count<30; x+=dx,count++){
    const xp=X(x);ctx.strokeStyle=colors.grid;ctx.beginPath();ctx.moveTo(xp,T);ctx.lineTo(xp,H-B);ctx.stroke();
    ctx.textAlign='center';ctx.fillStyle=colors.ink;ctx.fillText(fmt(x),xp,H-11);
  }
  count=0;
  for(let y=Math.ceil((y0-1e-10)/dy)*dy;y<=y1+1e-8 && count<30;y+=dy,count++){
    const yp=Y(y);ctx.strokeStyle=colors.grid;ctx.beginPath();ctx.moveTo(L,yp);ctx.lineTo(W-R,yp);ctx.stroke();
    ctx.textAlign='right';ctx.fillStyle=colors.ink;ctx.fillText(fmt(y),L-7,yp+3);
  }
  ctx.strokeStyle='#95a2b5';ctx.lineWidth=1.1;
  if(x0<=0&&x1>=0){ctx.beginPath();ctx.moveTo(X(0),T);ctx.lineTo(X(0),H-B);ctx.stroke();}
  if(y0<=0&&y1>=0){ctx.beginPath();ctx.moveTo(L,Y(0));ctx.lineTo(W-R,Y(0));ctx.stroke();}
  ctx.fillStyle=colors.ink;ctx.font='12px system-ui,sans-serif';ctx.textAlign='right';
  ctx.fillText(xName,W-10,H-12);
  if(yName){ctx.textAlign='left';ctx.fillText(yName, L+5,T+11);}
  ctx.save();ctx.beginPath();ctx.rect(L,T,W-L-R,H-T-B);ctx.clip();
  return {...p,X,Y,release:()=>ctx.restore()};
}
function line(g, xs, ys, color, width=2, stride=1, dashed=false){
  const c=g.ctx;c.beginPath();c.strokeStyle=color;c.lineWidth=width;
  if(dashed)c.setLineDash([5,5]);else c.setLineDash([]);
  for(let i=0;i<xs.length;i+=stride){const x=g.X(xs[i]),y=g.Y(ys[i]); if(i===0)c.moveTo(x,y);else c.lineTo(x,y);}
  if((xs.length-1)%stride!==0)c.lineTo(g.X(xs.at(-1)),g.Y(ys.at(-1)));
  c.stroke();c.setLineDash([]);
}
function timePlot(){
  const d=active, x=d.x, g=frame(el('time'),x[0],x.at(-1),...d.timeY);
  line(g,x,d.fr,colors.teal,2.5);
  if(d.complexSignal)line(g,x,d.fi,colors.orange,2.1);
  g.release();
}
function frequencyPlot(i){
  const d=active,w=d.w;
  const g=frame(el('frequency'),w[0],w.at(-1),...d.freqY,'ω');
  line(g,w,d.Fm,colors.purple,2.6);
  line(g,w,d.Fr,colors.teal,2.1);
  line(g,w,d.Fi,colors.orange,2.1);
  const selected=w[i];const c=g.ctx;
  c.lineWidth=1.4;c.strokeStyle=colors.blue;c.setLineDash([4,4]);
  c.beginPath();c.moveTo(g.X(selected),g.T);c.lineTo(g.X(selected),g.H-g.B);c.stroke();c.setLineDash([]);
  for(const [v,color] of [[d.Fm[i],colors.purple],[d.Fr[i],colors.teal],[d.Fi[i],colors.orange]]){
    c.fillStyle=color;c.beginPath();c.arc(g.X(selected),g.Y(v),3.6,0,Math.PI*2);c.fill();
  }
  g.release();
}
function integrandAndPath(i){
  const d=active,x=d.x,omega=d.w[i],N=x.length;
  const yr=new Float64Array(N),yi=new Float64Array(N);
  const zr=new Float64Array(N),zi=new Float64Array(N);
  for(let k=0;k<N;k++){
    const c=Math.cos(omega*x[k]),s=Math.sin(omega*x[k]);
    yr[k]=d.fr[k]*c+d.fi[k]*s;
    yi[k]=d.fi[k]*c-d.fr[k]*s;
    if(k>0){
      const dx=x[k]-x[k-1];
      zr[k]=zr[k-1]+dx*(yr[k]+yr[k-1])/2;
      zi[k]=zi[k-1]+dx*(yi[k]+yi[k-1])/2;
    }
  }
  const g=frame(el('integrand'),x[0],x.at(-1),...d.timeY);
  line(g,x,yr,colors.teal,2);line(g,x,yi,colors.orange,2);g.release();
  const bound=d.zY[1];
  // Identische Einheit pro Pixel auf beiden Achsen der komplexen Ebene.
  const cssWidth=Math.max(200,el('complex').getBoundingClientRect().width);
  const aspect=(cssWidth-48-15)/(230-12-30);
  const q=frame(el('complex'),-bound*aspect,bound*aspect,-bound,bound,'Re','Im');
  // Für die komplexe Kurve sind die x- und y-Daten gerade die partiellen Integrale.
  line(q,zr,zi,colors.blue,2.5);
  const c=q.ctx;
  c.fillStyle=colors.blue;c.beginPath();c.arc(q.X(zr.at(-1)),q.Y(zi.at(-1)),5,0,Math.PI*2);c.fill();
  c.fillStyle='#fff';c.beginPath();c.arc(q.X(zr.at(-1)),q.Y(zi.at(-1)),2,0,Math.PI*2);c.fill();
  q.release();
  const Ftxt=`∫ ≈ ${fmt(zr.at(-1))} ${zi.at(-1)<0?'−':'+'} ${fmt(Math.abs(zi.at(-1)))}i`;
  el('values').innerHTML='<span><i class="swatch blue"></i><span class="numeric">'+Ftxt+'</span></span>';
}
function draw(){
  const i=Number(slider.value);
  el('omega').textContent=fmt(active.w[i]);
  timePlot();frequencyPlot(i);integrandAndPath(i);
}
function stop(){if(playTimer!==null){clearInterval(playTimer);playTimer=null;}el('play').textContent='▶ Abspielen';}
function setExample(){
  stop();active=examples.find(d=>d.id===sel.value)||examples[0];
  slider.min='0';slider.max=String(active.w.length-1);slider.value=String(Math.floor((active.w.length-1)/2));
  el('function').innerHTML=active.function;
  el('transform').innerHTML=active.transform;
  el('note').textContent=active.note;
  el('time-legend').querySelector('.im').style.display=active.complexSignal?'flex':'none';
  draw();
}
sel.addEventListener('change',setExample);
slider.addEventListener('input',()=>{stop();draw();});
el('play').addEventListener('click',()=>{
  if(playTimer!==null){stop();return;}
  el('play').textContent='❚❚ Pause';
  playTimer=setInterval(()=>{
    let next=Number(slider.value)+3;
    if(next>Number(slider.max))next=0;
    slider.value=String(next);draw();
  },65);
});
let resizeQueued=false;
window.addEventListener('resize',()=>{
  if(!resizeQueued){resizeQueued=true;requestAnimationFrame(()=>{resizeQueued=false;draw();});}
});
window.addEventListener('pagehide',stop);
setExample();
</script>
</body>
</html>
'''


def main():
    data = json.dumps(serialize(), separators=(",", ":"), ensure_ascii=False, allow_nan=False)
    html = HTML.replace("__DATA__", data)
    OUTPUT.write_text(html, encoding="utf-8")
    print(f"Erstellt: {OUTPUT} ({OUTPUT.stat().st_size / 1024:.0f} KiB)")
    print("Öffne die HTML-Datei im Browser oder lade sie zu GitHub Pages hoch.")


if __name__ == "__main__":
    main()
