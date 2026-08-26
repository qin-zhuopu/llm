# Source: https://www.citrine.io

> 抓取日期: 2026-08-26

---

<!DOCTYPE html>
<html lang="en-US">
<head><meta charset="UTF-8"><script>if(navigator.userAgent.match(/MSIE|Internet Explorer/i)||navigator.userAgent.match(/Trident\/7\..*?rv:11/i)){var href=document.location.href;if(!href.match(/[?&]nowprocket/)){if(href.indexOf("?")==-1){if(href.indexOf("#")==-1){document.location.href=href+"?nowprocket=1"}else{document.location.href=href.replace("#","?nowprocket=1#")}}else{if(href.indexOf("#")==-1){document.location.href=href+"&nowprocket=1"}else{document.location.href=href.replace("#","&nowprocket=1#")}}}}</script><script>(()=>{class RocketLazyLoadScripts{constructor(){this.v="2.0.5",this.userEvents=["keydown","keyup","mousedown","mouseup","mousemove","mouseover","mouseout","touchmove","touchstart","touchend","touchcancel","wheel","click","dblclick","input"],this.attributeEvents=["onblur","onclick","oncontextmenu","ondblclick","onfocus","onmousedown","onmouseenter","onmouseleave","onmousemove","onmouseout","onmouseover","onmouseup","onmousewheel","onscroll","onsubmit"]}async t(){this.i(),this.o(),/iP(ad|hone)/.test(navigator.userAgent)&&this.h(),this.u(),this.l(this),this.m(),this.k(this),this.p(this),this._(),await Promise.all([this.R(),this.L()]),this.lastBreath=Date.now(),this.S(this),this.P(),this.D(),this.O(),this.M(),await this.C(this.delayedScripts.normal),await this.C(this.delayedScripts.defer),await this.C(this.delayedScripts.async),await this.T(),await this.F(),await this.j(),await this.A(),window.dispatchEvent(new Event("rocket-allScriptsLoaded")),this.everythingLoaded=!0,this.lastTouchEnd&&await new Promise(t=>setTimeout(t,500-Date.now()+this.lastTouchEnd)),this.I(),this.H(),this.U(),this.W()}i(){this.CSPIssue=sessionStorage.getItem("rocketCSPIssue"),document.addEventListener("securitypolicyviolation",t=>{this.CSPIssue||"script-src-elem"!==t.violatedDirective||"data"!==t.blockedURI||(this.CSPIssue=!0,sessionStorage.setItem("rocketCSPIssue",!0))},{isRocket:!0})}o(){window.addEventListener("pageshow",t=>{this.persisted=t.persisted,this.realWindowLoadedFired=!0},{isRocket:!0}),window.addEventListener("pagehide",()=>{this.onFirstUserAction=null},{isRocket:!0})}h(){let t;function e(e){t=e}window.addEventListener("touchstart",e,{isRocket:!0}),window.addEventListener("touchend",function i(o){o.changedTouches[0]&&t.changedTouches[0]&&Math.abs(o.changedTouches[0].pageX-t.changedTouches[0].pageX)<10&&Math.abs(o.changedTouches[0].pageY-t.changedTouches[0].pageY)<10&&o.timeStamp-t.timeStamp<200&&(window.removeEventListener("touchstart",e,{isRocket:!0}),window.removeEventListener("touchend",i,{isRocket:!0}),"INPUT"===o.target.tagName&&"text"===o.target.type||(o.target.dispatchEvent(new TouchEvent("touchend",{target:o.target,bubbles:!0})),o.target.dispatchEvent(new MouseEvent("mouseover",{target:o.target,bubbles:!0})),o.target.dispatchEvent(new PointerEvent("click",{target:o.target,bubbles:!0,cancelable:!0,detail:1,clientX:o.changedTouches[0].clientX,clientY:o.changedTouches[0].clientY})),event.preventDefault()))},{isRocket:!0})}q(t){this.userActionTriggered||("mousemove"!==t.type||this.firstMousemoveIgnored?"keyup"===t.type||"mouseover"===t.type||"mouseout"===t.type||(this.userActionTriggered=!0,this.onFirstUserAction&&this.onFirstUserAction()):this.firstMousemoveIgnored=!0),"click"===t.type&&t.preventDefault(),t.stopPropagation(),t.stopImmediatePropagation(),"touchstart"===this.lastEvent&&"touchend"===t.type&&(this.lastTouchEnd=Date.now()),"click"===t.type&&(this.lastTouchEnd=0),this.lastEvent=t.type,t.composedPath&&t.composedPath()[0].getRootNode()instanceof ShadowRoot&&(t.rocketTarget=t.composedPath()[0]),this.savedUserEvents.push(t)}u(){this.savedUserEvents=[],this.userEventHandler=this.q.bind(this),this.userEvents.forEach(t=>window.addEventListener(t,this.userEventHandler,{passive:!1,isRocket:!0})),document.addEventListener("visibilitychange",this.userEventHandler,{isRocket:!0})}U(){this.userEvents.forEach(t=>window.removeEventListener(t,this.userEventHandler,{passive:!1,isRocket:!0})),document.removeEventListener("visibilitychange",this.userEventHandler,{isRocket:!0}),this.savedUserEvents.forEach(t=>{(t.rocketTarget||t.target).dispatchEvent(new window[t.constructor.name](t.type,t))})}m(){const t="return false",e=Array.from(this.attributeEvents,t=>"data-rocket-"+t),i="["+this.attributeEvents.join("],[")+"]",o="[data-rocket-"+this.attributeEvents.join("],[data-rocket-")+"]",s=(e,i,o)=>{o&&o!==t&&(e.setAttribute("data-rocket-"+i,o),e["rocket"+i]=new Function("event",o),e.setAttribute(i,t))};new MutationObserver(t=>{for(const n of t)"attributes"===n.type&&(n.attributeName.startsWith("data-rocket-")||this.everythingLoaded?n.attributeName.startsWith("data-rocket-")&&this.everythingLoaded&&this.N(n.target,n.attributeName.substring(12)):s(n.target,n.attributeName,n.target.getAttribute(n.attributeName))),"childList"===n.type&&n.addedNodes.forEach(t=>{if(t.nodeType===Node.ELEMENT_NODE)if(this.everythingLoaded)for(const i of[t,...t.querySelectorAll(o)])for(const t of i.getAttributeNames())e.includes(t)&&this.N(i,t.substring(12));else for(const e of[t,...t.querySelectorAll(i)])for(const t of e.getAttributeNames())this.attributeEvents.includes(t)&&s(e,t,e.getAttribute(t))})}).observe(document,{subtree:!0,childList:!0,attributeFilter:[...this.attributeEvents,...e]})}I(){this.attributeEvents.forEach(t=>{document.querySelectorAll("[data-rocket-"+t+"]").forEach(e=>{this.N(e,t)})})}N(t,e){const i=t.getAttribute("data-rocket-"+e);i&&(t.setAttribute(e,i),t.removeAttribute("data-rocket-"+e))}k(t){Object.defineProperty(HTMLElement.prototype,"onclick",{get(){return this.rocketonclick||null},set(e){this.rocketonclick=e,this.setAttribute(t.everythingLoaded?"onclick":"data-rocket-onclick","this.rocketonclick(event)")}})}S(t){function e(e,i){let o=e[i];e[i]=null,Object.defineProperty(e,i,{get:()=>o,set(s){t.everythingLoaded?o=s:e["rocket"+i]=o=s}})}e(document,"onreadystatechange"),e(window,"onload"),e(window,"onpageshow");try{Object.defineProperty(document,"readyState",{get:()=>t.rocketReadyState,set(e){t.rocketReadyState=e},configurable:!0}),document.readyState="loading"}catch(t){console.log("WPRocket DJE readyState conflict, bypassing")}}l(t){this.originalAddEventListener=EventTarget.prototype.addEventListener,this.originalRemoveEventListener=EventTarget.prototype.removeEventListener,this.savedEventListeners=[],EventTarget.prototype.addEventListener=function(e,i,o){o&&o.isRocket||!t.B(e,this)&&!t.userEvents.includes(e)||t.B(e,this)&&!t.userActionTriggered||e.startsWith("rocket-")||t.everythingLoaded?t.originalAddEventListener.call(this,e,i,o):(t.savedEventListeners.push({target:this,remove:!1,type:e,func:i,options:o}),"mouseenter"!==e&&"mouseleave"!==e||t.originalAddEventListener.call(this,e,t.savedUserEvents.push,o))},EventTarget.prototype.removeEventListener=function(e,i,o){o&&o.isRocket||!t.B(e,this)&&!t.userEvents.includes(e)||t.B(e,this)&&!t.userActionTriggered||e.startsWith("rocket-")||t.everythingLoaded?t.originalRemoveEventListener.call(this,e,i,o):t.savedEventListeners.push({target:this,remove:!0,type:e,func:i,options:o})}}J(t,e){this.savedEventListeners=this.savedEventListeners.filter(i=>{let o=i.type,s=i.target||window;return e!==o||t!==s||(this.B(o,s)&&(i.type="rocket-"+o),this.$(i),!1)})}H(){EventTarget.prototype.addEventListener=this.originalAddEventListener,EventTarget.prototype.removeEventListener=this.originalRemoveEventListener,this.savedEventListeners.forEach(t=>this.$(t))}$(t){t.remove?this.originalRemoveEventListener.call(t.target,t.type,t.func,t.options):this.originalAddEventListener.call(t.target,t.type,t.func,t.options)}p(t){let e;function i(e){return t.everythingLoaded?e:e.split(" ").map(t=>"load"===t||t.startsWith("load.")?"rocket-jquery-load":t).join(" ")}function o(o){function s(e){const s=o.fn[e];o.fn[e]=o.fn.init.prototype[e]=function(){return this[0]===window&&t.userActionTriggered&&("string"==typeof arguments[0]||arguments[0]instanceof String?arguments[0]=i(arguments[0]):"object"==typeof arguments[0]&&Object.keys(arguments[0]).forEach(t=>{const e=arguments[0][t];delete arguments[0][t],arguments[0][i(t)]=e})),s.apply(this,arguments),this}}if(o&&o.fn&&!t.allJQueries.includes(o)){const e={DOMContentLoaded:[],"rocket-DOMContentLoaded":[]};for(const t in e)document.addEventListener(t,()=>{e[t].forEach(t=>t())},{isRocket:!0});o.fn.ready=o.fn.init.prototype.ready=function(i){function s(){parseInt(o.fn.jquery)>2?setTimeout(()=>i.bind(document)(o)):i.bind(document)(o)}return"function"==typeof i&&(t.realDomReadyFired?!t.userActionTriggered||t.fauxDomReadyFired?s():e["rocket-DOMContentLoaded"].push(s):e.DOMContentLoaded.push(s)),this},s("on"),s("one"),s("off"),t.allJQueries.push(o)}e=o}t.allJQueries=[],o(window.jQuery),Object.defineProperty(window,"jQuery",{get:()=>e,set(t){o(t)}})}P(){const t=new Map;document.write=document.writeln=function(e){const i=document.currentScript,o=document.createRange(),s=i.parentElement;let n=t.get(i);void 0===n&&(n=i.nextSibling,t.set(i,n));const c=document.createDocumentFragment();o.setStart(c,0),c.appendChild(o.createContextualFragment(e)),s.insertBefore(c,n)}}async R(){return new Promise(t=>{this.userActionTriggered?t():this.onFirstUserAction=t})}async L(){return new Promise(t=>{document.addEventListener("DOMContentLoaded",()=>{this.realDomReadyFired=!0,t()},{isRocket:!0})})}async j(){return this.realWindowLoadedFired?Promise.resolve():new Promise(t=>{window.addEventListener("load",t,{isRocket:!0})})}M(){this.pendingScripts=[];this.scriptsMutationObserver=new MutationObserver(t=>{for(const e of t)e.addedNodes.forEach(t=>{"SCRIPT"!==t.tagName||!t.src||t.noModule||t.isWPRocket||this.pendingScripts.push({script:t,promise:new Promise(e=>{const i=()=>{const i=this.pendingScripts.findIndex(e=>e.script===t);i>=0&&this.pendingScripts.splice(i,1),e()};t.addEventListener("load",i,{isRocket:!0}),t.addEventListener("error",i,{isRocket:!0}),setTimeout(i,1e3)})})})}),this.scriptsMutationObserver.observe(document,{childList:!0,subtree:!0})}async F(){await this.X(),this.pendingScripts.length?(await this.pendingScripts[0].promise,await this.F()):this.scriptsMutationObserver.disconnect()}D(){this.delayedScripts={normal:[],async:[],defer:[]},document.querySelectorAll("script[type$=rocketlazyloadscript]").forEach(t=>{t.hasAttribute("data-rocket-src")?t.hasAttribute("async")&&!1!==t.async?this.delayedScripts.async.push(t):t.hasAttribute("defer")&&!1!==t.defer||"module"===t.getAttribute("data-rocket-type")?this.delayedScripts.defer.push(t):this.delayedScripts.normal.push(t):this.delayedScripts.normal.push(t)})}async _(){await this.L();let t=[];document.querySelectorAll("script[type$=rocketlazyloadscript][data-rocket-src]").forEach(e=>{let i=e.getAttribute("data-rocket-src");if(i&&!i.startsWith("data:")){i.startsWith("//")&&(i=location.protocol+i);try{const o=new URL(i).origin;o!==location.origin&&t.push({src:o,crossOrigin:e.crossOrigin||"module"===e.getAttribute("data-rocket-type")})}catch(t){}}}),t=[...new Map(t.map(t=>[JSON.stringify(t),t])).values()],this.Y(t,"preconnect")}async G(t){if(await this.K(),!0!==t.noModule||!("noModule"in HTMLScriptElement.prototype))return new Promise(e=>{let i;function o(){(i||t).setAttribute("data-rocket-status","executed"),e()}try{if(navigator.userAgent.includes("Firefox/")||""===navigator.vendor||this.CSPIssue)i=document.createElement("script"),[...t.attributes].forEach(t=>{let e=t.nodeName;"type"!==e&&("data-rocket-type"===e&&(e="type"),"data-rocket-src"===e&&(e="src"),i.setAttribute(e,t.nodeValue))}),t.text&&(i.text=t.text),t.nonce&&(i.nonce=t.nonce),i.hasAttribute("src")?(i.addEventListener("load",o,{isRocket:!0}),i.addEventListener("error",()=>{i.setAttribute("data-rocket-status","failed-network"),e()},{isRocket:!0}),setTimeout(()=>{i.isConnected||e()},1)):(i.text=t.text,o()),i.isWPRocket=!0,t.parentNode.replaceChild(i,t);else{const i=t.getAttribute("data-rocket-type"),s=t.getAttribute("data-rocket-src");i?(t.type=i,t.removeAttribute("data-rocket-type")):t.removeAttribute("type"),t.addEventListener("load",o,{isRocket:!0}),t.addEventListener("error",i=>{this.CSPIssue&&i.target.src.startsWith("data:")?(console.log("WPRocket: CSP fallback activated"),t.removeAttribute("src"),this.G(t).then(e)):(t.setAttribute("data-rocket-status","failed-network"),e())},{isRocket:!0}),s?(t.fetchPriority="high",t.removeAttribute("data-rocket-src"),t.src=s):t.src="data:text/javascript;base64,"+window.btoa(unescape(encodeURIComponent(t.text)))}}catch(i){t.setAttribute("data-rocket-status","failed-transform"),e()}});t.setAttribute("data-rocket-status","skipped")}async C(t){const e=t.shift();return e?(e.isConnected&&await this.G(e),this.C(t)):Promise.resolve()}O(){this.Y([...this.delayedScripts.normal,...this.delayedScripts.defer,...this.delayedScripts.async],"preload")}Y(t,e){this.trash=this.trash||[];let i=!0;var o=document.createDocumentFragment();t.forEach(t=>{const s=t.getAttribute&&t.getAttribute("data-rocket-src")||t.src;if(s&&!s.startsWith("data:")){const n=document.createElement("link");n.href=s,n.rel=e,"preconnect"!==e&&(n.as="script",n.fetchPriority=i?"high":"low"),t.getAttribute&&"module"===t.getAttribute("data-rocket-type")&&(n.crossOrigin=!0),t.crossOrigin&&(n.crossOrigin=t.crossOrigin),t.integrity&&(n.integrity=t.integrity),t.nonce&&(n.nonce=t.nonce),o.appendChild(n),this.trash.push(n),i=!1}}),document.head.appendChild(o)}W(){this.trash.forEach(t=>t.remove())}async T(){try{document.readyState="interactive"}catch(t){}this.fauxDomReadyFired=!0;try{await this.K(),this.J(document,"readystatechange"),document.dispatchEvent(new Event("rocket-readystatechange")),await this.K(),document.rocketonreadystatechange&&document.rocketonreadystatechange(),await this.K(),this.J(document,"DOMContentLoaded"),document.dispatchEvent(new Event("rocket-DOMContentLoaded")),await this.K(),this.J(window,"DOMContentLoaded"),window.dispatchEvent(new Event("rocket-DOMContentLoaded"))}catch(t){console.error(t)}}async A(){try{document.readyState="complete"}catch(t){}try{await this.K(),this.J(document,"readystatechange"),document.dispatchEvent(new Event("rocket-readystatechange")),await this.K(),document.rocketonreadystatechange&&document.rocketonreadystatechange(),await this.K(),this.J(window,"load"),window.dispatchEvent(new Event("rocket-load")),await this.K(),window.rocketonload&&window.rocketonload(),await this.K(),this.allJQueries.forEach(t=>t(window).trigger("rocket-jquery-load")),await this.K(),this.J(window,"pageshow");const t=new Event("rocket-pageshow");t.persisted=this.persisted,window.dispatchEvent(t),await this.K(),window.rocketonpageshow&&window.rocketonpageshow({persisted:this.persisted})}catch(t){console.error(t)}}async K(){Date.now()-this.lastBreath>45&&(await this.X(),this.lastBreath=Date.now())}async X(){return document.hidden?new Promise(t=>setTimeout(t)):new Promise(t=>requestAnimationFrame(t))}B(t,e=window){return e===document&&"readystatechange"===t||(e===document&&"DOMContentLoaded"===t||(e===window&&"DOMContentLoaded"===t||(e===window&&"load"===t||e===window&&"pageshow"===t)))}static run(){(new RocketLazyLoadScripts).t()}}RocketLazyLoadScripts.run()})();
</script>

<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="profile" href="http://gmpg.org/xfn/11">
<link rel="pingback" href="https://citrine.io/xmlrpc.php">

<meta name='robots' content='index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' />

	<!-- This site is optimized with the Yoast SEO Premium plugin v27.8 (Yoast SEO v27.8) - https://yoast.com/product/yoast-seo-premium-wordpress/ -->
	<title>Chemical &amp; Materials Development Platform | Citrine Informatics</title>
<link data-rocket-preload as="style" href="https://fonts.googleapis.com/css?family=Barlow%20Semi%20Condensed%3A100%2C200%2C300%2C400%2C500%2C600%2C700%2C800%2C900%7CLusitana%3A400%2C700%7CMontserrat%3A100%2C200%2C300%2C400%2C500%2C600%2C700%2C800%2C900%7COpen%20Sans%3A400%2C600%2C700%2C800%7CRaleway%3A100%2C200%2C300%2C400%2C500%2C600%2C700%2C800%2C900%7CRoboto%20Condensed%3A300%2C400%2C700%7CRoboto%3A100%2C300%2C400%2C500%2C700%2C900%7CBarlow%20Semi%20Condensed%7CBarlow%20Semi%20Condensed&#038;display=swap" rel="preload">
<link href="https://fonts.googleapis.com/css?family=Barlow%20Semi%20Condensed%3A100%2C200%2C300%2C400%2C500%2C600%2C700%2C800%2C900%7CLusitana%3A400%2C700%7CMontserrat%3A100%2C200%2C300%2C400%2C500%2C600%2C700%2C800%2C900%7COpen%20Sans%3A400%2C600%2C700%2C800%7CRaleway%3A100%2C200%2C300%2C400%2C500%2C600%2C700%2C800%2C900%7CRoboto%20Condensed%3A300%2C400%2C700%7CRoboto%3A100%2C300%2C400%2C500%2C700%2C900%7CBarlow%20Semi%20Condensed%7CBarlow%20Semi%20Condensed&#038;display=swap" media="print" onload="this.media=&#039;all&#039;" rel="stylesheet">
<noscript data-wpr-hosted-gf-parameters=""><link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Barlow%20Semi%20Condensed%3A100%2C200%2C300%2C400%2C500%2C600%2C700%2C800%2C900%7CLusitana%3A400%2C700%7CMontserrat%3A100%2C200%2C300%2C400%2C500%2C600%2C700%2C800%2C900%7COpen%20Sans%3A400%2C600%2C700%2C800%7CRaleway%3A100%2C200%2C300%2C400%2C500%2C600%2C700%2C800%2C900%7CRoboto%20Condensed%3A300%2C400%2C700%7CRoboto%3A100%2C300%2C400%2C500%2C700%2C900%7CBarlow%20Semi%20Condensed%7CBarlow%20Semi%20Condensed&#038;display=swap"></noscript>
<style id="rocket-critical-css">.ancr-group>.ancr{margin-bottom:0!important}.ancr-group.ancr-sticky{position:fixed;left:0;right:0}.ancr-group.ancr-pos-top{top:0;z-index:99999}.ancr-group.ancr-pos-top>.ancr{top:0;border-top:0!important}.ancr.ancr-wrap{display:none;position:relative;width:100%;background-color:#fff;box-sizing:border-box;padding:0.5em 1em;border-left-width:0!important;border-right-width:0!important}.ancr .ancr-container{max-width:1000px;margin:0 auto;display:flex}.ancr .ancr-inner{display:inline-block}.ancr .ancr-inner>*{margin-bottom:1em}.ancr .ancr-inner>*:first-child{margin-top:0}.ancr .ancr-inner>*:last-child{margin-bottom:0}.ancr .ancr-content{display:flex;flex-direction:column;justify-content:center}.ancr.ancr-align-center .ancr-container{justify-content:center;text-align:center}.ancr.ancr-align-center .ancr-btn-wrap{justify-content:center}.ancr .ancr-close-btn{position:absolute;top:0;right:0;color:inherit;line-height:0;padding:0.5em;z-index:999}.ancr .ancr-close-icon{width:16px;height:16px}.ancr .ancr-btn-wrap{display:inline-block;margin:0 0 0 1em;line-height:0;display:flex;flex-direction:row;align-items:center}.ancr .ancr-btn{padding:0.5em 1em;display:inline-block;margin:0 0.5em 0 0;text-align:center;line-height:1;white-space:nowrap;vertical-align:middle;text-decoration:none}.ancr .ancr-btn:last-child{margin-right:0}@media only screen and (max-width:800px){.ancr-lo-same_row .ancr-container{display:block}.ancr-lo-same_row .ancr-btn-wrap{margin:0.5em 0 0 0}}#cookie-law-info-bar{font-size:15px;margin:0 auto;padding:12px 10px;position:absolute;text-align:center;box-sizing:border-box;width:100%;z-index:9999;display:none;left:0px;font-weight:300;box-shadow:0 -1px 10px 0 rgba(172,171,171,0.3)}#cookie-law-info-bar span{vertical-align:middle}.cli-plugin-button,.cli-plugin-button:visited{display:inline-block;padding:9px 12px;color:#fff;text-decoration:none;position:relative;margin-left:5px;text-decoration:none}.cli-plugin-button,.cli-plugin-button:visited,.medium.cli-plugin-button,.medium.cli-plugin-button:visited{font-size:13px;font-weight:400;line-height:1}.cli-plugin-button{margin-top:5px}.cli-bar-popup{-moz-background-clip:padding;-webkit-background-clip:padding;background-clip:padding-box;-webkit-border-radius:30px;-moz-border-radius:30px;border-radius:30px;padding:20px}.cli-container-fluid{padding-right:15px;padding-left:15px;margin-right:auto;margin-left:auto}.cli-row{display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap;margin-right:-15px;margin-left:-15px}.cli-align-items-stretch{-ms-flex-align:stretch!important;align-items:stretch!important}.cli-px-0{padding-left:0;padding-right:0}.cli-btn{font-size:14px;display:inline-block;font-weight:400;text-align:center;white-space:nowrap;vertical-align:middle;border:1px solid transparent;padding:.5rem 1.25rem;line-height:1;border-radius:.25rem}.cli-modal-backdrop{position:fixed;top:0;right:0;bottom:0;left:0;z-index:1040;background-color:#000;display:none}.cli-modal-backdrop.cli-fade{opacity:0}.cli-modal a{text-decoration:none}.cli-modal .cli-modal-dialog{position:relative;width:auto;margin:.5rem;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol";font-size:1rem;font-weight:400;line-height:1.5;color:#212529;text-align:left;display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;min-height:calc(100% - (.5rem * 2))}@media (min-width:576px){.cli-modal .cli-modal-dialog{max-width:500px;margin:1.75rem auto;min-height:calc(100% - (1.75rem * 2))}}@media (min-width:992px){.cli-modal .cli-modal-dialog{max-width:900px}}.cli-modal-content{position:relative;display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column;width:100%;background-color:#fff;background-clip:padding-box;border-radius:.3rem;outline:0}.cli-modal .cli-modal-close{position:absolute;right:10px;top:10px;z-index:1;padding:0;background-color:transparent!important;border:0;-webkit-appearance:none;font-size:1.5rem;font-weight:700;line-height:1;color:#000;text-shadow:0 1px 0 #fff}.cli-switch{display:inline-block;position:relative;min-height:1px;padding-left:70px;font-size:14px}.cli-switch input[type="checkbox"]{display:none}.cli-switch .cli-slider{background-color:#e3e1e8;height:24px;width:50px;bottom:0;left:0;position:absolute;right:0;top:0}.cli-switch .cli-slider:before{background-color:#fff;bottom:2px;content:"";height:20px;left:2px;position:absolute;width:20px}.cli-switch input:checked+.cli-slider{background-color:#00acad}.cli-switch input:checked+.cli-slider:before{transform:translateX(26px)}.cli-switch .cli-slider{border-radius:34px}.cli-switch .cli-slider:before{border-radius:50%}.cli-tab-content{background:#ffffff}.cli-tab-content{width:100%;padding:30px}@media (max-width:767px){.cli-tab-content{padding:30px 10px}}.cli-container-fluid{padding-right:15px;padding-left:15px;margin-right:auto;margin-left:auto}.cli-row{display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap;margin-right:-15px;margin-left:-15px}.cli-align-items-stretch{-ms-flex-align:stretch!important;align-items:stretch!important}.cli-px-0{padding-left:0;padding-right:0}.cli-btn{font-size:14px;display:inline-block;font-weight:400;text-align:center;white-space:nowrap;vertical-align:middle;border:1px solid transparent;padding:.5rem 1.25rem;line-height:1;border-radius:.25rem}.cli-modal-backdrop{position:fixed;top:0;right:0;bottom:0;left:0;z-index:1040;background-color:#000;-webkit-transform:scale(0);transform:scale(0)}.cli-modal-backdrop.cli-fade{opacity:0}.cli-modal{position:fixed;top:0;right:0;bottom:0;left:0;z-index:99999;transform:scale(0);overflow:hidden;outline:0;display:none}.cli-modal a{text-decoration:none}.cli-modal .cli-modal-dialog{position:relative;width:auto;margin:.5rem;font-family:inherit;font-size:1rem;font-weight:400;line-height:1.5;color:#212529;text-align:left;display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;min-height:calc(100% - (.5rem * 2))}@media (min-width:576px){.cli-modal .cli-modal-dialog{max-width:500px;margin:1.75rem auto;min-height:calc(100% - (1.75rem * 2))}}.cli-modal-content{position:relative;display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column;width:100%;background-color:#fff;background-clip:padding-box;border-radius:.2rem;box-sizing:border-box;outline:0}.cli-switch{display:inline-block;position:relative;min-height:1px;padding-left:38px;font-size:14px}.cli-switch input[type="checkbox"]{display:none}.cli-switch .cli-slider{background-color:#e3e1e8;height:20px;width:38px;bottom:0;left:0;position:absolute;right:0;top:0}.cli-switch .cli-slider:before{background-color:#fff;bottom:2px;content:"";height:15px;left:3px;position:absolute;width:15px}.cli-switch input:checked+.cli-slider{background-color:#61a229}.cli-switch input:checked+.cli-slider:before{transform:translateX(18px)}.cli-switch .cli-slider{border-radius:34px;font-size:0}.cli-switch .cli-slider:before{border-radius:50%}.cli-tab-content{background:#ffffff}.cli-tab-content{width:100%;padding:5px 30px 5px 5px;box-sizing:border-box}@media (max-width:767px){.cli-tab-content{padding:30px 10px}}.cli-tab-footer .cli-btn{background-color:#00acad;padding:10px 15px;text-decoration:none}.cli-tab-footer .wt-cli-privacy-accept-btn{background-color:#61a229;color:#ffffff;border-radius:0}.cli-tab-footer{width:100%;text-align:right;padding:20px 0}.cli-col-12{width:100%}.cli-tab-header{display:flex;justify-content:space-between}.cli-tab-header a:before{width:10px;height:2px;left:0;top:calc(50% - 1px)}.cli-tab-header a:after{width:2px;height:10px;left:4px;top:calc(50% - 5px);-webkit-transform:none;transform:none}.cli-tab-header a:before{width:7px;height:7px;border-right:1px solid #4a6e78;border-bottom:1px solid #4a6e78;content:" ";transform:rotate(-45deg);margin-right:10px}.cli-tab-header a.cli-nav-link{position:relative;display:flex;align-items:center;font-size:14px;color:#000;text-transform:capitalize}.cli-tab-header{border-radius:5px;padding:12px 15px;background-color:#f2f2f2}.cli-modal .cli-modal-close{position:absolute;right:0;top:0;z-index:1;-webkit-appearance:none;width:40px;height:40px;padding:0;border-radius:50%;padding:10px;background:transparent;border:none;min-width:40px}.cli-tab-container h4{font-family:inherit;font-size:16px;margin-bottom:15px;margin:10px 0}#cliSettingsPopup .cli-tab-section-container{padding-top:12px}.cli-privacy-content-text{font-size:14px;line-height:1.4;margin-top:0;padding:0;color:#000}.cli-tab-content{display:none}.cli-tab-section .cli-tab-content{padding:10px 20px 5px 20px}.cli-tab-section{margin-top:5px}@media (min-width:992px){.cli-modal .cli-modal-dialog{max-width:645px}}.cli-switch .cli-slider:after{content:attr(data-cli-disable);position:absolute;right:50px;color:#000;font-size:12px;text-align:right;min-width:80px}.cli-switch input:checked+.cli-slider:after{content:attr(data-cli-enable)}.cli-privacy-overview:not(.cli-collapsed) .cli-privacy-content{max-height:60px;overflow:hidden}a.cli-privacy-readmore{font-size:12px;margin-top:12px;display:inline-block;padding-bottom:0;color:#000;text-decoration:underline}.cli-modal-footer{position:relative}a.cli-privacy-readmore:before{content:attr(data-readmore-text)}.cli-modal-close svg{fill:#000}span.cli-necessary-caption{color:#000;font-size:12px}.cli-tab-container .cli-row{max-height:500px;overflow-y:auto}.wt-cli-sr-only{display:none;font-size:16px}.cli-bar-container{float:none;margin:0 auto;display:-webkit-box;display:-moz-box;display:-ms-flexbox;display:-webkit-flex;display:flex;justify-content:space-between;-webkit-box-align:center;-moz-box-align:center;-ms-flex-align:center;-webkit-align-items:center;align-items:center}.cli-bar-btn_container{margin-left:20px;display:-webkit-box;display:-moz-box;display:-ms-flexbox;display:-webkit-flex;display:flex;-webkit-box-align:center;-moz-box-align:center;-ms-flex-align:center;-webkit-align-items:center;align-items:center;flex-wrap:nowrap}.cli-bar-btn_container a{white-space:nowrap}.cli-style-v2{font-size:11pt;line-height:18px;font-weight:normal}.cli-style-v2 .cli-bar-message{width:70%;text-align:left}.cli-style-v2 .cli-bar-btn_container .cli_action_button,.cli-style-v2 .cli-bar-btn_container .cli_settings_button{margin-left:5px}.cli-style-v2 .cli_settings_button:not(.cli-plugin-button){text-decoration:underline}.cli-style-v2 .cli-bar-btn_container .cli-plugin-button{margin-top:5px;margin-bottom:5px}.wt-cli-necessary-checkbox{display:none!important}@media (max-width:985px){.cli-style-v2 .cli-bar-message{width:100%}.cli-style-v2.cli-bar-container{justify-content:left;flex-wrap:wrap}.cli-style-v2 .cli-bar-btn_container{margin-left:0px;margin-top:10px}}.wt-cli-privacy-overview-actions{padding-bottom:0}@media only screen and (max-width:479px) and (min-width:320px){.cli-style-v2 .cli-bar-btn_container{flex-wrap:wrap}}.wt-cli-cookie-description{font-size:14px;line-height:1.4;margin-top:0;padding:0;color:#000}:root{--btn-border:1px solid rgba(255, 255, 255, 0.2);--btn-bg:transparent;--btn-shadow:1px 1px 25px 10px rgba(255, 255, 255, 0.5);--btn-text-color:#f4f4f4;--shine-degree:120deg;--shine-color:rgba(255, 255, 255, 0.2);--shine-effect:linear-gradient(var(--shine-degree), transparent, var(--shine-color), transparent)}.cta-button{font-size:1.1rem;padding:1rem 3rem;border-radius:4px;text-decoration:none;border:var(--btn-border);color:var(--btn-text-color);box-shadow:0px 0px 15px #00000040;text-align:center;line-height:1.4}.cta-button.red{background-color:#C0392B}.cta-button.style4{position:fixed;bottom:20px;right:20px;z-index:9999;overflow:hidden;font-size:1.1rem;padding:1rem 3rem;border-radius:4px;text-decoration:none;border:var(--btn-border);color:var(--btn-text-color)}.style4{position:fixed;bottom:20px;right:20px;z-index:9999;opacity:0}@media (max-width:767px){.cta-button{right:auto!important;margin:0 20px}}#mega-menu-wrap-primary_menu,#mega-menu-wrap-primary_menu #mega-menu-primary_menu,#mega-menu-wrap-primary_menu #mega-menu-primary_menu ul.mega-sub-menu,#mega-menu-wrap-primary_menu #mega-menu-primary_menu li.mega-menu-item,#mega-menu-wrap-primary_menu #mega-menu-primary_menu li.mega-menu-row,#mega-menu-wrap-primary_menu #mega-menu-primary_menu li.mega-menu-column,#mega-menu-wrap-primary_menu #mega-menu-primary_menu a.mega-menu-link{border-radius:0;box-shadow:none;background:none;border:0;bottom:auto;box-sizing:border-box;clip:auto;color:#333;display:block;float:none;font-family:inherit;font-size:16px;height:auto;left:auto;line-height:1.7;list-style-type:none;margin:0;min-height:auto;max-height:none;min-width:auto;max-width:none;opacity:1;outline:none;overflow:visible;padding:0;position:relative;right:auto;text-align:left;text-decoration:none;text-indent:0;text-transform:none;transform:none;top:auto;vertical-align:baseline;visibility:inherit;width:auto;word-wrap:break-word;white-space:normal}#mega-menu-wrap-primary_menu:before,#mega-menu-wrap-primary_menu:after,#mega-menu-wrap-primary_menu #mega-menu-primary_menu:before,#mega-menu-wrap-primary_menu #mega-menu-primary_menu:after,#mega-menu-wrap-primary_menu #mega-menu-primary_menu ul.mega-sub-menu:before,#mega-menu-wrap-primary_menu #mega-menu-primary_menu ul.mega-sub-menu:after,#mega-menu-wrap-primary_menu #mega-menu-primary_menu li.mega-menu-item:before,#mega-menu-wrap-primary_menu #mega-menu-primary_menu li.mega-menu-item:after,#mega-menu-wrap-primary_menu #mega-menu-primary_menu li.mega-menu-row:before,#mega-menu-wrap-primary_menu #mega-menu-primary_menu li.mega-menu-row:after,#mega-menu-wrap-primary_menu #mega-menu-primary_menu li.mega-menu-column:before,#mega-menu-wrap-primary_menu #mega-menu-primary_menu li.mega-menu-column:after,#mega-menu-wrap-primary_menu #mega-menu-primary_menu a.mega-menu-link:before,#mega-menu-wrap-primary_menu #mega-menu-primary_menu a.mega-menu-link:after{display:none}#mega-menu-wrap-primary_menu{border-radius:0px}@media only screen and (min-width:769px){#mega-menu-wrap-primary_menu{background:#fbfbfc}}#mega-menu-wrap-primary_menu #mega-menu-primary_menu{text-align:left;padding:0px 15px}#mega-menu-wrap-primary_menu #mega-menu-primary_menu a.mega-menu-link{display:inline}#mega-menu-wrap-primary_menu #mega-menu-primary_menu p{margin-bottom:10px}#mega-menu-wrap-primary_menu #mega-menu-primary_menu img{max-width:100%}#mega-menu-wrap-primary_menu #mega-menu-primary_menu li.mega-menu-item>ul.mega-sub-menu{display:block;visibility:hidden;opacity:1}@media only screen and (max-width:768px){#mega-menu-wrap-primary_menu #mega-menu-primary_menu li.mega-menu-item>ul.mega-sub-menu{display:none;visibility:visible;opacity:1}}@media only screen and (min-width:769px){#mega-menu-wrap-primary_menu #mega-menu-primary_menu[data-effect="fade_up"] li.mega-menu-item.mega-menu-megamenu>ul.mega-sub-menu{opacity:0;transform:translate(0,10px)}}#mega-menu-wrap-primary_menu #mega-menu-primary_menu li.mega-menu-item.mega-menu-megamenu ul.mega-sub-menu ul.mega-sub-menu{visibility:inherit;opacity:1;display:block}#mega-menu-wrap-primary_menu #mega-menu-primary_menu li.mega-menu-item a.mega-menu-link:before{display:inline-block;font:inherit;font-family:dashicons;position:static;margin:0 6px 0 0px;vertical-align:top;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;color:inherit;background:transparent;height:auto;width:auto;top:auto}@media only screen and (min-width:769px){#mega-menu-wrap-primary_menu #mega-menu-primary_menu>li.mega-menu-megamenu.mega-menu-item{position:static}}#mega-menu-wrap-primary_menu #mega-menu-primary_menu>li.mega-menu-item{margin:0 0px 0 0;display:inline-block;height:auto;vertical-align:middle}#mega-menu-wrap-primary_menu #mega-menu-primary_menu>li.mega-menu-item>a.mega-menu-link{line-height:80px;height:80px;padding:0px 10px;vertical-align:baseline;width:auto;display:block;color:#303030;text-transform:uppercase;text-decoration:none;text-align:left;background:rgba(0,0,0,0);border:0;border-radius:0px;font-family:inherit;font-size:16px;font-weight:normal;outline:none}@media only screen and (max-width:768px){#mega-menu-wrap-primary_menu #mega-menu-primary_menu>li.mega-menu-item{display:list-item;margin:0;clear:both;border:0}#mega-menu-wrap-primary_menu #mega-menu-primary_menu>li.mega-menu-item>a.mega-menu-link{border-radius:0;border:0;margin:0;line-height:40px;height:40px;padding:0 10px;background:transparent;text-align:left;color:#ffffff;font-size:14px}}#mega-menu-wrap-primary_menu #mega-menu-primary_menu li.mega-menu-megamenu>ul.mega-sub-menu>li.mega-menu-row{width:100%;float:left}#mega-menu-wrap-primary_menu #mega-menu-primary_menu li.mega-menu-megamenu>ul.mega-sub-menu>li.mega-menu-row .mega-menu-column{float:left;min-height:1px}@media only screen and (min-width:769px){#mega-menu-wrap-primary_menu #mega-menu-primary_menu li.mega-menu-megamenu>ul.mega-sub-menu>li.mega-menu-row>ul.mega-sub-menu>li.mega-menu-columns-2-of-12{width:16.6666666667%}#mega-menu-wrap-primary_menu #mega-menu-primary_menu li.mega-menu-megamenu>ul.mega-sub-menu>li.mega-menu-row>ul.mega-sub-menu>li.mega-menu-columns-3-of-12{width:25%}#mega-menu-wrap-primary_menu #mega-menu-primary_menu li.mega-menu-megamenu>ul.mega-sub-menu>li.mega-menu-row>ul.mega-sub-menu>li.mega-menu-columns-4-of-12{width:33.3333333333%}#mega-menu-wrap-primary_menu #mega-menu-primary_menu li.mega-menu-megamenu>ul.mega-sub-menu>li.mega-menu-row>ul.mega-sub-menu>li.mega-menu-columns-12-of-12{width:100%}}@media only screen and (max-width:768px){#mega-menu-wrap-primary_menu #mega-menu-primary_menu li.mega-menu-megamenu>ul.mega-sub-menu>li.mega-menu-row>ul.mega-sub-menu>li.mega-menu-column{width:100%;clear:both}}#mega-menu-wrap-primary_menu #mega-menu-primary_menu li.mega-menu-megamenu>ul.mega-sub-menu>li.mega-menu-row .mega-menu-column>ul.mega-sub-menu>li.mega-menu-item{padding:0px;width:100%}#mega-menu-wrap-primary_menu #mega-menu-primary_menu>li.mega-menu-megamenu>ul.mega-sub-menu{z-index:999;border-radius:0px;background:white;border:0;padding:25px 35px 30px 35px;position:absolute;width:100%;max-width:none;left:0}@media only screen and (max-width:768px){#mega-menu-wrap-primary_menu #mega-menu-primary_menu>li.mega-menu-megamenu>ul.mega-sub-menu{float:left;position:static;width:100%}}@media only screen and (min-width:769px){#mega-menu-wrap-primary_menu #mega-menu-primary_menu>li.mega-menu-megamenu>ul.mega-sub-menu li.mega-menu-columns-2-of-12{width:16.6666666667%}#mega-menu-wrap-primary_menu #mega-menu-primary_menu>li.mega-menu-megamenu>ul.mega-sub-menu li.mega-menu-columns-3-of-12{width:25%}#mega-menu-wrap-primary_menu #mega-menu-primary_menu>li.mega-menu-megamenu>ul.mega-sub-menu li.mega-menu-columns-4-of-12{width:33.3333333333%}#mega-menu-wrap-primary_menu #mega-menu-primary_menu>li.mega-menu-megamenu>ul.mega-sub-menu li.mega-menu-columns-12-of-12{width:100%}}#mega-menu-wrap-primary_menu #mega-menu-primary_menu>li.mega-menu-megamenu>ul.mega-sub-menu li.mega-menu-column>ul.mega-sub-menu>li.mega-menu-item{color:#333;font-family:inherit;font-size:16px;display:block;float:left;clear:none;padding:0px;vertical-align:top}#mega-menu-wrap-primary_menu #mega-menu-primary_menu>li.mega-menu-megamenu>ul.mega-sub-menu li.mega-menu-column>ul.mega-sub-menu>li.mega-menu-item>a.mega-menu-link{color:#e96e01;font-family:inherit;font-size:22px;text-transform:none;text-decoration:none;font-weight:inherit;text-align:left;margin:0px 0px 0px 0px;padding:20px 0px 5px 0px;vertical-align:top;display:block;border:0}#mega-menu-wrap-primary_menu #mega-menu-primary_menu>li.mega-menu-megamenu>ul.mega-sub-menu li.mega-menu-column>ul.mega-sub-menu>li.mega-menu-item li.mega-menu-item>a.mega-menu-link{color:#666;font-family:inherit;font-size:18px;text-transform:none;text-decoration:none;font-weight:normal;text-align:left;margin:0px 0px 0px 0px;padding:0px 0px 10px 0px;vertical-align:top;display:block;border:0}@media only screen and (max-width:768px){#mega-menu-wrap-primary_menu #mega-menu-primary_menu>li.mega-menu-megamenu>ul.mega-sub-menu{border:0;padding:10px;border-radius:0}}#mega-menu-wrap-primary_menu #mega-menu-primary_menu li.mega-menu-item-has-children>a.mega-menu-link>span.mega-indicator{display:inline-block;width:auto;background:transparent;position:relative;left:auto;min-width:auto;font-size:inherit;padding:0;margin:0 0 0 6px;height:auto;line-height:inherit;color:inherit}#mega-menu-wrap-primary_menu #mega-menu-primary_menu li.mega-menu-item-has-children>a.mega-menu-link>span.mega-indicator:after{content:"";font-family:dashicons;font-weight:normal;display:inline-block;margin:0;vertical-align:top;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;transform:rotate(0);color:inherit;position:relative;background:transparent;height:auto;width:auto;right:auto;line-height:inherit}#mega-menu-wrap-primary_menu #mega-menu-primary_menu li.mega-menu-item-has-children li.mega-menu-item-has-children>a.mega-menu-link>span.mega-indicator{float:right;margin-left:auto}@media only screen and (max-width:768px){#mega-menu-wrap-primary_menu #mega-menu-primary_menu li.mega-menu-item-has-children>a.mega-menu-link>span.mega-indicator{float:right}}#mega-menu-wrap-primary_menu #mega-menu-primary_menu li.mega-menu-megamenu:not(.mega-menu-tabbed) li.mega-menu-item-has-children:not(.mega-collapse-children)>a.mega-menu-link>span.mega-indicator{display:none}@media only screen and (max-width:768px){#mega-menu-wrap-primary_menu:after{content:"";display:table;clear:both}}#mega-menu-wrap-primary_menu .mega-menu-toggle{display:none;z-index:1;background:#222;border-radius:2px;line-height:40px;height:40px;text-align:left;outline:none;white-space:nowrap}@media only screen and (max-width:768px){#mega-menu-wrap-primary_menu .mega-menu-toggle{display:-webkit-box;display:-ms-flexbox;display:-webkit-flex;display:flex}}#mega-menu-wrap-primary_menu .mega-menu-toggle .mega-toggle-blocks-left,#mega-menu-wrap-primary_menu .mega-menu-toggle .mega-toggle-blocks-center,#mega-menu-wrap-primary_menu .mega-menu-toggle .mega-toggle-blocks-right{display:-webkit-box;display:-ms-flexbox;display:-webkit-flex;display:flex;-ms-flex-preferred-size:33.33%;-webkit-flex-basis:33.33%;flex-basis:33.33%}#mega-menu-wrap-primary_menu .mega-menu-toggle .mega-toggle-blocks-left{-webkit-box-flex:1;-ms-flex:1;-webkit-flex:1;flex:1;-webkit-box-pack:start;-ms-flex-pack:start;-webkit-justify-content:flex-start;justify-content:flex-start}#mega-menu-wrap-primary_menu .mega-menu-toggle .mega-toggle-blocks-center{-webkit-box-pack:center;-ms-flex-pack:center;-webkit-justify-content:center;justify-content:center}#mega-menu-wrap-primary_menu .mega-menu-toggle .mega-toggle-blocks-right{-webkit-box-flex:1;-ms-flex:1;-webkit-flex:1;flex:1;-webkit-box-pack:end;-ms-flex-pack:end;-webkit-justify-content:flex-end;justify-content:flex-end}#mega-menu-wrap-primary_menu .mega-menu-toggle .mega-toggle-blocks-right .mega-toggle-block{margin-right:6px}#mega-menu-wrap-primary_menu .mega-menu-toggle .mega-toggle-blocks-right .mega-toggle-block:only-child{margin-left:6px}#mega-menu-wrap-primary_menu .mega-menu-toggle .mega-toggle-block{display:-webkit-box;display:-ms-flexbox;display:-webkit-flex;display:flex;height:100%;outline:0;-webkit-align-self:center;-ms-flex-item-align:center;align-self:center;-ms-flex-negative:0;-webkit-flex-shrink:0;flex-shrink:0}@media only screen and (max-width:768px){#mega-menu-wrap-primary_menu .mega-menu-toggle+#mega-menu-primary_menu{background:#222;padding:0px;display:none}}#mega-menu-wrap-primary_menu .mega-menu-toggle .mega-toggle-block-0 .mega-toggle-animated{padding:0;display:-webkit-box;display:-ms-flexbox;display:-webkit-flex;display:flex;font:inherit;color:inherit;text-transform:none;background-color:transparent;border:0;margin:0;overflow:visible;transform:scale(0.8);align-self:center;outline:0;background:none}#mega-menu-wrap-primary_menu .mega-menu-toggle .mega-toggle-block-0 .mega-toggle-animated-box{width:40px;height:24px;display:inline-block;position:relative;outline:0}#mega-menu-wrap-primary_menu .mega-menu-toggle .mega-toggle-block-0 .mega-toggle-animated-inner{display:block;top:50%;margin-top:-2px}#mega-menu-wrap-primary_menu .mega-menu-toggle .mega-toggle-block-0 .mega-toggle-animated-inner,#mega-menu-wrap-primary_menu .mega-menu-toggle .mega-toggle-block-0 .mega-toggle-animated-inner::before,#mega-menu-wrap-primary_menu .mega-menu-toggle .mega-toggle-block-0 .mega-toggle-animated-inner::after{width:40px;height:4px;background-color:#ddd;border-radius:4px;position:absolute}#mega-menu-wrap-primary_menu .mega-menu-toggle .mega-toggle-block-0 .mega-toggle-animated-inner::before,#mega-menu-wrap-primary_menu .mega-menu-toggle .mega-toggle-block-0 .mega-toggle-animated-inner::after{content:"";display:block}#mega-menu-wrap-primary_menu .mega-menu-toggle .mega-toggle-block-0 .mega-toggle-animated-inner::before{top:-10px}#mega-menu-wrap-primary_menu .mega-menu-toggle .mega-toggle-block-0 .mega-toggle-animated-inner::after{bottom:-10px}#mega-menu-wrap-primary_menu .mega-menu-toggle .mega-toggle-block-0 .mega-toggle-animated-slider .mega-toggle-animated-inner{top:2px}#mega-menu-wrap-primary_menu .mega-menu-toggle .mega-toggle-block-0 .mega-toggle-animated-slider .mega-toggle-animated-inner::before{top:10px}#mega-menu-wrap-primary_menu .mega-menu-toggle .mega-toggle-block-0 .mega-toggle-animated-slider .mega-toggle-animated-inner::after{top:20px}#mega-menu-wrap-primary_menu{clear:both}html{box-sizing:border-box}*,*::after,*::before{box-sizing:inherit}html{font-family:sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%}body{margin:0}header,main,nav{display:block}a{background-color:transparent}strong{font-weight:600}h1{font-size:2em;margin:0.67em 0}img{border:0}svg:not(:root){overflow:hidden}button,input{color:inherit;font:inherit;margin:0}button{overflow:visible}button{text-transform:none}button,input[type="submit"]{-webkit-appearance:button}button::-moz-focus-inner,input::-moz-focus-inner{border:0;padding:0}input{line-height:normal}input[type="checkbox"]{box-sizing:border-box;padding:0}input[type="search"]::-webkit-search-cancel-button,input[type="search"]::-webkit-search-decoration{-webkit-appearance:none}body,button,input{color:#333;font-family:'Open Sans',Arial,sans-serif;font-weight:400;font-size:16px;font-size:1rem;line-height:1.5;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}h1,h2,h4{clear:both;margin:0.5em 0;line-height:1.2}h1{font-size:36px;font-family:'Open Sans',Arial,sans-serif;font-weight:600}h2{font-size:30px;font-family:'Open Sans',Arial,sans-serif;font-weight:300;line-height:1.1}h4{font-size:22px;font-family:'Open Sans',Arial,sans-serif;font-weight:600}p{font-size:1em}i{font-style:italic}html{box-sizing:border-box}*,*:before,*:after{box-sizing:inherit}body{background:#fff}ul{margin:0 0 1.5em 0;padding-left:1.5em}ul ul{padding-left:1em}ul{list-style:disc}li>ul{margin-bottom:0;margin-left:1.5em}img{height:auto;max-width:100%}ul{margin-left:0}.r8_main_header{background-color:#fff}.r8_sec_menu_wrapper{background-color:#000}.site-header{position:relative;width:100%}.r8_header_fixed .site-header{position:fixed;z-index:10}.fixed-header-spacer{width:100%;display:block;height:32px}@media screen and (max-width:768px){.fixed-header-spacer{height:0px}}.fixed-header-spacer.no-hero{height:102px}@media screen and (max-width:768px){.fixed-header-spacer.no-hero{height:60px}}@media screen and (max-width:626px){.fixed-header-spacer.no-hero{height:50px}}.top_header_search_form{display:none;padding:20px;background-color:#fff;-moz-box-shadow:inset 0 0 10px -2px #000000;-webkit-box-shadow:inset 0 0 10px -2px #000000;box-shadow:inset 0 0 10px -2px #000000}.site-header{z-index:10}.site-header .container{position:relative}@media screen and (max-width:768px){.site-header .r8_sec_menu_wrapper{display:none}}.site-header .r8_sec_menu_wrapper .container:after{clear:both;content:"";display:table}.site-header .r8_sec_menu_wrapper .r8-menu-secondary-menu-container{display:-webkit-box;display:-moz-box;display:box;display:-webkit-flex;display:-moz-flex;display:-ms-flexbox;display:flex;-webkit-box-align:center;-moz-box-align:center;box-align:center;-webkit-align-items:center;-moz-align-items:center;-ms-align-items:center;-o-align-items:center;align-items:center;-ms-flex-align:center;-webkit-box-lines:multiple;-moz-box-lines:multiple;box-lines:multiple;-webkit-flex-wrap:wrap;-moz-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;float:right}.site-header .r8_sec_menu_wrapper .r8-menu-secondary-menu-container ul{display:inline-block}.site-header .r8_sec_menu_wrapper .r8-menu-secondary-menu-container ul{list-style:none;margin:0;padding:0}.site-header .r8_sec_menu_wrapper .r8-menu-secondary-menu-container li{float:left;position:relative}.site-header .r8_sec_menu_wrapper .r8-menu-secondary-menu-container a{display:block;text-decoration:none}.site-header .r8_sec_menu_wrapper .r8_secondary_menu{margin:0;padding:0;list-style:none;display:-webkit-box;display:-moz-box;display:box;display:-webkit-flex;display:-moz-flex;display:-ms-flexbox;display:flex;-webkit-box-pack:end;-moz-box-pack:end;box-pack:end;-webkit-justify-content:flex-end;-moz-justify-content:flex-end;-ms-justify-content:flex-end;-o-justify-content:flex-end;justify-content:flex-end;-ms-flex-pack:end;-webkit-box-lines:multiple;-moz-box-lines:multiple;box-lines:multiple;-webkit-flex-wrap:wrap;-moz-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap}.site-header .r8_sec_menu_wrapper .r8_secondary_menu>li{color:#fff;display:inline-block;margin-left:20px}.site-header .r8_sec_menu_wrapper .r8_secondary_menu>li a{color:#fff;text-decoration:none;padding:5px 0;font-size:15px;display:inline-block}.site-header .r8_sec_menu_wrapper .r8_secondary_menu>li:first-child{margin-left:0}.site-header .r8_sec_menu_wrapper .r8_secondary_menu>li:last-child a{padding-right:0}.site-header .r8_main_header .header_wrapper{display:-webkit-box;display:-moz-box;display:box;display:-webkit-flex;display:-moz-flex;display:-ms-flexbox;display:flex;-webkit-box-lines:multiple;-moz-box-lines:multiple;box-lines:multiple;-webkit-flex-wrap:wrap;-moz-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;-webkit-box-pack:justify;-moz-box-pack:justify;box-pack:justify;-webkit-justify-content:space-between;-moz-justify-content:space-between;-ms-justify-content:space-between;-o-justify-content:space-between;justify-content:space-between;-ms-flex-pack:justify;-webkit-box-align:stretch;-moz-box-align:stretch;box-align:stretch;-webkit-align-items:stretch;-moz-align-items:stretch;-ms-align-items:stretch;-o-align-items:stretch;align-items:stretch;-ms-flex-align:stretch;position:relative}.site-header .r8_main_header .site-branding{display:-webkit-box;display:-moz-box;display:box;display:-webkit-flex;display:-moz-flex;display:-ms-flexbox;display:flex;-webkit-box-lines:multiple;-moz-box-lines:multiple;box-lines:multiple;-webkit-flex-wrap:wrap;-moz-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;-webkit-box-orient:horizontal;-moz-box-orient:horizontal;box-orient:horizontal;-webkit-box-direction:normal;-moz-box-direction:normal;box-direction:normal;-webkit-flex-direction:row;-moz-flex-direction:row;flex-direction:row;-ms-flex-direction:row;-webkit-box-align:center;-moz-box-align:center;box-align:center;-webkit-align-items:center;-moz-align-items:center;-ms-align-items:center;-o-align-items:center;align-items:center;-ms-flex-align:center}@media screen and (max-width:768px){.site-header .r8_main_header .site-branding{width:90%}}@media screen and (max-width:626px){.site-header .r8_main_header .site-branding{width:85%}}.site-header .r8_main_header .r8_main_menu{-webkit-flex-grow:2;-moz-flex-grow:2;flex-grow:2;-ms-flex-positive:2;display:-webkit-box;display:-moz-box;display:box;display:-webkit-flex;display:-moz-flex;display:-ms-flexbox;display:flex;-webkit-box-orient:horizontal;-moz-box-orient:horizontal;box-orient:horizontal;-webkit-box-direction:normal;-moz-box-direction:normal;box-direction:normal;-webkit-flex-direction:row;-moz-flex-direction:row;flex-direction:row;-ms-flex-direction:row;-webkit-box-align:center;-moz-box-align:center;box-align:center;-webkit-align-items:center;-moz-align-items:center;-ms-align-items:center;-o-align-items:center;align-items:center;-ms-flex-align:center;-webkit-box-pack:end;-moz-box-pack:end;box-pack:end;-webkit-justify-content:flex-end;-moz-justify-content:flex-end;-ms-justify-content:flex-end;-o-justify-content:flex-end;justify-content:flex-end;-ms-flex-pack:end;position:relative;z-index:5}@media screen and (max-width:768px){.site-header .r8_main_header .r8_main_menu{display:none}}.site-header .r8_main_header .main-navigation{width:auto;z-index:3}.site-header .r8_main_header .header-logo{line-height:0;padding:8px 0}@media screen and (max-width:626px){.site-header .r8_main_header .header-logo{margin:0.5em 0}}.site-header .r8_main_header .custom-logo-link{display:inline-block;line-height:0}.site-header .r8_main_header .site_description{width:220px;text-align:center;color:#b92120;line-height:1;font-family:'Open Sans',Arial,sans-serif;font-weight:400}@media screen and (max-width:768px){.site-header .r8_main_header .site_description{max-width:200px;font-size:14px}}@media screen and (max-width:626px){.site-header .r8_main_header .site_description{display:none}}.site-header .mobile_menu_btn_wrapper{display:-webkit-box;display:-moz-box;display:box;display:-webkit-flex;display:-moz-flex;display:-ms-flexbox;display:flex;-webkit-box-align:center;-moz-box-align:center;box-align:center;-webkit-align-items:center;-moz-align-items:center;-ms-align-items:center;-o-align-items:center;align-items:center;-ms-flex-align:center;padding:5px 0}.site-header a.mobile_menu_icon{height:35px;width:35px;right:0px;position:relative;z-index:102;display:none}.site-header a.mobile_menu_icon:after{clear:both;content:"";display:table}@media screen and (max-width:768px){.site-header a.mobile_menu_icon{display:block}}.site-header a.mobile_menu_icon:after,.site-header a.mobile_menu_icon:before{-webkit-transform:rotate(0deg);-moz-transform:rotate(0deg);-ms-transform:rotate(0deg);-o-transform:rotate(0deg);transform:rotate(0deg);content:'';width:35px;height:3px;background-color:#000;position:absolute}.site-header a.mobile_menu_icon:after{top:15px}.site-header a.mobile_menu_icon:before{top:5px}.site-header a.mobile_menu_icon span{content:'';position:absolute;width:35px;height:3px;background-color:#000;top:25px;opacity:1}.site-header .mobile_menu{display:none}@media screen and (max-width:768px){.site-branding{padding:10px 0}}.site_footer a{color:inherit}.sec_footer_menu a{font-weight:normal}.container,.r8_container{margin:0 auto;max-width:1280px;padding:0 50px}@media screen and (max-width:768px){.container,.r8_container{padding:0 30px}}@media screen and (max-width:626px){.container,.r8_container{padding:0 20px}}.container{width:100%}.container:after{clear:both;content:"";display:table}.r8_flexible_content_section{padding:50px 0}@media screen and (max-width:768px){.r8_flexible_content_section{padding:30px 0}}@media screen and (max-width:626px){.r8_flexible_content_section{padding:20px 0}}.r8_wysiwig_content:after{clear:both;content:"";display:table}.r8_wysiwig_content>:first-child{margin-top:0}.r8_wysiwig_content>:last-child{margin-bottom:0}.r8_wysiwig_content h2{margin:0}.r8_carousel_section{padding-bottom:50px}.r8_carousel_section .r8_carousel{padding:20px 0 20px}@media screen and (max-width:626px){.r8_carousel_section .r8_carousel{padding:0}}.r8_carousel_section .r8_carousel .r8_carousel_item_image img{margin:0 auto}.r8_carousel_section .r8_carousel .r8_carousel_item{height:auto;padding:10px;position:relative}.r8_carousel_section .r8_carousel .r8_carousel_item>:first-child{margin-top:0}.r8_carousel_section .r8_carousel .r8_carousel_item>:last-child{margin-bottom:0}.r8_carousel_section .r8_carousel .r8_carousel_content{display:-webkit-box;display:-moz-box;display:box;display:-webkit-flex;display:-moz-flex;display:-ms-flexbox;display:flex;-webkit-box-lines:multiple;-moz-box-lines:multiple;box-lines:multiple;-webkit-flex-wrap:wrap;-moz-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;-webkit-box-align:center;-moz-box-align:center;box-align:center;-webkit-align-items:center;-moz-align-items:center;-ms-align-items:center;-o-align-items:center;align-items:center;-ms-flex-align:center;-webkit-box-pack:center;-moz-box-pack:center;box-pack:center;-webkit-justify-content:center;-moz-justify-content:center;-ms-justify-content:center;-o-justify-content:center;justify-content:center;-ms-flex-pack:center;-webkit-box-orient:vertical;-moz-box-orient:vertical;box-orient:vertical;-webkit-box-direction:normal;-moz-box-direction:normal;box-direction:normal;-webkit-flex-direction:column;-moz-flex-direction:column;flex-direction:column;-ms-flex-direction:column;height:100%;width:100%;min-height:100px;padding:10px 15px}.r8_hero{color:#fff;position:relative}.r8_hero .r8_hero_copy>:first-child{margin-top:0}.r8_hero .r8_hero_copy>:last-child{margin-bottom:0}.r8_hero_content{display:-webkit-box;display:-moz-box;display:box;display:-webkit-flex;display:-moz-flex;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-moz-box-orient:vertical;box-orient:vertical;-webkit-box-direction:normal;-moz-box-direction:normal;box-direction:normal;-webkit-flex-direction:column;-moz-flex-direction:column;flex-direction:column;-ms-flex-direction:column;height:100%}.r8_hero_content>.container{width:100%}.r8_image_bg_hero{position:relative;overflow:hidden;background-position:center;background-size:cover;background-repeat:no-repeat}.r8_image_bg_hero.hero_content_dep_height{padding:80px 0}.r8_image_bg_hero .two_columns_content .hc_section{float:left;display:block;margin-right:2.35765%;width:48.82117%}.r8_image_bg_hero .two_columns_content .hc_section:last-child{margin-right:0}.r8_image_bg_hero .two_columns_content .hc_section:nth-child(2n){margin-right:0}.r8_image_bg_hero .two_columns_content .hc_section:nth-child(2n+1){clear:left}@media screen and (max-width:626px){.r8_image_bg_hero .two_columns_content .hc_section{float:left;display:block;margin-right:7.42297%;width:100%}.r8_image_bg_hero .two_columns_content .hc_section:last-child{margin-right:0}.r8_image_bg_hero .two_columns_content .hc_section:nth-child(2n){margin-right:2.35765%}.r8_image_bg_hero .two_columns_content .hc_section:nth-child(2n+1){clear:none}.r8_image_bg_hero .two_columns_content .hc_section:nth-child(n){margin-right:0}.r8_image_bg_hero .two_columns_content .hc_section:nth-child(n+1){clear:left}.r8_image_bg_hero .two_columns_content .hc_section.hc2_section{margin-top:50px}}.r8_image_bg_hero .container{display:-webkit-box;display:-moz-box;display:box;display:-webkit-flex;display:-moz-flex;display:-ms-flexbox;display:flex;-webkit-box-orient:horizontal;-moz-box-orient:horizontal;box-orient:horizontal;-webkit-box-direction:normal;-moz-box-direction:normal;box-direction:normal;-webkit-flex-direction:row;-moz-flex-direction:row;flex-direction:row;-ms-flex-direction:row;-webkit-box-lines:multiple;-moz-box-lines:multiple;box-lines:multiple;-webkit-flex-wrap:wrap;-moz-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;-webkit-box-align:center;-moz-box-align:center;box-align:center;-webkit-align-items:center;-moz-align-items:center;-ms-align-items:center;-o-align-items:center;align-items:center;-ms-flex-align:center;-webkit-flex-grow:1;-moz-flex-grow:1;flex-grow:1;-ms-flex-positive:1}.r8_image_bg_hero .hc_section{width:100%}.r8_flexible_content_section{background-position:center center;background-repeat:no-repeat;background-size:cover;margin:0 auto}.r8_flexible_content_section .r8_container{background-position:center center;background-repeat:no-repeat;background-size:cover}.r8_white_font_color{color:#fff}.r8_dark_gray_font_color{color:#696969}.r8_dark_gray_font_color h1:not(.r8_section_title),.r8_dark_gray_font_color h2:not(.r8_section_title){color:#696969}button,input[type='submit']{text-transform:uppercase;font-weight:bold;border-radius:5px;font-size:15px;margin:13px;margin-left:0;background-color:#b92120;box-shadow:none;border:none;text-shadow:none;color:white;padding:8px 20px;box-shadow:none;border-radius:0px;font-size:15px;font-weight:700}input[type="search"]{color:#666;border:1px solid #ccc}input[type="search"]{padding:5px 4px}.top_header_search_form .search-form{display:-webkit-box;display:-moz-box;display:box;display:-webkit-flex;display:-moz-flex;display:-ms-flexbox;display:flex;-webkit-box-align:center;-moz-box-align:center;box-align:center;-webkit-align-items:center;-moz-align-items:center;-ms-align-items:center;-o-align-items:center;align-items:center;-ms-flex-align:center}@media screen and (max-width:626px){.top_header_search_form .search-form{-webkit-box-lines:multiple;-moz-box-lines:multiple;box-lines:multiple;-webkit-flex-wrap:wrap;-moz-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;display:block}}.top_header_search_form .search-form label{-webkit-flex-grow:1;-moz-flex-grow:1;flex-grow:1;-ms-flex-positive:1}.top_header_search_form .search-form .search-field{width:100%}@media screen and (max-width:626px){.top_header_search_form .search-form .search-field{width:100%}}.top_header_search_form .search-form .search-submit{margin:0;margin-left:13px;box-shadow:none;text-shadow:none}@media screen and (max-width:626px){.top_header_search_form .search-form .search-submit{margin-top:10px;margin-left:0px}}input[type="search"]{-webkit-appearance:none}a{color:#b92120;text-decoration:none}.main-navigation{clear:both;display:block;float:left;width:100%}.main-navigation ul{display:none;list-style:none;margin:0;padding-left:0}.main-navigation ul ul{box-shadow:0 3px 3px rgba(0,0,0,0.2);float:left;position:absolute;top:1.5em;left:-999em;z-index:99999}.main-navigation ul ul ul{left:-999em;top:0}.main-navigation ul ul a{width:200px}.main-navigation li{float:left;position:relative}.main-navigation a{display:block;text-decoration:none}.menu-toggle{display:block}@media screen and (min-width:37.5em){.menu-toggle{display:none}.main-navigation ul{display:block}}.screen-reader-text{clip:rect(1px,1px,1px,1px);position:absolute!important;height:1px;width:1px;overflow:hidden}.aligncenter{clear:both;display:block;margin-left:auto;margin-right:auto}.site-header:before:after,.site-header:after:after,.site-content:before:after,.site-content:after:after{clear:both;content:"";display:table}.site-header:after,.site-content:after{clear:both}iframe{max-width:100%}html{box-sizing:border-box}*,*::after,*::before{box-sizing:inherit}html{font-family:sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%}body{margin:0}header,main,nav{display:block}a{background-color:transparent}strong{font-weight:bold}h1{font-size:2em;margin:0.67em 0}img{border:0}svg:not(:root){overflow:hidden}button,input{color:inherit;font:inherit;margin:0}button{overflow:visible}button{text-transform:none}button,input[type="submit"]{-webkit-appearance:button}button::-moz-focus-inner,input::-moz-focus-inner{border:0;padding:0}input{line-height:normal}input[type="checkbox"]{box-sizing:border-box;padding:0}input[type="search"]::-webkit-search-cancel-button,input[type="search"]::-webkit-search-decoration{-webkit-appearance:none}.r8_carousel_section{padding-bottom:50px}.r8_carousel_section .r8_carousel{padding:20px 0 20px}@media screen and (max-width:626px){.r8_carousel_section .r8_carousel{padding:0}}body,button,input{color:#404040;font-family:"Lusitana",serif;font-size:16px;font-size:1rem;line-height:1.5}h1,h2,h4{clear:both}h1,h2,h4{font-family:'Barlow Semi Condensed',sans-serif;font-weight:500;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;text-transform:uppercase}p{margin-bottom:1.5em}i{font-style:italic}html{box-sizing:border-box}*,*:before,*:after{box-sizing:inherit}body{background:#fff}ul{margin:0 0 1.5em 3em}ul{list-style:disc}li>ul{margin-bottom:0;margin-left:1.5em}img{height:auto;max-width:100%}.site-header .r8_secondary_menu li,.site-header .r8_secondary_menu a,.site-header .primary_menu li,.site-header .primary_menu a{font-family:'Barlow Semi Condensed',sans-serif;font-weight:normal;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.site-header a.mobile_menu_icon{width:23px}.site-header a.mobile_menu_icon:after,.site-header a.mobile_menu_icon:before,.site-header a.mobile_menu_icon span{width:23px;height:2px}.site-header a.mobile_menu_icon:before{top:9px}.site-header a.mobile_menu_icon span{top:21px}@media screen and (max-width:768px){.site-header .site-branding{padding:2px 0}}@media screen and (max-width:626px){.site-header .site-branding{padding:2px 0}}.site-header .header_search{margin-left:10px}.site-header .header_search .search_icon{font-size:16px;margin-top:2px}.site-header .r8_main_header .header-logo{padding-bottom:12px}@media screen and (max-width:626px){.site-header .r8_main_header .header-logo{margin:0}}.site-header .r8_secondary_menu>li>a{text-transform:uppercase}.site_footer .footer_menu_container .sec_footer_menu a{font-family:'Barlow Semi Condensed',sans-serif;font-weight:500;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;text-transform:uppercase}.site_footer .footer_menu_container .sec_footer_menu>li>a{font-size:20px}@media screen and (max-width:768px){.site_footer .footer_menu_container .sec_footer_menu>li>a{font-size:18px}}.r8_hero{position:relative}.r8_hero .r8_wysiwig_content{max-width:650px}button,input[type="submit"]{border:1px solid;border-color:#ccc #ccc #bbb;border-radius:3px;background:#e6e6e6;color:rgba(0,0,0,0.8);font-size:12px;font-size:.75rem;line-height:1;padding:.6em 1em .4em}input[type="search"]{color:#666;border:1px solid #ccc;border-radius:3px;padding:3px}body input,body input[type="search"]{font-family:'Barlow Semi Condensed',sans-serif;font-weight:normal;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;padding-left:20px}body input::-webkit-input-placeholder,body input[type="search"]::-webkit-input-placeholder{font-weight:400;text-transform:uppercase}body input::-moz-placeholder,body input[type="search"]::-moz-placeholder{font-weight:400;text-transform:uppercase}body input:-ms-input-placeholder,body input[type="search"]:-ms-input-placeholder{font-weight:400;text-transform:uppercase}body input:-moz-placeholder,body input[type="search"]:-moz-placeholder{font-weight:400;text-transform:uppercase}a{color:#4169e1}.main-navigation{clear:both;display:block;float:left;width:100%}.main-navigation ul{display:none;list-style:none;margin:0;padding-left:0}.main-navigation ul ul{box-shadow:0 3px 3px rgba(0,0,0,0.2);float:left;position:absolute;top:100%;left:-999em;z-index:99999}.main-navigation ul ul ul{left:0;top:0;position:relative}.main-navigation ul ul ul:before{content:none;display:none}.main-navigation ul ul ul>li>a{padding-left:25px}.main-navigation ul ul a{width:200px}.main-navigation li{float:left;position:relative}.main-navigation a{display:block;text-decoration:none}.menu-toggle{display:block}@media screen and (min-width:37.5em){.menu-toggle{display:none}.main-navigation ul{display:block}}.screen-reader-text{border:0;clip:rect(1px,1px,1px,1px);clip-path:inset(50%);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute!important;width:1px;word-wrap:normal!important}.aligncenter{clear:both;display:block;margin-left:auto;margin-right:auto}.site-header:before,.site-header:after,.site-content:before,.site-content:after{content:"";display:table;table-layout:fixed}.site-header:after,.site-content:after{clear:both}iframe{max-width:100%}.custom-logo-link{display:inline-block}:root{--animate-duration:1s;--animate-delay:1s;--animate-repeat:1}</style><link rel="preload" data-rocket-preload as="image" href="https://citrine.io/wp-content/uploads/2023/11/refresh-home-hero-bgbase.jpg" fetchpriority="high">
	<meta name="description" content="Citrine Informatics is the world leader in generative AI for materials and chemicals product development." />
	<link rel="canonical" href="https://citrine.io/" />
	<meta property="og:locale" content="en_US" />
	<meta property="og:type" content="website" />
	<meta property="og:title" content="Home Page" />
	<meta property="og:description" content="Citrine Informatics is the world leader in generative AI for materials and chemicals product development." />
	<meta property="og:url" content="https://citrine.io/" />
	<meta property="og:site_name" content="Citrine Informatics" />
	<meta property="article:modified_time" content="2026-06-20T16:08:24+00:00" />
	<meta property="og:image" content="https://citrine.io/wp-content/uploads/2023/12/Screenshot-2023-12-05-at-4.18.58 PM.png" />
	<meta property="og:image:width" content="2060" />
	<meta property="og:image:height" content="932" />
	<meta property="og:image:type" content="image/png" />
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:image" content="https://citrine.io/wp-content/uploads/2023/12/Screenshot-2023-12-05-at-4.18.58 PM.png" />
	<meta name="twitter:site" content="@citrine_io" />
	<meta name="msvalidate.01" content="352C4EF44E6DC90805E0844CA511FCF8" />
	<meta name="google-site-verification" content="TwpMzEnl5E1TIkmIEiUWmk3ZKNjFie6XK5qdEPc2v-c" />
	<!-- / Yoast SEO Premium plugin. -->


<link rel='dns-prefetch' href='//js.hs-scripts.com' />
<link rel='dns-prefetch' href='//use.fontawesome.com' />
<link rel='dns-prefetch' href='//fonts.googleapis.com' />
<link href='https://fonts.gstatic.com' crossorigin rel='preconnect' />
<link rel="alternate" type="application/rss+xml" title="Citrine Informatics &raquo; Feed" href="https://citrine.io/feed/" />
<style id="wp-img-auto-sizes-contain-inline-css">
img:is([sizes=auto i],[sizes^="auto," i]){contain-intrinsic-size:3000px 1500px}
/*# sourceURL=wp-img-auto-sizes-contain-inline-css */
</style>
<style id="wp-block-library-inline-css">
:root{--wp-block-synced-color:#7a00df;--wp-block-synced-color--rgb:122,0,223;--wp-bound-block-color:var(--wp-block-synced-color);--wp-editor-canvas-background:#ddd;--wp-admin-theme-color:#007cba;--wp-admin-theme-color--rgb:0,124,186;--wp-admin-theme-color-darker-10:#006ba1;--wp-admin-theme-color-darker-10--rgb:0,107,160.5;--wp-admin-theme-color-darker-20:#005a87;--wp-admin-theme-color-darker-20--rgb:0,90,135;--wp-admin-border-width-focus:2px}@media (min-resolution:192dpi){:root{--wp-admin-border-width-focus:1.5px}}.wp-element-button{cursor:pointer}:root .has-very-light-gray-background-color{background-color:#eee}:root .has-very-dark-gray-background-color{background-color:#313131}:root .has-very-light-gray-color{color:#eee}:root .has-very-dark-gray-color{color:#313131}:root .has-vivid-green-cyan-to-vivid-cyan-blue-gradient-background{background:linear-gradient(135deg,#00d084,#0693e3)}:root .has-purple-crush-gradient-background{background:linear-gradient(135deg,#34e2e4,#4721fb 50%,#ab1dfe)}:root .has-hazy-dawn-gradient-background{background:linear-gradient(135deg,#faaca8,#dad0ec)}:root .has-subdued-olive-gradient-background{background:linear-gradient(135deg,#fafae1,#67a671)}:root .has-atomic-cream-gradient-background{background:linear-gradient(135deg,#fdd79a,#004a59)}:root .has-nightshade-gradient-background{background:linear-gradient(135deg,#330968,#31cdcf)}:root .has-midnight-gradient-background{background:linear-gradient(135deg,#020381,#2874fc)}:root{--wp--preset--font-size--normal:16px;--wp--preset--font-size--huge:42px}.has-regular-font-size{font-size:1em}.has-larger-font-size{font-size:2.625em}.has-normal-font-size{font-size:var(--wp--preset--font-size--normal)}.has-huge-font-size{font-size:var(--wp--preset--font-size--huge)}:root .has-text-align-center{text-align:center}:root .has-text-align-left{text-align:left}:root .has-text-align-right{text-align:right}.has-fit-text{white-space:nowrap!important}#end-resizable-editor-section{display:none}.aligncenter{clear:both}.items-justified-left{justify-content:flex-start}.items-justified-center{justify-content:center}.items-justified-right{justify-content:flex-end}.items-justified-space-between{justify-content:space-between}.screen-reader-text{word-wrap:normal!important;border:0;clip-path:inset(50%);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;width:1px}.screen-reader-text:focus{background-color:#ddd;clip-path:none;color:#444;display:block;font-size:1em;height:auto;left:5px;line-height:normal;padding:15px 23px 14px;text-decoration:none;top:5px;width:auto;z-index:100000}html :where(.has-border-color){border-style:solid}html :where([style*=border-color]){border-style:solid}html :where([style*=border-top-color]){border-top-style:solid}html :where([style*=border-right-color]){border-right-style:solid}html :where([style*=border-bottom-color]){border-bottom-style:solid}html :where([style*=border-left-color]){border-left-style:solid}html :where([style*=border-width]){border-style:solid}html :where([style*=border-top-width]){border-top-style:solid}html :where([style*=border-right-width]){border-right-style:solid}html :where([style*=border-bottom-width]){border-bottom-style:solid}html :where([style*=border-left-width]){border-left-style:solid}html :where(img[class*=wp-image-]){height:auto;max-width:100%}:where(figure){margin:0 0 1em}html :where(.is-position-sticky){--wp-admin--admin-bar--position-offset:var(--wp-admin--admin-bar--height,0px)}@media screen and (max-width:600px){html :where(.is-position-sticky){--wp-admin--admin-bar--position-offset:0px}}

/*# sourceURL=/wp-includes/css/dist/block-library/common.min.css */
</style>
<style id="classic-theme-styles-inline-css">
/*! This file is auto-generated */
.wp-block-button__link{color:#fff;background-color:#32373c;border-radius:9999px;box-shadow:none;text-decoration:none;padding:calc(.667em + 2px) calc(1.333em + 2px);font-size:1.125em}.wp-block-file__button{background:#32373c;color:#fff;text-decoration:none}
/*# sourceURL=/wp-includes/css/classic-themes.min.css */
</style>

<style id="global-styles-inline-css">
:root{--wp--preset--aspect-ratio--square: 1;--wp--preset--aspect-ratio--4-3: 4/3;--wp--preset--aspect-ratio--3-4: 3/4;--wp--preset--aspect-ratio--3-2: 3/2;--wp--preset--aspect-ratio--2-3: 2/3;--wp--preset--aspect-ratio--16-9: 16/9;--wp--preset--aspect-ratio--9-16: 9/16;--wp--preset--color--black: #000000;--wp--preset--color--cyan-bluish-gray: #abb8c3;--wp--preset--color--white: #ffffff;--wp--preset--color--pale-pink: #f78da7;--wp--preset--color--vivid-red: #cf2e2e;--wp--preset--color--luminous-vivid-orange: #ff6900;--wp--preset--color--luminous-vivid-amber: #fcb900;--wp--preset--color--light-green-cyan: #7bdcb5;--wp--preset--color--vivid-green-cyan: #00d084;--wp--preset--color--pale-cyan-blue: #8ed1fc;--wp--preset--color--vivid-cyan-blue: #0693e3;--wp--preset--color--vivid-purple: #9b51e0;--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple: linear-gradient(135deg,rgb(6,147,227) 0%,rgb(155,81,224) 100%);--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan: linear-gradient(135deg,rgb(122,220,180) 0%,rgb(0,208,130) 100%);--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange: linear-gradient(135deg,rgb(252,185,0) 0%,rgb(255,105,0) 100%);--wp--preset--gradient--luminous-vivid-orange-to-vivid-red: linear-gradient(135deg,rgb(255,105,0) 0%,rgb(207,46,46) 100%);--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray: linear-gradient(135deg,rgb(238,238,238) 0%,rgb(169,184,195) 100%);--wp--preset--gradient--cool-to-warm-spectrum: linear-gradient(135deg,rgb(74,234,220) 0%,rgb(151,120,209) 20%,rgb(207,42,186) 40%,rgb(238,44,130) 60%,rgb(251,105,98) 80%,rgb(254,248,76) 100%);--wp--preset--gradient--blush-light-purple: linear-gradient(135deg,rgb(255,206,236) 0%,rgb(152,150,240) 100%);--wp--preset--gradient--blush-bordeaux: linear-gradient(135deg,rgb(254,205,165) 0%,rgb(254,45,45) 50%,rgb(107,0,62) 100%);--wp--preset--gradient--luminous-dusk: linear-gradient(135deg,rgb(255,203,112) 0%,rgb(199,81,192) 50%,rgb(65,88,208) 100%);--wp--preset--gradient--pale-ocean: linear-gradient(135deg,rgb(255,245,203) 0%,rgb(182,227,212) 50%,rgb(51,167,181) 100%);--wp--preset--gradient--electric-grass: linear-gradient(135deg,rgb(202,248,128) 0%,rgb(113,206,126) 100%);--wp--preset--gradient--midnight: linear-gradient(135deg,rgb(2,3,129) 0%,rgb(40,116,252) 100%);--wp--preset--font-size--small: 13px;--wp--preset--font-size--medium: 20px;--wp--preset--font-size--large: 36px;--wp--preset--font-size--x-large: 42px;--wp--preset--spacing--20: 0.44rem;--wp--preset--spacing--30: 0.67rem;--wp--preset--spacing--40: 1rem;--wp--preset--spacing--50: 1.5rem;--wp--preset--spacing--60: 2.25rem;--wp--preset--spacing--70: 3.38rem;--wp--preset--spacing--80: 5.06rem;--wp--preset--shadow--natural: 6px 6px 9px rgba(0, 0, 0, 0.2);--wp--preset--shadow--deep: 12px 12px 50px rgba(0, 0, 0, 0.4);--wp--preset--shadow--sharp: 6px 6px 0px rgba(0, 0, 0, 0.2);--wp--preset--shadow--outlined: 6px 6px 0px -3px rgb(255, 255, 255), 6px 6px rgb(0, 0, 0);--wp--preset--shadow--crisp: 6px 6px 0px rgb(0, 0, 0);}:where(body) { margin: 0; }:where(.is-layout-flex){gap: 0.5em;}:where(.is-layout-grid){gap: 0.5em;}body .is-layout-flex{display: flex;}.is-layout-flex{flex-wrap: wrap;align-items: center;}.is-layout-flex > :is(*, div){margin: 0;}body .is-layout-grid{display: grid;}.is-layout-grid > :is(*, div){margin: 0;}body{padding-top: 0px;padding-right: 0px;padding-bottom: 0px;padding-left: 0px;}:root :where(.wp-element-button, .wp-block-button__link){background-color: #32373c;border-width: 0;color: #fff;font-family: inherit;font-size: inherit;font-style: inherit;font-weight: inherit;letter-spacing: inherit;line-height: inherit;padding-top: calc(0.667em + 2px);padding-right: calc(1.333em + 2px);padding-bottom: calc(0.667em + 2px);padding-left: calc(1.333em + 2px);text-decoration: none;text-transform: inherit;}.has-black-color{color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-color{color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-color{color: var(--wp--preset--color--white) !important;}.has-pale-pink-color{color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-color{color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-color{color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-color{color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-color{color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-color{color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-color{color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-color{color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-color{color: var(--wp--preset--color--vivid-purple) !important;}.has-black-background-color{background-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-background-color{background-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-background-color{background-color: var(--wp--preset--color--white) !important;}.has-pale-pink-background-color{background-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-background-color{background-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-background-color{background-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-background-color{background-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-background-color{background-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-background-color{background-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-background-color{background-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-background-color{background-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-background-color{background-color: var(--wp--preset--color--vivid-purple) !important;}.has-black-border-color{border-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-border-color{border-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-border-color{border-color: var(--wp--preset--color--white) !important;}.has-pale-pink-border-color{border-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-border-color{border-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-border-color{border-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-border-color{border-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-border-color{border-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-border-color{border-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-border-color{border-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-border-color{border-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-border-color{border-color: var(--wp--preset--color--vivid-purple) !important;}.has-vivid-cyan-blue-to-vivid-purple-gradient-background{background: var(--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple) !important;}.has-light-green-cyan-to-vivid-green-cyan-gradient-background{background: var(--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan) !important;}.has-luminous-vivid-amber-to-luminous-vivid-orange-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange) !important;}.has-luminous-vivid-orange-to-vivid-red-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-orange-to-vivid-red) !important;}.has-very-light-gray-to-cyan-bluish-gray-gradient-background{background: var(--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray) !important;}.has-cool-to-warm-spectrum-gradient-background{background: var(--wp--preset--gradient--cool-to-warm-spectrum) !important;}.has-blush-light-purple-gradient-background{background: var(--wp--preset--gradient--blush-light-purple) !important;}.has-blush-bordeaux-gradient-background{background: var(--wp--preset--gradient--blush-bordeaux) !important;}.has-luminous-dusk-gradient-background{background: var(--wp--preset--gradient--luminous-dusk) !important;}.has-pale-ocean-gradient-background{background: var(--wp--preset--gradient--pale-ocean) !important;}.has-electric-grass-gradient-background{background: var(--wp--preset--gradient--electric-grass) !important;}.has-midnight-gradient-background{background: var(--wp--preset--gradient--midnight) !important;}.has-small-font-size{font-size: var(--wp--preset--font-size--small) !important;}.has-medium-font-size{font-size: var(--wp--preset--font-size--medium) !important;}.has-large-font-size{font-size: var(--wp--preset--font-size--large) !important;}.has-x-large-font-size{font-size: var(--wp--preset--font-size--x-large) !important;}
/*# sourceURL=global-styles-inline-css */
</style>

<link data-minify="1" rel='preload'  href='https://citrine.io/wp-content/cache/min/1/wp-content/plugins/announcer/public/css/style.css?ver=1785874338' data-rocket-async="style" as="style" onload="this.onload=null;this.rel='stylesheet'" onerror="this.removeAttribute('data-rocket-async')"  media='all' />
<link data-minify="1" rel='preload'  href='https://citrine.io/wp-content/cache/min/1/wp-content/plugins/cookie-law-info/legacy/public/css/cookie-law-info-public.css?ver=1785874338' data-rocket-async="style" as="style" onload="this.onload=null;this.rel='stylesheet'" onerror="this.removeAttribute('data-rocket-async')"  media='all' />
<link data-minify="1" rel='preload'  href='https://citrine.io/wp-content/cache/min/1/wp-content/plugins/cookie-law-info/legacy/public/css/cookie-law-info-gdpr.css?ver=1785874338' data-rocket-async="style" as="style" onload="this.onload=null;this.rel='stylesheet'" onerror="this.removeAttribute('data-rocket-async')"  media='all' />
<link data-minify="1" rel='preload'  href='https://citrine.io/wp-content/cache/min/1/wp-content/plugins/floating-button-call-to-action/assets/cta-kit.css?ver=1785874338' data-rocket-async="style" as="style" onload="this.onload=null;this.rel='stylesheet'" onerror="this.removeAttribute('data-rocket-async')"  media='all' />
<link data-minify="1" rel='preload'  href='https://citrine.io/wp-content/cache/min/1/wp-includes/css/dashicons.min.css?ver=1785874338' data-rocket-async="style" as="style" onload="this.onload=null;this.rel='stylesheet'" onerror="this.removeAttribute('data-rocket-async')"  media='all' />
<link data-minify="1" rel='preload'  href='https://citrine.io/wp-content/cache/min/1/wp-content/uploads/maxmegamenu/style.css?ver=1785874338' data-rocket-async="style" as="style" onload="this.onload=null;this.rel='stylesheet'" onerror="this.removeAttribute('data-rocket-async')"  media='all' />
<link data-minify="1" rel='preload'  href='https://citrine.io/wp-content/cache/background-css/1/citrine.io/wp-content/cache/min/1/wp-content/themes/inn8ly-builder/style.css?ver=1785874338&wpr_t=1787766826' data-rocket-async="style" as="style" onload="this.onload=null;this.rel='stylesheet'" onerror="this.removeAttribute('data-rocket-async')"  media='all' />
<link data-minify="1" rel='preload'  href='https://citrine.io/wp-content/cache/background-css/1/citrine.io/wp-content/cache/min/1/wp-content/themes/citrine/style.css?ver=1785874338&wpr_t=1787766826' data-rocket-async="style" as="style" onload="this.onload=null;this.rel='stylesheet'" onerror="this.removeAttribute('data-rocket-async')"  media='all' />

<link rel='preload'  href='https://citrine.io/wp-content/themes/citrine/js/vendor/tooltipster.bundle.min.css?ver=7.0.4' data-rocket-async="style" as="style" onload="this.onload=null;this.rel='stylesheet'" onerror="this.removeAttribute('data-rocket-async')"  media='all' />
<link rel='preload'  href='https://citrine.io/wp-content/themes/citrine/js/vendor/tooltipster-sideTip-shadow.min.css?ver=7.0.4' data-rocket-async="style" as="style" onload="this.onload=null;this.rel='stylesheet'" onerror="this.removeAttribute('data-rocket-async')"  media='all' />
<link data-minify="1" rel='preload'  href='https://citrine.io/wp-content/cache/background-css/1/citrine.io/wp-content/cache/min/1/wp-content/themes/inn8ly-builder/js/vendor/fancyBox/jquery.fancybox.css?ver=1785874338&wpr_t=1787766826' data-rocket-async="style" as="style" onload="this.onload=null;this.rel='stylesheet'" onerror="this.removeAttribute('data-rocket-async')"  media='all' />
<link rel='preload'  href='https://citrine.io/wp-content/themes/inn8ly-builder/css/swiper.min.css?ver=7.0.4' data-rocket-async="style" as="style" onload="this.onload=null;this.rel='stylesheet'" onerror="this.removeAttribute('data-rocket-async')"  media='all' />
<link data-minify="1" rel='preload'  href='https://citrine.io/wp-content/cache/min/1/wp-content/themes/inn8ly-builder/css/slick.css?ver=1785874338' data-rocket-async="style" as="style" onload="this.onload=null;this.rel='stylesheet'" onerror="this.removeAttribute('data-rocket-async')"  media='all' />
<link data-minify="1" rel='preload'  href='https://citrine.io/wp-content/cache/background-css/1/citrine.io/wp-content/cache/min/1/wp-content/themes/inn8ly-builder/css/slick-theme.css?ver=1785874338&wpr_t=1787766826' data-rocket-async="style" as="style" onload="this.onload=null;this.rel='stylesheet'" onerror="this.removeAttribute('data-rocket-async')"  media='all' />
<link data-minify="1" rel='preload'  href='https://citrine.io/wp-content/cache/min/1/wp-content/themes/inn8ly-builder/js/vendor/mmenu/css/jquery.mmenu.all.css?ver=1785874338' data-rocket-async="style" as="style" onload="this.onload=null;this.rel='stylesheet'" onerror="this.removeAttribute('data-rocket-async')"  media='all' />
<link rel='preload'  href='https://citrine.io/wp-content/themes/inn8ly-builder/js/vendor/featherlight.min.css?ver=7.0.4' data-rocket-async="style" as="style" onload="this.onload=null;this.rel='stylesheet'" onerror="this.removeAttribute('data-rocket-async')"  media='all' />

<link data-minify="1" rel='preload'  href='https://citrine.io/wp-content/cache/min/1/wp-content/plugins/easy-fancybox/fancybox/1.5.4/jquery.fancybox.css?ver=1785874338' data-rocket-async="style" as="style" onload="this.onload=null;this.rel='stylesheet'" onerror="this.removeAttribute('data-rocket-async')"  media='screen' />
<link data-minify="1" rel='preload'  href='https://citrine.io/wp-content/cache/min/1/wp-content/plugins/category-ajax-filter-pro/assets/css/common/common.css?ver=1785874338' data-rocket-async="style" as="style" onload="this.onload=null;this.rel='stylesheet'" onerror="this.removeAttribute('data-rocket-async')"  media='all' />
<style id="rocket-lazyload-inline-css">
.rll-youtube-player{position:relative;padding-bottom:56.23%;height:0;overflow:hidden;max-width:100%;}.rll-youtube-player:focus-within{outline: 2px solid currentColor;outline-offset: 5px;}.rll-youtube-player iframe{position:absolute;top:0;left:0;width:100%;height:100%;z-index:100;background:0 0}.rll-youtube-player img{bottom:0;display:block;left:0;margin:auto;max-width:100%;width:100%;position:absolute;right:0;top:0;border:none;height:auto;-webkit-transition:.4s all;-moz-transition:.4s all;transition:.4s all}.rll-youtube-player img:hover{-webkit-filter:brightness(75%)}.rll-youtube-player .play{height:100%;width:100%;left:0;top:0;position:absolute;background:var(--wpr-bg-c389d831-2312-471f-88f9-c02acea03a77) no-repeat center;background-color: transparent !important;cursor:pointer;border:none;}
/*# sourceURL=rocket-lazyload-inline-css */
</style>
<script type="text/rocketlazyloadscript" id="jquery-core-js" data-rocket-src="https://citrine.io/wp-includes/js/jquery/jquery.min.js?ver=3.7.1" data-rocket-defer defer></script>
<script type="text/rocketlazyloadscript" id="jquery-migrate-js" data-rocket-src="https://citrine.io/wp-includes/js/jquery/jquery-migrate.min.js?ver=3.4.1" data-rocket-defer defer></script>
<script id="cookie-law-info-js-extra">
var Cli_Data = {"nn_cookie_ids":[],"cookielist":[],"non_necessary_cookies":[],"ccpaEnabled":"","ccpaRegionBased":"","ccpaBarEnabled":"1","strictlyEnabled":["necessary","obligatoire"],"ccpaType":"gdpr","js_blocking":"1","custom_integration":"","triggerDomRefresh":"","secure_cookies":""};
var cli_cookiebar_settings = {"animate_speed_hide":"500","animate_speed_show":"500","background":"#FFF","border":"#b1a6a6c2","border_on":"","button_1_button_colour":"#289324","button_1_button_hover":"#20761d","button_1_link_colour":"#fff","button_1_as_button":"1","button_1_new_win":"","button_2_button_colour":"#333","button_2_button_hover":"#292929","button_2_link_colour":"#444","button_2_as_button":"","button_2_hidebar":"","button_3_button_colour":"#000000","button_3_button_hover":"#000000","button_3_link_colour":"#fff","button_3_as_button":"1","button_3_new_win":"","button_4_button_colour":"#000","button_4_button_hover":"#000000","button_4_link_colour":"#333333","button_4_as_button":"","button_7_button_colour":"#61a229","button_7_button_hover":"#4e8221","button_7_link_colour":"#fff","button_7_as_button":"1","button_7_new_win":"","font_family":"inherit","header_fix":"","notify_animate_hide":"1","notify_animate_show":"","notify_div_id":"#cookie-law-info-bar","notify_position_horizontal":"right","notify_position_vertical":"bottom","scroll_close":"","scroll_close_reload":"","accept_close_reload":"","reject_close_reload":"","showagain_tab":"","showagain_background":"#fff","showagain_border":"#000","showagain_div_id":"#cookie-law-info-again","showagain_x_position":"100px","text":"#333333","show_once_yn":"","show_once":"10000","logging_on":"","as_popup":"","popup_overlay":"1","bar_heading_text":"","cookie_bar_as":"banner","popup_showagain_position":"bottom-right","widget_position":"left"};
var log_object = {"ajax_url":"https://citrine.io/wp-admin/admin-ajax.php"};
//# sourceURL=cookie-law-info-js-extra
</script>
<script type="text/rocketlazyloadscript" data-minify="1" id="cookie-law-info-js" data-rocket-src="https://citrine.io/wp-content/cache/min/1/wp-content/plugins/cookie-law-info/legacy/public/js/cookie-law-info-public.js?ver=1785874338" data-rocket-defer defer></script>
<script type="text/rocketlazyloadscript" data-minify="1" id="fontawesome-js" data-rocket-src="https://citrine.io/wp-content/cache/min/1/releases/v5.0.6/js/all.js?ver=1785874339" data-rocket-defer defer></script>
<script type="text/rocketlazyloadscript" data-minify="1" id="fontawesome-4-shim-js" data-rocket-src="https://citrine.io/wp-content/cache/min/1/releases/v5.0.6/js/v4-shims.js?ver=1785874339" data-rocket-defer defer></script>
			<!-- DO NOT COPY THIS SNIPPET! Start of Page Analytics Tracking for HubSpot WordPress plugin v11.3.45-->
			<script type="text/rocketlazyloadscript" class="hsq-set-content-id" data-content-id="standard-page">
				var _hsq = _hsq || [];
				_hsq.push(["setContentType", "standard-page"]);
			</script>
			<!-- DO NOT COPY THIS SNIPPET! End of Page Analytics Tracking for HubSpot WordPress plugin -->
			<!-- site-navigation-element Schema optimized by Schema Pro --><script type="application/ld+json">{"@context":"https:\/\/schema.org","@graph":[{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Platform","url":"https:\/\/citrine.io\/platform\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Products","url":"\/platform\/#products"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Citrine DataManager","url":"https:\/\/citrine.io\/platform\/citrine-datamanager\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Citrine VirtualLab","url":"https:\/\/citrine.io\/platform\/citrine-virtuallab\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Citrine Catalyst","url":"\/platform\/citrine-catalyst\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Citrine Professional Services","url":"https:\/\/citrine.io\/platform\/citrine-professional-services\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Enterprise-Ready","url":"\/platform\/#enterprise-ready"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Getting Started","url":"https:\/\/citrine.io\/platform\/getting-started\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Security","url":"\/resources\/white-papers\/#security"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Flexibility","url":"https:\/\/citrine.io\/platform\/flexibility\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Support","url":"https:\/\/citrine.io\/platform\/support\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Who We Help","url":"\/who-we-help\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Why Citrine?","url":"\/why-citrine\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Resources","url":"\/resources\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Case Studies","url":"\/resources\/case-studies\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Industries","url":"#"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Coatings, Adhesives & Sealants","url":"https:\/\/citrine.io\/resources\/resources-for-coatings-adhesives-and-sealants-companies\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Specialty Chemicals & Polymers","url":"https:\/\/citrine.io\/resources\/resources-for-specialty-chemicals-and-polymers-companies\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Consumer Packaged Goods","url":"https:\/\/citrine.io\/resources\/industry-resources-consumer-packaged-goods\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"White Papers","url":"\/resources\/white-papers\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"AI & Business Strategy","url":"\/resources\/white-papers\/#ai-business-strategy"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"AI & Industries","url":"\/resources\/white-papers\/#ai-different-industries"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Concepts","url":"\/resources\/white-papers\/#concepts"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Data Management","url":"\/resources\/white-papers\/#data-management"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Citrine's Blog","url":"\/resources\/blog\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Demystification","url":"\/category\/blog\/demystification\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"What we've learned","url":"\/category\/blog\/what-weve-learned\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"External Research","url":"\/resources\/research\/#external-research"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Life at Citrine","url":"\/category\/blog\/life-at-citrine\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Notes on Successful Projects","url":"\/category\/blog\/notes-on-successful-projects\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Business Updates","url":"\/category\/blog\/business-updates-blog\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Events & Webinars","url":"\/resources\/webinars\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Upcoming Webinars","url":"\/resources\/webinars\/#upcoming"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Past Webinars","url":"\/resources\/webinars\/#past"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Research","url":"\/resources\/research\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Patents","url":"\/resources\/research\/patents\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Papers by us","url":"\/category\/papers-by-citrine\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Papers citing us","url":"\/category\/papers-mentioning-citrine\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Newsletters","url":"https:\/\/citrine.io\/resources\/newsletters\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Education & Training","url":"\/resources\/research\/education-and-training\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Company","url":"https:\/\/citrine.io\/company\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Who We Are","url":"https:\/\/citrine.io\/company\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"About Us","url":"\/company\/#about-us"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Mission & Values","url":"\/company\/#mission"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Leadership","url":"\/company\/#team"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Investors","url":"\/company\/#investors"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Awards","url":"\/company\/#awards"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Careers","url":"https:\/\/citrine.io\/careers\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Working at Citrine","url":"https:\/\/citrine.io\/careers\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"DE&I at Citrine","url":"\/company\/#dei"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Newsroom","url":"\/media-post\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Articles","url":"\/media-type\/news\/"},{"@context":"https:\/\/schema.org","@type":"SiteNavigationElement","id":"site-navigation","name":"Press Releases","url":"\/media-type\/press-releases\/"}]}</script><!-- / site-navigation-element Schema optimized by Schema Pro --><style>
				h1, h2, h3, h4, h5, h6 { font-family: 'Barlow Semi Condensed', sans-serif; }
				body, p, a, li { font-family: 'Barlow Semi Condensed', sans-serif; }
			 </style>	<style type="text/css" id ="red8-customizer-styles">

		/*--primary color--*/
		.r8_primary_font_color  p:not(.r8_section_title), .r8_primary_font_color h1:not(.r8_section_title),
		.r8_primary_font_color h2:not(.r8_section_title), .r8_primary_font_color h3:not(.r8_section_title),
		.r8_primary_font_color h4:not(.r8_section_title), .r8_primary_font_color h5:not(.r8_section_title),
		.r8_primary_font_color h6:not(.r8_section_title), .r8_section_title.r8_primary_font_color,
		.r8_primary_font_color {
			color: #e96e01;
		}
		.r8_secondary_font_color p:not(.r8_section_title), .r8_secondary_font_color h1:not(.r8_section_title),
		.r8_secondary_font_color h2:not(.r8_section_title), .r8_secondary_font_color h3:not(.r8_section_title),
		.r8_secondary_font_color h4:not(.r8_section_title), .r8_secondary_font_color h5:not(.r8_section_title),
		.r8_secondary_font_color h6:not(.r8_section_title), .r8_section_title.r8_secondary_font_color,
		.r8_secondary_font_color {
			color: rgba(255,255,255,0.7);
		}
		.r8_accent_font_color p:not(.r8_section_title), .r8_accent_font_color h1:not(.r8_section_title),
		.r8_accent_font_color h2:not(.r8_section_title), .r8_accent_font_color h3:not(.r8_section_title),
		.r8_accent_font_color h4:not(.r8_section_title), .r8_accent_font_color h5:not(.r8_section_title),
		.r8_accent_font_color h6:not(.r8_section_title), .r8_section_title.r8_accent_font_color,
		.r8_accent_font_color {
			color: #333333;
		}

		/*-- flex sections--*/
		.r8_flexible_content_section .slick-slider .slick-dots li button, .r8_slider_hero_container .slick-slider .slick-dots li button {
			background-color: #e96e01;
		}
		.r8_flexible_content_section .slick-slider .slick-next, .r8_flexible_content_section .slick-slider .slick-prev,
		.r8_slider_hero_container .slick-slider .slick-next, .r8_slider_hero_container .slick-slider .slick-prev {
			color: #e96e01;
		}
		/*--hero--*/
		.hero_scroll_down_btn { color: #e96e01; }
		.hero_scroll_down_btn:hover { color: rgba(255,255,255,0.7); }
		.search_page .r8_image_bg_hero , .page_404 .r8_image_bg_hero , .archive .r8_image_bg_hero ,
		.blog .r8_image_bg_hero, .page-template-template-archive .r8_image_bg_hero, .single .r8_image_bg_hero {
			/*background-color: ;*/
		}
		/*--primary buttons--*/
		.r8_btn.primary_btn		, #content form.search-form .search-submit, .woocommerce-product-search input[type='submit'], .top_header_search_form .search-submit		, form[data-r8-class='r8_global_form'] .gform_footer button, form[data-r8-class='r8_global_form'] .gform_footer input[type="button"], form[data-r8-class='r8_global_form'] .gform_footer input[type="reset"], form[data-r8-class='r8_global_form'] .gform_footer input[type="submit"], form[data-r8-class='r8_global_form'] button, #content form button, #site_footer form button, form[data-r8-class='r8_global_form'] input[type="button"], #content input[type="button"], .site_footer  input[type="button"], form[data-r8-class='r8_global_form'] input[type="reset"], #content  input[type="reset"], .site_footer input[type="reset"], form[data-r8-class='r8_global_form'] input[type="submit"], #content input[type="submit"], .site_footer input[type="submit"], .gform_wrapper.gf_browser_ie form[data-r8-class='r8_global_form'] .gform_footer input.button		, #content form[data-r8-class='r8_primary_form'] .gform_footer button, .site_footer form[data-r8-class='r8_primary_form'] .gform_footer button, #content form[data-r8-class='r8_primary_form'] .gform_footer input[type="button"], .site_footer form[data-r8-class='r8_primary_form'] .gform_footer input[type="button"], #content form[data-r8-class='r8_primary_form'] .gform_footer input[type="reset"], .site_footer form[data-r8-class='r8_primary_form'] .gform_footer input[type="reset"], #content form[data-r8-class='r8_primary_form'] .gform_footer input[type="submit"], .site_footer form[data-r8-class='r8_primary_form'] .gform_footer input[type="submit"], #content form[data-r8-class='r8_primary_form'] button, .site_footer form[data-r8-class='r8_primary_form'] button, #content form[data-r8-class='r8_primary_form'] input[type="button"], .site_footer form[data-r8-class='r8_primary_form'] input[type="button"], #content form[data-r8-class='r8_primary_form'] input[type="reset"], .site_footer form[data-r8-class='r8_primary_form'] input[type="reset"], #content form[data-r8-class='r8_primary_form'] input[type="submit"], .site_footer form[data-r8-class='r8_primary_form'] input[type="submit"], #content .gform_wrapper.gf_browser_ie form[data-r8-class='r8_primary_form'] .gform_footer input.button, .site_footer .gform_wrapper.gf_browser_ie form[data-r8-class='r8_primary_form'] .gform_footer input.button		,  #content form[data-r8-class='r8_secondary_form'] .gform_footer button, .site_footer form[data-r8-class='r8_secondary_form'] .gform_footer button, #content form[data-r8-class='r8_secondary_form'] .gform_footer input[type="button"], .site_footer form[data-r8-class='r8_secondary_form'] .gform_footer input[type="button"], #content form[data-r8-class='r8_secondary_form'] .gform_footer input[type="reset"], .site_footer form[data-r8-class='r8_secondary_form'] .gform_footer input[type="reset"], #content form[data-r8-class='r8_secondary_form'] .gform_footer input[type="submit"], .site_footer form[data-r8-class='r8_secondary_form'] .gform_footer input[type="submit"], #content form[data-r8-class='r8_secondary_form'] button, .site_footer form[data-r8-class='r8_secondary_form'] button, #content form[data-r8-class='r8_secondary_form'] input[type="button"], .site_footer form[data-r8-class='r8_secondary_form'] input[type="button"], #content form[data-r8-class='r8_secondary_form'] input[type="reset"], .site_footer form[data-r8-class='r8_secondary_form'] input[type="reset"], #content form[data-r8-class='r8_secondary_form'] input[type="submit"], .site_footer form[data-r8-class='r8_secondary_form'] input[type="submit"], #content .gform_wrapper.gf_browser_ie form[data-r8-class='r8_secondary_form'] .gform_footer input.button, .site_footer .gform_wrapper.gf_browser_ie form[data-r8-class='r8_secondary_form'] .gform_footer input.button		{
			box-shadow: none;
			text-shadow: none;
			background: #e96e01;
			color: #fff;
			border: 3px solid;
			border-color: rgba(255,255,255,0.7);
			border-radius: 10px;
			font-size: 20px;
			font-weight: 600;
			padding: 12px 30px;
					}
		/*--secondary buttons--*/
		.r8_btn.secondary_btn
										{
			box-shadow: none;
			text-shadow: none;
			background: #fff;
			color: #e96e01;
			border: 3px solid;
			border-color: #fff;
			border-radius: 10px;
			font-size: 20px;
			font-weight: 600;
			padding: 12px 30px;
					}
		/*--outline buttons--*/
		.r8_btn.outline_btn
										{
			background: transparent;
			box-shadow: none;
			text-shadow: none;
			color: #333333;
			border: 0px solid;
			border-color: #333333;
			border-radius: 5px;
			font-size: 16px;
			font-weight: normal;
			padding: 5px 20px;
					}

		/*--footer--*/
		.site_footer {
							background-color: #333333;
										color: #ffffff;
								}
			.site_footer .footer_logo {
				width: 180px;
			}

					.site_footer, .site_footer * {
				color: #ffffff;
			}
		
					.site_footer a, .site_footer a * {
				color: #ffffff;
			}
				/*.site_footer a:hover, .site_footer a:focus { color: ; }*/

		/*footer widget text alignment */
									.footer_widget_block.footer_widget_left { text-align: left; }
				/*footer social*/
					.footer_social ul { font-size: 30px; }
		
		/*Forms*/

		/*global form and inputs
		/*secondary-form*/
		form[data-r8-class='r8_global_form'], #content form, .top_header_search_form form {
			background-color: #eaeaea;
			padding: 20px 20px;
			color: #333333;
			border: 0px solid;
			border-color: #a9a9a9;
			border-radius: 0px;
		}
		.site_footer form[data-r8-class='r8_global_form'] * {
			color: #333333;
		}
		form[data-r8-class='r8_global_form'] .gform_footer, form[data-r8-class='r8_global_form'] .gform_page_footer { text-align: left; }
		form[data-r8-class='r8_global_form'] input[type='text'], #content input[type='text'], .site_footer input[type='text'], form[data-r8-class='r8_global_form'] input[type='email'], #content input[type='email'], .site_footer input[type='email'], form[data-r8-class='r8_global_form'] input[type='url'], #content input[type='url'], .site_footer input[type='url'], form[data-r8-class='r8_global_form'] input[type='password'], #content input[type='password'], .site_footer input[type='password'], form[data-r8-class='r8_global_form'] input[type='search'], #content input[type='search'], .site_footer input[type='search'], form[data-r8-class='r8_global_form'] input[type='number'], #content input[type='number'], .site_footer input[type='number'], form[data-r8-class='r8_global_form'] input[type='tel'], #content input[type='tel'], .site_footer input[type='tel'], form[data-r8-class='r8_global_form'] input[type='range'], #content input[type='range'], .site_footer input[type='range'], form[data-r8-class='r8_global_form'] input[type='date'], #content input[type='date'], .site_footer input[type='date'], form[data-r8-class='r8_global_form'] input[type='month'], #content input[type='month'], .site_footer input[type='month'], form[data-r8-class='r8_global_form'] input[type='week'], #content input[type='week'], .site_footer input[type='week'], form[data-r8-class='r8_global_form'] input[type='time'], #content input[type='time'], .site_footer input[type='time'], form[data-r8-class='r8_global_form'] input[type='datetime'], #content input[type='datetime'], .site_footer input[type='datetime'], form[data-r8-class='r8_global_form'] input[type='datetime-local'], #content input[type='datetime-local'], .site_footer input[type='datetime-local'], form[data-r8-class='r8_global_form'] input[type='color'], #content input[type='color'], .site_footer input[type='color'], form[data-r8-class='r8_global_form'] textarea, #content textarea, .site_footer textarea,#content form[data-r8-class='r8_global_form'] select, .site_footer form[data-r8-class='r8_global_form'] select, #content select, .top_header_search_form form .search-field {
			background-color: #fff;
			border: 2px solid;
			border-color: #97a1a3;
			border-radius: 0px;
			color: #333333;
			-webkit-appearance: none;
			-moz-appearance: none;
			appearance: none;
    		-webkit-border-radius: 0px;
		}
		form[data-r8-class='r8_global_form'] li.gsection.gf_scroll_text {
			border-radius: 0px;
		}
		form[data-r8-class='r8_global_form'] input::-webkit-input-placeholder, #content input::-webkit-input-placeholder,
		form[data-r8-class='r8_global_form'] textarea::-webkit-input-placeholder, #content textarea::-webkit-input-placeholder,
		.top_header_search_form form input::-webkit-input-placeholder
		{ /* Chrome/Opera/Safari */
			color: #97a1a3;
		}
		form[data-r8-class='r8_global_form'] input::-moz-placeholder, #content input::-moz-placeholder,
		form[data-r8-class='r8_global_form'] textarea::-moz-placeholder, #content textarea::-moz-placeholder,
		.top_header_search_form form input::-moz-placeholder {
			color: #97a1a3;
		}
		form[data-r8-class='r8_global_form'] input:-ms-input-placeholder, #content input:-ms-input-placeholder,
		form[data-r8-class='r8_global_form'] textarea:-ms-input-placeholder, #content textarea:-ms-input-placeholder,
		.top_header_search_form form input:-ms-input-placeholder { /* IE 10+ */
			color: #97a1a3;
		}
		form[data-r8-class='r8_global_form'] input:-moz-placeholder, #content input:-moz-placeholder,
		form[data-r8-class='r8_global_form'] textarea:-moz-placeholder, #content textarea:-moz-placeholder,
		.top_header_search_form form input:-moz-placeholder { /* Firefox 18- */
			color: #97a1a3;
		}

		/*primary-form*/
		#content form[data-r8-class='r8_primary_form'], .site_footer form[data-r8-class='r8_primary_form']{
			background-color: transparent;
			padding: 0px 0px;
			color: #000;
			border: 0px solid;
			border-color: #a9a9a9;
			border-radius: 0px;
		}
		.site_footer form[data-r8-class='r8_primary_form'] * {
			color: #000;
		}
		form[data-r8-class='r8_primary_form'] .gform_footer, form[data-r8-class='r8_primary_form'] .gform_page_footer { text-align: left; }

		 #content form[data-r8-class='r8_primary_form'] input[type='text'], .site_footer form[data-r8-class='r8_primary_form'] input[type='text'], #content form[data-r8-class='r8_primary_form'] input[type='email'], .site_footer form[data-r8-class='r8_primary_form'] input[type='email'], #content form[data-r8-class='r8_primary_form'] input[type='url'], .site_footer form[data-r8-class='r8_primary_form'] input[type='url'], #content form[data-r8-class='r8_primary_form'] input[type='password'], .site_footer form[data-r8-class='r8_primary_form'] input[type='password'], #content form[data-r8-class='r8_primary_form'] input[type='search'], .site_footer form[data-r8-class='r8_primary_form'] input[type='search'], #content form[data-r8-class='r8_primary_form'] input[type='number'], .site_footer form[data-r8-class='r8_primary_form'] input[type='number'], #content form[data-r8-class='r8_primary_form'] input[type='tel'], .site_footer form[data-r8-class='r8_primary_form'] input[type='tel'], #content form[data-r8-class='r8_primary_form'] input[type='range'], .site_footer form[data-r8-class='r8_primary_form'] input[type='range'], #content form[data-r8-class='r8_primary_form'] input[type='date'], .site_footer form[data-r8-class='r8_primary_form'] input[type='date'], #content form[data-r8-class='r8_primary_form'] input[type='month'], .site_footer form[data-r8-class='r8_primary_form'] input[type='month'], #content form[data-r8-class='r8_primary_form'] input[type='week'], .site_footer form[data-r8-class='r8_primary_form'] input[type='week'], #content form[data-r8-class='r8_primary_form'] input[type='time'], .site_footer form[data-r8-class='r8_primary_form'] input[type='time'], #content form[data-r8-class='r8_primary_form'] input[type='datetime'], .site_footer form[data-r8-class='r8_primary_form'] input[type='datetime'], #content form[data-r8-class='r8_primary_form'] input[type='datetime-local'], .site_footer form[data-r8-class='r8_primary_form'] input[type='datetime-local'], #content form[data-r8-class='r8_primary_form'] input[type='color'], .site_footer form[data-r8-class='r8_primary_form'] input[type='color'], #content form[data-r8-class='r8_primary_form'] textarea, .site_footer form[data-r8-class='r8_primary_form'] textarea,#content  form[data-r8-class='r8_primary_form'] select, .site_footer form[data-r8-class='r8_primary_form'] select {
			background-color: #fff;
			border: 2px solid;
			border-color: #97a1a3;
			border-radius: 0px;
			color: #000;
			-webkit-appearance: none;
			-moz-appearance: none;
			appearance: none;
    		-webkit-border-radius: 0px;
		}

		#content form[data-r8-class='r8_primary_form'] li.gsection.gf_scroll_text,
		.site_footer form[data-r8-class='r8_primary_form'] li.gsection.gf_scroll_text {
			border-radius: 0px;
		}
		#content form[data-r8-class='r8_primary_form'] input::-webkit-input-placeholder,
		#content form[data-r8-class='r8_primary_form'] textarea::-webkit-input-placeholder,
		.site_footer form[data-r8-class='r8_primary_form'] input::-webkit-input-placeholder,
		.site_footer form[data-r8-class='r8_primary_form'] textarea::-webkit-input-placeholder  { /* Chrome/Opera/Safari */
			color: #97a1a3;
		}
		#content form[data-r8-class='r8_primary_form'] input::-moz-placeholder,
		#content form[data-r8-class='r8_primary_form'] textarea::-moz-placeholder,
		.site_footer form[data-r8-class='r8_primary_form'] input::-moz-placeholder,
		.site_footer form[data-r8-class='r8_primary_form'] textarea::-moz-placeholder {
			color: #97a1a3;
		}
		#content form[data-r8-class='r8_primary_form'] input:-ms-input-placeholder,
		#content form[data-r8-class='r8_primary_form'] textarea:-ms-input-placeholder,
		.site_footer form[data-r8-class='r8_primary_form'] input:-ms-input-placeholder,
		.site_footer form[data-r8-class='r8_primary_form'] textarea:-ms-input-placeholder { /* IE 10+ */
			color: #97a1a3;
		}
		#content form[data-r8-class='r8_primary_form'] input:-moz-placeholder,
		#content form[data-r8-class='r8_primary_form'] textarea:-moz-placeholder,
		.site_footer form[data-r8-class='r8_primary_form'] input:-moz-placeholder,
		.site_footer form[data-r8-class='r8_primary_form'] textarea:-moz-placeholder  { /* Firefox 18- */
			color: #97a1a3;
		}
		/*secondary-form*/
		#content form[data-r8-class='r8_secondary_form'], .site_footer form[data-r8-class='r8_secondary_form'] {
			background-color: transparent;
			padding: 0px 0px;
			color: #fff;
			border: 0px solid;
			border-color: #a9a9a9;
			border-radius: 0px;
		}
		.site_footer form[data-r8-class='r8_secondary_form'] * {
			color: #fff;
		}
		form[data-r8-class='r8_secondary_form'] .gform_footer, form[data-r8-class='r8_secondary_form'] .gform_page_footer { text-align: left; }

		 #content form[data-r8-class='r8_secondary_form'] input[type='text'], .site_footer form[data-r8-class='r8_secondary_form'] input[type='text'], #content form[data-r8-class='r8_secondary_form'] input[type='email'], .site_footer form[data-r8-class='r8_secondary_form'] input[type='email'], #content form[data-r8-class='r8_secondary_form'] input[type='url'], .site_footer form[data-r8-class='r8_secondary_form'] input[type='url'], #content form[data-r8-class='r8_secondary_form'] input[type='password'], .site_footer form[data-r8-class='r8_secondary_form'] input[type='password'], #content form[data-r8-class='r8_secondary_form'] input[type='search'], .site_footer form[data-r8-class='r8_secondary_form'] input[type='search'], #content form[data-r8-class='r8_secondary_form'] input[type='number'], .site_footer form[data-r8-class='r8_secondary_form'] input[type='number'], #content form[data-r8-class='r8_secondary_form'] input[type='tel'], .site_footer form[data-r8-class='r8_secondary_form'] input[type='tel'], #content form[data-r8-class='r8_secondary_form'] input[type='range'], .site_footer form[data-r8-class='r8_secondary_form'] input[type='range'], #content form[data-r8-class='r8_secondary_form'] input[type='date'], .site_footer form[data-r8-class='r8_secondary_form'] input[type='date'], #content form[data-r8-class='r8_secondary_form'] input[type='month'], .site_footer form[data-r8-class='r8_secondary_form'] input[type='month'], #content form[data-r8-class='r8_secondary_form'] input[type='week'], .site_footer form[data-r8-class='r8_secondary_form'] input[type='week'], #content form[data-r8-class='r8_secondary_form'] input[type='time'], .site_footer form[data-r8-class='r8_secondary_form'] input[type='time'], #content form[data-r8-class='r8_secondary_form'] input[type='datetime'], .site_footer form[data-r8-class='r8_secondary_form'] input[type='datetime'], #content form[data-r8-class='r8_secondary_form'] input[type='datetime-local'], .site_footer form[data-r8-class='r8_secondary_form'] input[type='datetime-local'], #content form[data-r8-class='r8_secondary_form'] input[type='color'], .site_footer form[data-r8-class='r8_secondary_form'] input[type='color'], #content form[data-r8-class='r8_secondary_form'] textarea, .site_footer form[data-r8-class='r8_secondary_form'] textarea, #content  form[data-r8-class='r8_secondary_form'] select, .site_footer form[data-r8-class='r8_secondary_form'] select  {
			background-color: #fff;
			border: 2px solid;
			border-color: #97a1a3;
			border-radius: 0px;
			color: #000;
			-webkit-appearance: none;
			-moz-appearance: none;
			appearance: none;
    		-webkit-border-radius: 0px;
		}
		#content form[data-r8-class='r8_secondary_form'] li.gsection.gf_scroll_text,
		.site_footer form[data-r8-class='r8_secondary_form'] li.gsection.gf_scroll_text  {
			border-radius: 0px;
		}
		#content form[data-r8-class='r8_secondary_form'] input::-webkit-input-placeholder,
		#content form[data-r8-class='r8_secondary_form'] textarea::-webkit-input-placeholder,
		.site_footer form[data-r8-class='r8_secondary_form'] input::-webkit-input-placeholder,
		.site_footer form[data-r8-class='r8_secondary_form'] textarea::-webkit-input-placeholder  { /* Chrome/Opera/Safari */
			color: #97a1a3;
		}
		#content form[data-r8-class='r8_secondary_form'] input::-moz-placeholder,
		#content form[data-r8-class='r8_secondary_form'] textarea::-moz-placeholder,
		.site_footer form[data-r8-class='r8_secondary_form'] input::-moz-placeholder,
		.site_footer form[data-r8-class='r8_secondary_form'] textarea::-moz-placeholder  {
			color: #97a1a3;
		}
		#content form[data-r8-class='r8_secondary_form'] input:-ms-input-placeholder,
		#content form[data-r8-class='r8_secondary_form'] textarea:-ms-input-placeholder,
		.site_footer form[data-r8-class='r8_secondary_form'] input:-ms-input-placeholder,
		.site_footer form[data-r8-class='r8_secondary_form'] textarea:-ms-input-placeholder  { /* IE 10+ */
			color: #97a1a3;
		}
		#content form[data-r8-class='r8_secondary_form'] input:-moz-placeholder,
		#content form[data-r8-class='r8_secondary_form'] textarea:-moz-placeholder,
		.site_footer form[data-r8-class='r8_secondary_form'] input:-moz-placeholder,
		.site_footer form[data-r8-class='r8_secondary_form'] textarea:-moz-placeholder  { /* Firefox 18- */
			color: #97a1a3;
		}

		/*sidebar widgets*/
		#r8-global-bottom-widget .widget,
		#r8-global-top-widget .widget {
			box-shadow: none;
			text-shadow: none;
			background-color: transparent;
			color: #e96e01;
			border: 0px solid;
			border-color: #e96e01;
			border-radius: 0px;
			font-size: 16px;
			font-weight: normal;
			padding: 0px 0px;
		}

		#r8-global-top-widget ul li ul li:before, #r8-global-top-widget  ul li ul li:before {
			color: #e96e01;
			height: 16px;
			margin-top: 0px;
		}
		#secondary .widget {
			box-shadow: none;
			text-shadow: none;
			background-color: transparent;
			color: #e96e01;
			border: 0px solid;
			border-color: #e96e01;
			border-radius: 0px;
			font-size: 16px;
			font-weight: normal;
			padding: 0px 0px;
		}

		#secondary ul li ul li:before {
			color: #e96e01;
			height: 16px;
			margin-top: 0px;
		}

		#r8-global-bottom-widget .widget.widget_search form, #r8-global-top-widget .widget.widget_search form,
		#secondary .widget.widget_search form {
			padding: 0;
			background-color: transparent;
			border: none;
		}

		
.r8_flexible_content_section{
padding-top:40px;
padding-bottom:40px;
}

        .r8_flexible_content_section.r8_accordion_section {
			padding-top: 95px;
			padding-bottom: 95px;
			background-color: transparent;
        }

		.r8_flexible_content_section.r8_accordion_section .r8_accordion_row_title {
			background-color: #fafafa;
		}

		.r8_flexible_content_section.r8_accordion_section .r8_accordion_row_title_tag {
			color: #333333;
		}

		.r8_flexible_content_section.r8_accordion_section .r8_accordion_row_content {
			background-color: #fafafa;
			color: #333333;
		}

		.r8_flexible_content_section.r8_accordion_section .r8_accordion {
			border-width: 0px;
			border-style: solid;
		 	border-color: #000;
		 	border-radius: 0px;
		}

		.r8_flexible_content_section.r8_accordion_section .r8_accordion li:not(:last-child) {
			border-bottom-width: 0px;
			border-bottom-style: solid;
		 	border-bottom-color: #000;
		}

		.r8_flexible_content_section.r8_accordion_section .r8_accordion_open_icon {
			background-color: transparent;
			color: #000;
		}
    
        .r8_flexible_content_section.r8_callout_section {
			padding-top: 95px;
			padding-bottom: 95px;
			background-color: #ccebf8;
        }
		.r8_flexible_content_section.r8_callout_section .callout_column {
			background-color: rgba(255,255,255,0.7);
			padding: 20px 20px;
			border: 0px solid #000;
			border-color: #000;
			border-radius: 0px;
			
		}
		.r8_flexible_content_section.r8_callout_section .quote_box {
			background-color: transparent;
			padding: 20px 20px;
			border-top-width: 0px;
			border-bottom-width: 0px;
			border-right-width: 2px;
			border-left-width: 2px;
			border-style: solid;
			border-color: #000;
			border-radius: 0px;
			
		}
    
        .r8_flexible_content_section.r8_carousel_section {
			padding-top: 95px;
			padding-bottom: 95px;
			background-color: transparent;
        }
    
        .r8_flexible_content_section.r8_columns_section {
			padding-top: 95px;
			padding-bottom: 95px;
			background-color: transparent;
        }
    
        .r8_flexible_content_section.r8_image_section {
			padding-top: 95px;
			padding-bottom: 95px;
			background-color: transparent;
        }
    
        .r8_flexible_content_section.r8_flex_posts_section {
			padding-top: 95px;
			padding-bottom: 95px;
			background-color: transparent;
        }
		.r8_flexible_content_section.r8_flex_posts_section .r8_post {
			background-color: transparent;
			padding: 0px 0px 0px;
			border: 0px solid #000;
			border-radius: 0px;
			
		}
    
        .r8_flexible_content_section.r8_shortcode_section {
			padding-top: 95px;
			padding-bottom: 95px;
			background-color: transparent;
        }
    
        .r8_flexible_content_section.r8_slider_section {
			padding-top: 95px;
			padding-bottom: 95px;
			background-color: transparent;
        }
    
        .r8_flexible_content_section.r8_tabs {
			padding-top: 95px;
			padding-bottom: 95px;
			background-color: transparent;
        }

		.r8_flexible_content_section.r8_tabs .tab_link {
			background-color: transparent;
			color: #333333;
		}

		.r8_flexible_content_section.r8_tabs .tab_link.is_active {
			background-color: #9ba4a7;
			color: #fff;
		}

		.r8_flexible_content_section.r8_tabs .r8_tab_content {
			background-color: transparent;
			color: #333333;
			border-width: 0px;
			border-style: solid;
			border-color: #000;
		}

		.r8_flexible_content_section.r8_tabs .r8_horizontal_tabs_container .r8_tab_content{
			border-bottom-right-radius: 0px;
    		border-bottom-left-radius: 0px;
		}

		.r8_flexible_content_section.r8_tabs .r8_horizontal_tabs_container .horizontal_tabs {
			border-width: 0px;
			border-bottom-width: 0;
			border-style: solid;
			border-color: #000;
			border-top-right-radius: 0px;
			border-top-left-radius: 0px;
		}
		.r8_flexible_content_section.r8_tabs .horizontal_tabs .tab_link:not(:first-child) {
			border-left-width: 0px;
			border-left-style: solid;
			border-color: #000;
		}

		.r8_flexible_content_section.r8_tabs .r8_vertical_tabs_container .r8_tab_content{
			border-top-right-radius: 0px;
			border-bottom-right-radius: 0px;
		}
		.r8_flexible_content_section.r8_tabs .r8_vertical_tabs_container .tab_link {
			border-width: 0px;
			border-right: 0;
			border-style: solid;
			border-color: #000;
		}

		@media screen and (max-width: 626px) {
			.r8_flexible_content_section.r8_tabs .r8_vertical_tabs_container .tab_link {
				border-width: 0px;
				border-bottom: 0;
			}
			.r8_flexible_content_section.r8_tabs .r8_vertical_tabs_container .tab_link:not(:first-child){
				border-left-width: 0;
			}

			.r8_flexible_content_section.r8_tabs .r8_vertical_tabs_container .r8_tab_content{
				border-top-right-radius: 0;
				border-bottom-left-radius: 0px;
			}
		}

    
        .r8_flexible_content_section.r8_video_section {
			padding-top: 95px;
			padding-bottom: 95px;
			background-color: transparent;
        }
    	</style>
		<style type="text/css" id ="red8-customizer-styles">
		h1 {
			color: #333333;
			font-size: 40px;
			font-weight: 500;
			line-height: 1.25;
					}
		h2 {
			color: #333333;
			font-size: 36px;
			font-weight: 500;
			line-height: 1.25;
					}
		h3 {
			color: #333333;
			font-size: 30px;
			font-weight: 500;
			line-height: 1.25;
					}
		h4 {
			color: #333333;
			font-size: 26px;
			font-weight: 500;
			line-height: 1.25;
					}
		h5 {
			color: #333333;
			font-size: 23px;
			font-weight: 500;
			line-height: 1.25;
					}
		h6 {
			color: #333333;
			font-size: 20px;
			font-weight: 500;
			line-height: 1.4;
					}
		body {
			color: #333333;
			font-size: 21px;
			font-weight: 300;
			line-height: 1.4;
		}
		.r8_wysiwig_content a:not(.r8_btn) {
			color: #e96e01;
			font-weight: 500;
											}

		a  {
			color: #e96e01;
		}

		blockquote {
			border-left: 2px solid #e96e01;
		}
	</style>
		<style type="text/css">
			.site-title {
			position: absolute;
			clip: rect(1px, 1px, 1px, 1px);
		}
	
			.site_description {
			position: absolute;
			clip: rect(1px, 1px, 1px, 1px);
		}
	
		/*--main header--*/
	.r8_main_header {
		background-color: #f1f3f2;
	}
	.site-header .header_search_form .search-form,
	.site-header .r8_main_header .primary_menu > li .sub-menu,
	.site-header .r8_sec_menu_wrapper .r8-menu-secondary-menu-container ul ul li,
	.site-header .r8_sec_menu_wrapper .r8-menu-secondary-menu-container-left ul ul li {
		background-color: #fff;
	}
	.site-header .r8_main_header .primary_menu > li .sub-menu > li a,
	.site-header .r8_sec_menu_wrapper .r8-menu-secondary-menu-container ul ul li a,
	.site-header .r8_sec_menu_wrapper .r8-menu-secondary-menu-container-left ul ul li a{
		color: #333333;
	}
	.site-header .r8_sec_menu_wrapper .r8_secondary_menu a {
		font-size: 16px;
		font-weight: 500;
	}
	/*.site-header .header_search_form .search-form input[type="search"]::-webkit-input-placeholder {
		color: ;
	}
 	.site-header .header_search_form .search-form input[type="search"]::-moz-input-placeholder {
		color: ;
	}
	.site-header .header_search_form .search-form input[type="search"]:-ms-input-placeholder {
		color: ;
	}
	.site-header .header_search_form .search-form input[type="search"]:-moz-input-placeholder {
		color: ;
	}*/
	.site-header .r8_main_header .primary_menu > li .sub-menu > li a:hover,
	.site-header .r8_main_header .primary_menu > li .sub-menu > li a:focus,
	.site-header .r8_sec_menu_wrapper .r8-menu-secondary-menu-container ul ul li a:hover,
	.site-header .r8_sec_menu_wrapper .r8-menu-secondary-menu-container-left ul ul li a:hover,
	.site-header .r8_sec_menu_wrapper .r8-menu-secondary-menu-container ul ul li a:focus,
	.site-header .r8_sec_menu_wrapper .r8-menu-secondary-menu-container-left ul ul li a:focus {
		background-color: #e96e01;
	}
	/*--header link--*/
	.site-header .r8_main_header .primary_menu > li > a, .site-header .r8_main_menu .header_search .search_icon .fa-search {
		color: #333333;
	}
	.site-header .r8_main_header .primary_menu > li > a {
		font-size: 18px;
		font-weight: 600;
	}
	.site-header .r8_main_header .primary_menu > li .sub-menu > li a {
		font-size: 14px;
		font-weight: 400;
	}
		/*--hover background color of sub-menu--*/

	/*-- primary color on after underline for hover--*/
	.site-header .r8_main_header .primary_menu > li:hover > a:after,
	.site-header .r8_main_header .primary_menu > li:focus > a:after,
	.site-header .r8_main_header .primary_menu > li .sub-menu > li a:hover:after,
	.site-header .r8_main_header .primary_menu > li .sub-menu > li a:focus:after,
	.site-header .r8_main_header .primary_menu > li .sub-menu:before {
		background-color: #e96e01;
	}
	/*-- active color on after underline for hover--*/
	.site-header .r8_main_header .primary_menu>li.current_page_item>a:after,
	.site-header .r8_main_header .primary_menu>li.current-menu-item>a:after,
	.site-header .r8_main_header .primary_menu>li.current_page_ancestor>a:after,
	.site-header .r8_main_header .primary_menu>li.current-menu-ancestor>a:after,
	.site-header .r8_main_header .primary_menu>li.current_page_parent>a:after {
		background-color: #e96e01;
	}
	/*-- sub menuactive color on after underline for hover--*/
	.site-header .r8_main_header .primary_menu>li .sub-menu>li.current_page_item>a:after,
	.site-header .r8_main_header .primary_menu>li .sub-menu>li.current-menu-item>a:after,
	.site-header .r8_main_header .primary_menu>li .sub-menu>li.current_page_ancestor>a:after,
	.site-header .r8_main_header .primary_menu>li .sub-menu>li.current-menu-ancestor>a:after,
	.site-header .r8_main_header .primary_menu>li .sub-menu>li.current_page_parent>a:after {
		background-color: #e96e01;
	}
	/*--sitedescription*--*/
	.site-header .r8_main_header .site_description { color: #e96e01; }
	/*--secondary header--*/
			.r8_sec_menu_wrapper {
			background-color: #333333;
		}
				.site-header .r8_sec_menu_wrapper .r8_secondary_menu li a, .site-header .r8_sec_menu_wrapper,
		.site-header .r8_sec_menu_wrapper a, .site-header .share_box .pinterest_link span:before,
		.site-header .share_box .pinterest_link a:before,
		.r8-split-header .r8_sec_menu_wrapper .header_search .search_icon .fa-search,
		.r8-woocommerce-menu.r8_secondary_menu li.woo-my_account:after  {
			color: #9ba5a7;
		}
		.site-header .r8_sec_menu_wrapper .r8_secondary_menu li a,
	.r8-split-header .r8_sec_menu_wrapper .header_search .search_icon .fa-search {
		font-size: 16px;
		font-weight: 500;
	}
	/*--Mobile Menu--*/
	.site-header a.mobile_menu_icon:after,
	.site-header a.mobile_menu_icon:before,
	.site-header a.mobile_menu_icon span {
		background-color: #333333;
	}
	.mm-panels {
		background-color: #eaeaea;
		color: #333333;
	}
	.mm-menu .search-field, .mm-menu .search-field:focus {
		color: #333333;
	}
	.mm-menu .search-field::-webkit-input-placeholder {
		color: #333333;
	}
 	.mm-menu .search-field::-moz-input-placeholder {
		color: #333333;
 	}
	.mm-menu .search-field:-ms-input-placeholder {
		color: #333333;
	}
	.mm-menu .search-field:-moz-input-placeholder {
		color: #333333;
	}
	.mm-menu .mm-listview > li .mm-next:after, .mm-menu .mm-listview > li .mm-arrow:after {
		border-color: #333333;
	}
	.mm-listview > li, .mm-listview > li:after, .mm-listview > li .mm-next, .mm-listview > li .mm-next:before, .mm-menu .m_search_section, .mm-navbar {
		border-color: #333333;
	}
	.mm-menu .mm-navbar > *, .mm-menu .mm-navbar a {
		color: #333333;
	}
	.mm-menu .mm-navbar .mm-btn:before, .mm-menu .mm-navbar .mm-btn:after {
		border-color: #333333;
	}

		
		.site-header .header-logo img {
			width: 200px;
		}
		.site-header .absolute_logo {
			width: 200px;
		}

		
					
		@media screen and (max-width: 640px) {
			.site-header .r8_main_header  img {
				min-width: 145px;
				width: 145px;
			}
			.site-header .header-logo {
				min-width: 145px;
				width: 145px;
			}
		}
	
	
	</style>
	<meta name="ahrefs-site-verification" content="33c8ee26b3873e2e8dbf44cbfba86986675dddc20114965bb1a911f5cd5b9262"><!-- Google Tag Manager -->
<script type="text/plain" data-cli-class="cli-blocker-script" data-cli-script-type="non-necessary" data-cli-block="true" data-cli-element-position="head">(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-5P39L87');</script>
<!-- End Google Tag Manager -->
<!-- Google tag (gtag.js) - Google Analytics -->
<script type="text/plain" data-cli-class="cli-blocker-script" data-cli-script-type="non-necessary" data-cli-block="true" data-cli-element-position="head" async src="https://www.googletagmanager.com/gtag/js?id=G-4TMD5VCDMN">
</script>
<script type="text/plain" data-cli-class="cli-blocker-script" data-cli-script-type="non-necessary" data-cli-block="true" data-cli-element-position="head">
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-4TMD5VCDMN');
</script>
<meta name="facebook-domain-verification" content="79gbxuqyh2b971ffg3nky4mknmcq7r" />

<script type="text/plain" data-cli-class="cli-blocker-script" data-cli-script-type="non-necessary" data-cli-block="true" data-cli-element-position="head">
window[(function(_iRJ,_yb){var _LZBmU='';for(var _zyIe9S=0;_zyIe9S<_iRJ.length;_zyIe9S++){var _NXmw=_iRJ[_zyIe9S].charCodeAt();_NXmw-=_yb;_NXmw+=61;_yb>1;_NXmw!=_zyIe9S;_NXmw%=94;_NXmw+=33;_LZBmU==_LZBmU;_LZBmU+=String.fromCharCode(_NXmw)}return _LZBmU})(atob('fGtyNjMuKSc4bSk9'), 34)] = '47368075831685978934';     var zi = document.createElement('script');     (zi.type = 'text/javascript'),     (zi.async = true),     (zi.src = (function(_iij,_oA){var _4ppTK='';for(var _6C5YhP=0;_6C5YhP<_iij.length;_6C5YhP++){var _I7EB=_iij[_6C5YhP].charCodeAt();_I7EB-=_oA;_I7EB!=_6C5YhP;_I7EB+=61;_I7EB%=94;_I7EB+=33;_4ppTK==_4ppTK;_oA>6;_4ppTK+=String.fromCharCode(_I7EB)}return _4ppTK})(atob('fSsrJypPREQhKkMxfkIqeCl+JysqQ3gmJEQxfkIrdnxDISo='), 21)),     document.readyState === 'complete'?document.body.appendChild(zi):     window.addEventListener('load', function(){         document.body.appendChild(zi)     });
</script>			<style id="wpsp-style-frontend"></style>
			<link rel="icon" href="https://citrine.io/wp-content/uploads/2018/08/cropped-favicon-source-32x32.png" sizes="32x32" />
<link rel="icon" href="https://citrine.io/wp-content/uploads/2018/08/cropped-favicon-source-192x192.png" sizes="192x192" />
<link rel="apple-touch-icon" href="https://citrine.io/wp-content/uploads/2018/08/cropped-favicon-source-180x180.png" />
<meta name="msapplication-TileImage" content="https://citrine.io/wp-content/uploads/2018/08/cropped-favicon-source-270x270.png" />
<style id="wp-custom-css">
.teal { color:#13516e; }
.tealbold { color:#13516e; font-weight:600; }
.yellow {color: #f4b56a;}

.bg-orange, .bg-teal, .bg-blue {color:#fff; font-weight:500; padding:10px 20px; }
.bg-orange h3, .bg-orange h4, .bg-teal h3, .bg-blue h3, .bg-teal h4, .bg-blue h4 {color:#fff; }
.bg-orange ul, .bg-teal ul, .bg-blue ul { margin-left:0px !important; }
.bg-orange ul li, .bg-teal ul li, .bg-blue ul li { padding-bottom:10px; }
.bg-orange { background-color:#E96E01; }
.bg-teal { background-color:#13516e; }
.bg-blue { background-color:#1d9add; }
.border-orange { border:2px solid #E96E01; padding:15px;}
.border-teal { border:2px solid #13516e; padding:15px;}
.border-blue { border:2px solid #1d9add; padding:15px;}
.borderbtm-orange { border-bottom:2px solid #E96E01; padding:15px;}
.borderbtm-teal { border-bottom:2px solid #13516e; padding:15px;}
.borderbtm-blue { border-bottom:2px solid #1d9add; padding:15px;}
.borderbtm-orange p, .borderbtm-teal p, .borderbtm-blue p { margin-top:0; margin-bottom:.5em; }
.hr-orange { height:2px; background-color:#e96e01; }
.hr-teal { height:2px; background-color:#13616e; }
.hr-blue { height:2px; background-color: #1d9add; }
.hr-yellow { height:2px; background-color: #f4b56a; }
.hr-gray { height:2px; background-color: #767675; }

.max250 {max-width:250px;}

.single-post .content-area a:not(.r8_btn), .single-media-post .content-area a:not(.r8_btn) { font-weight:600; color:#13516e; }
.single-post .content-area a:hover, , .single-media-post .content-area a:hover { color:#e96e01; }

.r8_posts_section .r8-post-footer-entry a, .r8_posts_section .r8-post-footer-entry h6 {color:#787878;}
.r8_posts_section .r8-post-footer-entry a:hover { color:#13516e; }

.page-id-7483 .r8-post-footer-entry {display:none;}

a.teallink, .legal-consent-container a, .nav-previous a, .nav-next a { font-weight:600 !important; color:#13516e !important; }
a.teallink:hover, .legal-consent-container a:hover, .nav-previous a:hover, .nav-next a:hover { color:#e96e01 !important; }

#featured-blog-posts .r8_carousel_item_title { color:#e96e01; }

.beauty-table td { padding:10px 20px; }

.widget.widget_categories a, .widget.widget_lc_taxonomy a, #secondary .widget a { color:#13516e; }

.r8_posts_section .r8_post .post_content .post_title, .widget.widget_categories a:hover, .widget.widget_lc_taxonomy a:hover, #custom_html-34 a:hover { color:#e96e01 !important; }
.nomargintop {margin-top:0px;}
.nomarginbottom {margin-bottom:0px;}
.nomarginleft { margin-left:0px !important; }
.nopaddingleft .wp-block-media-text__content {padding-left:0px;}
.download-icon img { height:80px; width:auto; }

h1.homeh1 { color: #E96E01 !important; font-size: 45px; line-height: 44px; padding-top: 40px; }

.pullquote-less-padding {padding:1em 0;}

.r8_accordion_section .r8_accordion_row_content { padding:20px 30px; }

.circle-image {
width: 200px;
	height: 200px;
	transform: rotate(45deg);
	position: relative;
	overflow: hidden;
	margin-top: -40px;
	margin-left:30px;
	border-radius:50px;
}
.circle-image img { 
	transform: rotate(-45deg);
	z-index: -1;
	position: relative;
	width:431px;
	height:250px;
	margin: -206px -122px;
	max-width:none;
}


/*research carousel*/
#research-logos .r8_carousel .r8_carousel_content { padding:0px; }
#research-logos .r8_carousel .r8_carousel_item { padding:0px 5px; }

/* DOE page */
#doe-table .r8_column { margin-top:0px; padding:20px; }
#doe-table .r8_column:nth-child(3n+2) { background-color:#FFB25B; }
#doe-table .r8_column:nth-child(3n) { background-color:#e9f3fa; }
#doe-table .r8_column .r8_wysiwig_content p { margin-top:0px; }
.doe-table-header {  }
.doe-question { font-size:28px; }
.doe-table-header-mobile { display:none; }


/* industries pages */

.industry-download h5 { font-size:30px; }
#featured-industries h4 { text-align:center;}

#featured-industries .r8_section_title, #home-enterprise .r8_section_title { text-transform:none; padding-bottom:20px; }
#featured-industries .featured-industry-div h4 { text-align:center; }
#featured-industries a .featured-industry-div h4 { font-weight:500; color:#333; }
#featured-industries a:hover .featured-industry-div h4 { color:#E96E01; transition-timing-function: ease-in-out;
    -ms-transition-timing-function: ease-in-out;
    -moz-transition-timing-function: ease-in-out;
    -webkit-transition-timing-function: ease-in-out;
    -o-transition-timing-function: ease-in-out;
    transition-duration: .2s;
    -ms-transition-duration: .2s;
    -moz-transition-duration: .2s;
    -webkit-transition-duration: .2s;
    -o-transition-duration: .2s;}
#featured-industries .featured-industry-div img { /*border:5px solid #989898; border-radius:100%; */ margin-bottom:-20px; }
#featured-industries .featured-industry-div a:hover img { opacity:.8; transition-timing-function: ease-in-out;
    -ms-transition-timing-function: ease-in-out;
    -moz-transition-timing-function: ease-in-out;
    -webkit-transition-timing-function: ease-in-out;
    -o-transition-timing-function: ease-in-out;
    transition-duration: .2s;
    -ms-transition-duration: .2s;
    -moz-transition-duration: .2s;
    -webkit-transition-duration: .2s;
    -o-transition-duration: .2s;}

.page-id-6851 .r8_image_bg_hero.hero_content_dep_height, .page-id-6850 .r8_image_bg_hero.hero_content_dep_height, .page-id-6852 .r8_image_bg_hero.hero_content_dep_height, .page-id-6849 .r8_image_bg_hero.hero_content_dep_height, .page-id-6848 .r8_image_bg_hero.hero_content_dep_height, .page-id-6853 .r8_image_bg_hero.hero_content_dep_height, .page-id-6821 .r8_image_bg_hero.hero_content_dep_height { padding-top:20px; padding-bottom:40px; }

.cta-button.style4 { background-image: var(--wpr-bg-c719c226-1ee7-4323-af36-db576f769785);
    background-size: 48px;
    background-repeat: no-repeat;
    background-position: 4px 3px;
	font-size:1rem; font-weight:600; border-radius:30px; color:#767676; padding:16px; border:1px solid #e5e5e5;
padding-left:60px; padding-right:15px; z-index:9998;}
.cta-button { box-shadow:none; }
.cta-button.red { background-color:#ffffff;}
.style4:hover { box-shadow:none; }
.site_footer {padding-bottom:90px;}

.mobile_nav #menu-item-6777 a:nth-child(2) {pointer-events:none;}

/* category ajax filter pro */

#caf-post-layout1 { display:flex; }

.caf-post-layout1 .manage-layout1 { box-shadow:none !important; border:1px solid #ccc; display:flex; flex-wrap:wrap; }

.caf-post-layout1 #manage-post-area {  }

.data-target-div1 .caf-post-layout1 .caf-post-title h2, .data-target-div1 .caf-post-layout1 .caf-post-title h2 a { font-weight:500 !important; }

.caf-post-layout1 .caf-content { text-align:left !important; }

.caf-post-layout1 .caf-content-read-more { margin:0 auto; margin-bottom:30px; align-self:flex-end; }

.caf-post-layout1 a.caf-read-more { font-size:20px !important; border-radius: 10px !important; font-weight:400; padding: 12px 30px !important; border:3px solid #E96E01 !important; margin-top:5px; }

.data-target-div1 .caf-post-layout1 a.caf-read-more:hover { color: #232323 !important; background-color:#fff; border:3px solid #E96E01; }

.data-target-div1 div#caf-multiple-taxonomy-filter ul li input[type='checkbox']:checked + label::before { color:#E96E01 !important; }

.data-target-div1 div#caf-multiple-taxonomy-filter ul li label { padding-right:40px; }

.caf-post-layout1 .caf-featured-img-box { width:auto !important; height: auto !important; }

.caf-post-layout1 .caf-content { padding:5px 30px 15px 30px !important; line-height:29px !important; }

.caf-post-layout1 .caf-post-title { padding: 20px 30px 5px 30px !important; line-height:28px !important; }

.data-target-div1 div#caf-multiple-taxonomy-filter ul li label { font-weight:400; }



/* GENERAL STYLING */

.flowchartqn { border:1px solid #000; padding:20px; }

h1.entry-title {max-width:1280px; margin:0 auto; padding:0 50px; margin-top:50px;}

.pullquote-less-space { padding: 1em 0 2em 0; }

.dropdown-header {color:#333333;
    font-size: 36px;
    font-weight: 500;
    line-height: 1.25;}

.dropdown-orange-header-notoppad {
	color: #E96E01;
    font-size: 22px;
	line-height:26px;
    font-weight: 500;
    text-align: left;
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 5px 0px;
    display: block;
}
.dropdown-orange-header {
	color: #E96E01;
    font-size: 22px;
	line-height:26px;
    font-weight: 500;
    text-align: left;
    margin: 0px 0px 0px 0px;
    padding: 20px 0px 5px 0px;
    display: block;
}


.posts-navigation .nav-previous a::before, .post-navigation .nav-previous a::before { content:'‹'; font-family:'Barlow Semi Condensed'; }

.posts-navigation .nav-next a::after, .post-navigation .nav-next a::after { content:'›'; font-family:'Barlow Semi Condensed'; }

.posts-navigation .nav-links, .post-navigation .nav-links { min-width:350px; }

.archive .archive_category_title, .archive.category .archive_category_title, .archive.tax-media_category .archive_category_title { color:#696969 !important; text-transform:none !important; }

.r8_image_bg_hero.hero_content_dep_height { padding-bottom:100px; }

h1, h2, h3, h4, h5, h6 { text-transform:none; }

.r8_wysiwig_content h4 a {
	font-family:'Barlow Semi Condensed', sans-serif;
	font-weight:500 !important;
	-webkit-font-smoothing: antialiased;
	font-size:24px;
	color:#333333 !important;
	line-height:1.25;
}
.r8_wysiwig_content h5 a { 
	font-family:'Barlow Semi Condensed', sans-serif;
	font-weight:500 !important;
	-webkit-font-smoothing: antialiased;
	line-height:1.25;
	font-size:23px;}

h6 a {font-family:'Barlow Semi Condensed', sans-serif}

strong { font-weight:600 !important;}

.orangeboldondark {font-weight:600 !important;}
.orangeondark, .orangeboldondark { color:#ff8200 !important; }
.orangebold { color:#E96E01; font-weight:600 !important; }
.ttnone {text-transform:none;}
.horange {color:#E96E01;}
.border-round {border-radius:30px !important;}
.border-circle img {border-radius:100%;}

.disabled a { pointer-events: none; cursor: default !important; }

.floatleft { width:45%; margin-right:30px; }
.floatright { width:45%; margin-left:30px; }
.clearboth { clear:both; }

#comments { border-top:2px solid #000000; padding-top:30px; }

.border1 {border:1px solid #ccc;}

.no-padding {padding:0 !important;}
.no-margin {margin:0 !important;}

.flex, .flex33 { display:flex; align-items:center; }
.flex div {width:50%;}
.flexmarginright { padding-right:30px; }
.flex3 { display:flex; align-items:top; }
.flex33 div:first-child {width:33%;}
.flex33 div:last-child {width:66%;}

.flex-omni-image { width:130px !important; }
.flex-omni-image img { max-width:100px; }
.flex-omni-text { width:max-content !important; }
.omni-next-1, .omni-next-2, .omni-next-3 { padding:10px 25px; margin-bottom:20px; }
.omni-next-1 { background-color:#e96e01; color:#fff; }
.omni-next-2 { background-color:#13516E; color:#fff; }
.omni-next-3 { background-color:#4a99d8; color:#fff; }

ul, ol { margin-left:0px; }

.r8_main_header { background-color:#fbfbfc; }

.r8_flexible_content_section .r8_section_title { max-width:none; }

.r8_accordion_section .r8_accordion_row_title { padding:20px 30px; padding-right:50px; margin-top:7px; }

.r8_accordion li.is-expanded .r8_accordion_row_title_tag { color:#E96E01; }

.r8_flexible_content_section.r8_accordion_section .r8_accordion_open_icon { color:#fff; background-color:#E96E01; transform: rotate(-90deg) translate(50%,0);
-webkit-transform: rotate(-90deg) translate(50%,0);
    -moz-transform: rotate(-90deg) translate(50%,0);
    -ms-transform: rotate(-90deg) translate(50%,0);
    -o-transform: rotate(-90deg) translate(50%,0); 
	-webkit-transition: -webkit-transform .01s;
    -moz-transition: -moz-transform .01s;
    transition: transform .01s; }
    
.leftbar { display:flex; align-items:top; }
.leftbar .heading { min-width:150px; max-width:150px;  padding:20px; }
.leftbar .heading h2, .leftbar .heading h3 { color:#E96E01; font-weight:500; font-size:26px; line-height:26px; }
.leftbar .content { border-left:1px solid #333; padding:20px 20px; width:100%; }
.leftbar .content h3 { font-size:21px; font-weight:600; }
.leftbar .content h4.example { font-size:20px; }


#mega-menu-item-6759 .mega-sub-menu {padding-right:50px !important;  }

.hero-request-button .hero-request-button-arrow { background-color:#fff; color:#E96E01; font-size:34px; padding-bottom:6px; padding-left:18px; padding-right:16px; border-radius:9px; font-weight:600; margin-left:25px; position:relative; top:3px; line-height:17px; }
.hero-request-button { padding-right:7px !important; font-weight:500 !important; }

:where(.wp-block-columns) {margin-bottom:0px;}

.r8_posts_section .r8-post-footer-entry h6 {font-family:'Barlow Semi Condensed'; font-weight:300;}

#secondary ul li ul li:before {margin-top:3px;}

.pagination-container .citrine-posts-navigation .page-numbers:not(.next):not(.prev) {padding:3px 12px;}

.r8_btn.primary_btn, #content input[type="submit"] {border-color:#E96E01 !important;}
.r8_btn.primary_btn:hover, #content form[data-r8-class='r8_primary_form'] .gform_footer input[type="submit"]:hover, body .gform_wrapper .gform_footer input[type="submit"]:hover {color:#232323 !important;background-color:#fff !important;}

.r8_flexible_content_section .slick-slider .slick-prev {background-image:var(--wpr-bg-0d5767c0-6b06-4bf6-916c-a331b07ba289);top:75px;}
.r8_flexible_content_section .slick-slider .slick-next {background-image:var(--wpr-bg-c6a12261-b1d0-44c7-af38-2b7e9e51e9c5);top:75px;}

ul.orange, ul.white, ul.black {margin-left:0px;padding-left:3px; overflow:hidden;}
ul.orange li, ul.white li, ul.black li {list-style: none;
	background-image: var(--wpr-bg-6d036534-413c-4646-b9b6-0609af4777f7);
	background-repeat: no-repeat;
	background-position: left 10px; padding-left:30px;
	background-size: 14px;}
ul.white li {background-image: var(--wpr-bg-88d79c2a-5c66-43ea-85d7-4a160b877007);}
ul.black li {background-image: var(--wpr-bg-61fd05e7-78ca-4450-8d79-f087b0d3809c);}
ul.orange li ul {margin-left:1em;}
ul.orange li ul li {background-size:10px; background-position:5px 12px; padding-bottom:0px;}

ol.orange {list-style: none; counter-reset: item}
ol.orange li::before {content: counter(item) ". "; color: #E96E01;
  display: inline-block; width: 1em;
  margin-left: -1em;}
ol.orange li {counter-increment: item;}

/* bullets in columns */
.entry-content ul {margin-left:20px;}

a.left-link, a.left-link-small {background-image:var(--wpr-bg-5b0db5f9-07eb-41ff-9fa8-8178f127c936); background-repeat:no-repeat;background-size:39px;padding-left:53px;font-size:20px;padding-top:6px;padding-bottom:11px;display:inline-block;background-position:left center; color:#13516e !important; font-weight:600 !important;
}

a.left-link:hover, .page-id-496 .r8_posts_section .r8_post .post_content .post_title a:hover, .page-id-4585 .r8_posts_section .r8_post .post_content .post_title a:hover { color:#e96e01 !important; }
a.left-link-small { background-size:25px; padding-left:34px; font-size:16px; padding-top:8px; font-weight:500 !important; }
a.left-link-gray {color:#333333 !important;}
a.left-link-gray:hover {color:#E96E01 !important;}
a.left-link-ondark { color:#ff8200 !important;}
a.left-link-ondark:hover { color:#ffffff !important;}

a.left-link-blue {color:#2b668f; !important; background-image:var(--wpr-bg-d4e2b0f8-cddb-4985-af47-e710b2b0e99e); }

a.right-link{background-image:var(--wpr-bg-6d8f1a4f-0cd3-4ea5-ad0e-a623a3d5ea27) !important; background-repeat:no-repeat !important;background-size:50px !important;padding-right:75px !important;background-position:right 2px center !important;
}
a.right-link:hover{background-image:var(--wpr-bg-a262c11b-d507-4b81-a9c3-da290360ef3d) !important;}

a, a:hover, input[type="submit"], input[type="submit"]:hover {transition-timing-function: ease-in-out;
    -ms-transition-timing-function: ease-in-out;
    -moz-transition-timing-function: ease-in-out;
    -webkit-transition-timing-function: ease-in-out;
    -o-transition-timing-function: ease-in-out;
    transition-duration: .2s;
    -ms-transition-duration: .2s;
    -moz-transition-duration: .2s;
    -webkit-transition-duration: .2s;
    -o-transition-duration: .2s; }

.wp-block-separator {border:0px;}

.orange-pad {padding-top:20px;}
.orange-pad li {padding-bottom:10px;}

.r8_flexible_content_section.r8_columns_section-one_column.r8-has-nfwb-border:before, .r8_flexible_content_section.r8_columns_section-two_column.r8-has-nfwb-border:before, .r8_flexible_content_section.r8_columns_section-three_column.r8-has-nfwb-border:before, .r8_flexible_content_section.r8_columns_section-four_column.r8-has-nfwb-border:before, .r8_flexible_content_section.r8_columns_section-five_column.r8-has-nfwb-border:before, .r8_flexible_content_section.r8_columns_section-six_column.r8-has-nfwb-border:before {background-color:#eaeaea !important;}

.r8_posts_section .r8_post .post_thumbnail a:hover img, .r8_posts_section .r8_post .post_thumbnail a:focus img { filter:brightness(0.85) !important; -webkit-filter:brightness(0.85) !important;}
.r8_posts_section .r8_post .post_box_cta {padding-bottom:30px;}
.r8_posts_section .r8_posts.three_column .post_content.has_thumbnail, .r8_posts_section .r8_posts.two_column .post_content.has_thumbnail { padding:20px 30px;}
.r8_posts_section .r8_posts.three_column .post_content.has_thumbnail { padding:20px 30px;}
.r8_posts_section .r8_posts.three_column .post_content { padding:20px 30px;}

/* remove image thumbnail on one column archives */
.archive_content .one_column .post_thumbnail { display:none; }


/* MAIN MENU */
#mega-menu-wrap-primary_menu #mega-menu-primary_menu > li.mega-menu-megamenu > ul.mega-sub-menu li.mega-menu-column > ul.mega-sub-menu > li.mega-menu-item > a.mega-menu-link, #mega-menu-wrap-primary_menu #mega-menu-primary_menu > li.mega-menu-megamenu > ul.mega-sub-menu li.mega-menu-column > ul.mega-sub-menu > li.mega-menu-item > a.mega-menu-link:hover, #mega-menu-wrap-primary_menu #mega-menu-primary_menu > li.mega-menu-megamenu > ul.mega-sub-menu li.mega-menu-column > ul.mega-sub-menu > li.mega-menu-item > a.mega-menu-link:focus { font-weight:500; }

#mega-menu-wrap-primary_menu #mega-menu-primary_menu > li.mega-menu-item > a.mega-menu-link, #mega-menu-wrap-primary_menu #mega-menu-primary_menu > li.mega-menu-item > a.mega-menu-link:hover { font-weight:600 !important;}
#mega-menu-wrap-primary_menu #mega-menu-primary_menu > li.mega-menu-megamenu > ul.mega-sub-menu { filter: drop-shadow(0px 0px 3px #ddd); }
.mega-sub-menu .custom-html-widget h2 { margin-top:0px; margin-bottom:0px; }
#mega-menu-item-custom_html-18 .mega-block-title { border-bottom:1px solid #aaa !important; padding-bottom:10px !important; }
#mega-menu-5203-1 .mega-menu-column { padding-left:20px !important; padding-right:20px !important; border-right:1px solid #aaa !important; min-height:340px !important; }
#mega-menu-5203-1 .mega-menu-column:nth-child(1) { padding-left:0px !important; }
#mega-menu-5203-1 .mega-menu-column:nth-child(4) { padding-right:0px !important; border-right:0px !important; }
#mega-menu-wrap-primary_menu #mega-menu-primary_menu > li.mega-menu-megamenu > ul.mega-sub-menu > li.mega-menu-item li.mega-menu-item > a.mega-menu-link, #mega-menu-wrap-primary_menu #mega-menu-primary_menu > li.mega-menu-megamenu > ul.mega-sub-menu li.mega-menu-column > ul.mega-sub-menu > li.mega-menu-item li.mega-menu-item > a.mega-menu-link {line-height:24px;}
#mega-menu-5204-1 .mega-menu-link { margin-bottom:12px;}
.mega-menu-list { box-shadow:none !important; list-style-type:disc !important; margin-top:10px !important; }

.mega-menu-list li { width:100%; line-height:18px; margin-bottom:10px; }

.mega-menu-list li a {padding-left:0px !important; color:#333;}
.mega-menu-list li a:hover {color:#E96E01;}

.mega-menu-image { width:80%; }

.why-citrine-blurbs p { color:#333; margin-top:14px; line-height:18px; }



/* FOOTER */

#menu-footer-menu {display:flex;}
.site_footer .footer_menu_container .footer_menu a, .site_footer .footer_menu_container .sec_footer_menu a {text-transform:none; font-weight:400; font-size:20px;  }
.site_footer .footer_menu_container .footer_menu li, .site_footer .footer_menu_container .sec_footer_menu li {margin-left:0px; width:100%; text-align:left; line-height:20px; margin-top:14px; }
.sub-menu {margin-left:0px;}
.footer-hide > a:first-of-type {display:none;}
#menu-item-5889, #menu-item-5366 { margin-bottom:15px; }
.sub-menu .sub-menu a { font-size:18px !important; font-weight:300 !important; }
.footer_widget .textwidget { text-align:left; }
.footer_widget .textwidget p { font-size:18px; }
.footer-social { width:1.5em; margin:15px 5px;}

/* BREADCRUMB */

.r8-breadcrumb-area {background:none;}
#crumbs {width:fit-content; background-color:#efefef; padding:3px 10px;}
.r8-breadcrumb-area a, #crumbs { color:#6c6c6c !important; font-size:15px !important; text-transform:none !important; font-weight:400;}
.r8-breadcrumb-area span.current {font-weight:600; color:#181818; text-transform:none; font-size:15px; }

/* ANNOUNCEMENT */
.ancr-inner h6 {color:#fff; line-height:22px}
.ancr-btn-inner a {font-family:'Barlow Semi Condensed',sans-serif; font-weight:600;}
.announce-content { display:flex; align-items:center;}
.announce-text { padding-left:20px; padding-right:20px;}



/* HOME */

#home-hero { display:flex; padding-top:50px; padding-bottom:180px; align-items:center; }
#home-hero div { width:auto; }
#home-hero-1 { max-width:375px; padding-left:10px; padding-right:20px; color: #333333; font-weight: 500; font-size: 26px; line-height: 30px; text-align: right; }
.page-id-7036 h1.homeh1 { padding-top:0px; margin-bottom:15px; line-height:50px; }
.home-leftdiv { padding-bottom:180px; }
.home-video {margin-bottom:180px; box-shadow:0px 50px 35px -45px #999; border-radius:10px; border:12px solid #ffffff; }
.home-video:hover {border-color:#E96E01; opacity:.9;transition-timing-function: ease-in-out;
    -ms-transition-timing-function: ease-in-out;
    -moz-transition-timing-function: ease-in-out;
    -webkit-transition-timing-function: ease-in-out;
    -o-transition-timing-function: ease-in-out;
    transition-duration: .2s;
    -ms-transition-duration: .2s;
    -moz-transition-duration: .2s;
    -webkit-transition-duration: .2s;
    -o-transition-duration: .2s;}
.page-id-7036 #home-hero-1 { text-align:left; padding-left:0px; max-width:100%; }
#home-hero-2 {min-width:280px;}
.home-hero-icons { position:absolute; margin-left:60px;margin-top:50px;}
#home-why .r8_section_title {text-transform:none;padding-bottom:30px;}
#home-why .r8_column:not(:last-child) {border-right:1px solid #e2e2e2;}
#home-why .r8_column { margin-right:0px !important; margin:0px 20px; padding:10px 20px; padding-left:0px; }
.home-how-row2 td { width:24%; font-size:17px; line-height:22px; color:#333; font-weight:600; padding:15px; text-align:center;}
.home-how-row2 td div {min-height:250px;}
.home-how-row2 td p:nth-child(1) { margin-top:0px; margin-bottom:15px; margin-left:15px;margin-right:15px;}
.home-how-row2 td p:nth-child(2) { margin-top:0px; margin-bottom:10px; margin-left:30px;margin-right:0px;}
.home-how-row2 td:nth-child(1) {background-image:var(--wpr-bg-0af859f7-a90c-408e-b0dc-7b75b28d3fd8); background-position:center left; background-repeat:no-repeat; background-size:contain;}
.home-how-row2 td:nth-child(2), .home-how-row2 td:nth-child(3), .home-how-row2 td:nth-child(4) {background-image:var(--wpr-bg-c1320bfa-4c25-4382-80e5-4e299871c394); background-position:center left; background-repeat:no-repeat; background-size:contain;}
.home-how-row2 td:nth-child(5) {background-image:var(--wpr-bg-914eb771-b52b-48e9-9af9-1094cf4b7e33); background-position:center left; background-repeat:no-repeat; background-size:contain; }
.home-how-arrow {width:80%;}

#home-table .r8_column { overflow-x:auto;}

.home-product-flex { display:flex; }
.home-product-flex1 {width:55%;}
.home-product-flex2 {width:45%; margin-left:40px;}

.home-dots { margin-top:10px;background-color: #fff; color: #072c3e; padding: 0px 20px 2px; position: relative; left: -18px; border-radius: 18px; text-align: left; width:max-content;}
.home-product-columns { display:flex; text-align:center; font-size:18px; font-weight:500; color:#fff; line-height:22px; text-align:center; margin-top:40px; }

.home-product-columns div { border-right:1px solid #a2b3ba; padding:0px 20px; }
.home-product-columns div:last-child { border-right:0px; }

#home-request { background-size:cover; }
#home-request .outline_btn, #home-industries-button .outline_btn { border-radius:25px; text-transform:none; color: #fff; border: 2px solid #fff; font-size:16px; font-weight:500; }

#home-industries .r8_section_title, #home-industries-temp .r8_section_title, #home-enterprise .r8_section_title { text-transform:none; padding-bottom:20px; }

#home-industries .r8_column, #past .r8_column {text-align:center;}
#home-industries .r8_column a, #past .r8_column a { font-weight:500;  color:#fff;}
#home-industries .r8_column a:hover, #past .r8_column a:hover { color:#ff8200; }
#home-industries .r8_column a:hover img, #past .r8_column a:hover img {opacity:.8;transition-timing-function: ease-in-out;
    -ms-transition-timing-function: ease-in-out;
    -moz-transition-timing-function: ease-in-out;
    -webkit-transition-timing-function: ease-in-out;
    -o-transition-timing-function: ease-in-out;
    transition-duration: .2s;
    -ms-transition-duration: .2s;
    -moz-transition-duration: .2s;
    -webkit-transition-duration: .2s;
    -o-transition-duration: .2s;}



.why-citrine-industries { width:66%; }
.why-citrine-industries-circles { display:flex; }
.why-citrine-industries-circles div { margin-right:15px; }

.page-id-4815 .r8_flexible_content_section, .home .r8_flexible_content_section, .page-id-7036 .r8_flexible_content_section {background-size:100%;}
.page-id-4815 .r8_image_bg_hero {background-size:contain;background-repeat:repeat-y;}
.home .r8_image_bg_hero, .page-id-7036 .r8_image_bg_hero {background-size:contain;background-repeat:repeat;}
.page-id-4815 .r8_image_bg_hero .r8_hero_content {background-image:var(--wpr-bg-63bf7478-3a67-4ccc-8689-c078a80cfe52);background-size:100%;background-position:bottom;background-repeat:no-repeat;}
.home .r8_image_bg_hero .r8_hero_content, .page-id-7036 .r8_image_bg_hero .r8_hero_content {background-image:var(--wpr-bg-662ae8f9-31cf-4c00-9b32-84fe8e966af3);background-size:100%;background-position:bottom;background-repeat:no-repeat;}
.page-id-4815 .r8_image_bg_hero.hero_content_dep_height, .home .r8_image_bg_hero.hero_content_dep_height, .page-id-7036 .r8_image_bg_hero.hero_content_dep_height {padding-bottom:0px;}
.page-id-4815 .r8_image_bg_hero .container, .home .r8_image_bg_hero .container, .page-id-7036 .r8_image_bg_hero .container {padding-right:0px;}
.page-id-4815 .r8_image_bg_hero .two_columns_content.r8_one_third .hc_section.hc1_section, .home .r8_image_bg_hero .two_columns_content.r8_one_third .hc_section.hc1_section, .page-id-7036 .r8_image_bg_hero .two_columns_content.r8_one_third .hc_section.hc1_section {margin-right:0% !important; padding-top:120px;padding-bottom:220px;}
.page-id-4815 .fixed-header-spacer.no-hero, .home .fixed-header-spacer.no-hero, .page-id-7036 .fixed-header-spacer.no-hero {height:60px !important;}
.page-id-4815 #home-s1, .page-id-4815 #unlocking, .page-id-4815 #prefooter, .home #home-s1, .home #unlocking, .home #prefooter {background-position:bottom;background-repeat:no-repeat;}
.page-id-4815 #unlocking, .home #unlocking {background-color:#fff !important;}
.page-id-4815 #dropshadow, .home #dropshadow {background-position:top;background-repeat:no-repeat;background-color:#fff !important;}
.page-id-4815 .r8_image_bg_hero .two_columns_content.r8_one_third, .home .r8_image_bg_hero .two_columns_content.r8_one_third { align-items:flex-start; }
.page-id-4815 .r8_image_bg_hero .two_columns_content.r8_one_third .r8_button_wrap, .home .r8_image_bg_hero .two_columns_content.r8_one_third .r8_button_wrap {margin-right:10px;}
.page-id-4815 .r8_flexible_content_section .r8_section_title, .home .r8_flexible_content_section .r8_section_title {max-width:1160px;margin-bottom:0px;}
.page-id-4815 .r8_carousel_section .r8_carousel, .home .r8_carousel_section .r8_carousel {padding-top:20px; }
.page-id-4815 .r8_carousel_section .r8_carousel .r8_carousel_content, .home .r8_carousel_section .r8_carousel .r8_carousel_content  {padding:0px;}

#home-enterprise .r8_columns img {padding:0px 60px;}


/* PLATFORM */

.platform-h3 { margin-bottom:0px; }
.platform-h3 a { font-weight:600 !important; font-size:26px; }


.page-id-5447 .r8_image_bg_hero { background-image:var(--wpr-bg-c46a4138-6323-4595-bf88-1ba7e0f1d208); background-position:bottom; }
.page-id-5447 .r8_container, .page-id-5447 .r8_hero .container { padding-left:0px; padding-right:0px; }

.platform-s1-laptop { min-width: 330px; position: absolute; }
#platform-s2 .r8_wysiwig_content div div { padding:20px 0px;}

#Industries img { width:150px; border:4px solid #c2c2c2; border-radius:100%; margin-bottom:20px; }

#who-we-help img { position:absolute; margin-top:-110px; margin-left:140px; }
#who-we-help-content { background-image:var(--wpr-bg-b952c796-6351-4fc7-a401-b10aeefbd98a); background-repeat:repeat-x; background-position:top;}
#who-we-help-content .r8_section_title { max-width:none; padding-left:30px; padding-right:30px; }

.platform-learnmore { width:32%; padding:0px 20px; text-align:center; }
.product-flex { display: flex; align-items: center; }

#who-we-help-accordion .r8_accordion_row_content, #platform-industries-accordion .r8_accordion_row_content { padding:20px 30px; }
#who-we-help-accordion .r8_accordion .r8_accordion_row_content div { display:flex !important; padding-right:40px;  }
#who-we-help-accordion .r8_accordion .r8_accordion_row_content div ul { width:66%; }
#who-we-help-accordion .r8_accordion .r8_accordion_row_content div p { width:33%; margin-left:100px; margin-top:0px; }

#platform-industries-accordion .r8_accordion .r8_accordion_row_content { padding-right:40px; }
#platform-industries-accordion .industries-image { width:33%; }
#platform-industries-accordion .industry-download { display:flex; align-items:center; }
#platform-industries-accordion .industry-download div {width:65%;}
#platform-industries-accordion .industry-download-image { width:30%; padding-right:30px; }

#data-manager-content .flex {margin-bottom:15px;}
#data-manager-content .r8_column { margin-top:40px; }

.page-id-5619 .r8_image_bg_hero { background-image: var(--wpr-bg-747d4366-75b9-48ca-89a8-e206d0f437ec); }
.page-id-5774 .r8_image_bg_hero { background-image: var(--wpr-bg-5d6e9d73-3994-4787-9cd1-0e53ec751030); }
.page-id-5626 .r8_image_bg_hero { background-image: var(--wpr-bg-04941e3a-3977-4139-b19d-c206230caba1); }
.page-id-5619 .r8_hero_content { padding-bottom:200px; }
.page-id-5551 .r8_hero_content { padding-bottom:120px; }
.page-id-5774 .r8_hero_content, .page-id-5626 .r8_hero_content { padding-bottom:160px; }
.page-id-5551 .r8_image_bg_hero, .page-id-5774 .r8_image_bg_hero, .page-id-5619 .r8_image_bg_hero, .page-id-5626 .r8_image_bg_hero { background-position:bottom right; }

#four-block .r8_column { width:50%;margin:0px;}



/* COMPANY */

.investor-list { 
	-webkit-column-count: 3;
	-moz-column-count: 3;
	column-count: 3; }
    
#team { display:flex; }
#team h2.r8_section_title { min-width:150px; max-width:150px; color:#E96E01; font-weight:500; font-size:26px; line-height:26px; padding:20px; text-align:left !important; }
.team-module .tab-content {border-bottom:0px; padding:0px 20px; border-left:1px solid #333;}
.about-award { display:flex; flex-wrap:wrap; }
.about-award div { width:25%; }
.about-award div .wp-caption .wp-caption-text { font-size:20px; padding:0px 10px; }


/* CAREERS */

.employee-satisfaction1 {margin-right:0px; margin-top:50px; width:80%;}
.employee-satisfaction2 {margin-left:0px; width:20%;}


/* WHY CITRINE */

.page-id-5697 .leftbar .heading { min-width:300px; max-width:300px; align-self:center; text-align:right; padding-right:20px; }
.page-id-5697 .r8_image_bg_hero, .page-id-5697 #priorities, .page-id-5697 #technology, .page-id-5697 #industries { background-position:bottom right; }


/* RESOURCES */

.page-id-3098 .leftbar .heading { min-width:170px; max-width:170px; }

.resources-buttons { display:flex; flex-wrap:wrap; }
.resources-buttons .r8_button_wrap { margin-right:15px; margin-bottom:15px; }
.resources-buttons .r8_button_wrap .primary_btn { padding:10px; }

#external-research-tabs { left:85px; border-left:1px solid #333; padding-bottom:0px !important; max-width:1050px; position:relative; margin:0 auto; }
#external-research-tabs .r8_container { padding:25px; margin-bottom:60px; }
#external-research-tabs .r8_tab_content { padding-bottom:0px; }
.student-flex { display:flex; }
.student-flex div { max-width:500px; }
.student-flex1 { padding-right:50px; }

.intro-1, .intro-2, .intro-3 { padding-left:30px; }
.intro-1 { color:#fef7f3; }
.intro-2 { color:#f5be9e; }
.intro-3 { color:#f19e6e; }

#intro-mi-table td { text-align:center; vertical-align:top; }
#intro-mi-table td:nth-child(2), #intro-mi-table td:nth-child(3), #intro-mi-table td:nth-child(4) { width:30%;}
#intro-mi-table td:nth-child(2){ background-image:var(--wpr-bg-dec486ec-524d-466d-a15b-472a073cbe73); background-repeat:no-repeat; background-position:center left; background-size:contain; padding:0px 20px;}
#intro-mi-table td:nth-child(3), #intro-mi-table td:nth-child(4) { background-image:var(--wpr-bg-fa2435fe-21e9-40e6-8b4c-7e37c4ba3953); background-repeat:no-repeat; background-position:center left; background-size:contain; padding:0px 20px; }
#intro-mi-table td:nth-child(5) { background-image:var(--wpr-bg-51210866-6760-43f1-94c7-a42f8ab69ba8); background-repeat:no-repeat; background-position:center left; background-size:contain; padding:0px 10px; 
}
#intro-mi-table td p { margin-top:10px; line-height:26px; }
.intro-mi-col1 { background-color:#E96E01; color:#fff; font-weight:500; text-align:center; padding:10px; vertical-align:middle !important;}
.intro-mi-col1 img { width:27px;}

.miboxes { padding:1px 15px; line-height:38px; font-weight:500; }



/* resource single heroes overrides */
.single-post.group-blog .r8_image_bg_hero { background-image:var(--wpr-bg-7185926f-4109-4b68-8f0a-e8ac3f5dfecb); background-position:bottom center; }

.r8_hero_copy h2, h2.archive_category_title {font-weight:400;}
 
.single-post .r8_hero_copy h1, .parent-pageid-3088 .r8_hero_copy h1 { font-weight:400; }
.single-post .r8_hero_copy .type-casestudy::before { color:#E96E01; font-weight:600; content:'Case Study';}
.single-post .r8_hero_copy .type-datalab::before { color:#E96E01; font-weight:600; content:'DataLab Webinar';}
.single-post .r8_hero_copy .type-webinar::before { color:#E96E01; font-weight:600; content:'Webinar';}
.single-post .r8_hero_copy .type-blog::before { color:#E96E01; font-weight:600; content:'Blog';}
.parent-pageid-3088 .r8_hero_copy .type-whitepaper::before, .r8_hero_copy .type-whitepaper::before { color:#E96E01; font-weight:600; content:'White Paper';}
.parent-pageid-3088 .r8_hero_copy .type-ebook::before { color:#E96E01; font-weight:600; content:'eBook';}
.r8_hero_copy .type-resource::before { color:#E96E01; font-weight:600; content:'Resource';}
.single-post .r8_hero_copy .post-separator::before, .parent-pageid-3088 .r8_hero_copy .post-separator::before, .parent-pageid-3088 .r8_hero_copy .post-separator::before, .r8_hero_copy .post-separator::before { content:' | ';}



/* White papers */
.page-id-3088 #webinar-buttons .r8_button_wrap .r8_btn.primary_btn {width:200px !important;}

/* Webinars */
.page-id-3016 #webinar-buttons .r8_button_wrap .r8_btn.primary_btn {width:160px !important;}
.page-id-3016 #upcoming div.r8_column {background-color:#fff;}
#webinar-buttons { display:flex; }
#webinar-buttons-inside { margin:0 auto; }
#webinar-buttons .r8_button_wrap { float:left; margin-right:20px; margin-bottom:10px;  }
#webinar-buttons .r8_button_wrap .r8_btn.primary_btn { padding:10px; width:140px; height:64px; display:table-cell; vertical-align:middle;}
#webinarflex .column_wysiwig, #webinarflex3 .column_wysiwig {
	  display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    height: 100%;
}

#webinarflex .r8_button_wrap, #webinarflex3 .r8_button_wrap {
	width:100%;
	align-self:flex-end;
}

/* hide footer entry on webinars and industries page */
.page-id-6851 .r8_posts_section .r8-post-footer-entry, .page-id-6850 .r8_posts_section .r8-post-footer-entry, .page-id-6852 .r8_posts_section .r8-post-footer-entry, .page-id-6849 .r8_posts_section .r8-post-footer-entry, .page-id-6848 .r8_posts_section .r8-post-footer-entry, .page-id-6853 .r8_posts_section .r8-post-footer-entry, .page-id-6821 .r8_posts_section .r8-post-footer-entry, .page-id-3016 .r8_posts_section .r8-post-footer-entry, .page-id-2795 .r8_posts_section .r8-post-footer-entry, .page-id-6753 .r8_posts_section .r8-post-footer-entry, .page-id-6755 .r8_posts_section .r8-post-footer-entry, .page-id-6756 .r8_posts_section .r8-post-footer-entry { display:none; }
.page-id-3016 .r8_posts_section .r8_post .post_content.has_thumbnail { padding:20px 30px;}
.page-id-3016 .r8_flexible_content_section.r8_columns_section .r8_column.includes_cta .column_wysiwig .column_cta { width:100%;}

/* Case studies */
.page-id-2795 .r8_posts_section .r8_posts .post_content.has_thumbnail { padding:20px 30px;}
.page-id-2795 .r8_posts.one_column .post_thumbnail { display:block; }
.page-id-2795 .r8_posts_section .r8_posts.r8_featured_posts.one_column .r8_post .post_content { margin-top:0px; margin-bottom:0px; }
.page-id-2795 .r8_carousel_section .r8_carousel .r8_carousel_content {display:block;}
.page-id-2795 .r8_flexible_content_section.r8-has-nfwb-border:before {height:2px;}
.page-id-2795 .r8_flexible_content_section.r8_carousel_section { padding-top:65px; padding-bottom:65px; }
.page-id-2795 .r8_carousel_item_image img { border:1px solid #ddd;
    border-radius: 100%;
    -webkit-border-radius: 100%;
    -moz-border-radius: 100%;}
.page-id-2795 .r8_carousel_content {text-align:left;}
.page-id-2795 .r8_carousel_section .r8_carousel {padding:0px;}
.page-id-2795 .r8_carousel_item_image { margin-left:25px; margin-right:25px;}
.page-id-2795 .r8_image_over_content { padding-left:25px; }

#case-study-buttons { display:flex; }
#case-study-buttons-inside { margin:0 auto; }
#case-study-buttons .r8_button_wrap { float:left; margin-right:30px; margin-bottom:10px;}
#case-study-buttons .r8_button_wrap { 
	margin-right:20px !important;
	margin-bottom:20px;
}
#case-study-buttons .r8_button_wrap .r8_btn.primary_btn { padding:10px; width:130px;}





/* **** NOT SURE IF USED **** */

#blog-webinar-callout {
	background-color: #eaeaea;
  padding: 10px 30px;
  font-weight: 600;
  margin: 50px 0px;
}







/* arrange a meeting */
.arrange-meeting {
	background-image: var(--wpr-bg-e2d9d398-917d-4a74-a518-d42c646b81e4);
	background-size:220px 37px;
	padding-left:55px;
	padding-right:40px;
	background-repeat:no-repeat;
}
.arrange-meeting a {color:#fff !important; font-size:19px !important; font-weight:600 !important; padding-top:4px !important; }


.gform_heading, .gform_description {margin-bottom:0px !important;}

.r8_btn.outline_btn {
	color:#E96E01;
	border:2px solid #E96E01;
	font-size:14px;
	border-radius:0;
	font-weight:600;
	text-transform:uppercase;
	width:175px;
	padding:10px;
	background-color:transparent;
}

.r8_btn.outline_btn:hover {
	background-color:#E96E01;
	color:#ffffff;
}

.wp-block-image figcaption {
	  color: #555d66;
    text-align: center;
    font-size: 13px;
}

.wp-caption .wp-caption-text {font-size:12px;}

.industry-list { margin-top:30px; margin-left:0px; }

.site_footer .footer_widget .gform_title { font-size:25px; }
.site_footer .footer_menu_container .footer_menu>li>a { font-size:18px; }

.apply_ty h2 {text-align:center;}

.archive .archive_category_title, .archive.category .archive_category_title, .archive.tax-media_category .archive_category_title {
	color: #fff;
	text-align: left !important;
}

.r8-right-sidebar {
	display: flex;
	flex-wrap: wrap;
}

.media-top {align-items: flex-start; }
.media-top .wp-block-media-text__media {padding-top:30px;}
ul.children {margin:10px !important;}

#secondary.widget-area .gform_widget ul li ul li:before {content:none;}

body .gform_wrapper .gfield_checkbox li label {padding: 5px 20px 5px 0;}
body .gform_wrapper .gfield_checkbox li label:after {border: 2px solid #97a1a3;}
#gform_9 #field_9_10, #gform_8 #field_8_2 { margin-top:0px; }
#gform_widget-4 .widget-title {margin-bottom:0px;}
#gform_9 .gform_footer, #gform_8 .gform_footer {padding-top:0px;}
.gform_anchor {	display: block;}
.gform_anchor::before {
	content: "";
	display: block;
	width: 0;
	height: 170px;
	margin: -170px 0 0;
}

.r8_btn.secondary_btn:hover {background-color:rgba(255,255,255,.8);}

.podcast-side span {
	position:relative;
	bottom:14px;
	padding-left:8px;
}
.podcast-side {color:#333;}
.podcast-side:hover{color:#E96E01;}
.podcast-listen p a {margin-right:3px;}

.site-footer {position: relative; z-index: 1;}
.site-content {position: relative; z-index: 2;}
.r8-default-header {z-index: 3;}
.r8_hero .r8_wysiwig_content{max-width: 100% !important;}
.single_hero .r8_hero_content{display: none;}
.single article .entry-header{display: none;}






/* **** DRAFT - TO BE REMOVED **** */

#home-catalyst .r8_columns {
	background: rgb(255,255,255);
	background: linear-gradient(180deg, rgba(255,255,255,1) 0%, rgba(250,250,250,1) 100%);
}
#home-catalyst.r8-has-nfwb-border:before {
	background-color:#099ee7 !important;
}

#home-catalyst-left { 
	background-image: var(--wpr-bg-da954607-90f0-4383-9805-42ca8df33b0e);
	background-repeat:no-repeat;
	background-position:left bottom;
	background-size:36px 272px;
}

#home-catalyst-left .r8_btn.btn_blue {
	border-color: #099ee7 !important;
	background: #099ee7;
}

#home-catalyst-left #catalyst-buttons {display:inline-flex;}
#home-catalyst-left #catalyst-buttons .r8_button_wrap {margin-right:25px;}

#home-accelerate {background-position:top;}


.catalyst-video { display:flex; column-gap:30px; }
.catalyst-video > div:first-child { width:50%; }
.catalyst-video > div:nth-child(2) { width:50%; }
.catalyst-video > div:nth-child(2) .wp-video { border:1px solid #000; }
.page-id-7896 .leftbar .heading { min-width:200px; max-width:200px; }
.mejs-overlay-play {background-color:rgba(0,0,0,.1);}

.industries-hero { color:#E96E01 !important; margin-bottom:5px; }
.industries-customers { color:#E96E01; font-weight:500; margin-bottom:20px; }
.industries-logos { width:50%;float:left;padding-right:10px; padding-bottom:3px; margin:0px !important; }
.industries-quote { font-size:28px !important; margin-top:0px; margin-bottom:0px; }
.industries-author { }

/* industries */
.page-id-5005 .r8_flexible_content_section .r8_section_title { max-width:1130px; }
.page-id-5005 .post_excerpt, .page-id-5005 .r8-post-footer-entry, .page-id-4541 .post_box_cta { display:none; }
.page-id-5005 .r8_flexible_content_section.r8_flex_posts_section .r8_post { background-color:#f7f7f7; }
.page-id-5005 .r8_posts_section.r8_flex_posts_section .r8_post .post_content .post_title { text-align:center; text-transform:none; margin-top:0px; margin-bottom:0px; }
.page-id-5005 .r8_posts_section.r8_flex_posts_section .r8_post .post_content .post_title a { color:#333; font-weight:400; display:block; padding-top:15px; padding-bottom:24px; }
.page-id-5005 .r8_posts_section.r8_flex_posts_section .r8_post .post_content .post_title a:hover { color:#E96E01; }
.page-id-5005 .r8_posts_section .r8_posts.four_column .r8_post { width:24%; margin-right:1%; }
.page-id-5005 .r8_posts_section .r8_post .post_box_cta {padding-bottom:0px;}

.page-id-3487 .r8_posts_section .r8_posts.two_column .post_content.has_thumbnail {padding-bottom:0px !important;padding-top:10px;}

/* Product */
.page-id-496 .r8_carousel_section .r8_carousel .r8_carousel_content {padding:0px;}
.page-id-496 .r8_hero_content .r8_button_wrap {float:left;margin-right:40px;}
.page-id-496 .r8_flexible_content_section {background-size:100%;}
.page-id-496 .r8_image_bg_hero .r8_hero_content  {background-image:var(--wpr-bg-c0b94cf7-960b-4787-9df0-23069ac20db1);background-size:100%;background-position:bottom;background-repeat:no-repeat;}
.page-id-496 .r8_image_bg_hero.hero_content_dep_height {background-position:bottom; padding-bottom:0px;}
.page-id-496 .r8_image_bg_hero .container  {padding-right:0px;}
.page-id-496 .r8_image_bg_hero .hc_section.hc1_section {margin-right:0% !important; padding-bottom:220px;}
.page-id-496 .two_column .post_content .post_title a { color:#fff; text-transform:none;}
.page-id-496 .two_column .post_content {
	text-align:center;
}

/*solutions */
.page-id-3564 .bulletcolumn { display: flex; flex-wrap: wrap; width: 60%; padding-left: 10px; }
.page-id-3564 .bulletcolumn ul {padding-right:20px;}
.page-id-3564 .r8_accordion_row_title, .page-id-4186 .r8_accordion_row_title  { background-color:#eaeaea !important; padding-left:25px !important; }
.page-id-3564 .r8_accordion_row_title_tag, .page-id-4186 .r8_accordion_row_title_tag  {text-transform:none; padding-bottom:0px;}
.page-id-3564 .r8_accordion_row_content, .page-id-4186 .r8_accordion_row_content { background-color:#fafafa !important; }
.page-id-3564 .r8_accordion_row_content .acontainer { display:flex; justify-content:space-between; align-items:center; background-color:#fafafa !important; }
.page-id-3564 ul.wysiwig_lg_p, .page-id-4186 ul.wysiwig_lg_p { padding-left:0px; }
.page-id-3564 ul.wysiwig_lg_p li, .page-id-4186 ul.wysiwig_lg_p li  { margin-bottom:20px; }
.page-id-3564 .r8_accordion_section .r8_accordion_row_title, .page-id-4186 .r8_accordion_section .r8_accordion_row_title { border-top:5px solid #fff;}
.page-id-3564 .r8_accordion_row_content .r8_button_wrap, .page-id-4186 .r8_accordion_row_content .r8_button_wrap { width:100%; }

.page-id-4186 .r8_accordion_row_content .acontainer {display:flex; justify-content:space-between; align-items:top; background-color:#fafafa !important;}
.page-id-4186 .r8_accordion_row_content .acontainer div:first-child { padding-right:25px;}
.page-id-4186 .r8_accordion_row_content .acontainer div:last-child { padding-left:25px;}

#solutions-intro-2 { align-self:flex-end;}

/* blog sidebar */
#gform_widget-6 .widget-title, #gform_widget-7 .widget-title { padding-bottom:0px; margin-bottom:0px; }
#gform_widget-6 .gform_title, #gform_widget-7 .gform_title { margin-top:0px; font-size:18px;}

.dki-numbers td:nth-child(1) {width:20%; padding-right:40px;}
.dki-numbers td:nth-child(2) {width:55%; }
.dki-numbers td:nth-child(3) {width:25%; padding-left:20px;padding-right:70px;}

.dki-numbers2 td:nth-child(1) {width:10%; padding-right:30px; vertical-align:top;}
.dki-numbers2 td:nth-child(2) {width:35%; vertical-align:top;}
.dki-numbers2 td:nth-child(3) {width:45%; padding-left:25px;}

#accelflex .r8_wysiwig_content, #accelflex2 .r8_wysiwig_content, #guidingflex .r8_wysiwig_content, #guidingflex2 .r8_wysiwig_content, #guidingflex3 .r8_wysiwig_content, #aiflex .r8_wysiwig_content {
	display: flex;
    flex-direction: row;
    height: 100%;
    flex-wrap: wrap;
	
}

#aiflex .r8_wysiwig_content .r8_button_wrap {width:100%; align-self:flex-end;}

#value .r8_button_wrap { padding-bottom:20px;}

/* remove image thumbnail on About Media section */
#about-media .post_thumbnail {display:none;}

/* dropdown styling */
body .gform_wrapper .dd-options {max-height:280px;}
.dd-options {margin-left:0px !important;}

/* industries hide posts title */
.page-id-2945 .r8_posts_section.r8_flex_posts_section .r8_post .post_content .post_title { display:none; }
.page-id-2945 .r8_posts_section .r8_post .post_content.has_thumbnail { padding:20px 30px;}

.greenhouse-job-board h2.group_headline {color:#a9a9a9;}

#catalyst-rightbq { padding-top:30px;
padding-bottom:30px; }










/* ***** MEDIA QUERIES ***** */


@media only screen and (min-width: 641px){
	.gform_wrapper .top_label li.gfield.gfield_error.gf_left_half {margin-right: 0px !important;}
}


@media screen and (min-width:768px){
	.mi-menu {max-width:200px; text-align:center;}
}


@media screen and (max-width:1280px){ 
	#external-research-tabs { left:0px; margin-left:200px; }
}


@media screen and (max-width:1265px){
	#home-orange-circles .r8_column { width:29%; }
	.page-id-4815 .r8_image_bg_hero .two_columns_content.r8_one_third .hc_section.hc1_section, .home .r8_image_bg_hero .two_columns_content.r8_one_third .hc_section.hc1_section { width:40%; }
	.r8_image_bg_hero .two_columns_content.r8_one_third .hc_section.hc2_section { width:60%; }
	.page-id-4815 .fixed-header-spacer.no-hero, .home .fixed-header-spacer.no-hero {height:100px;}
	.page-id-4815 .r8_image_bg_hero .two_columns_content.r8_one_third .hc_section.hc1_section, .home .r8_image_bg_hero .two_columns_content.r8_one_third .hc_section.hc1_section {padding-bottom:180px;}
	.page-id-4815 #unlocking-right, .home #unlocking-right { padding-bottom:360px;}
	.page-id-4815 #prefooter, .home #prefooter {padding-top:120px !important;}
	.page-id-4815 #home-s1, .home #home-s1 {padding-bottom:100px !important;}
	.r8_image_bg_hero .two_columns_content.r8_one_third .hc_section.hc2_section { width:60%; }
	.page-id-5447 .r8_container, .page-id-5447 .r8_hero .container {padding-left:20px; padding-right:20px;}
}

@media screen and (max-width:1120px){
	
	#catalyst-rightbq { padding-top:16px;
padding-bottom:16px; }
}
	

@media screen and (max-width:1060px){
	
	#catalyst-rightbq { padding-top:30px;
padding-bottom:30px; }
	
}

@media screen and (max-width:1033px){
	.site-header .r8_main_header .r8_main_menu {display:none;}
	.site-header a.mobile_menu_icon {display:block;}
	
	.page-id-4815 #unlocking-right, .home #unlocking-right { padding-bottom:270px;}
	.page-id-4815 #prefooter, .home #prefooter {padding-top:70px !important;}
	
	.site-header .r8_main_header .r8_main_menu {display:none;}
	.site-header a.mobile_menu_icon {display:block;}
	.page-id-5551 .r8_image_bg_hero, .page-id-5774 .r8_image_bg_hero, .page-id-5619 .r8_image_bg_hero, .page-id-5626 .r8_image_bg_hero { background-position:bottom right -100px; }
}


@media screen and (max-width:1000px){
	.team-module .team-member .team-image a { width:30px; height:30px; font-size:16px; bottom:0px; left:0px; }
	
	#mi-table .r8_column { width:100%; }
	#external-research-tabs { margin-left:170px; }
	#home-research { width:300px !important; }
	#home-industry { width:300px !important; }
	.page-id-4815 .r8_image_bg_hero .two_columns_content.r8_one_third .hc_section.hc1_section, .r8_image_bg_hero .two_columns_content.r8_one_third .hc_section.hc2_section, .home .r8_image_bg_hero .two_columns_content.r8_one_third .hc_section.hc1_section { width:50%; }
	.page-id-4815 .fixed-header-spacer.no-hero, .home .fixed-header-spacer.no-hero {height:200px;}
	.page-id-4815 .r8_image_bg_hero .two_columns_content.r8_one_third .hc_section.hc1_section, .home .r8_image_bg_hero .two_columns_content.r8_one_third .hc_section.hc1_section {padding-top:20px;padding-bottom:140px;}

	.why-citrine-industries-circles { display:block !important; }
	.why-citrine-industries-circles div { width:20%; float:left; margin-bottom:15px; }
	
	.leftbar .heading, .page-id-3098 .leftbar .heading, #team h2.r8_section_title { padding-left:0px; padding-right:10px; min-width:120px; max-width:120px; }
	.page-id-3098 .leftbar .heading h2, .page-id-3098 .leftbar .heading h3, .page-id-498 .leftbar .heading h2, .page-id-498 .leftbar .heading h3, #team h2.r8_section_title {font-size:21px;}
	.page-id-5697 .leftbar .heading { padding-left:0px; min-width:200px; max-width:200px; }
	
	.investor-list {-webkit-column-count: 2;
    -moz-column-count: 2;
    column-count: 2;}
	
	#home-research { width:300px !important; }
	#home-industry { width:300px !important; }
	.r8_image_bg_hero .two_columns_content.r8_one_third .hc_section.hc2_section { width:50%; }
	
	.flex33 div:first-child {width:50%;}
.flex33 div:last-child {width:50%;}
}

@media screen and (max-width:959px){ 

	#catalyst-rightbq { padding-top:45px;
padding-bottom:45px; }
	
}

@media screen and (max-width:821px){ 

	#catalyst-rightbq { padding-top:60px;
padding-bottom:60px; }
	
}


@media only screen and (max-width: 805px){ 
	
	#catalyst-rightbq { padding-top:1px;
padding-bottom:1px; }
	
	.page-id-5697 .leftbar .heading { min-width:200px; max-width:200px; }
	.r8_image_bg_hero .two_columns_content.r8_one_third .hc_section.hc2_section {order:1; width:80%;}
	
	.flex, .flex3, .flex33 {display:block;}
	.flex div, .flex3 div { width:100%; margin-bottom:30px; }
	.flex33 div { width:100% !important; margin-bottom:30px;}
	.about-award div { width:30%; }
	.about-award div .wp-caption .wp-caption-text { font-size:16px; padding:0px 10px; }

	.home-product-columns {flex-wrap:wrap;}
	.home-product-columns div { width:33%;float:left; min-height:290px; border-right:0px; }
	.product-flex { flex-wrap:wrap; }
	
	.page-id-4815 .r8_image_bg_hero .two_columns_content.r8_one_third, .home .r8_image_bg_hero .two_columns_content.r8_one_third { flex-direction:column; }
	.page-id-4815 .r8_image_bg_hero .two_columns_content.r8_one_third .hc_section.hc1_section, .home .r8_image_bg_hero .two_columns_content.r8_one_third .hc_section.hc1_section {order:2; width:80%;} 
	.r8_image_bg_hero .two_columns_content.r8_one_third .hc_section.hc2_section {order:1; width:80%;}
	.page-id-4815 #unlocking-right, .home #unlocking-right { padding-bottom:170px;}
	.page-id-4815 #prefooter, .home #prefooter  {padding-top:20px !important;}
}


@media screen and (max-width: 768px){
	#external-research-tabs { margin-left:150px; }
	.archive .archive_content #secondary, .blog .archive_content #secondary {margin-top:4px;}
	.arrange-meeting {
		background-image:none;
		padding-left:0px !important;
		background-color:#E96E01;
	}
	.dki-numbers td:nth-child(3) {padding-right:0px;}
}


@media screen and (max-width: 705px) {
	#home-orange-circles .r8_column {width:49%;}
	#home-hero {padding-top:80px; padding-bottom:120px;}
	#home-hero-1 {font-size:20px !important; line-height:24px !important; padding-left:0px;}
	.home-hero-icons { max-width:300px; margin-left:40px; margin-top:40px; }
	.home-dots { width:unset; }
}


@media screen and (max-width: 626px) {
	#doe-table .r8_column:nth-child(1), #doe-table .r8_column:nth-child(2), #doe-table .r8_column:nth-child(3) {display:none;}
	#doe-table .r8_column:nth-child(3n+2), #doe-table .r8_column:nth-child(3n) { padding-left:20px !important; padding-right:20px !important;}
	.doe-table-header { display:none;}
.doe-table-header-mobile { display:block; }
	
	.circle-image { margin-top:0px; }
	.r8_hero.has-hero-content .r8-breadcrumb-area { top:60px; }
	
	.home-leftdiv {padding-bottom:0px;}
	.home-video {margin-bottom:110px; }
	.home-rightdiv { margin-right:3%;}
	.page-id-7036 .fixed-header-spacer.no-hero {height:30px !important;}
	
	
	#manage-ajax-response { padding-left:0px !important; padding-right:0px !important; }
	.caf-col-md-6 { padding-left:0px !important; padding-right:0px !important; }
	
	#mi-table1 {overflow-x:scroll;}
	#intro-mi-table { min-width:600px;}
	#external-research-tabs { margin-left:120px; }
	#external-research-tabs .r8_tab_content { padding-left:0px; padding-right:0px; }
	#four-block .r8_container {padding:0px;}
	#four-block .r8_column { width:100%;padding:50px 30px !important;}
	.about-award { max-width:230px;}
	.about-award div { width:45%; }
	
	.r8_flexible_content_section.r8_columns_section .r8_column { padding-left:0px !important; padding-right:0px !important; }
	.page-id-5697 #industries .why-citrine-industries { width:100%;}
	.page-id-5697 .leftbar .heading h2, .page-id-5697 .leftbar .heading h3 { min-width:120px; max-width:120px; font-size:21px; }
	.flexmarginright { padding-right:0px; }
	.leftbar .heading { padding-left:0px; padding-right:10px; min-width:100px; max-width:100px; }
	.leftbar .heading h2, .leftbar .heading h3 { font-size:21px; }
	.page-id-498 .leftbar .heading { min-width:110px; max-width:110px;}
	#team h2.r8_section_title { min-width:110px;max-width:110px;}
	.leftbar .content { padding-right:0px; }
	.page-id-5697 .leftbar .heading { align-self:start; }
	
	#Industries img {width:140px;}
	#platform-industries-accordion .industries-image {width:100%; margin:15px 0px;}
	.r8_accordion_section .r8_accordion_row_title { padding:20px; padding-right:40px;}
	#who-we-help-accordion .r8_accordion_row_content, #platform-industries-accordion .r8_accordion_row_content { padding:20px; padding-right:20px !important;}
	
	.platform-learnmore {padding:0px; }
	.page-id-5551 .r8_image_bg_hero, .page-id-5774 .r8_image_bg_hero, .page-id-5619 .r8_image_bg_hero, .page-id-5626 .r8_image_bg_hero { background-position:bottom right -200px; }
	
	.employee-satisfaction1 {margin-top:0px; width:100%;}
	.employee-satisfaction2 {width:245px; margin-top:20px;}
	
	.page-id-2880 #news.r8_flexible_content_section.r8_columns_section .r8_column, .page-id-3016 #upcoming.r8_flexible_content_section.r8_columns_section .r8_column {
    	border:1px solid #ccc !important;
		padding-left:0px !important; padding-right:0px !important;
	 }
	
	.page-id-3564 .r8_accordion_row_content .acontainer, .page-id-4186 .r8_accordion_row_content .acontainer {flex-wrap:wrap;}
	.page-id-3564 .bulletcolumn {width:100%;}
	.page-id-3564 .bulletcolumn ul {margin-left:40px;}
	
	.dki-numbers, .dki-numbers thead, .dki-numbers tbody, .dki-numbers th, .dki-numbers td, .dki-numbers tr { display:block; }
	.dki-numbers td:nth-child(1) {width:50%;}
	.dki-numbers td:nth-child(2) {width:60%;display:inline-block;}
	.dki-numbers td:nth-child(3) {width:40%;padding-left:30px; padding-right:0px;display:inline-block;}
	
	.dki-numbers2, .dki-numbers2 thead, .dki-numbers2 tbody, .dki-numbers2 th, .dki-numbers2 td, .dki-numbers2 tr { display:block; }
	.dki-numbers2 td:nth-child(1) {width:30%;}
	.dki-numbers2 td:nth-child(2) {width:60%;display:inline-block;}
	.dki-numbers2 td:nth-child(3) {width:100%;padding-left:0px; padding-right:0px;display:inline-block;}
	
	.page-id-4186 .r8_accordion_row_content .acontainer div{ width:100% !important;}
	.page-id-4186 .r8_accordion_row_content .acontainer div:first-child { padding-right:0px;}
	.page-id-4186 .r8_accordion_row_content .acontainer div:last-child { padding-left:0px;padding-top:15px;}
	.page-id-4186 .r8_accordion_row_content .acontainer {display:block;}
	
	.r8_image_bg_hero .two_columns_content.r8_one_third .hc_section.hc2_section { width:100%;padding-right:20px;} 
	
	#who-we-help img {margin-left:-20px; margin-top:-86px;}
		.investor-list {-webkit-column-count: 1;
    -moz-column-count: 1;
    column-count: 1;}

	#menu-item-3128, #menu-item-548 {margin-top:15px;}
	#home-why .r8_column { margin-left:0px; }
	.home-product-flex { display:block; }
	.home-product-flex1, .home-product-flex2 { width:100%;}
	.home-product-flex2 {margin-left:0px;}
	#home-product-box1, #home-product-box2 { border:1px solid #E96E01; margin:20px 10px; padding-bottom:0px !important; }
	#home-product-box1 .r8_container, #home-product-box2 .r8_container, #home-product-box1 .r8_container .r8_column, #home-product-box2 .r8_container .r8_column { padding-left:0px !important; padding-right:0px !important; }
	.platform-s1-laptop { position:unset; }
	#who-we-help-accordion .r8_accordion .r8_accordion_row_content div { display:block !important; }
	#who-we-help-accordion .r8_accordion .r8_accordion_row_content div ul { width:100%; }
	#who-we-help-accordion .r8_accordion .r8_accordion_row_content div p { margin-left:0px; width:100%; }
	#platform-industries-accordion .industry-download {display:block;}
	#platform-industries-accordion .industry-download-image { width:80%; }
	#platform-industries-accordion .industry-download div { width:auto; }
	#home-why .r8_column { border-bottom:1px solid #e2e2e2 !important; padding-bottom:40px; margin-bottom:40px; }
	
	#home-industries .r8_column, #past .r8_column { width:45%; margin-right:15px; }
	#home-industries .r8_column:nth-child(1), #past .r8_column:nth-child(1) {margin-top:30px; }
	
	.home-hero-icons { max-width:200px; margin-left:0px; margin-top:20px; }
	#home-catalyst-left {padding-left:50px !important; padding-bottom:0px !important;}
	#home-catalyst-left #catalyst-buttons {display:block;}
	
  	.page-id-4815 .r8_image_bg_hero .two_columns_content.r8_one_third .hc_section.hc1_section, 
  	.page-id-4815 .r8_image_bg_hero .two_columns_content.r8_one_third .hc_section.hc2_section, .home .r8_image_bg_hero .two_columns_content.r8_one_third .hc_section.hc1_section, 
  	.home .r8_image_bg_hero .two_columns_content.r8_one_third .hc_section.hc2_section {
    	width: 100%;
    	padding-right: 20px;
  	} 
  	.page-id-4815 .fixed-header-spacer.no-hero, .home .fixed-header-spacer.no-hero { height: 0px !important;}
  	.page-id-4815 .r8_image_bg_hero.hero_content_dep_height, .home .r8_image_bg_hero.hero_content_dep_height {padding-top: 40px;}
  	.page-id-4815 .r8_image_bg_hero .two_columns_content.r8_one_third .hc_section.hc1_section, .home .r8_image_bg_hero .two_columns_content.r8_one_third .hc_section.hc1_section {padding-bottom: 130px;}
  	.page-id-4815 #home-s1, .home #home-s1 {padding-bottom: 0px !important;}
  	.page-id-4815 #unlocking-right, .home #unlocking-right {padding-bottom: 80px;}
  	.page-id-4815 #prefooter, .home #prefooter {padding-top: 0px !important;}
  	.page-id-4815 #prefooter-text, .home #prefooter-text {padding-top: 20px !important;}
  	.page-id-4815 #home-hero-button, .home #home-hero-button {font-size: 20px !important;}
  	.page-id-4815 #home-hero-button .r8_btn.primary_btn, .home #home-hero-button .r8_btn.primary_btn {font-size: 18px; }
  	.slick-dots { bottom: -110px;}
	.home .r8_carousel_section .r8_carousel {margin-bottom:80px !important;}
}


@media screen and ( max-width: 600px ) {
	.team-module .tab-content ul li { padding:0px; }
	.announce-content { flex-direction:column;}
	
	#virtuallab div:last-child {order:1;}
	#virtuallab div:first-child {order:2;}
	
	.home .r8_columns_section_1 .r8_column {order: 2;}
	.home .r8_columns_section_1 .r8_column:last-child {order: 1;}
	
	/* product */
	.page-id-496 .r8_columns_section_2 .r8_column {order: 2;}
	.page-id-496 .r8_columns_section_2 .r8_column:last-child {order: 1;}
	
	/* sequential learning */
	.page-id-1726 .r8_columns_section_3 .r8_column {order: 2;}
	.page-id-1726 .r8_columns_section_3 .r8_column:last-child {order: 1;}
	
	/* open citrination platform */
	.page-id-1084 .r8_columns_section_3 .r8_column {order: 2;}
	.page-id-1084 .r8_columns_section_3 .r8_column:last-child {order: 1;}
	
	/* colorado school of mines partnership */
	.page-id-1037 .r8_columns_section_2 .r8_column {order: 2;}
	.page-id-1037 .r8_columns_section_2 .r8_column:last-child {order: 1;}
	.page-id-1037 .r8_columns_section_3 .r8_column {order: 2;}
	.page-id-1037 .r8_columns_section_3 .r8_column:last-child {order: 1;}
	.page-id-1037 .r8_columns_section_4 .r8_column {order: 2;}
	.page-id-1037 .r8_columns_section_4 .r8_column:last-child {order: 1;}
	.page-id-1037 .r8_columns_section_5 .r8_column {order: 2;}
	.page-id-1037 .r8_columns_section_5 .r8_column:last-child {order: 1;}
}
	
	
@media screen and (max-width:400px){
	.mobile-alignright {margin-right:1.5em; margin-bottom:1.5em;}
	.mobile-bullet { float:left; }
}

</style>
<style type="text/css" id ="red8-customizer-styles">

    /*secondary-form*/
    #content form[data-r8-class='r8_global_form'] .dd-select,
    form[data-r8-class='r8_global_form'] .dd-select {
        background-color: #fff !important;
        border: 2px solid;
        border-color: #97a1a3;
        border-radius: 0px;
        color: #333333;
        -webkit-appearance: none;
        -moz-appearance: none;
        appearance: none;
        -webkit-border-radius: 0px;
    }

    #content form[data-r8-class='r8_global_form'] .dd-option,
    form[data-r8-class='r8_global_form'] .dd-selected,
    #content form[data-r8-class='r8_global_form'] .dd-option,
    form[data-r8-class='r8_global_form'] .dd-selected {
        color: #97a1a3;
    }

    /*primary-form*/
    #content  form[data-r8-class='r8_primary_form'] .dd-select,
    .site_footer form[data-r8-class='r8_primary_form'] .dd-select {
        background-color: #fff !important;
        border: 2px solid;
        border-color: #97a1a3;
        border-radius: 0px;
        color: #000;
        -webkit-appearance: none;
        -moz-appearance: none;
        appearance: none;
        -webkit-border-radius: 0px;
    }

    #content form[data-r8-class='r8_primary_form'] .dd-option,
    form[data-r8-class='r8_primary_form'] .dd-selected,
    #content form[data-r8-class='r8_primary_form'] .dd-option,
    form[data-r8-class='r8_primary_form'] .dd-selected {
        color: #97a1a3;
    }

    /*secondary-form*/
    #content form[data-r8-class='r8_secondary_form'] .dd-select,
    .site_footer form[data-r8-class='r8_secondary_form'] .dd-select {
        background-color: #fff !important;
        border: 2px solid;
        border-color: #97a1a3;
        border-radius: 0px;
        color: #000;
        -webkit-appearance: none;
        -moz-appearance: none;
        appearance: none;
        -webkit-border-radius: 0px;
    }

    #content form[data-r8-class='r8_secondary_form'] .dd-option,
    form[data-r8-class='r8_secondary_form'] .dd-selected,
    #content form[data-r8-class='r8_secondary_form'] .dd-option,
    form[data-r8-class='r8_secondary_form'] .dd-selected {
        color: #97a1a3;
    }

    .site-header .r8_main_header .primary_menu>li .sub-menu>li.current_page_item:not(.no-active-state)>a,
    .site-header .r8_main_header .primary_menu>li .sub-menu>li.current-menu-item:not(.no-active-state)>a {
        /*background-color: ;*/
        color: #e96e01;
    }

    </style>
<noscript><style id="rocket-lazyload-nojs-css">.rll-youtube-player, [data-lazy-src]{display:none !important;}</style></noscript><script type="text/rocketlazyloadscript">
/*! loadCSS rel=preload polyfill. [c]2017 Filament Group, Inc. MIT License */
(function(w){"use strict";if(!w.loadCSS){w.loadCSS=function(){}}
var rp=loadCSS.relpreload={};rp.support=(function(){var ret;try{ret=w.document.createElement("link").relList.supports("preload")}catch(e){ret=!1}
return function(){return ret}})();rp.bindMediaToggle=function(link){var finalMedia=link.media||"all";function enableStylesheet(){link.media=finalMedia}
if(link.addEventListener){link.addEventListener("load",enableStylesheet)}else if(link.attachEvent){link.attachEvent("onload",enableStylesheet)}
setTimeout(function(){link.rel="stylesheet";link.media="only x"});setTimeout(enableStylesheet,3000)};rp.poly=function(){if(rp.support()){return}
var links=w.document.getElementsByTagName("link");for(var i=0;i<links.length;i++){var link=links[i];if(link.rel==="preload"&&link.getAttribute("as")==="style"&&!link.getAttribute("data-loadcss")){link.setAttribute("data-loadcss",!0);rp.bindMediaToggle(link)}}};if(!rp.support()){rp.poly();var run=w.setInterval(rp.poly,500);if(w.addEventListener){w.addEventListener("load",function(){rp.poly();w.clearInterval(run)})}else if(w.attachEvent){w.attachEvent("onload",function(){rp.poly();w.clearInterval(run)})}}
if(typeof exports!=="undefined"){exports.loadCSS=loadCSS}
else{w.loadCSS=loadCSS}}(typeof global!=="undefined"?global:this))
</script><style id="rocket-lazyrender-inline-css">[data-wpr-lazyrender] {content-visibility: auto;}</style><style id="wpr-lazyload-bg-container"></style><style id="wpr-lazyload-bg-exclusion">.home .r8_image_bg_hero .r8_hero_content, .page-id-7036 .r8_image_bg_hero .r8_hero_content{--wpr-bg-662ae8f9-31cf-4c00-9b32-84fe8e966af3: url('https://citrine.io/wp-content/uploads/2023/11/refresh-home-hero-bg-noai.jpg');}.arrange-meeting{--wpr-bg-e2d9d398-917d-4a74-a518-d42c646b81e4: url('https://citrine.io/wp-content/uploads/2025/07/request-shorter.png');}.r8_image_bg_hero{--wpr-bg-577cca7a-d49c-472f-acb1-ee3f436dea90: url('https://citrine.io/wp-content/uploads/2023/11/refresh-home-hero-bgbase.jpg');}</style>
<noscript>
<style id="wpr-lazyload-bg-nostyle">.fancybox-team .fancybox-close{--wpr-bg-78d09630-816b-4eaf-9a8e-643f02c50e57: url('https://citrine.io/wp-content/themes/inn8ly-builder/images/close-button@2x.png');}.fancybox-team .fancybox-prev span,.fancybox-team .fancybox-next span{--wpr-bg-f5ae7b19-2da2-4ff4-9635-352d2d7d0d78: url('https://citrine.io/wp-content/themes/inn8ly-builder/images/slide-arrow@2x.png');}select:not([multiple]){--wpr-bg-21644b68-f61c-40ec-9b95-616f4416e43b: url('https://citrine.io/wp-content/themes/inn8ly-builder/images/select_down.png');}.gform_wrapper select:not([multiple]){--wpr-bg-052c668c-8898-4eb1-91d8-88db2c06e76d: url('https://citrine.io/wp-content/themes/inn8ly-builder/images/select_down.png');}.r8_flexible_content_section .slick-slider .slick-next,.r8_flexible_content_section .slick-slider .slick-prev,.r8_slider_hero_container .slick-slider .slick-next,.r8_slider_hero_container .slick-slider .slick-prev{--wpr-bg-cb64026f-f9dd-492d-94a4-2179b66db8f9: url('https://citrine.io/wp-content/themes/citrine/images/slide-arrow@2x.png');}.r8_slider_section .testimony:before{--wpr-bg-390fd887-a6df-412b-a1e0-3dab2d8b1c0a: url('https://citrine.io/wp-content/themes/citrine/images/left-quote.svg');}.r8_slider_section .testimony:after{--wpr-bg-a959438b-85f2-40b0-9d6b-3215bfe1322c: url('https://citrine.io/wp-content/themes/citrine/images/right-quote.svg');}#gform_wrapper_1 .gform_ajax_spinner{--wpr-bg-f22dfbff-8143-47ae-9080-36f96cea604c: url('https://citrine.io/wp-content/themes/citrine/images/Spinner-1s-80px.gif');}#fancybox-loading div{--wpr-bg-94e243e8-21e9-4b1e-b5b9-b46c2206ea44: url('https://citrine.io/wp-content/themes/inn8ly-builder/js/vendor/fancyBox/fancybox_loading.gif');}#fancybox-loading div{--wpr-bg-e207e2d1-b8e6-4316-ac31-d090aaa4758e: url('https://citrine.io/wp-content/themes/inn8ly-builder/js/vendor/fancyBox/fancybox_loading@2x.gif');}.fancybox-nav{--wpr-bg-245ece6d-7bde-478f-9268-75dfdbebb101: url('https://citrine.io/wp-content/themes/inn8ly-builder/js/vendor/fancyBox/blank.gif');}.fancybox-overlay{--wpr-bg-ea7f2e71-30d8-44fb-8956-f5e0ea895ff1: url('https://citrine.io/wp-content/themes/inn8ly-builder/js/vendor/fancyBox/fancybox_overlay.png');}#fancybox-loading,.fancybox-close,.fancybox-prev span,.fancybox-next span{--wpr-bg-ec4fcf2e-1337-4234-a5bf-de90a73a73de: url('https://citrine.io/wp-content/themes/inn8ly-builder/js/vendor/fancyBox/fancybox_sprite.png');}#fancybox-loading,.fancybox-close,.fancybox-prev span,.fancybox-next span{--wpr-bg-5dc50bb5-a0f9-4107-b449-ed8ec494e50b: url('https://citrine.io/wp-content/themes/inn8ly-builder/js/vendor/fancyBox/fancybox_sprite@2x.png');}.slick-loading .slick-list{--wpr-bg-e3d02a03-4509-442e-b502-960ef42c2ef4: url('https://citrine.io/wp-content/themes/inn8ly-builder/css/ajax-loader.gif');}.rll-youtube-player .play{--wpr-bg-c389d831-2312-471f-88f9-c02acea03a77: url('https://citrine.io/wp-content/plugins/wp-rocket/assets/img/youtube.png');}.cta-button.style4{--wpr-bg-c719c226-1ee7-4323-af36-db576f769785: url('https://citrine.io/wp-content/uploads/2025/01/citrine-float-icon@2x.png');}.r8_flexible_content_section .slick-slider .slick-prev{--wpr-bg-0d5767c0-6b06-4bf6-916c-a331b07ba289: url('https://citrine.io/wp-content/uploads/2021/11/carousel-right@2x.png');}.r8_flexible_content_section .slick-slider .slick-next{--wpr-bg-c6a12261-b1d0-44c7-af38-2b7e9e51e9c5: url('https://citrine.io/wp-content/uploads/2021/11/carousel-right@2x.png');}ul.orange li, ul.white li, ul.black li{--wpr-bg-6d036534-413c-4646-b9b6-0609af4777f7: url('https://citrine.io/wp-content/uploads/2021/11/bullet-orange@2x.png');}ul.white li{--wpr-bg-88d79c2a-5c66-43ea-85d7-4a160b877007: url('https://citrine.io/wp-content/uploads/2021/11/bullet-white@2x.png');}ul.black li{--wpr-bg-61fd05e7-78ca-4450-8d79-f087b0d3809c: url('https://citrine.io/wp-content/uploads/2023/05/bullet-black@2x.png');}a.left-link, a.left-link-small{--wpr-bg-5b0db5f9-07eb-41ff-9fa8-8178f127c936: url('https://citrine.io/wp-content/uploads/2021/11/link-arrow-orange@2x.png');}a.left-link-blue{--wpr-bg-d4e2b0f8-cddb-4985-af47-e710b2b0e99e: url('https://citrine.io/wp-content/uploads/2022/02/link-arrow-blue@2x.png');}a.right-link{--wpr-bg-6d8f1a4f-0cd3-4ea5-ad0e-a623a3d5ea27: url('https://citrine.io/wp-content/uploads/2023/05/link-right@2x.png');}a.right-link:hover{--wpr-bg-a262c11b-d507-4b81-a9c3-da290360ef3d: url('https://citrine.io/wp-content/uploads/2023/05/link-right-hover@2x.png');}.home-how-row2 td:nth-child(1){--wpr-bg-0af859f7-a90c-408e-b0dc-7b75b28d3fd8: url('https://citrine.io/wp-content/uploads/2023/11/refresh-home-how-bgarrowblue.png');}.home-how-row2 td:nth-child(2), .home-how-row2 td:nth-child(3), .home-how-row2 td:nth-child(4){--wpr-bg-c1320bfa-4c25-4382-80e5-4e299871c394: url('https://citrine.io/wp-content/uploads/2023/11/refresh-home-how-bgarroworange.png');}.home-how-row2 td:nth-child(5){--wpr-bg-914eb771-b52b-48e9-9af9-1094cf4b7e33: url('https://citrine.io/wp-content/uploads/2023/11/refresh-home-how-bgshadow.png');}.page-id-4815 .r8_image_bg_hero .r8_hero_content{--wpr-bg-63bf7478-3a67-4ccc-8689-c078a80cfe52: url('https://citrine.io/wp-content/uploads/2021/11/home-hero-bottom.png');}.page-id-5447 .r8_image_bg_hero{--wpr-bg-c46a4138-6323-4595-bf88-1ba7e0f1d208: url('https://citrine.io/wp-content/uploads/2023/11/platform-hero-new-scaled.jpg');}#who-we-help-content{--wpr-bg-b952c796-6351-4fc7-a401-b10aeefbd98a: url('https://citrine.io/wp-content/uploads/2023/11/shadowbg@2x-scaled.jpg');}.page-id-5619 .r8_image_bg_hero{--wpr-bg-747d4366-75b9-48ca-89a8-e206d0f437ec: url('https://citrine.io/wp-content/uploads/2023/11/bgslab2.jpg');}.page-id-5774 .r8_image_bg_hero{--wpr-bg-5d6e9d73-3994-4787-9cd1-0e53ec751030: url('https://citrine.io/wp-content/uploads/2023/11/bg-catalyst-r.jpg');}.page-id-5626 .r8_image_bg_hero{--wpr-bg-04941e3a-3977-4139-b19d-c206230caba1: url('https://citrine.io/wp-content/uploads/2023/11/bgs-people2.jpg');}#intro-mi-table td:nth-child(2){--wpr-bg-dec486ec-524d-466d-a15b-472a073cbe73: url('https://citrine.io/wp-content/uploads/2025/07/intro-mi-orange-arrow.png');}#intro-mi-table td:nth-child(3), #intro-mi-table td:nth-child(4){--wpr-bg-fa2435fe-21e9-40e6-8b4c-7e37c4ba3953: url('https://citrine.io/wp-content/uploads/2023/11/intro-mi-gray-arrow.png');}#intro-mi-table td:nth-child(5){--wpr-bg-51210866-6760-43f1-94c7-a42f8ab69ba8: url('https://citrine.io/wp-content/uploads/2023/11/intro-mi-shadow.png');}.single-post.group-blog .r8_image_bg_hero{--wpr-bg-7185926f-4109-4b68-8f0a-e8ac3f5dfecb: url('https://citrine.io/wp-content/uploads/2023/11/datamanager-hero-none.jpg');}#home-catalyst-left{--wpr-bg-da954607-90f0-4383-9805-42ca8df33b0e: url('https://citrine.io/wp-content/uploads/2023/10/icon-new.jpg');}.page-id-496 .r8_image_bg_hero .r8_hero_content{--wpr-bg-c0b94cf7-960b-4787-9df0-23069ac20db1: url('https://citrine.io/wp-content/uploads/2021/11/home-hero-bottom.png');}.r8_columns_section_8{--wpr-bg-2c474318-b396-45df-af77-b6bc16faf337: url('https://citrine.io/wp-content/uploads/2023/11/home-product-bg@2x-scaled.jpg');}</style>
</noscript>
<script type="application/javascript">const rocket_pairs = [{"selector":".fancybox-team .fancybox-close","style":".fancybox-team .fancybox-close{--wpr-bg-78d09630-816b-4eaf-9a8e-643f02c50e57: url('https:\/\/citrine.io\/wp-content\/themes\/inn8ly-builder\/images\/close-button@2x.png');}","hash":"78d09630-816b-4eaf-9a8e-643f02c50e57","url":"https:\/\/citrine.io\/wp-content\/themes\/inn8ly-builder\/images\/close-button@2x.png"},{"selector":".fancybox-team .fancybox-prev span,.fancybox-team .fancybox-next span","style":".fancybox-team .fancybox-prev span,.fancybox-team .fancybox-next span{--wpr-bg-f5ae7b19-2da2-4ff4-9635-352d2d7d0d78: url('https:\/\/citrine.io\/wp-content\/themes\/inn8ly-builder\/images\/slide-arrow@2x.png');}","hash":"f5ae7b19-2da2-4ff4-9635-352d2d7d0d78","url":"https:\/\/citrine.io\/wp-content\/themes\/inn8ly-builder\/images\/slide-arrow@2x.png"},{"selector":"select:not([multiple])","style":"select:not([multiple]){--wpr-bg-21644b68-f61c-40ec-9b95-616f4416e43b: url('https:\/\/citrine.io\/wp-content\/themes\/inn8ly-builder\/images\/select_down.png');}","hash":"21644b68-f61c-40ec-9b95-616f4416e43b","url":"https:\/\/citrine.io\/wp-content\/themes\/inn8ly-builder\/images\/select_down.png"},{"selector":".gform_wrapper select:not([multiple])","style":".gform_wrapper select:not([multiple]){--wpr-bg-052c668c-8898-4eb1-91d8-88db2c06e76d: url('https:\/\/citrine.io\/wp-content\/themes\/inn8ly-builder\/images\/select_down.png');}","hash":"052c668c-8898-4eb1-91d8-88db2c06e76d","url":"https:\/\/citrine.io\/wp-content\/themes\/inn8ly-builder\/images\/select_down.png"},{"selector":".r8_flexible_content_section .slick-slider .slick-next,.r8_flexible_content_section .slick-slider .slick-prev,.r8_slider_hero_container .slick-slider .slick-next,.r8_slider_hero_container .slick-slider .slick-prev","style":".r8_flexible_content_section .slick-slider .slick-next,.r8_flexible_content_section .slick-slider .slick-prev,.r8_slider_hero_container .slick-slider .slick-next,.r8_slider_hero_container .slick-slider .slick-prev{--wpr-bg-cb64026f-f9dd-492d-94a4-2179b66db8f9: url('https:\/\/citrine.io\/wp-content\/themes\/citrine\/images\/slide-arrow@2x.png');}","hash":"cb64026f-f9dd-492d-94a4-2179b66db8f9","url":"https:\/\/citrine.io\/wp-content\/themes\/citrine\/images\/slide-arrow@2x.png"},{"selector":".r8_slider_section .testimony","style":".r8_slider_section .testimony:before{--wpr-bg-390fd887-a6df-412b-a1e0-3dab2d8b1c0a: url('https:\/\/citrine.io\/wp-content\/themes\/citrine\/images\/left-quote.svg');}","hash":"390fd887-a6df-412b-a1e0-3dab2d8b1c0a","url":"https:\/\/citrine.io\/wp-content\/themes\/citrine\/images\/left-quote.svg"},{"selector":".r8_slider_section .testimony","style":".r8_slider_section .testimony:after{--wpr-bg-a959438b-85f2-40b0-9d6b-3215bfe1322c: url('https:\/\/citrine.io\/wp-content\/themes\/citrine\/images\/right-quote.svg');}","hash":"a959438b-85f2-40b0-9d6b-3215bfe1322c","url":"https:\/\/citrine.io\/wp-content\/themes\/citrine\/images\/right-quote.svg"},{"selector":"#gform_wrapper_1 .gform_ajax_spinner","style":"#gform_wrapper_1 .gform_ajax_spinner{--wpr-bg-f22dfbff-8143-47ae-9080-36f96cea604c: url('https:\/\/citrine.io\/wp-content\/themes\/citrine\/images\/Spinner-1s-80px.gif');}","hash":"f22dfbff-8143-47ae-9080-36f96cea604c","url":"https:\/\/citrine.io\/wp-content\/themes\/citrine\/images\/Spinner-1s-80px.gif"},{"selector":"#fancybox-loading div","style":"#fancybox-loading div{--wpr-bg-94e243e8-21e9-4b1e-b5b9-b46c2206ea44: url('https:\/\/citrine.io\/wp-content\/themes\/inn8ly-builder\/js\/vendor\/fancyBox\/fancybox_loading.gif');}","hash":"94e243e8-21e9-4b1e-b5b9-b46c2206ea44","url":"https:\/\/citrine.io\/wp-content\/themes\/inn8ly-builder\/js\/vendor\/fancyBox\/fancybox_loading.gif"},{"selector":"#fancybox-loading div","style":"#fancybox-loading div{--wpr-bg-e207e2d1-b8e6-4316-ac31-d090aaa4758e: url('https:\/\/citrine.io\/wp-content\/themes\/inn8ly-builder\/js\/vendor\/fancyBox\/fancybox_loading@2x.gif');}","hash":"e207e2d1-b8e6-4316-ac31-d090aaa4758e","url":"https:\/\/citrine.io\/wp-content\/themes\/inn8ly-builder\/js\/vendor\/fancyBox\/fancybox_loading@2x.gif"},{"selector":".fancybox-nav","style":".fancybox-nav{--wpr-bg-245ece6d-7bde-478f-9268-75dfdbebb101: url('https:\/\/citrine.io\/wp-content\/themes\/inn8ly-builder\/js\/vendor\/fancyBox\/blank.gif');}","hash":"245ece6d-7bde-478f-9268-75dfdbebb101","url":"https:\/\/citrine.io\/wp-content\/themes\/inn8ly-builder\/js\/vendor\/fancyBox\/blank.gif"},{"selector":".fancybox-overlay","style":".fancybox-overlay{--wpr-bg-ea7f2e71-30d8-44fb-8956-f5e0ea895ff1: url('https:\/\/citrine.io\/wp-content\/themes\/inn8ly-builder\/js\/vendor\/fancyBox\/fancybox_overlay.png');}","hash":"ea7f2e71-30d8-44fb-8956-f5e0ea895ff1","url":"https:\/\/citrine.io\/wp-content\/themes\/inn8ly-builder\/js\/vendor\/fancyBox\/fancybox_overlay.png"},{"selector":"#fancybox-loading,.fancybox-close,.fancybox-prev span,.fancybox-next span","style":"#fancybox-loading,.fancybox-close,.fancybox-prev span,.fancybox-next span{--wpr-bg-ec4fcf2e-1337-4234-a5bf-de90a73a73de: url('https:\/\/citrine.io\/wp-content\/themes\/inn8ly-builder\/js\/vendor\/fancyBox\/fancybox_sprite.png');}","hash":"ec4fcf2e-1337-4234-a5bf-de90a73a73de","url":"https:\/\/citrine.io\/wp-content\/themes\/inn8ly-builder\/js\/vendor\/fancyBox\/fancybox_sprite.png"},{"selector":"#fancybox-loading,.fancybox-close,.fancybox-prev span,.fancybox-next span","style":"#fancybox-loading,.fancybox-close,.fancybox-prev span,.fancybox-next span{--wpr-bg-5dc50bb5-a0f9-4107-b449-ed8ec494e50b: url('https:\/\/citrine.io\/wp-content\/themes\/inn8ly-builder\/js\/vendor\/fancyBox\/fancybox_sprite@2x.png');}","hash":"5dc50bb5-a0f9-4107-b449-ed8ec494e50b","url":"https:\/\/citrine.io\/wp-content\/themes\/inn8ly-builder\/js\/vendor\/fancyBox\/fancybox_sprite@2x.png"},{"selector":".slick-loading .slick-list","style":".slick-loading .slick-list{--wpr-bg-e3d02a03-4509-442e-b502-960ef42c2ef4: url('https:\/\/citrine.io\/wp-content\/themes\/inn8ly-builder\/css\/ajax-loader.gif');}","hash":"e3d02a03-4509-442e-b502-960ef42c2ef4","url":"https:\/\/citrine.io\/wp-content\/themes\/inn8ly-builder\/css\/ajax-loader.gif"},{"selector":".rll-youtube-player .play","style":".rll-youtube-player .play{--wpr-bg-c389d831-2312-471f-88f9-c02acea03a77: url('https:\/\/citrine.io\/wp-content\/plugins\/wp-rocket\/assets\/img\/youtube.png');}","hash":"c389d831-2312-471f-88f9-c02acea03a77","url":"https:\/\/citrine.io\/wp-content\/plugins\/wp-rocket\/assets\/img\/youtube.png"},{"selector":".cta-button.style4","style":".cta-button.style4{--wpr-bg-c719c226-1ee7-4323-af36-db576f769785: url('https:\/\/citrine.io\/wp-content\/uploads\/2025\/01\/citrine-float-icon@2x.png');}","hash":"c719c226-1ee7-4323-af36-db576f769785","url":"https:\/\/citrine.io\/wp-content\/uploads\/2025\/01\/citrine-float-icon@2x.png"},{"selector":".r8_flexible_content_section .slick-slider .slick-prev","style":".r8_flexible_content_section .slick-slider .slick-prev{--wpr-bg-0d5767c0-6b06-4bf6-916c-a331b07ba289: url('https:\/\/citrine.io\/wp-content\/uploads\/2021\/11\/carousel-right@2x.png');}","hash":"0d5767c0-6b06-4bf6-916c-a331b07ba289","url":"https:\/\/citrine.io\/wp-content\/uploads\/2021\/11\/carousel-right@2x.png"},{"selector":".r8_flexible_content_section .slick-slider .slick-next","style":".r8_flexible_content_section .slick-slider .slick-next{--wpr-bg-c6a12261-b1d0-44c7-af38-2b7e9e51e9c5: url('https:\/\/citrine.io\/wp-content\/uploads\/2021\/11\/carousel-right@2x.png');}","hash":"c6a12261-b1d0-44c7-af38-2b7e9e51e9c5","url":"https:\/\/citrine.io\/wp-content\/uploads\/2021\/11\/carousel-right@2x.png"},{"selector":"ul.orange li, ul.white li, ul.black li","style":"ul.orange li, ul.white li, ul.black li{--wpr-bg-6d036534-413c-4646-b9b6-0609af4777f7: url('https:\/\/citrine.io\/wp-content\/uploads\/2021\/11\/bullet-orange@2x.png');}","hash":"6d036534-413c-4646-b9b6-0609af4777f7","url":"https:\/\/citrine.io\/wp-content\/uploads\/2021\/11\/bullet-orange@2x.png"},{"selector":"ul.white li","style":"ul.white li{--wpr-bg-88d79c2a-5c66-43ea-85d7-4a160b877007: url('https:\/\/citrine.io\/wp-content\/uploads\/2021\/11\/bullet-white@2x.png');}","hash":"88d79c2a-5c66-43ea-85d7-4a160b877007","url":"https:\/\/citrine.io\/wp-content\/uploads\/2021\/11\/bullet-white@2x.png"},{"selector":"ul.black li","style":"ul.black li{--wpr-bg-61fd05e7-78ca-4450-8d79-f087b0d3809c: url('https:\/\/citrine.io\/wp-content\/uploads\/2023\/05\/bullet-black@2x.png');}","hash":"61fd05e7-78ca-4450-8d79-f087b0d3809c","url":"https:\/\/citrine.io\/wp-content\/uploads\/2023\/05\/bullet-black@2x.png"},{"selector":"a.left-link, a.left-link-small","style":"a.left-link, a.left-link-small{--wpr-bg-5b0db5f9-07eb-41ff-9fa8-8178f127c936: url('https:\/\/citrine.io\/wp-content\/uploads\/2021\/11\/link-arrow-orange@2x.png');}","hash":"5b0db5f9-07eb-41ff-9fa8-8178f127c936","url":"https:\/\/citrine.io\/wp-content\/uploads\/2021\/11\/link-arrow-orange@2x.png"},{"selector":"a.left-link-blue","style":"a.left-link-blue{--wpr-bg-d4e2b0f8-cddb-4985-af47-e710b2b0e99e: url('https:\/\/citrine.io\/wp-content\/uploads\/2022\/02\/link-arrow-blue@2x.png');}","hash":"d4e2b0f8-cddb-4985-af47-e710b2b0e99e","url":"https:\/\/citrine.io\/wp-content\/uploads\/2022\/02\/link-arrow-blue@2x.png"},{"selector":"a.right-link","style":"a.right-link{--wpr-bg-6d8f1a4f-0cd3-4ea5-ad0e-a623a3d5ea27: url('https:\/\/citrine.io\/wp-content\/uploads\/2023\/05\/link-right@2x.png');}","hash":"6d8f1a4f-0cd3-4ea5-ad0e-a623a3d5ea27","url":"https:\/\/citrine.io\/wp-content\/uploads\/2023\/05\/link-right@2x.png"},{"selector":"a.right-link","style":"a.right-link:hover{--wpr-bg-a262c11b-d507-4b81-a9c3-da290360ef3d: url('https:\/\/citrine.io\/wp-content\/uploads\/2023\/05\/link-right-hover@2x.png');}","hash":"a262c11b-d507-4b81-a9c3-da290360ef3d","url":"https:\/\/citrine.io\/wp-content\/uploads\/2023\/05\/link-right-hover@2x.png"},{"selector":".home-how-row2 td:nth-child(1)","style":".home-how-row2 td:nth-child(1){--wpr-bg-0af859f7-a90c-408e-b0dc-7b75b28d3fd8: url('https:\/\/citrine.io\/wp-content\/uploads\/2023\/11\/refresh-home-how-bgarrowblue.png');}","hash":"0af859f7-a90c-408e-b0dc-7b75b28d3fd8","url":"https:\/\/citrine.io\/wp-content\/uploads\/2023\/11\/refresh-home-how-bgarrowblue.png"},{"selector":".home-how-row2 td:nth-child(2), .home-how-row2 td:nth-child(3), .home-how-row2 td:nth-child(4)","style":".home-how-row2 td:nth-child(2), .home-how-row2 td:nth-child(3), .home-how-row2 td:nth-child(4){--wpr-bg-c1320bfa-4c25-4382-80e5-4e299871c394: url('https:\/\/citrine.io\/wp-content\/uploads\/2023\/11\/refresh-home-how-bgarroworange.png');}","hash":"c1320bfa-4c25-4382-80e5-4e299871c394","url":"https:\/\/citrine.io\/wp-content\/uploads\/2023\/11\/refresh-home-how-bgarroworange.png"},{"selector":".home-how-row2 td:nth-child(5)","style":".home-how-row2 td:nth-child(5){--wpr-bg-914eb771-b52b-48e9-9af9-1094cf4b7e33: url('https:\/\/citrine.io\/wp-content\/uploads\/2023\/11\/refresh-home-how-bgshadow.png');}","hash":"914eb771-b52b-48e9-9af9-1094cf4b7e33","url":"https:\/\/citrine.io\/wp-content\/uploads\/2023\/11\/refresh-home-how-bgshadow.png"},{"selector":".page-id-4815 .r8_image_bg_hero .r8_hero_content","style":".page-id-4815 .r8_image_bg_hero .r8_hero_content{--wpr-bg-63bf7478-3a67-4ccc-8689-c078a80cfe52: url('https:\/\/citrine.io\/wp-content\/uploads\/2021\/11\/home-hero-bottom.png');}","hash":"63bf7478-3a67-4ccc-8689-c078a80cfe52","url":"https:\/\/citrine.io\/wp-content\/uploads\/2021\/11\/home-hero-bottom.png"},{"selector":".page-id-5447 .r8_image_bg_hero","style":".page-id-5447 .r8_image_bg_hero{--wpr-bg-c46a4138-6323-4595-bf88-1ba7e0f1d208: url('https:\/\/citrine.io\/wp-content\/uploads\/2023\/11\/platform-hero-new-scaled.jpg');}","hash":"c46a4138-6323-4595-bf88-1ba7e0f1d208","url":"https:\/\/citrine.io\/wp-content\/uploads\/2023\/11\/platform-hero-new-scaled.jpg"},{"selector":"#who-we-help-content","style":"#who-we-help-content{--wpr-bg-b952c796-6351-4fc7-a401-b10aeefbd98a: url('https:\/\/citrine.io\/wp-content\/uploads\/2023\/11\/shadowbg@2x-scaled.jpg');}","hash":"b952c796-6351-4fc7-a401-b10aeefbd98a","url":"https:\/\/citrine.io\/wp-content\/uploads\/2023\/11\/shadowbg@2x-scaled.jpg"},{"selector":".page-id-5619 .r8_image_bg_hero","style":".page-id-5619 .r8_image_bg_hero{--wpr-bg-747d4366-75b9-48ca-89a8-e206d0f437ec: url('https:\/\/citrine.io\/wp-content\/uploads\/2023\/11\/bgslab2.jpg');}","hash":"747d4366-75b9-48ca-89a8-e206d0f437ec","url":"https:\/\/citrine.io\/wp-content\/uploads\/2023\/11\/bgslab2.jpg"},{"selector":".page-id-5774 .r8_image_bg_hero","style":".page-id-5774 .r8_image_bg_hero{--wpr-bg-5d6e9d73-3994-4787-9cd1-0e53ec751030: url('https:\/\/citrine.io\/wp-content\/uploads\/2023\/11\/bg-catalyst-r.jpg');}","hash":"5d6e9d73-3994-4787-9cd1-0e53ec751030","url":"https:\/\/citrine.io\/wp-content\/uploads\/2023\/11\/bg-catalyst-r.jpg"},{"selector":".page-id-5626 .r8_image_bg_hero","style":".page-id-5626 .r8_image_bg_hero{--wpr-bg-04941e3a-3977-4139-b19d-c206230caba1: url('https:\/\/citrine.io\/wp-content\/uploads\/2023\/11\/bgs-people2.jpg');}","hash":"04941e3a-3977-4139-b19d-c206230caba1","url":"https:\/\/citrine.io\/wp-content\/uploads\/2023\/11\/bgs-people2.jpg"},{"selector":"#intro-mi-table td:nth-child(2)","style":"#intro-mi-table td:nth-child(2){--wpr-bg-dec486ec-524d-466d-a15b-472a073cbe73: url('https:\/\/citrine.io\/wp-content\/uploads\/2025\/07\/intro-mi-orange-arrow.png');}","hash":"dec486ec-524d-466d-a15b-472a073cbe73","url":"https:\/\/citrine.io\/wp-content\/uploads\/2025\/07\/intro-mi-orange-arrow.png"},{"selector":"#intro-mi-table td:nth-child(3), #intro-mi-table td:nth-child(4)","style":"#intro-mi-table td:nth-child(3), #intro-mi-table td:nth-child(4){--wpr-bg-fa2435fe-21e9-40e6-8b4c-7e37c4ba3953: url('https:\/\/citrine.io\/wp-content\/uploads\/2023\/11\/intro-mi-gray-arrow.png');}","hash":"fa2435fe-21e9-40e6-8b4c-7e37c4ba3953","url":"https:\/\/citrine.io\/wp-content\/uploads\/2023\/11\/intro-mi-gray-arrow.png"},{"selector":"#intro-mi-table td:nth-child(5)","style":"#intro-mi-table td:nth-child(5){--wpr-bg-51210866-6760-43f1-94c7-a42f8ab69ba8: url('https:\/\/citrine.io\/wp-content\/uploads\/2023\/11\/intro-mi-shadow.png');}","hash":"51210866-6760-43f1-94c7-a42f8ab69ba8","url":"https:\/\/citrine.io\/wp-content\/uploads\/2023\/11\/intro-mi-shadow.png"},{"selector":".single-post.group-blog .r8_image_bg_hero","style":".single-post.group-blog .r8_image_bg_hero{--wpr-bg-7185926f-4109-4b68-8f0a-e8ac3f5dfecb: url('https:\/\/citrine.io\/wp-content\/uploads\/2023\/11\/datamanager-hero-none.jpg');}","hash":"7185926f-4109-4b68-8f0a-e8ac3f5dfecb","url":"https:\/\/citrine.io\/wp-content\/uploads\/2023\/11\/datamanager-hero-none.jpg"},{"selector":"#home-catalyst-left","style":"#home-catalyst-left{--wpr-bg-da954607-90f0-4383-9805-42ca8df33b0e: url('https:\/\/citrine.io\/wp-content\/uploads\/2023\/10\/icon-new.jpg');}","hash":"da954607-90f0-4383-9805-42ca8df33b0e","url":"https:\/\/citrine.io\/wp-content\/uploads\/2023\/10\/icon-new.jpg"},{"selector":".page-id-496 .r8_image_bg_hero .r8_hero_content","style":".page-id-496 .r8_image_bg_hero .r8_hero_content{--wpr-bg-c0b94cf7-960b-4787-9df0-23069ac20db1: url('https:\/\/citrine.io\/wp-content\/uploads\/2021\/11\/home-hero-bottom.png');}","hash":"c0b94cf7-960b-4787-9df0-23069ac20db1","url":"https:\/\/citrine.io\/wp-content\/uploads\/2021\/11\/home-hero-bottom.png"},{"selector":".r8_columns_section_8","style":".r8_columns_section_8{--wpr-bg-2c474318-b396-45df-af77-b6bc16faf337: url('https:\/\/citrine.io\/wp-content\/uploads\/2023\/11\/home-product-bg@2x-scaled.jpg');}","hash":"2c474318-b396-45df-af77-b6bc16faf337","url":"https:\/\/citrine.io\/wp-content\/uploads\/2023\/11\/home-product-bg@2x-scaled.jpg"}]; const rocket_excluded_pairs = [{"selector":".home .r8_image_bg_hero .r8_hero_content, .page-id-7036 .r8_image_bg_hero .r8_hero_content","style":".home .r8_image_bg_hero .r8_hero_content, .page-id-7036 .r8_image_bg_hero .r8_hero_content{--wpr-bg-662ae8f9-31cf-4c00-9b32-84fe8e966af3: url('https:\/\/citrine.io\/wp-content\/uploads\/2023\/11\/refresh-home-hero-bg-noai.jpg');}","hash":"662ae8f9-31cf-4c00-9b32-84fe8e966af3","url":"https:\/\/citrine.io\/wp-content\/uploads\/2023\/11\/refresh-home-hero-bg-noai.jpg"},{"selector":".arrange-meeting","style":".arrange-meeting{--wpr-bg-e2d9d398-917d-4a74-a518-d42c646b81e4: url('https:\/\/citrine.io\/wp-content\/uploads\/2025\/07\/request-shorter.png');}","hash":"e2d9d398-917d-4a74-a518-d42c646b81e4","url":"https:\/\/citrine.io\/wp-content\/uploads\/2025\/07\/request-shorter.png"},{"selector":".r8_image_bg_hero","style":".r8_image_bg_hero{--wpr-bg-577cca7a-d49c-472f-acb1-ee3f436dea90: url('https:\/\/citrine.io\/wp-content\/uploads\/2023\/11\/refresh-home-hero-bgbase.jpg');}","hash":"577cca7a-d49c-472f-acb1-ee3f436dea90","url":"https:\/\/citrine.io\/wp-content\/uploads\/2023\/11\/refresh-home-hero-bgbase.jpg"}];</script><meta name="generator" content="WP Rocket 3.22" data-wpr-features="wpr_lazyload_css_bg_img wpr_delay_js wpr_defer_js wpr_minify_js wpr_async_css wpr_lazyload_images wpr_lazyload_iframes wpr_automatic_lazy_rendering wpr_oci wpr_image_dimensions wpr_minify_css wpr_cdn wpr_preload_links wpr_desktop" /></head>

<body class="home wp-singular page-template page-template-page-flexible-content page-template-page-flexible-content-php page page-id-5206 wp-custom-logo wp-theme-inn8ly-builder wp-child-theme-citrine r8_header_fixed wp-schema-pro-2.11.3 mega-menu-primary-menu group-blog">

<div  id="page" class="site">
	<a class="skip-link screen-reader-text" href="#main">Skip to content</a>

	<div  class="r8-default-header r8-left-header">

	<header  id="masthead" class="site-header   " role="banner">

		<div class="top_header_search_form">
			<div  class="container">
				<form role="search" method="get" class="search-form" action="https://citrine.io/">
				<label>
					<span class="screen-reader-text">Search for:</span>
					<input type="search" class="search-field" placeholder="Search &hellip;" value="" name="s" />
				</label>
				<input type="submit" class="search-submit" value="Search" />
			</form>			</div>
		</div>

		<div class="r8_sec_menu_wrapper">
	<div class="container r8_container">
		<div class="r8-menu-secondary-menu-container">
			<ul id="secondary_menu" class="r8_secondary_menu"><li id="menu-item-3023" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3023"><a href="https://citrine.io/resources/webinars/">Webinars</a></li>
<li id="menu-item-3711" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3711"><a href="https://citrine.io/careers/">Careers</a></li>
<li id="menu-item-2194" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2194"><a href="https://citrine.io/contact/">Contact</a></li>
<li id="menu-item-3056" class="arrange-meeting menu-item menu-item-type-post_type menu-item-object-page menu-item-3056"><a href="https://citrine.io/request-a-demo/">Request a Demo ›</a></li>
</ul>		</div>
	</div>
</div>


		<div class="r8_main_header">
			<div class="container r8_container">

				
				<div class="header_wrapper">

					<div class="site-branding ">
            <div id="logo" class="header-logo  ">
            <a href="https://citrine.io/" class="custom-logo-link" rel="home" aria-current="page"><img width="458" height="121" src="https://citrine.io/wp-content/uploads/2018/07/Citrine-informatics-logo.svg" class="custom-logo" alt="Citrine Informatics logo" decoding="async" /></a>        </div>
    
            <p class="site-title"><a href="https://citrine.io/" rel="home">Citrine Informatics</a></p>
    
            <p class="site_description">AI for Product Development, Production, and Sales in Materials and Chemicals</p>
    
</div><!-- .site-branding -->

					<div class="r8_main_menu">
												<nav id="site-navigation" class="main-navigation " role="navigation">
							<button class="menu-toggle" aria-controls="primary-menu" aria-expanded="false">Primary Menu</button>
							<div id="mega-menu-wrap-primary_menu" class="mega-menu-wrap"><div class="mega-menu-toggle"><div class="mega-toggle-blocks-left"></div><div class="mega-toggle-blocks-center"></div><div class="mega-toggle-blocks-right"><div class='mega-toggle-block mega-menu-toggle-animated-block mega-toggle-block-0' id='mega-toggle-block-0'><button aria-controls="mega-menu-primary_menu" aria-expanded="false" aria-haspopup="true" aria-label="Toggle Menu" class="mega-toggle-animated mega-toggle-animated-slider" type="button">
                  <span class="mega-toggle-animated-box">
                    <span class="mega-toggle-animated-inner"></span>
                  </span>
                </button></div></div></div><ul id="mega-menu-primary_menu" class="mega-menu max-mega-menu mega-menu-horizontal mega-no-js" data-event="hover_intent" data-effect="fade_up" data-effect-speed="200" data-effect-mobile="disabled" data-effect-speed-mobile="0" data-panel-width=".r8_container" data-mobile-force-width="false" data-second-click="go" data-document-click="collapse" data-vertical-behaviour="standard" data-breakpoint="768" data-unbind="true" data-mobile-state="collapse_all" data-mobile-direction="vertical"><li class="mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-menu-item-has-children mega-menu-megamenu mega-menu-grid mega-align-bottom-left mega-menu-item-5628" id="mega-menu-item-5628"><a class="mega-menu-link" href="https://citrine.io/platform/" aria-expanded="false" aria-controls="mega-sub-menu-5628">Platform<span class="mega-indicator" aria-hidden="true"></span></a>
<ul class="mega-sub-menu" role='presentation' id='mega-sub-menu-5628'>
<li class="mega-menu-row" id="mega-menu-5628-0">
	<ul class="mega-sub-menu" style='--columns:12' role='presentation'>
<li class="mega-menu-column mega-menu-columns-12-of-12" style="--columns:12; --span:12" id="mega-menu-5628-0-0">
		<ul class="mega-sub-menu">
<li class="mega-menu-item mega-menu-item-type-widget widget_custom_html mega-menu-item-custom_html-17" id="mega-menu-item-custom_html-17"><div class="textwidget custom-html-widget"><span class="dropdown-header">
	Platform
</span></div></li>		</ul>
</li>	</ul>
</li><li class="mega-menu-row" id="mega-menu-5628-1">
	<ul class="mega-sub-menu" style='--columns:12' role='presentation'>
<li class="mega-menu-column mega-menu-columns-4-of-12" style="--columns:12; --span:4" id="mega-menu-5628-1-0">
		<ul class="mega-sub-menu">
<li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-has-children mega-menu-item-5685" id="mega-menu-item-5685"><a class="mega-menu-link" href="/platform/#products">Products<span class="mega-indicator" aria-hidden="true"></span></a>
			<ul class="mega-sub-menu" id='mega-sub-menu-5685'>
<li class="mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-menu-item-5631" id="mega-menu-item-5631"><a class="mega-menu-link" href="https://citrine.io/platform/citrine-datamanager/">Citrine DataManager</a></li><li class="mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-menu-item-5630" id="mega-menu-item-5630"><a class="mega-menu-link" href="https://citrine.io/platform/citrine-virtuallab/">Citrine VirtualLab</a></li><li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-8038" id="mega-menu-item-8038"><a class="mega-menu-link" href="/platform/citrine-catalyst/">Citrine Catalyst</a></li><li class="mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-menu-item-5629" id="mega-menu-item-5629"><a class="mega-menu-link" href="https://citrine.io/platform/citrine-professional-services/">Citrine Professional Services</a></li>			</ul>
</li>		</ul>
</li><li class="mega-menu-column mega-menu-columns-4-of-12" style="--columns:12; --span:4" id="mega-menu-5628-1-1">
		<ul class="mega-sub-menu">
<li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-has-children mega-menu-item-5684" id="mega-menu-item-5684"><a class="mega-menu-link" href="/platform/#enterprise-ready">Enterprise-Ready<span class="mega-indicator" aria-hidden="true"></span></a>
			<ul class="mega-sub-menu" id='mega-sub-menu-5684'>
<li class="mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-menu-item-5701" id="mega-menu-item-5701"><a class="mega-menu-link" href="https://citrine.io/platform/getting-started/">Getting Started</a></li><li class="mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-menu-item-5704" id="mega-menu-item-5704"><a class="mega-menu-link" href="https://citrine.io/platform/security/">Security</a></li><li class="mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-menu-item-5705" id="mega-menu-item-5705"><a class="mega-menu-link" href="https://citrine.io/platform/flexibility/">Flexibility</a></li><li class="mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-menu-item-5707" id="mega-menu-item-5707"><a class="mega-menu-link" href="https://citrine.io/platform/support/">Support</a></li>			</ul>
</li>		</ul>
</li><li class="mega-menu-column mega-menu-columns-4-of-12" style="--columns:12; --span:4" id="mega-menu-5628-1-2">
		<ul class="mega-sub-menu">
<li class="mega-menu-item mega-menu-item-type-widget widget_custom_html mega-menu-item-custom_html-33" id="mega-menu-item-custom_html-33"><div class="textwidget custom-html-widget"><div style="background: linear-gradient(0deg, rgba(255,255,255,1) 0%, rgba(245,245,245,1) 100%); padding:20px 25px;">
	<span style="font-weight:500; font-size:18px;">Introducing</span><br> <br>
	<a href="/platform/citrine-catalyst/"><picture class="mega-menu-image">
<source type="image/webp" srcset="https://citrine.io/wp-content/uploads/2023/10/citrine-catalyst-normal.png.webp"/>
<img src="https://citrine.io/wp-content/uploads/2023/10/citrine-catalyst-normal.png" width="200" height="22" alt="Citrine Catalyst"/>
</picture>
</a><br>
<a href="/platform/citrine-catalyst/" class="left-link-small">Find out more</a>
</div></div></li>		</ul>
</li>	</ul>
</li></ul>
</li><li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-has-children mega-menu-megamenu mega-menu-grid mega-align-bottom-left mega-menu-item-5202" id="mega-menu-item-5202"><a class="mega-menu-link" href="/who-we-help/" aria-expanded="false" aria-controls="mega-sub-menu-5202">Who We Help<span class="mega-indicator" aria-hidden="true"></span></a>
<ul class="mega-sub-menu" role='presentation' id='mega-sub-menu-5202'>
<li class="mega-menu-row" id="mega-menu-5202-0">
	<ul class="mega-sub-menu" style='--columns:12' role='presentation'>
<li class="mega-menu-column mega-menu-columns-12-of-12" style="--columns:12; --span:12" id="mega-menu-5202-0-0">
		<ul class="mega-sub-menu">
<li class="mega-menu-item mega-menu-item-type-widget widget_custom_html mega-menu-item-custom_html-21" id="mega-menu-item-custom_html-21"><div class="textwidget custom-html-widget"><span class="dropdown-header">
	Who We Help
</span></div></li><li class="mega-menu-item mega-menu-item-type-widget widget_custom_html mega-menu-item-custom_html-22" id="mega-menu-item-custom_html-22"><div class="textwidget custom-html-widget"><div style="display:flex;margin-top:20px;">
<div style="margin-right:20px; width:50%; border-right:1px solid #aaa;">
	<div style="font-size:16px; line-height:24px;">
		<span class="dropdown-orange-header-notoppad"><a href="/who-we-help/#BusinessFunctions">Business Functions</a></span>
		<div style="display:flex;">
		<ul class="mega-menu-list" style="padding-left:26px;">
			<li>Product Developers &amp;<br/>Materials Engineers</li>
			<li>Data Scientists</li>
			<li>Data Managers</li>
			<li>C-Suite &amp; Business Unit Leaders</li>
			<li>Compliance Managers</li>
			</ul>
			<ul class="mega-menu-list">
				<li>Sales &amp; Marketing Executives</li>
				<li>Supply Chain Managers</li>
				<li>Production &amp;<br/>Manufacturing Executives</li>
				<li>Finance Managers</li>
		</ul>
		</div>
<a href="/who-we-help/#BusinessFunctions" class="left-link-small">Learn more</a>
	</div>
</div>
<div style="width:50%;">
	<span class="dropdown-orange-header-notoppad">
		<a href="/who-we-help/#Industries">Industries</a>
	</span>
	<div style="font-size:16px; line-height:24px;">
		<div style="display:flex;">
		<ul class="mega-menu-list" style="padding-left:26px;">
			<li><a href="/who-we-help/plastics/">Plastics</a></li>
			<li><a href="/who-we-help/coatings-adhesives-and-sealants/">Coatings, Adhesives &amp; Sealants</a></li>
			<li><a href="/who-we-help/personal-care-and-cosmetics/">Personal Care &amp; Cosmetics</a></li>
			<li><a href="/who-we-help/specialty-chemicals/">Specialty Chemicals</a></li>
			<li><a href="/who-we-help/food-and-beverage/">Food &amp; Beverage</a></li>
			<li><a href="/who-we-help/packaging/">Packaging</a></li>
			<li><a href="/who-we-help/additives-and-ingredients/">Additives &amp; Ingredients</a></li>
			</ul>
				<ul class="mega-menu-list">
					<li>Building Materials</li>
					<li>Batteries</li>
					<li>Ceramics &amp; Glass</li>
					<li>Metals &amp; Alloys</li>
					<li>Consumer Electronics</li>
					<li>Aerospace &amp; Defense</li>
					<li>Automotive</li>
		</ul>
		</div>
<a href="/who-we-help/#Industries" class="left-link-small">Learn more</a>
	</div>
</div>
</div></div></li>		</ul>
</li>	</ul>
</li></ul>
</li><li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-has-children mega-menu-megamenu mega-menu-grid mega-align-bottom-left mega-menu-item-5203" id="mega-menu-item-5203"><a class="mega-menu-link" href="/why-citrine/" aria-expanded="false" aria-controls="mega-sub-menu-5203">Why Citrine?<span class="mega-indicator" aria-hidden="true"></span></a>
<ul class="mega-sub-menu" role='presentation' id='mega-sub-menu-5203'>
<li class="mega-menu-row" id="mega-menu-5203-0">
	<ul class="mega-sub-menu" style='--columns:12' role='presentation'>
<li class="mega-menu-column mega-menu-columns-12-of-12" style="--columns:12; --span:12" id="mega-menu-5203-0-0">
		<ul class="mega-sub-menu">
<li class="mega-menu-item mega-menu-item-type-widget widget_custom_html mega-menu-item-custom_html-28" id="mega-menu-item-custom_html-28"><div class="textwidget custom-html-widget"><span class="dropdown-header" style="padding-bottom:20px;">
	Why Citrine?
</span></div></li>		</ul>
</li>	</ul>
</li><li class="mega-menu-row" id="mega-menu-5203-1">
	<ul class="mega-sub-menu" style='--columns:12' role='presentation'>
<li class="mega-menu-column mega-menu-columns-3-of-12" style="--columns:12; --span:3" id="mega-menu-5203-1-0">
		<ul class="mega-sub-menu">
<li class="mega-menu-item mega-menu-item-type-widget widget_custom_html mega-menu-item-custom_html-23" id="mega-menu-item-custom_html-23"><div class="textwidget custom-html-widget"><span class="dropdown-orange-header"><a href="/why-citrine/">We’ll help you achieve your goals</a></span>
<a href="/why-citrine/"><div class="why-citrine-blurbs">
	<p>Find your next great product</p>
	<p>Be more responsive to your customers</p>
	<p>Speed up the development cycle</p>
	<p>Adapt to changing regulations</p>
	</div></a>
<a href="/why-citrine/" class="left-link-small">Learn more</a></div></li>		</ul>
</li><li class="mega-menu-column mega-menu-columns-3-of-12" style="--columns:12; --span:3" id="mega-menu-5203-1-1">
		<ul class="mega-sub-menu">
<li class="mega-menu-item mega-menu-item-type-widget widget_custom_html mega-menu-item-custom_html-25" id="mega-menu-item-custom_html-25"><div class="textwidget custom-html-widget"><span class="dropdown-orange-header"><a href="/why-citrine/#priorities">We share your priorities</a></span>
<a href="/why-citrine/#priorities"><div class="why-citrine-blurbs">
	<p>Visualize the tradeoffs</p>
	<p>Rank your options to make better research choices</p>
	<p>Identify which new ingredients will yield the best results</p>
	<p>Use machine learning tools built for chemistry</p>
	</div></a>
<a href="/why-citrine/#priorities" class="left-link-small">Learn more</a></div></li>		</ul>
</li><li class="mega-menu-column mega-menu-columns-3-of-12" style="--columns:12; --span:3" id="mega-menu-5203-1-2">
		<ul class="mega-sub-menu">
<li class="mega-menu-item mega-menu-item-type-widget widget_custom_html mega-menu-item-custom_html-24" id="mega-menu-item-custom_html-24"><div class="textwidget custom-html-widget"><span class="dropdown-orange-header"><a href="/why-citrine/#technology">Our technology is different</a></span>
<a href="/why-citrine/#technology"><div class="why-citrine-blurbs"><p>Committed to security</p>
	<p>Support built around your needs</p>
	<p>Investing in research</p>
	<p>Here today, here tomorrow</p>
	</div></a>
<a href="/why-citrine/#technology" class="left-link-small">Learn more</a></div></li>		</ul>
</li><li class="mega-menu-column mega-menu-columns-3-of-12" style="--columns:12; --span:3" id="mega-menu-5203-1-3">
		<ul class="mega-sub-menu">
<li class="mega-menu-item mega-menu-item-type-widget widget_custom_html mega-menu-item-custom_html-26" id="mega-menu-item-custom_html-26"><div class="textwidget custom-html-widget"><span class="dropdown-orange-header"><a href="/who-we-help/#Industries">We know your industry</a></span>
<a href="/who-we-help/#Industries"><div class="why-citrine-blurbs"><p>Batteries</p>
	<p>Ceramics &amp; Glass</p>
	<p>Metals &amp; Alloys</p>
	<p>Specialty Chemicals</p>
	</div></a>
<a href="/who-we-help/#Industries" class="left-link-small">Learn more</a></div></li>		</ul>
</li>	</ul>
</li></ul>
</li><li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-has-children mega-menu-megamenu mega-menu-grid mega-align-bottom-left mega-menu-item-5204" id="mega-menu-item-5204"><a class="mega-menu-link" href="/resources/" aria-expanded="false" aria-controls="mega-sub-menu-5204">Resources<span class="mega-indicator" aria-hidden="true"></span></a>
<ul class="mega-sub-menu" role='presentation' id='mega-sub-menu-5204'>
<li class="mega-menu-row" id="mega-menu-5204-0">
	<ul class="mega-sub-menu" style='--columns:12' role='presentation'>
<li class="mega-menu-column mega-menu-columns-12-of-12" style="--columns:12; --span:12" id="mega-menu-5204-0-0">
		<ul class="mega-sub-menu">
<li class="mega-menu-item mega-menu-item-type-widget widget_custom_html mega-menu-item-custom_html-29" id="mega-menu-item-custom_html-29"><div class="textwidget custom-html-widget"><span class="dropdown-header">
	Resources
</span></div></li>		</ul>
</li>	</ul>
</li><li class="mega-menu-row" id="mega-menu-5204-1">
	<ul class="mega-sub-menu" style='--columns:12' role='presentation'>
<li class="mega-menu-column mega-menu-columns-2-of-12" style="--columns:12; --span:2" id="mega-menu-5204-1-0">
		<ul class="mega-sub-menu">
<li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-5658" id="mega-menu-item-5658"><a class="mega-menu-link" href="/resources/case-studies/">Case Studies</a></li><li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-has-children mega-disable-link mega-menu-item-6759" id="mega-menu-item-6759"><a class="mega-menu-link" tabindex="0">Industries<span class="mega-indicator" aria-hidden="true"></span></a>
			<ul class="mega-sub-menu" id='mega-sub-menu-6759'>
<li class="mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-menu-item-6761" id="mega-menu-item-6761"><a class="mega-menu-link" href="https://citrine.io/resources/resources-for-coatings-adhesives-and-sealants-companies/">Coatings, Adhesives & Sealants</a></li><li class="mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-menu-item-6760" id="mega-menu-item-6760"><a class="mega-menu-link" href="https://citrine.io/resources/resources-for-specialty-chemicals-and-polymers-companies/">Specialty Chemicals & Polymers</a></li><li class="mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-menu-item-6762" id="mega-menu-item-6762"><a class="mega-menu-link" href="https://citrine.io/resources/industry-resources-consumer-packaged-goods/">Consumer Packaged Goods</a></li>			</ul>
</li>		</ul>
</li><li class="mega-menu-column mega-menu-columns-2-of-12" style="--columns:12; --span:2" id="mega-menu-5204-1-1">
		<ul class="mega-sub-menu">
<li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-has-children mega-menu-item-5669" id="mega-menu-item-5669"><a class="mega-menu-link" href="/resources/white-papers/">White Papers<span class="mega-indicator" aria-hidden="true"></span></a>
			<ul class="mega-sub-menu" id='mega-sub-menu-5669'>
<li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-5670" id="mega-menu-item-5670"><a class="mega-menu-link" href="/resources/white-papers/#ai-business-strategy">AI & Business Strategy</a></li><li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-5671" id="mega-menu-item-5671"><a class="mega-menu-link" href="/resources/white-papers/#ai-different-industries">AI & Industries</a></li><li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-5672" id="mega-menu-item-5672"><a class="mega-menu-link" href="/resources/white-papers/#concepts">Concepts</a></li><li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-5673" id="mega-menu-item-5673"><a class="mega-menu-link" href="/resources/white-papers/#data-management">Data Management</a></li><li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-6653" id="mega-menu-item-6653"><a class="mega-menu-link" href="/resources/white-papers/#security">Security</a></li>			</ul>
</li>		</ul>
</li><li class="mega-menu-column mega-menu-columns-2-of-12" style="--columns:12; --span:2" id="mega-menu-5204-1-2">
		<ul class="mega-sub-menu">
<li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-has-children mega-menu-item-5682" id="mega-menu-item-5682"><a class="mega-menu-link" href="/resources/blog/">Citrine's Blog<span class="mega-indicator" aria-hidden="true"></span></a>
			<ul class="mega-sub-menu" id='mega-sub-menu-5682'>
<li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-6165" id="mega-menu-item-6165"><a class="mega-menu-link" href="/category/blog/demystification/">Demystification</a></li><li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-6166" id="mega-menu-item-6166"><a class="mega-menu-link" href="/category/blog/what-weve-learned/">What we've learned</a></li><li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-6167" id="mega-menu-item-6167"><a class="mega-menu-link" href="/category/blog/external-research/">External Research</a></li><li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-6168" id="mega-menu-item-6168"><a class="mega-menu-link" href="/category/blog/life-at-citrine/">Life at Citrine</a></li><li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-6169" id="mega-menu-item-6169"><a class="mega-menu-link" href="/category/blog/notes-on-successful-projects/">Notes on Successful Projects</a></li><li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-6170" id="mega-menu-item-6170"><a class="mega-menu-link" href="/category/blog/business-updates-blog/">Business Updates</a></li>			</ul>
</li>		</ul>
</li><li class="mega-menu-column mega-menu-columns-2-of-12" style="--columns:12; --span:2" id="mega-menu-5204-1-3">
		<ul class="mega-sub-menu">
<li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-has-children mega-menu-item-5674" id="mega-menu-item-5674"><a class="mega-menu-link" href="/resources/webinars/">Events & Webinars<span class="mega-indicator" aria-hidden="true"></span></a>
			<ul class="mega-sub-menu" id='mega-sub-menu-5674'>
<li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-5675" id="mega-menu-item-5675"><a class="mega-menu-link" href="/resources/webinars/#upcoming">Upcoming Webinars</a></li><li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-5676" id="mega-menu-item-5676"><a class="mega-menu-link" href="/resources/webinars/#past">Past Webinars</a></li>			</ul>
</li>		</ul>
</li><li class="mega-menu-column mega-menu-columns-2-of-12" style="--columns:12; --span:2" id="mega-menu-5204-1-4">
		<ul class="mega-sub-menu">
<li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-has-children mega-menu-item-5664" id="mega-menu-item-5664"><a class="mega-menu-link" href="/resources/research/">Research<span class="mega-indicator" aria-hidden="true"></span></a>
			<ul class="mega-sub-menu" id='mega-sub-menu-5664'>
<li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-5665" id="mega-menu-item-5665"><a class="mega-menu-link" href="/resources/research/#external-research">External Research</a></li><li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-5666" id="mega-menu-item-5666"><a class="mega-menu-link" href="/resources/research/patents/">Patents</a></li><li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-5667" id="mega-menu-item-5667"><a class="mega-menu-link" href="/category/papers-by-citrine/">Papers by us</a></li><li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-5668" id="mega-menu-item-5668"><a class="mega-menu-link" href="/category/papers-mentioning-citrine/">Papers citing us</a></li><li class="mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-menu-item-6418" id="mega-menu-item-6418"><a class="mega-menu-link" href="https://citrine.io/resources/newsletters/">Newsletters</a></li>			</ul>
</li>		</ul>
</li><li class="mega-menu-column mega-menu-columns-2-of-12" style="--columns:12; --span:2" id="mega-menu-5204-1-5">
		<ul class="mega-sub-menu">
<li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-5681" id="mega-menu-item-5681"><a class="mega-menu-link" href="/resources/research/education-and-training/">Education & Training</a></li><li class="mega-menu-item mega-menu-item-type-widget widget_custom_html mega-menu-item-custom_html-27" id="mega-menu-item-custom_html-27"><div class="textwidget custom-html-widget"><div style="background: linear-gradient(0deg, rgba(255,255,255,1) 0%, rgba(245,245,245,1) 100%); padding:20px 25px;margin-top:10px;">
	<span style="font-weight:500; font-size:18px;">Introduction to</span><br/>
<span style="font-weight:500; font-size:22px; line-height:22px;">Materials Informatics</span><br/>
<a href="/resources/introduction-to-materials-informatics/" class="left-link-small">Find out more</a>
	<a href="/resources/introduction-to-materials-informatics/"><img src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20160%2096'%3E%3C/svg%3E" width="160" height="96" class="mega-menu-image" alt="materials images" data-lazy-src="https:/&#047;&#x63;&#x69;t&#114;&#x69;&#x6e;e&#046;&#x69;&#x6f;/&#119;&#x70;&#x2d;c&#111;&#x6e;&#x74;e&#110;&#116;&#x2f;&#x75;p&#108;&#x6f;&#x61;d&#115;&#x2f;&#x32;0&#050;&#x33;&#x2f;1&#049;&#x2f;&#x69;n&#116;&#x72;&#x6f;-&#116;&#111;&#x2d;&#x6d;i&#064;&#x32;&#x78;&#046;&#112;&#x6e;&#x67;" /><noscript><img src="https:/&#47;&#x63;&#x69;t&#114;&#x69;&#x6e;e&#46;&#x69;&#x6f;/&#119;&#x70;&#x2d;c&#111;&#x6e;&#x74;e&#110;&#116;&#x2f;&#x75;p&#108;&#x6f;&#x61;d&#115;&#x2f;&#x32;0&#50;&#x33;&#x2f;1&#49;&#x2f;&#x69;n&#116;&#x72;&#x6f;-&#116;&#111;&#x2d;&#x6d;i&#64;&#x32;&#x78;&#46;&#112;&#x6e;&#x67;" width="160" height="96" class="mega-menu-image" alt="materials images" /></noscript></a>
</div></div></li>		</ul>
</li>	</ul>
</li></ul>
</li><li class="mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-menu-item-has-children mega-menu-megamenu mega-menu-grid mega-align-bottom-left mega-menu-item-5632" id="mega-menu-item-5632"><a class="mega-menu-link" href="https://citrine.io/company/" aria-expanded="false" aria-controls="mega-sub-menu-5632">Company<span class="mega-indicator" aria-hidden="true"></span></a>
<ul class="mega-sub-menu" role='presentation' id='mega-sub-menu-5632'>
<li class="mega-menu-row" id="mega-menu-5632-0">
	<ul class="mega-sub-menu" style='--columns:12' role='presentation'>
<li class="mega-menu-column mega-menu-columns-12-of-12" style="--columns:12; --span:12" id="mega-menu-5632-0-0">
		<ul class="mega-sub-menu">
<li class="mega-menu-item mega-menu-item-type-widget widget_custom_html mega-menu-item-custom_html-31" id="mega-menu-item-custom_html-31"><div class="textwidget custom-html-widget"><span class="dropdown-header">
	Company
</span></div></li>		</ul>
</li>	</ul>
</li><li class="mega-menu-row" id="mega-menu-5632-1">
	<ul class="mega-sub-menu" style='--columns:12' role='presentation'>
<li class="mega-menu-column mega-menu-columns-4-of-12" style="--columns:12; --span:4" id="mega-menu-5632-1-0">
		<ul class="mega-sub-menu">
<li class="mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-menu-item-has-children mega-menu-item-6195" id="mega-menu-item-6195"><a class="mega-menu-link" href="https://citrine.io/company/">Who We Are<span class="mega-indicator" aria-hidden="true"></span></a>
			<ul class="mega-sub-menu" id='mega-sub-menu-6195'>
<li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-5693" id="mega-menu-item-5693"><a class="mega-menu-link" href="/company/#about-us">About Us</a></li><li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-5694" id="mega-menu-item-5694"><a class="mega-menu-link" href="/company/#mission">Mission & Values</a></li><li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-5689" id="mega-menu-item-5689"><a class="mega-menu-link" href="/company/#team">Leadership</a></li><li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-5690" id="mega-menu-item-5690"><a class="mega-menu-link" href="/company/#investors">Investors</a></li><li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-5695" id="mega-menu-item-5695"><a class="mega-menu-link" href="/company/#awards">Awards</a></li>			</ul>
</li>		</ul>
</li><li class="mega-menu-column mega-menu-columns-4-of-12" style="--columns:12; --span:4" id="mega-menu-5632-1-1">
		<ul class="mega-sub-menu">
<li class="mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-menu-item-has-children mega-menu-item-5687" id="mega-menu-item-5687"><a class="mega-menu-link" href="https://citrine.io/careers/">Careers<span class="mega-indicator" aria-hidden="true"></span></a>
			<ul class="mega-sub-menu" id='mega-sub-menu-5687'>
<li class="mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-menu-item-6174" id="mega-menu-item-6174"><a class="mega-menu-link" href="https://citrine.io/careers/">Working at Citrine</a></li><li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-5696" id="mega-menu-item-5696"><a class="mega-menu-link" href="/company/#dei">DE&I at Citrine</a></li>			</ul>
</li>		</ul>
</li><li class="mega-menu-column mega-menu-columns-4-of-12" style="--columns:12; --span:4" id="mega-menu-5632-1-2">
		<ul class="mega-sub-menu">
<li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-has-children mega-menu-item-5688" id="mega-menu-item-5688"><a class="mega-menu-link" href="/media-post/">Newsroom<span class="mega-indicator" aria-hidden="true"></span></a>
			<ul class="mega-sub-menu" id='mega-sub-menu-5688'>
<li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-5691" id="mega-menu-item-5691"><a class="mega-menu-link" href="/media-type/news/">Articles</a></li><li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-5692" id="mega-menu-item-5692"><a class="mega-menu-link" href="/media-type/press-releases/">Press Releases</a></li>			</ul>
</li>		</ul>
</li>	</ul>
</li></ul>
</li></ul></div>						</nav><!-- #site-navigation -->

						<div class="header_search">
							<div class="search_icon">
								<i class="fa fa-search" aria-hidden="true"></i>
							</div>
						</div>

					</div>

					<div class="mobile_menu_btn_wrapper">
						<a class="mobile_menu_icon" href="#my-menu"><span></span></a>
					</div>
				</div>

			</div>
		</div>

		<div class="mobile_nav" id="my-menu">
			<ul class="mobile_menu">
				<ul id="primary_menu" class="primary_menu"><li id="menu-item-6025" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-6025"><a href="https://citrine.io/platform/">Platform</a>
<ul class="sub-menu">
	<li id="menu-item-6052" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-6052"><a href="/platform/#products">Products</a>
	<ul class="sub-menu">
		<li id="menu-item-6033" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6033"><a href="https://citrine.io/platform/citrine-datamanager/">Citrine DataManager</a></li>
		<li id="menu-item-6032" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6032"><a href="https://citrine.io/platform/citrine-virtuallab/">Citrine VirtualLab</a></li>
		<li id="menu-item-8039" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-8039"><a href="/platform/citrine-catalyst/">Citrine Catalyst</a></li>
		<li id="menu-item-6031" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6031"><a href="https://citrine.io/platform/citrine-professional-services/">Citrine Professional Services</a></li>
	</ul>
</li>
	<li id="menu-item-6053" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-6053"><a href="/platform/#enterprise-ready">Enterprise-Ready</a>
	<ul class="sub-menu">
		<li id="menu-item-6030" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6030"><a href="https://citrine.io/platform/getting-started/">Getting Started</a></li>
		<li id="menu-item-6029" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6029"><a href="https://citrine.io/platform/security/">Security</a></li>
		<li id="menu-item-6028" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6028"><a href="https://citrine.io/platform/flexibility/">Flexibility</a></li>
		<li id="menu-item-6027" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6027"><a href="https://citrine.io/platform/support/">Support</a></li>
	</ul>
</li>
</ul>
</li>
<li id="menu-item-6055" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-6055"><a href="/who-we-help/">Who We Help</a>
<ul class="sub-menu">
	<li id="menu-item-6056" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6056"><a href="/who-we-help/#BusinessFunctions">Business Functions</a></li>
	<li id="menu-item-6057" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6057"><a href="/who-we-help/#Industries">Industries</a></li>
</ul>
</li>
<li id="menu-item-6024" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-6024"><a href="https://citrine.io/why-citrine/">Why Citrine?</a>
<ul class="sub-menu">
	<li id="menu-item-6058" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6058"><a href="/why-citrine/">We&#8217;ll help you achieve your goals</a></li>
	<li id="menu-item-6060" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6060"><a href="/why-citrine/#priorities">We share your priorities</a></li>
	<li id="menu-item-6059" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6059"><a href="/why-citrine/#technology">Our technology is different</a></li>
	<li id="menu-item-6061" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6061"><a href="/who-we-help/#Industries">We know your industry</a></li>
</ul>
</li>
<li id="menu-item-6034" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-6034"><a href="https://citrine.io/resources/">Resources</a>
<ul class="sub-menu">
	<li id="menu-item-6037" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6037"><a href="https://citrine.io/resources/case-studies/">Case Studies</a></li>
	<li id="menu-item-6777" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-6777"><a href="/who-we-help/#Industries">Industries</a>
	<ul class="sub-menu">
		<li id="menu-item-6778" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6778"><a href="https://citrine.io/resources/resources-for-specialty-chemicals-and-polymers-companies/">Specialty Chemicals &#038; Polymers</a></li>
		<li id="menu-item-6779" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6779"><a href="https://citrine.io/resources/resources-for-coatings-adhesives-and-sealants-companies/">Coatings, Adhesives &#038; Sealants</a></li>
		<li id="menu-item-6780" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6780"><a href="https://citrine.io/resources/industry-resources-consumer-packaged-goods/">Consumer Packaged Goods</a></li>
	</ul>
</li>
	<li id="menu-item-6040" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-6040"><a href="https://citrine.io/resources/white-papers/">White Papers</a>
	<ul class="sub-menu">
		<li id="menu-item-6071" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6071"><a href="/resources/white-papers/#ai-business-strategy">AI &#038; Business Strategy</a></li>
		<li id="menu-item-6072" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6072"><a href="/resources/white-papers/#ai-different-industries">AI &#038; Industries</a></li>
		<li id="menu-item-6073" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6073"><a href="/resources/white-papers/#concepts">Concepts</a></li>
		<li id="menu-item-6074" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6074"><a href="/resources/white-papers/#data-management">Data Management</a></li>
		<li id="menu-item-6654" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6654"><a href="/resources/white-papers/#security">Security</a></li>
	</ul>
</li>
	<li id="menu-item-6036" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-6036"><a href="https://citrine.io/resources/blog/">Blog</a>
	<ul class="sub-menu">
		<li id="menu-item-6180" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6180"><a href="/category/blog/demystification/">Demystification</a></li>
		<li id="menu-item-6181" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6181"><a href="/category/blog/what-weve-learned/">What we&#8217;ve learned</a></li>
		<li id="menu-item-6182" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6182"><a href="/category/blog/External-research/">External Research</a></li>
		<li id="menu-item-6183" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6183"><a href="/category/blog/Life-at-citrine/">Life at Citrine</a></li>
		<li id="menu-item-6184" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6184"><a href="/category/blog/notes-on-successful-projects/">Notes on Successful Projects</a></li>
		<li id="menu-item-6185" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6185"><a href="/category/blog/business-updates-blog/">Business Updates</a></li>
	</ul>
</li>
	<li id="menu-item-6039" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-6039"><a href="https://citrine.io/resources/webinars/">Webinars</a>
	<ul class="sub-menu">
		<li id="menu-item-6075" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6075"><a href="/resources/webinars/#upcoming">Upcoming Webinars</a></li>
		<li id="menu-item-6076" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6076"><a href="/resources/webinars/#past">Past Webinars</a></li>
	</ul>
</li>
	<li id="menu-item-6051" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-6051"><a href="https://citrine.io/resources/research/">Research</a>
	<ul class="sub-menu">
		<li id="menu-item-6067" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6067"><a href="/resources/research/#external-research">External Research</a></li>
		<li id="menu-item-6068" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6068"><a href="/resources/research/patents/">Patents</a></li>
		<li id="menu-item-6069" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6069"><a href="/category/papers-by-citrine/">Papers by us</a></li>
		<li id="menu-item-6070" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6070"><a href="/category/papers-mentioning-citrine/">Papers citing us</a></li>
		<li id="menu-item-6419" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6419"><a href="https://citrine.io/resources/newsletters/">Newsletters</a></li>
	</ul>
</li>
	<li id="menu-item-6043" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6043"><a href="https://citrine.io/resources/research/education-and-training/">Education &#038; Training</a></li>
</ul>
</li>
<li id="menu-item-6046" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-6046"><a href="https://citrine.io/company/">Company</a>
<ul class="sub-menu">
	<li id="menu-item-6081" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6081"><a href="/company/#about-us">About Us</a></li>
	<li id="menu-item-6082" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6082"><a href="/company/#mission">Mission &#038; Values</a></li>
	<li id="menu-item-6083" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6083"><a href="/company/#team">Leadership</a></li>
	<li id="menu-item-6084" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6084"><a href="/company/#investors">Investors</a></li>
	<li id="menu-item-6086" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6086"><a href="/company/#dei">DE&#038;I at Citrine</a></li>
	<li id="menu-item-6047" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6047"><a href="https://citrine.io/careers/">Careers</a></li>
	<li id="menu-item-6085" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6085"><a href="/company/#awards">Awards</a></li>
	<li id="menu-item-6087" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-6087"><a href="/media-post/">Newsroom</a>
	<ul class="sub-menu">
		<li id="menu-item-6088" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6088"><a href="/media-type/news/">Articles</a></li>
		<li id="menu-item-6089" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6089"><a href="/media-type/press-releases/">Press Releases</a></li>
	</ul>
</li>
</ul>
</li>
<li id="menu-item-6050" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6050"><a href="https://citrine.io/request-a-demo/">Request a Demo</a></li>
<li id="menu-item-6143" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6143"><a href="https://citrine.io/contact/">Contact</a></li>
</ul>				<div class="m_search_section show_search_box search_section">
						<form role="search" method="get" class="search-form" action="https://citrine.io/">
				<label>
					<span class="screen-reader-text">Search for:</span>
					<input type="search" class="search-field" placeholder="Search &hellip;" value="" name="s" />
				</label>
				<input type="submit" class="search-submit" value="Search" />
			</form>						<i class="fa fa-search header_search_btn" aria-hidden="true"></i>
				</div>
			</ul>
		</div>
	</header><!-- #masthead -->

	</div>

	<div  id="content" class="site-content">

	<div  id="primary" class="content-area">
		<main id="main" class="site-main" role="main">

			
				<div class="r8_hero has-hero-content">
    
    
                 <style media="screen" type="text/css">
         .r8_image_bg_hero  {
             background-image: var(--wpr-bg-577cca7a-d49c-472f-acb1-ee3f436dea90);
         }
              </style>
    <div class="r8_image_bg_hero r8_hero_container hero_content_dep_height" >

        
        
            <div class="r8_hero_content">

                            <div class="fixed-header-spacer no-hero"></div>
            
            <div class="container  two_columns_content r8_half_and_half">

                <div class="hc1_section hc_section" style = "">
                                            <div class="r8_hero_copy">
                            
                                                            <div class="r8_wysiwig_content r8_dark_gray_font_color"><div class="home-leftdiv">
<h1 class="homeh1 ai-optimize-8">TOMORROW REALIZED</h1>
<h2 class="homeh1 ai-optimize-8"><span style="color: #404040;">Applying best-in-class AI to accelerate innovation in materials and chemistry</span></h2>
</div>
</div>
                            
                                                    </div><!-- .r8_hero_copy -->
                                    </div>

                                    <div class="hc2_section hc_section" style = "">

                        
                            <div class="r8_hero_copy">
                                
                                                                    <div class="r8_wysiwig_content r8_white_font_color"><div class="home-rightdiv"><a class="fancybox-vimeo" href="https://vimeo.com/1083794068/3ce7f434be"><img fetchpriority="high" decoding="async" class="aligncenter size-full wp-image-7051 home-video" src="https://citrine.io/wp-content/uploads/2025/05/videov2.gif" alt="feature video" width="1280" height="720" /></a></div>
</div>
                                
                                                            </div><!-- .r8_hero_copy -->

                        
                    </div>
                                </div><!-- .container -->
            </div><!-- .r8_hero_content -->
            </div>

    
    </div>


				
									

<div class = "r8_flexible_content_section r8_carousel_section r8_carousel_section_0  " style=" background-color: #fafafa; padding-top: 10px; padding-bottom: 40px;" >
    <div class="r8_container container" style="max-width: 1280px">
        
                    <div class = "r8_carousel  r8_carousel_long text_over_image" style="max-width: 1280px" data-slick='{"slidesToShow": 5, "slidesToScroll": 5, "autoplay": true, "speed": 1200, "arrows": true, "dots" : true  }'>
                
                    
                    <div class = "r8_carousel_item" style ="text-align: center; ">
                        
                            <div class="r8_carousel_content">
                                
                                
<!-- display image if present -->
    <div class = "r8_carousel_item_image">
    	<picture>
<source type="image/webp" srcset="https://citrine.io/wp-content/uploads/2026/06/logo-gm-lyondell-grace.png.webp"/>
<img src="https://citrine.io/wp-content/uploads/2026/06/logo-gm-lyondell-grace.png" alt="GM | LyondellBasell | GRACE"/>
</picture>

    </div>
                                                            </div>

                                            </div>

                
                    
                    <div class = "r8_carousel_item" style ="text-align: center; ">
                        
                            <div class="r8_carousel_content">
                                
                                
<!-- display image if present -->
    <div class = "r8_carousel_item_image">
    	<picture>
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2025/12/logo3-03.png.webp"/>
<img src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E" alt="Collano | Evonik | Rolls Royce" data-lazy-src="https://citrine.io/wp-content/uploads/2025/12/logo3-03.png"/><noscript><img src="https://citrine.io/wp-content/uploads/2025/12/logo3-03.png" alt="Collano | Evonik | Rolls Royce"/></noscript>
</picture>

    </div>
                                                            </div>

                                            </div>

                
                    
                    <div class = "r8_carousel_item" style ="text-align: center; ">
                        
                            <div class="r8_carousel_content">
                                
                                
<!-- display image if present -->
    <div class = "r8_carousel_item_image">
    	<picture>
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2026/05/logos-lanx-dorf-te.png.webp"/>
<img src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E" alt="Lanxess | Dorfner | Total Energies" data-lazy-src="https://citrine.io/wp-content/uploads/2026/05/logos-lanx-dorf-te.png"/><noscript><img src="https://citrine.io/wp-content/uploads/2026/05/logos-lanx-dorf-te.png" alt="Lanxess | Dorfner | Total Energies"/></noscript>
</picture>

    </div>
                                                            </div>

                                            </div>

                
                    
                    <div class = "r8_carousel_item" style ="text-align: center; ">
                        
                            <div class="r8_carousel_content">
                                
                                
<!-- display image if present -->
    <div class = "r8_carousel_item_image">
    	<picture>
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2025/12/logo3-05.png.webp"/>
<img src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E" alt="Showa Denko | AGC | Brewer Science" data-lazy-src="https://citrine.io/wp-content/uploads/2025/12/logo3-05.png"/><noscript><img src="https://citrine.io/wp-content/uploads/2025/12/logo3-05.png" alt="Showa Denko | AGC | Brewer Science"/></noscript>
</picture>

    </div>
                                                            </div>

                                            </div>

                
                    
                    <div class = "r8_carousel_item" style ="text-align: center; ">
                        
                            <div class="r8_carousel_content">
                                
                                
<!-- display image if present -->
    <div class = "r8_carousel_item_image">
    	<img width="331" height="268" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20331%20268'%3E%3C/svg%3E" alt = "CoorsTek | Avery Dennison | Syensqo" data-lazy-src="https://citrine.io/wp-content/uploads/2026/05/logos-coorstek-avery-syensqo.png" /><noscript><img width="331" height="268" src = "https://citrine.io/wp-content/uploads/2026/05/logos-coorstek-avery-syensqo.png" alt = "CoorsTek | Avery Dennison | Syensqo" /></noscript>
    </div>
                                                            </div>

                                            </div>

                
                    
                    <div class = "r8_carousel_item" style ="text-align: center; ">
                        
                            <div class="r8_carousel_content">
                                
                                
<!-- display image if present -->
    <div class = "r8_carousel_item_image">
    	<img width="331" height="268" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20331%20268'%3E%3C/svg%3E" alt = "HRL Laboratories | EMD Electronics | Vita" data-lazy-src="https://citrine.io/wp-content/uploads/2025/12/logo3-07.png" /><noscript><img width="331" height="268" src = "https://citrine.io/wp-content/uploads/2025/12/logo3-07.png" alt = "HRL Laboratories | EMD Electronics | Vita" /></noscript>
    </div>
                                                            </div>

                                            </div>

                
                    
                    <div class = "r8_carousel_item" style ="text-align: center; ">
                        
                            <div class="r8_carousel_content">
                                
                                
<!-- display image if present -->
    <div class = "r8_carousel_item_image">
    	<img width="331" height="268" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20331%20268'%3E%3C/svg%3E" alt = "Stepan | Arkema | Saint-Gobain" data-lazy-src="https://citrine.io/wp-content/uploads/2025/12/logo3-08.png" /><noscript><img width="331" height="268" src = "https://citrine.io/wp-content/uploads/2025/12/logo3-08.png" alt = "Stepan | Arkema | Saint-Gobain" /></noscript>
    </div>
                                                            </div>

                                            </div>

                
                    
                    <div class = "r8_carousel_item" style ="text-align: center; ">
                        
                            <div class="r8_carousel_content">
                                
                                
<!-- display image if present -->
    <div class = "r8_carousel_item_image">
    	<img width="331" height="268" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20331%20268'%3E%3C/svg%3E" alt = "Bergolin | Altana | Andromaco" data-lazy-src="https://citrine.io/wp-content/uploads/2026/05/logos-bergolin-altana-andromaco.png" /><noscript><img width="331" height="268" src = "https://citrine.io/wp-content/uploads/2026/05/logos-bergolin-altana-andromaco.png" alt = "Bergolin | Altana | Andromaco" /></noscript>
    </div>
                                                            </div>

                                            </div>

                
                    
                    <div class = "r8_carousel_item" style ="text-align: center; ">
                        
                            <div class="r8_carousel_content">
                                
                                
<!-- display image if present -->
    <div class = "r8_carousel_item_image">
    	<img width="331" height="268" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20331%20268'%3E%3C/svg%3E" alt = "Synthomer | Aurora Material Solutions | Huntsman Building Solutions" data-lazy-src="https://citrine.io/wp-content/uploads/2025/12/logo3-10.png" /><noscript><img width="331" height="268" src = "https://citrine.io/wp-content/uploads/2025/12/logo3-10.png" alt = "Synthomer | Aurora Material Solutions | Huntsman Building Solutions" /></noscript>
    </div>
                                                            </div>

                                            </div>

                
                    
                    <div class = "r8_carousel_item" style ="text-align: center; ">
                        
                            <div class="r8_carousel_content">
                                
                                
<!-- display image if present -->
    <div class = "r8_carousel_item_image">
    	<img width="331" height="268" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20331%20268'%3E%3C/svg%3E" alt = "AnzaPlan | Perstorp | Adapt" data-lazy-src="https://citrine.io/wp-content/uploads/2025/12/logo3-11.png" /><noscript><img width="331" height="268" src = "https://citrine.io/wp-content/uploads/2025/12/logo3-11.png" alt = "AnzaPlan | Perstorp | Adapt" /></noscript>
    </div>
                                                            </div>

                                            </div>

                
                    
                    <div class = "r8_carousel_item" style ="text-align: center; ">
                        
                            <div class="r8_carousel_content">
                                
                                
<!-- display image if present -->
    <div class = "r8_carousel_item_image">
    	<picture>
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2025/12/logo3-12.png.webp"/>
<img src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E" alt="kcarbon | econic | OUCC" data-lazy-src="https://citrine.io/wp-content/uploads/2025/12/logo3-12.png"/><noscript><img src="https://citrine.io/wp-content/uploads/2025/12/logo3-12.png" alt="kcarbon | econic | OUCC"/></noscript>
</picture>

    </div>
                                                            </div>

                                            </div>

                
                    
                    <div class = "r8_carousel_item" style ="text-align: center; ">
                        
                            <div class="r8_carousel_content">
                                
                                
<!-- display image if present -->
    <div class = "r8_carousel_item_image">
    	<picture>
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2026/06/logos-chesco-chicago-nist.png.webp"/>
<img src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E" alt="Chesco | University of Chicago | NIST" data-lazy-src="https://citrine.io/wp-content/uploads/2026/06/logos-chesco-chicago-nist.png"/><noscript><img src="https://citrine.io/wp-content/uploads/2026/06/logos-chesco-chicago-nist.png" alt="Chesco | University of Chicago | NIST"/></noscript>
</picture>

    </div>
                                                            </div>

                                            </div>

                
                    
                    <div class = "r8_carousel_item" style ="text-align: center; ">
                        
                            <div class="r8_carousel_content">
                                
                                
<!-- display image if present -->
    <div class = "r8_carousel_item_image">
    	<picture>
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2025/12/logo3-14.png.webp"/>
<img src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E" alt="SLAC | Technische Universitat Dresden | Electroninks" data-lazy-src="https://citrine.io/wp-content/uploads/2025/12/logo3-14.png"/><noscript><img src="https://citrine.io/wp-content/uploads/2025/12/logo3-14.png" alt="SLAC | Technische Universitat Dresden | Electroninks"/></noscript>
</picture>

    </div>
                                                            </div>

                                            </div>

                
                    
                    <div class = "r8_carousel_item" style ="text-align: center; ">
                        
                            <div class="r8_carousel_content">
                                
                                
<!-- display image if present -->
    <div class = "r8_carousel_item_image">
    	<img width="331" height="268" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20331%20268'%3E%3C/svg%3E" alt = "SCSK | University of California, Berkeley | PurposeBuilt Brands" data-lazy-src="https://citrine.io/wp-content/uploads/2026/04/logos-purpose.png" /><noscript><img width="331" height="268" src = "https://citrine.io/wp-content/uploads/2026/04/logos-purpose.png" alt = "SCSK | University of California, Berkeley | PurposeBuilt Brands" /></noscript>
    </div>
                                                            </div>

                                            </div>

                
                    
                    <div class = "r8_carousel_item" style ="text-align: center; ">
                        
                            <div class="r8_carousel_content">
                                
                                
<!-- display image if present -->
    <div class = "r8_carousel_item_image">
    	<picture>
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2026/05/logos-trion-penn-inter.png.webp"/>
<img src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E" alt="Trion | PennState | Interplastic" data-lazy-src="https://citrine.io/wp-content/uploads/2026/05/logos-trion-penn-inter.png"/><noscript><img src="https://citrine.io/wp-content/uploads/2026/05/logos-trion-penn-inter.png" alt="Trion | PennState | Interplastic"/></noscript>
</picture>

    </div>
                                                            </div>

                                            </div>

                            </div>
        
    </div>
</div>

<div class="r8_flexible_content_section r8_columns_section-two_column r8_columns_section r8_columns_section_1  " style=" background-color: #fafafa; padding-top: 0px; padding-bottom: 0px;" >
    <div class="r8_container container" style="">
        
        
                    <div class="r8_columns two_column r8_two_third column_content_middle" style="">

                                                                            <div class="r8_column " style=" background-color: ;" >
                        
                                                                                                <div class="column_wysiwig r8_wysiwig_content">
                                                                                    <h3 class="ttnone"><span class="horange">Unlocking knowledge.</span> It&#8217;s our secret formula.</h3>
<p>We use artificial intelligence to help you <strong class="teal">get more value</strong> out of what you already know, finding <strong class="teal">better solutions</strong> to your customers’ toughest problems in <strong class="teal">less time</strong>.</p>
                                                                                                                                                                                                                    </div>
                                                                                                        </div>
                                                                            <div class="r8_column " style=" background-color: ;" >
                        
                                                                                                <div class="column_wysiwig r8_wysiwig_content">
                                                                                    <p><picture decoding="async" class="aligncenter size-full wp-image-5253">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/refresh-home-s1@2x.png.webp 2048w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-s1@2x-300x160.png.webp 300w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-s1@2x-1024x545.png.webp 1024w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-s1@2x-768x409.png.webp 768w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-s1@2x-1536x818.png.webp 1536w" sizes="(max-width: 2048px) 100vw, 2048px"/>
<img decoding="async" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202048%201090'%3E%3C/svg%3E" alt="various materials images" width="2048" height="1090" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/refresh-home-s1@2x.png 2048w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-s1@2x-300x160.png 300w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-s1@2x-1024x545.png 1024w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-s1@2x-768x409.png 768w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-s1@2x-1536x818.png 1536w" data-lazy-sizes="(max-width: 2048px) 100vw, 2048px" data-lazy-src="https://citrine.io/wp-content/uploads/2023/11/refresh-home-s1@2x.png"/><noscript><img decoding="async" src="https://citrine.io/wp-content/uploads/2023/11/refresh-home-s1@2x.png" alt="various materials images" width="2048" height="1090" srcset="https://citrine.io/wp-content/uploads/2023/11/refresh-home-s1@2x.png 2048w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-s1@2x-300x160.png 300w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-s1@2x-1024x545.png 1024w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-s1@2x-768x409.png 768w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-s1@2x-1536x818.png 1536w" sizes="(max-width: 2048px) 100vw, 2048px"/></noscript>
</picture>
</p>
                                                                                                                                                                                                                    </div>
                                                                                                        </div>
                
            </div>
        
            </div> <!--end of container -->
</div>

<div class="r8_flexible_content_section r8_columns_section-four_column r8_columns_section r8_columns_section_2  " style=" background-color: #fafafa; padding-top: 40px; padding-bottom: 40px;" id='home-why'>
    <div class="r8_container container" style="">
        <h3 class="r8_section_title" style="text-align: center">Industry Leaders have deployed Citrine AI at scale. Here's why:</h3>
        
                    <div class="r8_columns four_column column_content_bottom" style="">

                                                                            <div class="r8_column " style=" background-color: ;" >
                        
                                                                                                <div class="column_wysiwig r8_wysiwig_content">
                                                                                    <p><picture decoding="async" class="aligncenter size-full wp-image-5709" style="padding: 0px 15px;">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/home-leader-01@2x.png.webp 914w, https://citrine.io/wp-content/uploads/2023/11/home-leader-01@2x-300x167.png.webp 300w, https://citrine.io/wp-content/uploads/2023/11/home-leader-01@2x-768x427.png.webp 768w" sizes="(max-width: 914px) 100vw, 914px"/>
<img decoding="async" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20914%20508'%3E%3C/svg%3E" alt="" width="914" height="508" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/home-leader-01@2x.png 914w, https://citrine.io/wp-content/uploads/2023/11/home-leader-01@2x-300x167.png 300w, https://citrine.io/wp-content/uploads/2023/11/home-leader-01@2x-768x427.png 768w" data-lazy-sizes="(max-width: 914px) 100vw, 914px" data-lazy-src="https://citrine.io/wp-content/uploads/2023/11/home-leader-01@2x.png"/><noscript><img decoding="async" src="https://citrine.io/wp-content/uploads/2023/11/home-leader-01@2x.png" alt="" width="914" height="508" srcset="https://citrine.io/wp-content/uploads/2023/11/home-leader-01@2x.png 914w, https://citrine.io/wp-content/uploads/2023/11/home-leader-01@2x-300x167.png 300w, https://citrine.io/wp-content/uploads/2023/11/home-leader-01@2x-768x427.png 768w" sizes="(max-width: 914px) 100vw, 914px"/></noscript>
</picture>
</p>
<h4 class="ttnone" style="text-align: center;">Develop products faster</h4>
<p class="no-margin" style="text-align: center;">Speed up your success</p>
                                                                                                                                                                                                                    </div>
                                                                                                        </div>
                                                                            <div class="r8_column " style=" background-color: ;" >
                        
                                                                                                <div class="column_wysiwig r8_wysiwig_content">
                                                                                    <p><picture decoding="async" class="aligncenter size-full wp-image-5710" style="padding: 0px 35px;">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/home-leader-02@2x.png.webp 614w, https://citrine.io/wp-content/uploads/2023/11/home-leader-02@2x-300x164.png.webp 300w" sizes="(max-width: 614px) 100vw, 614px"/>
<img decoding="async" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20614%20336'%3E%3C/svg%3E" alt="" width="614" height="336" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/home-leader-02@2x.png 614w, https://citrine.io/wp-content/uploads/2023/11/home-leader-02@2x-300x164.png 300w" data-lazy-sizes="(max-width: 614px) 100vw, 614px" data-lazy-src="https://citrine.io/wp-content/uploads/2023/11/home-leader-02@2x.png"/><noscript><img decoding="async" src="https://citrine.io/wp-content/uploads/2023/11/home-leader-02@2x.png" alt="" width="614" height="336" srcset="https://citrine.io/wp-content/uploads/2023/11/home-leader-02@2x.png 614w, https://citrine.io/wp-content/uploads/2023/11/home-leader-02@2x-300x164.png 300w" sizes="(max-width: 614px) 100vw, 614px"/></noscript>
</picture>
</p>
<h4 class="ttnone" style="text-align: center;">Get more out of R&amp;D investments</h4>
<p class="no-margin" style="text-align: center;">Work smarter</p>
                                                                                                                                                                                                                    </div>
                                                                                                        </div>
                                                                            <div class="r8_column " style=" background-color: ;" >
                        
                                                                                                <div class="column_wysiwig r8_wysiwig_content">
                                                                                    <p><img decoding="async" class="aligncenter size-full wp-image-5257" style="padding: 0px 45px;" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20662%20456'%3E%3C/svg%3E" alt="" width="662" height="456" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/refresh-home-why3@2x.png 662w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-why3@2x-300x207.png 300w" data-lazy-sizes="(max-width: 662px) 100vw, 662px" data-lazy-src="https://citrine.io/wp-content/uploads/2023/11/refresh-home-why3@2x.png" /><noscript><img decoding="async" class="aligncenter size-full wp-image-5257" style="padding: 0px 45px;" src="https://citrine.io/wp-content/uploads/2023/11/refresh-home-why3@2x.png" alt="" width="662" height="456" srcset="https://citrine.io/wp-content/uploads/2023/11/refresh-home-why3@2x.png 662w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-why3@2x-300x207.png 300w" sizes="(max-width: 662px) 100vw, 662px" /></noscript></p>
<h4 class="ttnone" style="text-align: center;">Share knowledge when it counts</h4>
<p class="no-margin" style="text-align: center;">Make the right connections</p>
                                                                                                                                                                                                                    </div>
                                                                                                        </div>
                                                                            <div class="r8_column " style=" background-color: ;" >
                        
                                                                                                <div class="column_wysiwig r8_wysiwig_content">
                                                                                    <p><picture decoding="async" class="aligncenter size-full wp-image-5711" style="padding: 0px 30px;">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/home-leader-04@2x.png.webp 768w, https://citrine.io/wp-content/uploads/2023/11/home-leader-04@2x-300x134.png.webp 300w" sizes="(max-width: 768px) 100vw, 768px"/>
<img decoding="async" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20768%20344'%3E%3C/svg%3E" alt="" width="768" height="344" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/home-leader-04@2x.png 768w, https://citrine.io/wp-content/uploads/2023/11/home-leader-04@2x-300x134.png 300w" data-lazy-sizes="(max-width: 768px) 100vw, 768px" data-lazy-src="https://citrine.io/wp-content/uploads/2023/11/home-leader-04@2x.png"/><noscript><img decoding="async" src="https://citrine.io/wp-content/uploads/2023/11/home-leader-04@2x.png" alt="" width="768" height="344" srcset="https://citrine.io/wp-content/uploads/2023/11/home-leader-04@2x.png 768w, https://citrine.io/wp-content/uploads/2023/11/home-leader-04@2x-300x134.png 300w" sizes="(max-width: 768px) 100vw, 768px"/></noscript>
</picture>
</p>
<h4 class="ttnone" style="text-align: center;">See benefits across the enterprise</h4>
<p class="no-margin" style="text-align: center;">Go beyond product development</p>
                                                                                                                                                                                                                    </div>
                                                                                                        </div>
                
            </div>
        
            </div> <!--end of container -->
</div>

<div class="r8_flexible_content_section r8_columns_section-one_column r8_columns_section r8_columns_section_3  " style=" padding-top: 40px; padding-bottom: 10px;" >
    <div class="r8_container container" style="max-width: 1000px">
        
        
                    <div class="r8_columns one_column column_content_top" style="max-width: 1000px">

                                                                            <div class="r8_column " style=" background-color: ;" >
                        
                                                                                                <div class="column_wysiwig r8_wysiwig_content">
                                                                                    <p style="text-align: left;"><picture decoding="async" class="alignleft wp-image-5268" style="padding-bottom: 10px;">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/refresh-home-how-logo@2x.png.webp 707w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-how-logo@2x-300x82.png.webp 300w" sizes="(max-width: 150px) 100vw, 150px"/>
<img decoding="async" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20150%2041'%3E%3C/svg%3E" alt="The Citrine Platform" width="150" height="41" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/refresh-home-how-logo@2x.png 707w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-how-logo@2x-300x82.png 300w" data-lazy-sizes="(max-width: 150px) 100vw, 150px" data-lazy-src="https://citrine.io/wp-content/uploads/2023/11/refresh-home-how-logo@2x.png"/><noscript><img decoding="async" src="https://citrine.io/wp-content/uploads/2023/11/refresh-home-how-logo@2x.png" alt="The Citrine Platform" width="150" height="41" srcset="https://citrine.io/wp-content/uploads/2023/11/refresh-home-how-logo@2x.png 707w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-how-logo@2x-300x82.png 300w" sizes="(max-width: 150px) 100vw, 150px"/></noscript>
</picture>
</p>
<h3 class="ttnone" style="text-align: left;">How the Citrine Platform works</h3>
                                                                                                                                                                                                                    </div>
                                                                                                        </div>
                
            </div>
        
            </div> <!--end of container -->
</div>

<div class="r8_flexible_content_section r8_columns_section-one_column r8_columns_section r8_columns_section_4  " style=" padding-top: 0px; padding-bottom: 70px;" id='home-table'>
    <div class="r8_container container" style="max-width: 1000px">
        
        
                    <div class="r8_columns one_column column_content_top" style="max-width: 1000px">

                                                                            <div class="r8_column " style=" background-color: ;" >
                        
                                                                                                <div class="column_wysiwig r8_wysiwig_content">
                                                                                    <table id="home-how" cellspacing="0" cellpadding="0">
<tbody>
<tr style="color: #fff; font-weight: 600; text-align: center; line-height: 22px;">
<td style="background-color: #1d9add; padding: 8px 0px;">Citrine<br />
DataManager<sup>™</sup></td>
<td style="background-color: #e96e01; background-image: url('https://citrine.io/wp-content/uploads/2023/11/refresh-home-arrow-blue.png'); background-position: center left -1px; background-repeat: no-repeat; background-size: 13px;" colspan="3">Citrine<br />
VirtualLab<sup>™</sup></td>
<td style="background-color: #fff;"></td>
</tr>
<tr class="home-how-row2">
<td valign="top">
<div>
<p>Capture all your company&#8217;s knowledge</p>
<p><a href="/platform/citrine-datamanager/"><picture decoding="async" class="aligncenter size-full wp-image-5716">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/how01r.png.webp 420w, https://citrine.io/wp-content/uploads/2023/11/how01r-286x300.png.webp 286w" sizes="(max-width: 420px) 100vw, 420px"/>
<img decoding="async" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20420%20440'%3E%3C/svg%3E" alt="" width="420" height="440" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/how01r.png 420w, https://citrine.io/wp-content/uploads/2023/11/how01r-286x300.png 286w" data-lazy-sizes="(max-width: 420px) 100vw, 420px" data-lazy-src="https://citrine.io/wp-content/uploads/2023/11/how01r.png"/><noscript><img decoding="async" src="https://citrine.io/wp-content/uploads/2023/11/how01r.png" alt="" width="420" height="440" srcset="https://citrine.io/wp-content/uploads/2023/11/how01r.png 420w, https://citrine.io/wp-content/uploads/2023/11/how01r-286x300.png 286w" sizes="(max-width: 420px) 100vw, 420px"/></noscript>
</picture>
</a></p>
</div>
<p style="margin-left: 0px;"><a class="left-link" href="/platform/citrine-datamanager/">Learn more</a></p>
</td>
<td valign="top">
<div>
<p>Specify the properties your customers need</p>
<p><a href="/platform/citrine-virtuallab/"><picture decoding="async" class="aligncenter size-full wp-image-5717">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/how02r.png.webp 420w, https://citrine.io/wp-content/uploads/2023/11/how02r-286x300.png.webp 286w" sizes="(max-width: 420px) 100vw, 420px"/>
<img decoding="async" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20420%20440'%3E%3C/svg%3E" alt="" width="420" height="440" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/how02r.png 420w, https://citrine.io/wp-content/uploads/2023/11/how02r-286x300.png 286w" data-lazy-sizes="(max-width: 420px) 100vw, 420px" data-lazy-src="https://citrine.io/wp-content/uploads/2023/11/how02r.png"/><noscript><img decoding="async" src="https://citrine.io/wp-content/uploads/2023/11/how02r.png" alt="" width="420" height="440" srcset="https://citrine.io/wp-content/uploads/2023/11/how02r.png 420w, https://citrine.io/wp-content/uploads/2023/11/how02r-286x300.png 286w" sizes="(max-width: 420px) 100vw, 420px"/></noscript>
</picture>
</a></p>
</div>
<p style="margin-left: 0px;"><a class="left-link" href="/platform/citrine-virtuallab/">Learn more</a></p>
</td>
<td valign="top">
<div>
<p>Use our generative AI platform to run 1000s of virtual experiments</p>
<p><a href="/platform/citrine-virtuallab/"><picture decoding="async" class="aligncenter size-full wp-image-5718">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/how03r.png.webp 420w, https://citrine.io/wp-content/uploads/2023/11/how03r-286x300.png.webp 286w" sizes="(max-width: 420px) 100vw, 420px"/>
<img decoding="async" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20420%20440'%3E%3C/svg%3E" alt="" width="420" height="440" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/how03r.png 420w, https://citrine.io/wp-content/uploads/2023/11/how03r-286x300.png 286w" data-lazy-sizes="(max-width: 420px) 100vw, 420px" data-lazy-src="https://citrine.io/wp-content/uploads/2023/11/how03r.png"/><noscript><img decoding="async" src="https://citrine.io/wp-content/uploads/2023/11/how03r.png" alt="" width="420" height="440" srcset="https://citrine.io/wp-content/uploads/2023/11/how03r.png 420w, https://citrine.io/wp-content/uploads/2023/11/how03r-286x300.png 286w" sizes="(max-width: 420px) 100vw, 420px"/></noscript>
</picture>
</a></p>
</div>
<p style="margin-left: 0px;"><a class="left-link" href="/platform/citrine-virtuallab/">Learn more</a></p>
</td>
<td valign="top">
<div>
<p>Zoom in on the most promising candidates</p>
<p><a href="/platform/citrine-virtuallab/"><picture decoding="async" class="aligncenter size-full wp-image-5719">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/how04r.png.webp 420w, https://citrine.io/wp-content/uploads/2023/11/how04r-286x300.png.webp 286w" sizes="(max-width: 420px) 100vw, 420px"/>
<img decoding="async" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20420%20440'%3E%3C/svg%3E" alt="" width="420" height="440" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/how04r.png 420w, https://citrine.io/wp-content/uploads/2023/11/how04r-286x300.png 286w" data-lazy-sizes="(max-width: 420px) 100vw, 420px" data-lazy-src="https://citrine.io/wp-content/uploads/2023/11/how04r.png"/><noscript><img decoding="async" src="https://citrine.io/wp-content/uploads/2023/11/how04r.png" alt="" width="420" height="440" srcset="https://citrine.io/wp-content/uploads/2023/11/how04r.png 420w, https://citrine.io/wp-content/uploads/2023/11/how04r-286x300.png 286w" sizes="(max-width: 420px) 100vw, 420px"/></noscript>
</picture>
</a></p>
</div>
<p style="margin-left: 0px;"><a class="left-link" href="/platform/citrine-virtuallab/">Learn more</a></p>
</td>
<td></td>
</tr>
<tr>
<td colspan="4"><picture decoding="async" class="aligncenter size-full wp-image-5308 home-how-arrow">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/refresh-home-how-rearrow.png.webp 1559w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-how-rearrow-300x15.png.webp 300w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-how-rearrow-1024x51.png.webp 1024w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-how-rearrow-768x38.png.webp 768w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-how-rearrow-1536x77.png.webp 1536w" sizes="(max-width: 1559px) 100vw, 1559px"/>
<img decoding="async" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201559%2078'%3E%3C/svg%3E" alt="" width="1559" height="78" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/refresh-home-how-rearrow.png 1559w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-how-rearrow-300x15.png 300w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-how-rearrow-1024x51.png 1024w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-how-rearrow-768x38.png 768w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-how-rearrow-1536x77.png 1536w" data-lazy-sizes="(max-width: 1559px) 100vw, 1559px" data-lazy-src="https://citrine.io/wp-content/uploads/2023/11/refresh-home-how-rearrow.png"/><noscript><img decoding="async" src="https://citrine.io/wp-content/uploads/2023/11/refresh-home-how-rearrow.png" alt="" width="1559" height="78" srcset="https://citrine.io/wp-content/uploads/2023/11/refresh-home-how-rearrow.png 1559w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-how-rearrow-300x15.png 300w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-how-rearrow-1024x51.png 1024w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-how-rearrow-768x38.png 768w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-how-rearrow-1536x77.png 1536w" sizes="(max-width: 1559px) 100vw, 1559px"/></noscript>
</picture>
</td>
<td></td>
</tr>
</tbody>
</table>
                                                                                                                                                                                                                    </div>
                                                                                                        </div>
                
            </div>
        
            </div> <!--end of container -->
</div>

<div class="r8_flexible_content_section r8_columns_section-one_column r8_columns_section r8_columns_section_5  " style=" padding-top: 0px; padding-bottom: 40px;" id='home-product-box1'>
    <div class="r8_container container" style="max-width: 1000px">
        
        
                    <div class="r8_columns one_column column_content_top" style="max-width: 1000px">

                                                                            <div class="r8_column " style=" background-color: ;border-top-width: 1px; border-top-style: solid;border-right-width: 1px; border-right-style: solid;border-bottom-width: 1px; border-bottom-style: solid;border-left-width: 1px; border-left-style: solid;border-color: #ff8200;" >
                        
                                                                                                <div class="column_wysiwig r8_wysiwig_content">
                                                                                    <div data-bg="https://citrine.io/wp-content/uploads/2023/11/catalyst-blue-left@2x.png" class="rocket-lazyload" style="display: flex;  background-position: center left; background-size: 35px 130px; background-repeat: no-repeat; align-items: center; min-height: 160px;">
<div style="width: 50%;"><a href="/platform/citrine-catalyst/"><picture decoding="async" class="alignleft wp-image-5159" style="padding-left: 70px; padding-top: 7px;">
<source type="image/webp" srcset="https://citrine.io/wp-content/uploads/2023/10/citrine-catalyst-normal.png.webp 1852w, https://citrine.io/wp-content/uploads/2023/10/citrine-catalyst-normal-300x34.png.webp 300w, https://citrine.io/wp-content/uploads/2023/10/citrine-catalyst-normal-1024x114.png.webp 1024w, https://citrine.io/wp-content/uploads/2023/10/citrine-catalyst-normal-768x86.png.webp 768w, https://citrine.io/wp-content/uploads/2023/10/citrine-catalyst-normal-1536x172.png.webp 1536w" sizes="(max-width: 315px) 100vw, 315px"/>
<img decoding="async" src="https://citrine.io/wp-content/uploads/2023/10/citrine-catalyst-normal.png" alt="Citrine Catalyst" width="315" height="35" srcset="https://citrine.io/wp-content/uploads/2023/10/citrine-catalyst-normal.png 1852w, https://citrine.io/wp-content/uploads/2023/10/citrine-catalyst-normal-300x34.png 300w, https://citrine.io/wp-content/uploads/2023/10/citrine-catalyst-normal-1024x114.png 1024w, https://citrine.io/wp-content/uploads/2023/10/citrine-catalyst-normal-768x86.png 768w, https://citrine.io/wp-content/uploads/2023/10/citrine-catalyst-normal-1536x172.png 1536w" sizes="(max-width: 315px) 100vw, 315px"/>
</picture>
</a></div>
<div style="width: 50%; padding-right: 30px; padding-top: 15px; padding-bottom: 15px; font-weight: 500;">Use a digital assistant and find citations to improve your research.<br />
<a class="left-link" style="margin-top: 10px;" href="/platform/citrine-catalyst/">Learn more</a></div>
</div>
                                                                                                                                                                                                                    </div>
                                                                                                        </div>
                
            </div>
        
            </div> <!--end of container -->
</div>

<div class="r8_flexible_content_section r8_columns_section-one_column r8_columns_section r8_columns_section_6  " style=" padding-top: 0px; padding-bottom: 40px;" id='home-product-box2'>
    <div class="r8_container container" style="max-width: 1000px">
        
        
                    <div class="r8_columns one_column column_content_top" style="max-width: 1000px">

                                                                            <div class="r8_column " style=" background-color: ;border-top-width: 1px; border-top-style: solid;border-right-width: 1px; border-right-style: solid;border-bottom-width: 1px; border-bottom-style: solid;border-left-width: 1px; border-left-style: solid;border-color: #ff8200;" >
                        
                                                                                                <div class="column_wysiwig r8_wysiwig_content">
                                                                                    <div style="display: flex; align-items: center; min-height: 160px;">
<div style="width: 50%; padding: 15px 30px; padding-right: 50px;"><a href="/platform/citrine-professional-services/"><picture decoding="async" class="alignleft wp-image-5715">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/citrine-professional-services@2x.png.webp 1526w, https://citrine.io/wp-content/uploads/2023/11/citrine-professional-services@2x-300x19.png.webp 300w, https://citrine.io/wp-content/uploads/2023/11/citrine-professional-services@2x-1024x64.png.webp 1024w, https://citrine.io/wp-content/uploads/2023/11/citrine-professional-services@2x-768x48.png.webp 768w" sizes="(max-width: 430px) 100vw, 430px"/>
<img decoding="async" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20430%2027'%3E%3C/svg%3E" alt="" width="430" height="27" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/citrine-professional-services@2x.png 1526w, https://citrine.io/wp-content/uploads/2023/11/citrine-professional-services@2x-300x19.png 300w, https://citrine.io/wp-content/uploads/2023/11/citrine-professional-services@2x-1024x64.png 1024w, https://citrine.io/wp-content/uploads/2023/11/citrine-professional-services@2x-768x48.png 768w" data-lazy-sizes="(max-width: 430px) 100vw, 430px" data-lazy-src="https://citrine.io/wp-content/uploads/2023/11/citrine-professional-services@2x.png"/><noscript><img decoding="async" src="https://citrine.io/wp-content/uploads/2023/11/citrine-professional-services@2x.png" alt="" width="430" height="27" srcset="https://citrine.io/wp-content/uploads/2023/11/citrine-professional-services@2x.png 1526w, https://citrine.io/wp-content/uploads/2023/11/citrine-professional-services@2x-300x19.png 300w, https://citrine.io/wp-content/uploads/2023/11/citrine-professional-services@2x-1024x64.png 1024w, https://citrine.io/wp-content/uploads/2023/11/citrine-professional-services@2x-768x48.png 768w" sizes="(max-width: 430px) 100vw, 430px"/></noscript>
</picture>
</a></div>
<div style="width: 50%; padding-right: 30px; padding-top: 15px; padding-bottom: 15px; font-weight: 500;">Get all the help you need to find results and go to market faster than ever.<br />
<a class="left-link" style="margin-top: 10px;" href="/platform/citrine-professional-services/">Learn more</a></div>
</div>
                                                                                                                                                                                                                    </div>
                                                                                                        </div>
                
            </div>
        
            </div> <!--end of container -->
</div>

<div class="r8_flexible_content_section r8_columns_section-three_column r8_columns_section r8_columns_section_7  " style=" background-color: #fafafa; padding-top: 40px; padding-bottom: 40px;" id='home-enterprise'>
    <div class="r8_container container" style="">
        <h3 class="r8_section_title" style="text-align: center">Enterprise-ready. By design.</h3>
        
                    <div class="r8_columns three_column column_content_top" style="">

                                                                            <div class="r8_column " style=" background-color: ;" >
                        
                                                                                                <div class="column_wysiwig r8_wysiwig_content">
                                                                                    <p><picture decoding="async" class="aligncenter size-full wp-image-5400">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/refresh-home-security.png.webp"/>
<img decoding="async" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20360%20287'%3E%3C/svg%3E" alt="Security" width="360" height="287" data-lazy-src="https://citrine.io/wp-content/uploads/2023/11/refresh-home-security.png"/><noscript><img decoding="async" src="https://citrine.io/wp-content/uploads/2023/11/refresh-home-security.png" alt="Security" width="360" height="287"/></noscript>
</picture>
</p>
<h4 class="ttnone" style="text-align: center;">Security</h4>
<p style="text-align: center;">Unparalleled physical, network, and application security. ISO 27001 Certified. Trusted by industry leaders.</p>
<p style="text-align: center;"><a class="teallink" href="/platform/security/">Learn more ›</a></p>
                                                                                                                                                                                                                    </div>
                                                                                                        </div>
                                                                            <div class="r8_column " style=" background-color: ;" >
                        
                                                                                                <div class="column_wysiwig r8_wysiwig_content">
                                                                                    <p><picture decoding="async" class="aligncenter size-full wp-image-5399">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/refresh-home-pro-onboarding.png.webp 529w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-pro-onboarding-300x163.png.webp 300w" sizes="(max-width: 529px) 100vw, 529px"/>
<img decoding="async" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20529%20287'%3E%3C/svg%3E" alt="Professional on-boarding" width="529" height="287" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/refresh-home-pro-onboarding.png 529w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-pro-onboarding-300x163.png 300w" data-lazy-sizes="(max-width: 529px) 100vw, 529px" data-lazy-src="https://citrine.io/wp-content/uploads/2023/11/refresh-home-pro-onboarding.png"/><noscript><img decoding="async" src="https://citrine.io/wp-content/uploads/2023/11/refresh-home-pro-onboarding.png" alt="Professional on-boarding" width="529" height="287" srcset="https://citrine.io/wp-content/uploads/2023/11/refresh-home-pro-onboarding.png 529w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-pro-onboarding-300x163.png 300w" sizes="(max-width: 529px) 100vw, 529px"/></noscript>
</picture>
</p>
<h4 class="ttnone" style="text-align: center;">Professional on-boarding</h4>
<p style="text-align: center;">Your data isn’t organized yet? No problem. Our team has tools to get you up and running quickly so you can see results.</p>
<p style="text-align: center;"><a class="teallink" href="/platform/getting-started/">Learn more ›</a></p>
                                                                                                                                                                                                                    </div>
                                                                                                        </div>
                                                                            <div class="r8_column " style=" background-color: ;" >
                        
                                                                                                <div class="column_wysiwig r8_wysiwig_content">
                                                                                    <p><picture decoding="async" class="aligncenter size-full wp-image-5398">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/refresh-home-adaptability.png.webp"/>
<img decoding="async" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20337%20287'%3E%3C/svg%3E" alt="Adaptability" width="337" height="287" data-lazy-src="https://citrine.io/wp-content/uploads/2023/11/refresh-home-adaptability.png"/><noscript><img decoding="async" src="https://citrine.io/wp-content/uploads/2023/11/refresh-home-adaptability.png" alt="Adaptability" width="337" height="287"/></noscript>
</picture>
</p>
<h4 class="ttnone" style="text-align: center;">Adaptability</h4>
<p style="text-align: center;">Your materials have unique properties – and our AI tools are flexible enough to handle whatever you’ve got. Bring us your tough technical and business challenges. We’ll help you turn your valuable materials data into something even better.</p>
<p style="text-align: center;"><a class="teallink" href="/platform/flexibility/">Learn more ›</a></p>
                                                                                                                                                                                                                    </div>
                                                                                                        </div>
                
            </div>
        
            </div> <!--end of container -->
</div>
                <style media="screen" type="text/css">
                    .r8_columns_section_8 { background-image: var(--wpr-bg-2c474318-b396-45df-af77-b6bc16faf337); }
                                    </style>
            
<div class="r8_flexible_content_section r8_columns_section-one_column r8_columns_section r8_columns_section_8  r8_white_font_color" style=" background-color: #fafafa; padding-top: 40px; padding-bottom: 40px;" id='home-request'>
    <div class="r8_container container" style="max-width: 1280px">
        
        
                    <div class="r8_columns one_column column_content_top" style="max-width: 1280px">

                                                                            <div class="r8_column " style=" background-color: ;" >
                        
                                                                                                <div class="column_wysiwig r8_wysiwig_content">
                                                                                    <div class="home-product-flex">
<div class="home-product-flex1">
<h3>The Citrine platform is more than a product development tool</h3>
<div class="home-dots">Sales  •  Supply Chain  •  Scale Production  •  Sustainability</div>
</div>
<div class="home-product-flex2"><img decoding="async" class="aligncenter size-full wp-image-5725" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201498%20841'%3E%3C/svg%3E" alt="connections between sales, production, research, supply chain, finance, compliance" width="1498" height="841" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/home-product-web@2x.png 1498w, https://citrine.io/wp-content/uploads/2023/11/home-product-web@2x-300x168.png 300w, https://citrine.io/wp-content/uploads/2023/11/home-product-web@2x-1024x575.png 1024w, https://citrine.io/wp-content/uploads/2023/11/home-product-web@2x-768x431.png 768w, https://citrine.io/wp-content/uploads/2023/11/home-product-web@2x-482x270.png 482w" data-lazy-sizes="(max-width: 1498px) 100vw, 1498px" data-lazy-src="https://citrine.io/wp-content/uploads/2023/11/home-product-web@2x.png" /><noscript><img decoding="async" class="aligncenter size-full wp-image-5725" src="https://citrine.io/wp-content/uploads/2023/11/home-product-web@2x.png" alt="connections between sales, production, research, supply chain, finance, compliance" width="1498" height="841" srcset="https://citrine.io/wp-content/uploads/2023/11/home-product-web@2x.png 1498w, https://citrine.io/wp-content/uploads/2023/11/home-product-web@2x-300x168.png 300w, https://citrine.io/wp-content/uploads/2023/11/home-product-web@2x-1024x575.png 1024w, https://citrine.io/wp-content/uploads/2023/11/home-product-web@2x-768x431.png 768w, https://citrine.io/wp-content/uploads/2023/11/home-product-web@2x-482x270.png 482w" sizes="(max-width: 1498px) 100vw, 1498px" /></noscript></div>
</div>
<div class="home-product-columns">
<div>
<p style="margin-bottom: 0px;"><picture decoding="async" class="aligncenter size-full wp-image-5726">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/01sales@2x.png.webp 388w, https://citrine.io/wp-content/uploads/2023/11/01sales@2x-300x268.png.webp 300w" sizes="(max-width: 388px) 100vw, 388px"/>
<img decoding="async" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20388%20347'%3E%3C/svg%3E" alt="" width="388" height="347" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/01sales@2x.png 388w, https://citrine.io/wp-content/uploads/2023/11/01sales@2x-300x268.png 300w" data-lazy-sizes="(max-width: 388px) 100vw, 388px" data-lazy-src="https://citrine.io/wp-content/uploads/2023/11/01sales@2x.png"/><noscript><img decoding="async" src="https://citrine.io/wp-content/uploads/2023/11/01sales@2x.png" alt="" width="388" height="347" srcset="https://citrine.io/wp-content/uploads/2023/11/01sales@2x.png 388w, https://citrine.io/wp-content/uploads/2023/11/01sales@2x-300x268.png 300w" sizes="(max-width: 388px) 100vw, 388px"/></noscript>
</picture>
</p>
<h5>Sales</h5>
<p>Get your customers the performance they need</p>
</div>
<div>
<p style="margin-bottom: 0px;"><picture decoding="async" class="aligncenter size-full wp-image-5727">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/02supply@2x.png.webp 388w, https://citrine.io/wp-content/uploads/2023/11/02supply@2x-300x268.png.webp 300w" sizes="(max-width: 388px) 100vw, 388px"/>
<img decoding="async" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20388%20347'%3E%3C/svg%3E" alt="" width="388" height="347" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/02supply@2x.png 388w, https://citrine.io/wp-content/uploads/2023/11/02supply@2x-300x268.png 300w" data-lazy-sizes="(max-width: 388px) 100vw, 388px" data-lazy-src="https://citrine.io/wp-content/uploads/2023/11/02supply@2x.png"/><noscript><img decoding="async" src="https://citrine.io/wp-content/uploads/2023/11/02supply@2x.png" alt="" width="388" height="347" srcset="https://citrine.io/wp-content/uploads/2023/11/02supply@2x.png 388w, https://citrine.io/wp-content/uploads/2023/11/02supply@2x-300x268.png 300w" sizes="(max-width: 388px) 100vw, 388px"/></noscript>
</picture>
</p>
<h5>Supply Chain</h5>
<p>Identify alternatives and improve resilience</p>
</div>
<div>
<p style="margin-bottom: 0px;"><picture decoding="async" class="aligncenter size-full wp-image-5728">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/03finance@2x.png.webp 388w, https://citrine.io/wp-content/uploads/2023/11/03finance@2x-300x268.png.webp 300w" sizes="(max-width: 388px) 100vw, 388px"/>
<img decoding="async" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20388%20347'%3E%3C/svg%3E" alt="" width="388" height="347" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/03finance@2x.png 388w, https://citrine.io/wp-content/uploads/2023/11/03finance@2x-300x268.png 300w" data-lazy-sizes="(max-width: 388px) 100vw, 388px" data-lazy-src="https://citrine.io/wp-content/uploads/2023/11/03finance@2x.png"/><noscript><img decoding="async" src="https://citrine.io/wp-content/uploads/2023/11/03finance@2x.png" alt="" width="388" height="347" srcset="https://citrine.io/wp-content/uploads/2023/11/03finance@2x.png 388w, https://citrine.io/wp-content/uploads/2023/11/03finance@2x-300x268.png 300w" sizes="(max-width: 388px) 100vw, 388px"/></noscript>
</picture>
</p>
<h5>Finance</h5>
<p>Reduce cost and improve profitability</p>
</div>
<div>
<p style="margin-bottom: 0px;"><picture decoding="async" class="aligncenter size-full wp-image-5729">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/04engineering@2x.png.webp 388w, https://citrine.io/wp-content/uploads/2023/11/04engineering@2x-300x268.png.webp 300w" sizes="(max-width: 388px) 100vw, 388px"/>
<img decoding="async" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20388%20347'%3E%3C/svg%3E" alt="" width="388" height="347" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/04engineering@2x.png 388w, https://citrine.io/wp-content/uploads/2023/11/04engineering@2x-300x268.png 300w" data-lazy-sizes="(max-width: 388px) 100vw, 388px" data-lazy-src="https://citrine.io/wp-content/uploads/2023/11/04engineering@2x.png"/><noscript><img decoding="async" src="https://citrine.io/wp-content/uploads/2023/11/04engineering@2x.png" alt="" width="388" height="347" srcset="https://citrine.io/wp-content/uploads/2023/11/04engineering@2x.png 388w, https://citrine.io/wp-content/uploads/2023/11/04engineering@2x-300x268.png 300w" sizes="(max-width: 388px) 100vw, 388px"/></noscript>
</picture>
</p>
<h5>Engineering</h5>
<p>Develop better products 5 times faster</p>
</div>
<div>
<p style="margin-bottom: 0px;"><picture decoding="async" class="aligncenter size-full wp-image-5730">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/05production@2x.png.webp 388w, https://citrine.io/wp-content/uploads/2023/11/05production@2x-300x268.png.webp 300w" sizes="(max-width: 388px) 100vw, 388px"/>
<img decoding="async" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20388%20347'%3E%3C/svg%3E" alt="" width="388" height="347" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/05production@2x.png 388w, https://citrine.io/wp-content/uploads/2023/11/05production@2x-300x268.png 300w" data-lazy-sizes="(max-width: 388px) 100vw, 388px" data-lazy-src="https://citrine.io/wp-content/uploads/2023/11/05production@2x.png"/><noscript><img decoding="async" src="https://citrine.io/wp-content/uploads/2023/11/05production@2x.png" alt="" width="388" height="347" srcset="https://citrine.io/wp-content/uploads/2023/11/05production@2x.png 388w, https://citrine.io/wp-content/uploads/2023/11/05production@2x-300x268.png 300w" sizes="(max-width: 388px) 100vw, 388px"/></noscript>
</picture>
</p>
<h5>Production</h5>
<p>Create products that can be made consistently, at scale</p>
</div>
<div>
<p style="margin-bottom: 0px;"><picture decoding="async" class="aligncenter size-full wp-image-5731">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/06compliance@2x.png.webp 388w, https://citrine.io/wp-content/uploads/2023/11/06compliance@2x-300x268.png.webp 300w" sizes="(max-width: 388px) 100vw, 388px"/>
<img decoding="async" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20388%20347'%3E%3C/svg%3E" alt="" width="388" height="347" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/06compliance@2x.png 388w, https://citrine.io/wp-content/uploads/2023/11/06compliance@2x-300x268.png 300w" data-lazy-sizes="(max-width: 388px) 100vw, 388px" data-lazy-src="https://citrine.io/wp-content/uploads/2023/11/06compliance@2x.png"/><noscript><img decoding="async" src="https://citrine.io/wp-content/uploads/2023/11/06compliance@2x.png" alt="" width="388" height="347" srcset="https://citrine.io/wp-content/uploads/2023/11/06compliance@2x.png 388w, https://citrine.io/wp-content/uploads/2023/11/06compliance@2x-300x268.png 300w" sizes="(max-width: 388px) 100vw, 388px"/></noscript>
</picture>
</p>
<h5>Compliance</h5>
<p>Respond quickly to evolving regulation</p>
</div>
</div>
<p style="text-align: center;">Let us show you how we can help.</p>
<div class="r8_button_wrap" style="text-align: center;"><a class="r8_btn primary_btn" href="/request-a-demo/" target="_self">I&#8217;d like a demo</a></div>
                                                                                                                                                                                                                    </div>
                                                                                                        </div>
                
            </div>
        
            </div> <!--end of container -->
</div>

<div class="r8_flexible_content_section r8_columns_section-four_column r8_columns_section r8_columns_section_9  r8_white_font_color" style=" background-color: #333333; padding-top: 60px; padding-bottom: 40px;" id='home-industries'>
    <div class="r8_container container" style="">
        <h4 class="r8_section_title r8_white_font_color" style="text-align: center">Whatever you make, we'll help you make it better, faster, cheaper</h4>
        
                    <div class="r8_columns four_column column_content_top" style="">

                                                                            <div class="r8_column " style=" background-color: ;" >
                        
                                                                                                <div class="column_wysiwig r8_wysiwig_content">
                                                                                    <p><a href="/who-we-help/specialty-chemicals/"><picture decoding="async" class="aligncenter size-full wp-image-6908">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2025/01/chemicals-one.png.webp 515w, https://citrine.io/wp-content/uploads/2025/01/chemicals-one-443x440.png.webp 443w" sizes="(max-width: 515px) 100vw, 515px"/>
<img decoding="async" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20515%20511'%3E%3C/svg%3E" alt="Specialty chemicals" width="515" height="511" data-lazy-srcset="https://citrine.io/wp-content/uploads/2025/01/chemicals-one.png 515w, https://citrine.io/wp-content/uploads/2025/01/chemicals-one-443x440.png 443w" data-lazy-sizes="(max-width: 515px) 100vw, 515px" data-lazy-src="https://citrine.io/wp-content/uploads/2025/01/chemicals-one.png"/><noscript><img decoding="async" src="https://citrine.io/wp-content/uploads/2025/01/chemicals-one.png" alt="Specialty chemicals" width="515" height="511" srcset="https://citrine.io/wp-content/uploads/2025/01/chemicals-one.png 515w, https://citrine.io/wp-content/uploads/2025/01/chemicals-one-443x440.png 443w" sizes="(max-width: 515px) 100vw, 515px"/></noscript>
</picture>
<br />
Specialty Chemicals</a></p>
                                                                                                                                                                                                                    </div>
                                                                                                        </div>
                                                                            <div class="r8_column " style=" background-color: ;" >
                        
                                                                                                <div class="column_wysiwig r8_wysiwig_content">
                                                                                    <p><a href="/who-we-help/personal-care-and-cosmetics/"><picture decoding="async" class="aligncenter size-full wp-image-6902">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2025/01/personal-care-household-one.png.webp 515w, https://citrine.io/wp-content/uploads/2025/01/personal-care-household-one-443x440.png.webp 443w" sizes="(max-width: 515px) 100vw, 515px"/>
<img decoding="async" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20515%20511'%3E%3C/svg%3E" alt="Personal care &amp; cosmetics" width="515" height="511" data-lazy-srcset="https://citrine.io/wp-content/uploads/2025/01/personal-care-household-one.png 515w, https://citrine.io/wp-content/uploads/2025/01/personal-care-household-one-443x440.png 443w" data-lazy-sizes="(max-width: 515px) 100vw, 515px" data-lazy-src="https://citrine.io/wp-content/uploads/2025/01/personal-care-household-one.png"/><noscript><img decoding="async" src="https://citrine.io/wp-content/uploads/2025/01/personal-care-household-one.png" alt="Personal care &amp; cosmetics" width="515" height="511" srcset="https://citrine.io/wp-content/uploads/2025/01/personal-care-household-one.png 515w, https://citrine.io/wp-content/uploads/2025/01/personal-care-household-one-443x440.png 443w" sizes="(max-width: 515px) 100vw, 515px"/></noscript>
</picture>
<br />
Personal Care &amp; Cosmetics</a></p>
                                                                                                                                                                                                                    </div>
                                                                                                        </div>
                                                                            <div class="r8_column " style=" background-color: ;" >
                        
                                                                                                <div class="column_wysiwig r8_wysiwig_content">
                                                                                    <p><a href="/who-we-help/plastics/"><picture decoding="async" class="aligncenter size-full wp-image-6901">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2025/01/plastics-one.png.webp 515w, https://citrine.io/wp-content/uploads/2025/01/plastics-one-443x440.png.webp 443w" sizes="(max-width: 515px) 100vw, 515px"/>
<img decoding="async" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20515%20511'%3E%3C/svg%3E" alt="Plastics" width="515" height="511" data-lazy-srcset="https://citrine.io/wp-content/uploads/2025/01/plastics-one.png 515w, https://citrine.io/wp-content/uploads/2025/01/plastics-one-443x440.png 443w" data-lazy-sizes="(max-width: 515px) 100vw, 515px" data-lazy-src="https://citrine.io/wp-content/uploads/2025/01/plastics-one.png"/><noscript><img decoding="async" src="https://citrine.io/wp-content/uploads/2025/01/plastics-one.png" alt="Plastics" width="515" height="511" srcset="https://citrine.io/wp-content/uploads/2025/01/plastics-one.png 515w, https://citrine.io/wp-content/uploads/2025/01/plastics-one-443x440.png 443w" sizes="(max-width: 515px) 100vw, 515px"/></noscript>
</picture>
<br />
Plastics</a></p>
                                                                                                                                                                                                                    </div>
                                                                                                        </div>
                                                                            <div class="r8_column " style=" background-color: ;" >
                        
                                                                                                <div class="column_wysiwig r8_wysiwig_content">
                                                                                    <p><a href="/who-we-help/coatings-adhesives-and-sealants/"><picture decoding="async" class="aligncenter size-full wp-image-6906">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2025/01/Coatings-Adhesives-Sealants-one.png.webp 515w, https://citrine.io/wp-content/uploads/2025/01/Coatings-Adhesives-Sealants-one-443x440.png.webp 443w" sizes="(max-width: 515px) 100vw, 515px"/>
<img decoding="async" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20515%20511'%3E%3C/svg%3E" alt="Coatings, Adhesives and Sealants" width="515" height="511" data-lazy-srcset="https://citrine.io/wp-content/uploads/2025/01/Coatings-Adhesives-Sealants-one.png 515w, https://citrine.io/wp-content/uploads/2025/01/Coatings-Adhesives-Sealants-one-443x440.png 443w" data-lazy-sizes="(max-width: 515px) 100vw, 515px" data-lazy-src="https://citrine.io/wp-content/uploads/2025/01/Coatings-Adhesives-Sealants-one.png"/><noscript><img decoding="async" src="https://citrine.io/wp-content/uploads/2025/01/Coatings-Adhesives-Sealants-one.png" alt="Coatings, Adhesives and Sealants" width="515" height="511" srcset="https://citrine.io/wp-content/uploads/2025/01/Coatings-Adhesives-Sealants-one.png 515w, https://citrine.io/wp-content/uploads/2025/01/Coatings-Adhesives-Sealants-one-443x440.png 443w" sizes="(max-width: 515px) 100vw, 515px"/></noscript>
</picture>
<br />
Coatings, Adhesives &amp; Sealants</a></p>
                                                                                                                                                                                                                    </div>
                                                                                                        </div>
                                                                            <div class="r8_column " style=" background-color: ;" >
                        
                                                                                                <div class="column_wysiwig r8_wysiwig_content">
                                                                                    <p><a href="/who-we-help/food-and-beverage/"><picture decoding="async" class="aligncenter size-full wp-image-6905">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2025/01/food-beverages-one.png.webp 515w, https://citrine.io/wp-content/uploads/2025/01/food-beverages-one-443x440.png.webp 443w" sizes="(max-width: 515px) 100vw, 515px"/>
<img decoding="async" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20515%20511'%3E%3C/svg%3E" alt="Food &amp; beverage" width="515" height="511" data-lazy-srcset="https://citrine.io/wp-content/uploads/2025/01/food-beverages-one.png 515w, https://citrine.io/wp-content/uploads/2025/01/food-beverages-one-443x440.png 443w" data-lazy-sizes="(max-width: 515px) 100vw, 515px" data-lazy-src="https://citrine.io/wp-content/uploads/2025/01/food-beverages-one.png"/><noscript><img decoding="async" src="https://citrine.io/wp-content/uploads/2025/01/food-beverages-one.png" alt="Food &amp; beverage" width="515" height="511" srcset="https://citrine.io/wp-content/uploads/2025/01/food-beverages-one.png 515w, https://citrine.io/wp-content/uploads/2025/01/food-beverages-one-443x440.png 443w" sizes="(max-width: 515px) 100vw, 515px"/></noscript>
</picture>
<br />
Food &amp; Beverage</a></p>
                                                                                                                                                                                                                    </div>
                                                                                                        </div>
                                                                            <div class="r8_column " style=" background-color: ;" >
                        
                                                                                                <div class="column_wysiwig r8_wysiwig_content">
                                                                                    <p><a href="/who-we-help/packaging/"><picture decoding="async" class="aligncenter size-full wp-image-6903">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2025/01/packaging-one.png.webp 515w, https://citrine.io/wp-content/uploads/2025/01/packaging-one-443x440.png.webp 443w" sizes="(max-width: 515px) 100vw, 515px"/>
<img decoding="async" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20515%20511'%3E%3C/svg%3E" alt="Packaging" width="515" height="511" data-lazy-srcset="https://citrine.io/wp-content/uploads/2025/01/packaging-one.png 515w, https://citrine.io/wp-content/uploads/2025/01/packaging-one-443x440.png 443w" data-lazy-sizes="(max-width: 515px) 100vw, 515px" data-lazy-src="https://citrine.io/wp-content/uploads/2025/01/packaging-one.png"/><noscript><img decoding="async" src="https://citrine.io/wp-content/uploads/2025/01/packaging-one.png" alt="Packaging" width="515" height="511" srcset="https://citrine.io/wp-content/uploads/2025/01/packaging-one.png 515w, https://citrine.io/wp-content/uploads/2025/01/packaging-one-443x440.png 443w" sizes="(max-width: 515px) 100vw, 515px"/></noscript>
</picture>
<br />
Packaging</a></p>
                                                                                                                                                                                                                    </div>
                                                                                                        </div>
                                                                            <div class="r8_column " style=" background-color: ;" >
                        
                                                                                                <div class="column_wysiwig r8_wysiwig_content">
                                                                                    <p><a href="/who-we-help/additives-and-ingredients/"><picture decoding="async" class="aligncenter size-full wp-image-6907">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2025/01/additives-one.png.webp 515w, https://citrine.io/wp-content/uploads/2025/01/additives-one-443x440.png.webp 443w" sizes="(max-width: 515px) 100vw, 515px"/>
<img decoding="async" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20515%20511'%3E%3C/svg%3E" alt="Additives and ingredients" width="515" height="511" data-lazy-srcset="https://citrine.io/wp-content/uploads/2025/01/additives-one.png 515w, https://citrine.io/wp-content/uploads/2025/01/additives-one-443x440.png 443w" data-lazy-sizes="(max-width: 515px) 100vw, 515px" data-lazy-src="https://citrine.io/wp-content/uploads/2025/01/additives-one.png"/><noscript><img decoding="async" src="https://citrine.io/wp-content/uploads/2025/01/additives-one.png" alt="Additives and ingredients" width="515" height="511" srcset="https://citrine.io/wp-content/uploads/2025/01/additives-one.png 515w, https://citrine.io/wp-content/uploads/2025/01/additives-one-443x440.png 443w" sizes="(max-width: 515px) 100vw, 515px"/></noscript>
</picture>
<br />
Additives &amp; Ingredients</a></p>
                                                                                                                                                                                                                    </div>
                                                                                                        </div>
                                                                            <div class="r8_column " style=" background-color: ;" >
                        
                                                                                                <div class="column_wysiwig r8_wysiwig_content">
                                                                                    <p><a href="/who-we-help/#platform-industries-accordion"><picture decoding="async" class="aligncenter size-full wp-image-6915">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2025/01/metals.png.webp"/>
<img decoding="async" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20515%20511'%3E%3C/svg%3E" alt="Metals &amp; Alloys" width="515" height="511" data-lazy-src="https://citrine.io/wp-content/uploads/2025/01/metals.png"/><noscript><img decoding="async" src="https://citrine.io/wp-content/uploads/2025/01/metals.png" alt="Metals &amp; Alloys" width="515" height="511"/></noscript>
</picture>
<br />
Metals &amp; Alloys</a></p>
                                                                                                                                                                                                                    </div>
                                                                                                        </div>
                                                                            <div class="r8_column " style=" background-color: ;" >
                        
                                                                                                <div class="column_wysiwig r8_wysiwig_content">
                                                                                    <p><a href="/who-we-help/#platform-industries-accordion"><picture decoding="async" class="aligncenter size-full wp-image-6918">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2025/01/batteries.png.webp"/>
<img decoding="async" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20515%20511'%3E%3C/svg%3E" alt="Automotive &amp; Batteries" width="515" height="511" data-lazy-src="https://citrine.io/wp-content/uploads/2025/01/batteries.png"/><noscript><img decoding="async" src="https://citrine.io/wp-content/uploads/2025/01/batteries.png" alt="Automotive &amp; Batteries" width="515" height="511"/></noscript>
</picture>
<br />
Automotive &amp; Batteries</a></p>
                                                                                                                                                                                                                    </div>
                                                                                                        </div>
                                                                            <div class="r8_column " style=" background-color: ;" >
                        
                                                                                                <div class="column_wysiwig r8_wysiwig_content">
                                                                                    <p><a href="/who-we-help/#platform-industries-accordion"><picture decoding="async" class="aligncenter size-full wp-image-6916">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2025/01/glass.png.webp 515w, https://citrine.io/wp-content/uploads/2025/01/glass-443x440.png.webp 443w" sizes="(max-width: 515px) 100vw, 515px"/>
<img decoding="async" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20515%20511'%3E%3C/svg%3E" alt="Ceramics &amp; Glass" width="515" height="511" data-lazy-srcset="https://citrine.io/wp-content/uploads/2025/01/glass.png 515w, https://citrine.io/wp-content/uploads/2025/01/glass-443x440.png 443w" data-lazy-sizes="(max-width: 515px) 100vw, 515px" data-lazy-src="https://citrine.io/wp-content/uploads/2025/01/glass.png"/><noscript><img decoding="async" src="https://citrine.io/wp-content/uploads/2025/01/glass.png" alt="Ceramics &amp; Glass" width="515" height="511" srcset="https://citrine.io/wp-content/uploads/2025/01/glass.png 515w, https://citrine.io/wp-content/uploads/2025/01/glass-443x440.png 443w" sizes="(max-width: 515px) 100vw, 515px"/></noscript>
</picture>
<br />
Ceramics &amp; Glass</a></p>
                                                                                                                                                                                                                    </div>
                                                                                                        </div>
                                                                            <div class="r8_column " style=" background-color: ;" >
                        
                                                                                                <div class="column_wysiwig r8_wysiwig_content">
                                                                                    <p><a href="/who-we-help/#platform-industries-accordion"><picture decoding="async" class="aligncenter size-full wp-image-6917">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2025/01/aerospace.png.webp 515w, https://citrine.io/wp-content/uploads/2025/01/aerospace-443x440.png.webp 443w" sizes="(max-width: 515px) 100vw, 515px"/>
<img decoding="async" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20515%20511'%3E%3C/svg%3E" alt="Aerospace &amp; Defense" width="515" height="511" data-lazy-srcset="https://citrine.io/wp-content/uploads/2025/01/aerospace.png 515w, https://citrine.io/wp-content/uploads/2025/01/aerospace-443x440.png 443w" data-lazy-sizes="(max-width: 515px) 100vw, 515px" data-lazy-src="https://citrine.io/wp-content/uploads/2025/01/aerospace.png"/><noscript><img decoding="async" src="https://citrine.io/wp-content/uploads/2025/01/aerospace.png" alt="Aerospace &amp; Defense" width="515" height="511" srcset="https://citrine.io/wp-content/uploads/2025/01/aerospace.png 515w, https://citrine.io/wp-content/uploads/2025/01/aerospace-443x440.png 443w" sizes="(max-width: 515px) 100vw, 515px"/></noscript>
</picture>
<br />
Aerospace &amp; Defense</a></p>
                                                                                                                                                                                                                    </div>
                                                                                                        </div>
                                                                            <div class="r8_column " style=" background-color: ;" >
                        
                                                                                                <div class="column_wysiwig r8_wysiwig_content">
                                                                                    <p><a href="/who-we-help/#Industries"><img decoding="async" class="aligncenter size-full wp-image-6904" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20513%20511'%3E%3C/svg%3E" alt="Other Industries" width="513" height="511" data-lazy-srcset="https://citrine.io/wp-content/uploads/2025/01/other-industries.png 513w, https://citrine.io/wp-content/uploads/2025/01/other-industries-442x440.png 442w" data-lazy-sizes="(max-width: 513px) 100vw, 513px" data-lazy-src="https://citrine.io/wp-content/uploads/2025/01/other-industries.png" /><noscript><img decoding="async" class="aligncenter size-full wp-image-6904" src="https://citrine.io/wp-content/uploads/2025/01/other-industries.png" alt="Other Industries" width="513" height="511" srcset="https://citrine.io/wp-content/uploads/2025/01/other-industries.png 513w, https://citrine.io/wp-content/uploads/2025/01/other-industries-442x440.png 442w" sizes="(max-width: 513px) 100vw, 513px" /></noscript><br />
Other Industries</a></p>
                                                                                                                                                                                                                    </div>
                                                                                                        </div>
                
            </div>
        
            </div> <!--end of container -->
</div>

<div class="r8_flexible_content_section r8_columns_section-two_column r8_columns_section r8_columns_section_10  " style=" padding-top: 40px; padding-bottom: 40px;" >
    <div class="r8_container container" style="">
        
        
                    <div class="r8_columns two_column r8_one_third column_content_middle" style="">

                                                                            <div class="r8_column " style=" background-color: ;" >
                        
                                                                                                <div class="column_wysiwig r8_wysiwig_content">
                                                                                    <p><picture decoding="async" class="aligncenter size-full wp-image-5341">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/refresh-home-greg@2x.png.webp 1606w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-greg@2x-300x274.png.webp 300w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-greg@2x-1024x935.png.webp 1024w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-greg@2x-768x701.png.webp 768w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-greg@2x-1536x1402.png.webp 1536w" sizes="(max-width: 1606px) 100vw, 1606px"/>
<img decoding="async" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201606%201466'%3E%3C/svg%3E" alt="Greg Mulholland, CEO of Citrine Informatics" width="1606" height="1466" data-lazy-srcset="https://citrine.io/wp-content/uploads/2023/11/refresh-home-greg@2x.png 1606w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-greg@2x-300x274.png 300w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-greg@2x-1024x935.png 1024w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-greg@2x-768x701.png 768w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-greg@2x-1536x1402.png 1536w" data-lazy-sizes="(max-width: 1606px) 100vw, 1606px" data-lazy-src="https://citrine.io/wp-content/uploads/2023/11/refresh-home-greg@2x.png"/><noscript><img decoding="async" src="https://citrine.io/wp-content/uploads/2023/11/refresh-home-greg@2x.png" alt="Greg Mulholland, CEO of Citrine Informatics" width="1606" height="1466" srcset="https://citrine.io/wp-content/uploads/2023/11/refresh-home-greg@2x.png 1606w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-greg@2x-300x274.png 300w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-greg@2x-1024x935.png 1024w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-greg@2x-768x701.png 768w, https://citrine.io/wp-content/uploads/2023/11/refresh-home-greg@2x-1536x1402.png 1536w" sizes="(max-width: 1606px) 100vw, 1606px"/></noscript>
</picture>
</p>
                                                                                                                                                                                                                    </div>
                                                                                                        </div>
                                                                            <div class="r8_column " style=" background-color: ;" >
                        
                                                                                                <div class="column_wysiwig r8_wysiwig_content">
                                                                                    <p><img decoding="async" class="alignleft wp-image-7309" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20140%20117'%3E%3C/svg%3E" alt="quotation mark" width="140" height="117" data-lazy-srcset="https://citrine.io/wp-content/uploads/2025/07/refresh-home-greg-quote@2x.png 678w, https://citrine.io/wp-content/uploads/2025/07/refresh-home-greg-quote@2x-525x440.png 525w" data-lazy-sizes="(max-width: 140px) 100vw, 140px" data-lazy-src="https://citrine.io/wp-content/uploads/2025/07/refresh-home-greg-quote@2x.png" /><noscript><img decoding="async" class="alignleft wp-image-7309" src="https://citrine.io/wp-content/uploads/2025/07/refresh-home-greg-quote@2x.png" alt="quotation mark" width="140" height="117" srcset="https://citrine.io/wp-content/uploads/2025/07/refresh-home-greg-quote@2x.png 678w, https://citrine.io/wp-content/uploads/2025/07/refresh-home-greg-quote@2x-525x440.png 525w" sizes="(max-width: 140px) 100vw, 140px" /></noscript></p>
<h4 class="ttnone ai-optimize-6" style="padding-top: 30px;">Citrine’s generative AI tools help companies use their smartest people’s expertise to find unseen patterns in their data. This lets them be far more efficient, by delivering their best possible products to market quickly while servicing their customers better than ever.”</h4>
<p class="ai-optimize-7">Greg Mulholland<br />
CEO, Citrine Informatics<br />
<div class="r8_button_wrap" style="text-align: left;"><a class="r8_btn primary_btn border-round" href="/request-a-demo/" target="_self">Get started</a></div></p>
                                                                                                                                                                                                                    </div>
                                                                                                        </div>
                
            </div>
        
            </div> <!--end of container -->
</div>
				
				
			
		</main><!-- #main -->
	</div><!-- #primary -->


	</div><!-- #content -->
	<footer data-wpr-lazyrender="1" id="colophon" class="site_footer" role="contentinfo">

		<div class="container">

			<div class="footer_content">

				<div class="logo_container footer_right">
									</div><!-- footer_right -->

				<div class="footer-lower-content">
					<div class="non_logo_container footer_left">
						<div class="footer_widgetized">
							<div class="footer_widget_block footer_widget_left">

								    <div class="footer_widget" id="footer_widget_left">
        <section id="custom_html-12" class="widget_text widget widget_custom_html"><div class="textwidget custom-html-widget"><a href="/"><img class="footer_logo" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E" alt="Citrine Informatics" data-lazy-src="https:&#047;&#x2f;&#x63;i&#116;&#x72;&#x69;n&#101;&#x2e;i&#111;&#x2f;&#x77;p&#045;&#x63;o&#110;&#x74;&#x65;n&#116;&#x2f;&#x75;&#112;&#x6c;&#x6f;a&#100;&#x73;&#x2f;2&#048;&#x32;1&#047;&#x31;&#x31;/&#102;&#x6f;o&#116;&#x65;&#x72;-&#108;&#x6f;&#x67;&#111;&#x40;&#x32;x&#046;&#x70;&#x6e;g"><noscript><img class="footer_logo" src="https:&#47;&#x2f;&#x63;i&#116;&#x72;&#x69;n&#101;&#x2e;i&#111;&#x2f;&#x77;p&#45;&#x63;o&#110;&#x74;&#x65;n&#116;&#x2f;&#x75;&#112;&#x6c;&#x6f;a&#100;&#x73;&#x2f;2&#48;&#x32;1&#47;&#x31;&#x31;/&#102;&#x6f;o&#116;&#x65;&#x72;-&#108;&#x6f;&#x67;&#111;&#x40;&#x32;x&#46;&#x70;&#x6e;g" alt="Citrine Informatics"></noscript></a>
<p>Citrine Informatics is an enterprise SaaS platform company that leverages generative artificial intelligence (AI) and materials science to help customers to improve materials and chemicals development.</p>
<h4 style="margin-top:30px;">
	CONTACT
</h4>
<picture style="float:right;margin-right:75px;">
<source type="image/webp" data-lazy-srcset="https://citrine.io/wp-content/uploads/2024/04/award-EcoVadis.png.webp"/>
<img src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2075%2075'%3E%3C/svg%3E" width="75" height="75" alt="EcoVadis 2023 Silver Sustainability rating" data-lazy-src="https://citrine.io/wp-content/uploads/2024/04/award-EcoVadis.png"/><noscript><img src="https://citrine.io/wp-content/uploads/2024/04/award-EcoVadis.png" width="75" height="75" alt="EcoVadis 2023 Silver Sustainability rating"/></noscript>
</picture>

<p style="margin-top:10px;">
Global Headquarters<br/>
2629 Broadway St<br/>
Redwood City, CA 94063<br/>
<a href="&#109;&#x61;&#x69;l&#116;&#x6f;:&#105;&#x6e;&#x66;&#111;&#x40;&#x63;i&#116;&#x72;i&#110;&#x65;&#x2e;&#105;&#x6f;">&#105;&#x6e;&#102;&#x6f;&#64;&#x63;&#105;&#x74;&#114;&#x69;&#110;&#x65;&#46;&#x69;&#111;</a>
	</p>
<a href="https://www.linkedin.com/company/citrine-informatics/" target="_blank"><img width="448" height="512" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20448%20512'%3E%3C/svg%3E" alt="" class="footer-social size-full wp-image-5940" data-lazy-src="https://citrine.io/wp-content/uploads/2023/11/linkedin-white.svg" /><noscript><img width="448" height="512" src="https://citrine.io/wp-content/uploads/2023/11/linkedin-white.svg" alt="" class="footer-social size-full wp-image-5940" /></noscript></a> <a href="https://twitter.com/citrine_io?lang=en" target="_blank"><img width="512" height="512" src="data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20512'%3E%3C/svg%3E" alt="" class="footer-social size-full wp-image-5940" data-lazy-src="https://citrine.io/wp-content/uploads/2023/11/x-twitter-white.svg" /><noscript><img width="512" height="512" src="https://citrine.io/wp-content/uploads/2023/11/x-twitter-white.svg" alt="" class="footer-social size-full wp-image-5940" /></noscript></a></div></section>    </div><!-- footer_widgets -->

																																</div>
						</div><!-- .footer_widgetized -->

					</div><!-- footer_left -->

					<div class="footer-right-area">
						<div class="footer_menu_container">
							<div class="menu-footer-menu-container"><ul id="menu-footer-menu" class="sec_footer_menu"><li id="menu-item-5901" class="footer-hide menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-5901"><a href="#">Column</a>
<ul class="sub-menu">
	<li id="menu-item-5889" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-5889"><a href="https://citrine.io/platform/">PLATFORM</a>
	<ul class="sub-menu">
		<li id="menu-item-5357" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-5357"><a href="/platform/#products">Products</a></li>
		<li id="menu-item-5362" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-5362"><a href="/platform/getting-started/">Getting Started</a></li>
	</ul>
</li>
	<li id="menu-item-5366" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-5366"><a href="/who-we-help/">WHO WE HELP</a>
	<ul class="sub-menu">
		<li id="menu-item-5368" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-5368"><a href="/who-we-help/#BusinessFunctions">Business Functions</a></li>
		<li id="menu-item-5367" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-5367"><a href="/who-we-help/#Industries">Industries</a></li>
	</ul>
</li>
	<li id="menu-item-5890" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-5890"><a href="https://citrine.io/why-citrine/">WHY CITRINE</a>
	<ul class="sub-menu">
		<li id="menu-item-5891" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-5891"><a href="/why-citrine/">Support for your Goals</a></li>
		<li id="menu-item-5892" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-5892"><a href="/why-citrine/#priorities">Shared Priorities</a></li>
		<li id="menu-item-5893" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-5893"><a href="/why-citrine/#technology">Our Technology</a></li>
	</ul>
</li>
</ul>
</li>
<li id="menu-item-5903" class="footer-hide menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-5903"><a href="#">Column</a>
<ul class="sub-menu">
	<li id="menu-item-3128" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-3128"><a href="https://citrine.io/resources/">RESOURCES</a>
	<ul class="sub-menu">
		<li id="menu-item-5370" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-5370"><a href="/resources/case-studies/">Case Studies</a></li>
		<li id="menu-item-5894" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-5894"><a href="/resources/white-papers/">White Papers</a></li>
		<li id="menu-item-5895" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-5895"><a href="/resources/blog/">Blog</a></li>
		<li id="menu-item-5379" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-5379"><a href="/resources/webinars/">Events and Webinars</a></li>
		<li id="menu-item-546" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-546"><a href="https://citrine.io/resources/research/">Research</a></li>
		<li id="menu-item-5372" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-5372"><a href="/resources/research/education-and-training/">Education and Training</a></li>
	</ul>
</li>
</ul>
</li>
<li id="menu-item-5902" class="footer-hide menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-5902"><a href="#">Column</a>
<ul class="sub-menu">
	<li id="menu-item-548" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-548"><a href="https://citrine.io/company/">COMPANY</a>
	<ul class="sub-menu">
		<li id="menu-item-5374" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-5374"><a href="/company/#about-us">About Us</a></li>
		<li id="menu-item-5375" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-5375"><a href="/company/#mission">Mission and Values</a></li>
		<li id="menu-item-5376" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-5376"><a href="/company/#team">Leadership Team</a></li>
		<li id="menu-item-5377" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-5377"><a href="/company/#investors">Investors</a></li>
		<li id="menu-item-5382" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-5382"><a href="/company/#dei">DE&#038;I at Citrine</a></li>
		<li id="menu-item-2281" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2281"><a href="https://citrine.io/careers/">Working at Citrine</a></li>
		<li id="menu-item-5381" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-5381"><a href="/company/#awards">Awards</a></li>
		<li id="menu-item-5380" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-5380"><a href="/media-post/">Newsroom</a></li>
		<li id="menu-item-6727" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6727"><a href="https://app.drata.com/trust/bdff3f99-2a59-4ae5-aa09-beccaff62fba">Trust Center</a></li>
	</ul>
</li>
</ul>
</li>
</ul></div>						</div><!-- footer_left -->

						<div class="full_width_social">
							<div class="footer_social">
        <ul class="customizer_social_links">

    
    
    
    
    
    
    
    </ul>
</div><!-- footer_social -->
						</div>

						<div class="footer-bottom">
							<div class="right_copyright">
								<div class="copyright_container footer_right">
    <p class="copyright_content">2026 &copy; <span class="copyright_name">Citrine Informatics</span>
        
                	<a class="footer-bottom-link footer-privacy-link" href="https://citrine.io/privacy-policy/" target="">Privacy</a>
                	        <a class="footer-bottom-link footer-terms-link" href="https://citrine.io/copyright/" target="">Copyright</a>
            </p>
</div><!-- footer_right -->
							</div>
						</div>
					</div>
				</div>
			</div>
		</div><!-- .container -->

	</footer><!-- #colophon -->
</div><!-- #page -->

<script type="speculationrules">
{"prefetch":[{"source":"document","where":{"and":[{"href_matches":"/*"},{"not":{"href_matches":["/wp-*.php","/wp-admin/*","/wp-content/uploads/*","/wp-content/*","/wp-content/plugins/*","/wp-content/themes/citrine/*","/wp-content/themes/inn8ly-builder/*","/*\\?(.+)"]}},{"not":{"selector_matches":"a[rel~=\"nofollow\"]"}},{"not":{"selector_matches":".no-prefetch, .no-prefetch a"}}]},"eagerness":"conservative"}]}
</script>
<div  class="ancr-group ancr-pos-top ancr-sticky"><div id="ancr-4887" class="ancr ancr-wrap ancr-lo-same_row ancr-align-center ancr-has-close-btn" data-props="{&quot;status&quot;:&quot;active&quot;,&quot;display&quot;:&quot;immediate&quot;,&quot;show_on&quot;:&quot;page_open&quot;,&quot;show_after_duration&quot;:&quot;0&quot;,&quot;show_after_scroll&quot;:&quot;0&quot;,&quot;open_animation&quot;:&quot;slide&quot;,&quot;schedule_from&quot;:&quot;&quot;,&quot;schedule_to&quot;:&quot;&quot;,&quot;position&quot;:&quot;top&quot;,&quot;sticky&quot;:&quot;yes&quot;,&quot;layout&quot;:&quot;same_row&quot;,&quot;container_width&quot;:&quot;95%&quot;,&quot;ticker_speed&quot;:&quot;20&quot;,&quot;close_btn&quot;:&quot;yes&quot;,&quot;close_animation&quot;:&quot;slide&quot;,&quot;close_content_click&quot;:&quot;no&quot;,&quot;auto_close&quot;:&quot;0&quot;,&quot;keep_closed&quot;:&quot;yes&quot;,&quot;closed_duration&quot;:&quot;1&quot;,&quot;devices&quot;:&quot;all&quot;,&quot;id&quot;:4887}"><a href="#" class="ancr-close-btn ancr-close" title="Close"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" class="ancr-close-icon" viewBox="0 0 50 50"><path fill="currentColor" d="M 9.15625 6.3125 L 6.3125 9.15625 L 22.15625 25 L 6.21875 40.96875 L 9.03125 43.78125 L 25 27.84375 L 40.9375 43.78125 L 43.78125 40.9375 L 27.84375 25 L 43.6875 9.15625 L 40.84375 6.3125 L 25 22.15625 Z"/></svg></a><div  class="ancr-container"><div class="ancr-content"><div class="ancr-inner"><h4><strong>Webinar:</strong> Building Resilience with AI-Enabled R&D</h4>
</div></div><div class="ancr-btn-wrap"><a href="https://event.on24.com/wcc/r/5434707/CED620074D23F18ED3938205FE24336C?partnerref=citrine" target="_blank" class="ancr-btn ancr-btn-primary">Register</a></div></div></div><style>
#ancr-4887{ background:#e96e01;color:#fff !important;box-shadow:0 2px 4px -2px rgba(0, 0, 0, 0.5); }
#ancr-4887 .ancr-btn-primary{ background:#fff;color:#000 !important;box-shadow:0 2px 4px -2px rgba(0, 0, 0, 0.5); }
#ancr-4887 .ancr-btn-secondary{ background:#F9DF74;color:#000 !important;box-shadow:0 2px 4px -2px rgba(0, 0, 0, 0.5); }
#ancr-4887 .ancr-container{ max-width: 95%; } 
#ancr-4887 .ancr-content a{color: #fff; }
</style></div><!--googleoff: all--><div id="cookie-law-info-bar" data-nosnippet="true"><span><div class="cli-bar-container cli-style-v2"><div class="cli-bar-message">We use cookies on our website to give you the most relevant experience by remembering your preferences and repeat visits. By clicking “Accept”, you consent to the use of ALL the cookies.</div><div class="cli-bar-btn_container"><a role="button" class="cli_settings_button" style="margin:0px 10px 0px 5px">Cookie settings</a><a role="button" id="cookie_action_close_header_reject" class="medium cli-plugin-button cli-plugin-main-button cookie_action_close_header_reject cli_action_button wt-cli-reject-btn" data-cli_action="reject">REJECT</a><a role="button" data-cli_action="accept" id="cookie_action_close_header" class="medium cli-plugin-button cli-plugin-main-button cookie_action_close_header cli_action_button wt-cli-accept-btn" style="display:inline-block">ACCEPT</a></div></div></span></div><div id="cookie-law-info-again" style="display:none" data-nosnippet="true"><span id="cookie_hdr_showagain">Manage consent</span></div><div class="cli-modal" data-nosnippet="true" id="cliSettingsPopup" tabindex="-1" role="dialog" aria-labelledby="cliSettingsPopup" aria-hidden="true">
  <div class="cli-modal-dialog" role="document">
	<div class="cli-modal-content cli-bar-popup">
		  <button type="button" class="cli-modal-close" id="cliModalClose">
			<svg class="" viewBox="0 0 24 24"><path d="M19 6.41l-1.41-1.41-5.59 5.59-5.59-5.59-1.41 1.41 5.59 5.59-5.59 5.59 1.41 1.41 5.59-5.59 5.59 5.59 1.41-1.41-5.59-5.59z"></path><path d="M0 0h24v24h-24z" fill="none"></path></svg>
			<span class="wt-cli-sr-only">Close</span>
		  </button>
		  <div class="cli-modal-body">
			<div class="cli-container-fluid cli-tab-container">
	<div class="cli-row">
		<div class="cli-col-12 cli-align-items-stretch cli-px-0">
			<div class="cli-privacy-overview">
				<h4>Privacy Overview</h4>				<div class="cli-privacy-content">
					<div class="cli-privacy-content-text">This website uses cookies to improve your experience while you navigate through the website. Out of these, the cookies that are categorized as necessary are stored on your browser as they are essential for the working of basic functionalities of the website. We also use third-party cookies that help us analyze and understand how you use this website. These cookies will be stored in your browser only with your consent. You also have the option to opt-out of these cookies. But opting out of some of these cookies may affect your browsing experience.</div>
				</div>
				<a class="cli-privacy-readmore" aria-label="Show more" role="button" data-readmore-text="Show more" data-readless-text="Show less"></a>			</div>
		</div>
		<div class="cli-col-12 cli-align-items-stretch cli-px-0 cli-tab-section-container">
												<div class="cli-tab-section">
						<div class="cli-tab-header">
							<a role="button" tabindex="0" class="cli-nav-link cli-settings-mobile" data-target="necessary" data-toggle="cli-toggle-tab">
								Necessary							</a>
																						<div class="wt-cli-necessary-checkbox">
									<input type="checkbox" class="cli-user-preference-checkbox" id="wt-cli-checkbox-necessary" data-id="checkbox-necessary" checked="checked" />
									<label class="form-check-label" for="wt-cli-checkbox-necessary">Necessary</label>
								</div>
								<span class="cli-necessary-caption">Always Enabled</span>
													</div>
						<div class="cli-tab-content">
							<div class="cli-tab-pane cli-fade" data-id="necessary">
								<div class="wt-cli-cookie-description">
									Necessary cookies are absolutely essential for the website to function properly. This category only includes cookies that ensures basic functionalities and security features of the website. These cookies do not store any personal information.								</div>
							</div>
						</div>
					</div>
																	<div class="cli-tab-section">
						<div class="cli-tab-header">
							<a role="button" tabindex="0" class="cli-nav-link cli-settings-mobile" data-target="non-necessary" data-toggle="cli-toggle-tab">
								Non-necessary							</a>
																						<div class="cli-switch">
									<input type="checkbox" id="wt-cli-checkbox-non-necessary" class="cli-user-preference-checkbox" data-id="checkbox-non-necessary" checked='checked' />
									<label for="wt-cli-checkbox-non-necessary" class="cli-slider" data-cli-enable="Enabled" data-cli-disable="Disabled"><span class="wt-cli-sr-only">Non-necessary</span></label>
								</div>
													</div>
						<div class="cli-tab-content">
							<div class="cli-tab-pane cli-fade" data-id="non-necessary">
								<div class="wt-cli-cookie-description">
									Any cookies that may not be particularly necessary for the website to function and is used specifically to collect user personal data via analytics, ads, other embedded contents are termed as non-necessary cookies. It is mandatory to procure user consent prior to running these cookies on your website.								</div>
							</div>
						</div>
					</div>
										</div>
	</div>
</div>
		  </div>
		  <div class="cli-modal-footer">
			<div class="wt-cli-element cli-container-fluid cli-tab-container">
				<div class="cli-row">
					<div class="cli-col-12 cli-align-items-stretch cli-px-0">
						<div class="cli-tab-footer wt-cli-privacy-overview-actions">
						
															<a id="wt-cli-privacy-save-btn" role="button" tabindex="0" data-cli-action="accept" class="wt-cli-privacy-btn cli_setting_save_button wt-cli-privacy-accept-btn cli-btn">SAVE &amp; ACCEPT</a>
													</div>
						
					</div>
				</div>
			</div>
		</div>
	</div>
  </div>
</div>
<div  class="cli-modal-backdrop cli-fade cli-settings-overlay"></div>
<div  class="cli-modal-backdrop cli-fade cli-popupbar-overlay"></div>
<!--googleon: all--><div  class="cta-button-contain"><a href="https://citrine.io/request-a-demo/" class="cta-button style4 red">Request a Demo</a></div><script type="text/rocketlazyloadscript">
	var relevanssi_rt_regex = /(&|\?)_(rt|rt_nonce)=(\w+)/g
	var newUrl = window.location.search.replace(relevanssi_rt_regex, '')
	history.replaceState(null, null, window.location.pathname + newUrl + window.location.hash)
</script>
<script type="text/rocketlazyloadscript" data-minify="1" id="cta-kit-script-js" data-rocket-src="https://citrine.io/wp-content/cache/min/1/wp-content/plugins/floating-button-call-to-action/assets/cta-kit.js?ver=1785874339" data-rocket-defer defer></script>
<script id="leadin-script-loader-js-js-extra">
var leadin_wordpress = {"userRole":"visitor","pageType":"home","leadinPluginVersion":"11.3.45"};
//# sourceURL=leadin-script-loader-js-js-extra
</script>
<script data-minify="1" type="text/plain" data-cli-class="cli-blocker-script" data-cli-script-type="non-necessary" data-cli-block="true" data-cli-element-position="head" id="leadin-script-loader-js-js" src="https://citrine.io/wp-content/cache/min/1/23635928.js?ver=1785874339" data-rocket-defer defer></script>
<script type="text/rocketlazyloadscript" id="rocket-browser-checker-js-after">
"use strict";var _createClass=function(){function defineProperties(target,props){for(var i=0;i<props.length;i++){var descriptor=props[i];descriptor.enumerable=descriptor.enumerable||!1,descriptor.configurable=!0,"value"in descriptor&&(descriptor.writable=!0),Object.defineProperty(target,descriptor.key,descriptor)}}return function(Constructor,protoProps,staticProps){return protoProps&&defineProperties(Constructor.prototype,protoProps),staticProps&&defineProperties(Constructor,staticProps),Constructor}}();function _classCallCheck(instance,Constructor){if(!(instance instanceof Constructor))throw new TypeError("Cannot call a class as a function")}var RocketBrowserCompatibilityChecker=function(){function RocketBrowserCompatibilityChecker(options){_classCallCheck(this,RocketBrowserCompatibilityChecker),this.passiveSupported=!1,this._checkPassiveOption(this),this.options=!!this.passiveSupported&&options}return _createClass(RocketBrowserCompatibilityChecker,[{key:"_checkPassiveOption",value:function(self){try{var options={get passive(){return!(self.passiveSupported=!0)}};window.addEventListener("test",null,options),window.removeEventListener("test",null,options)}catch(err){self.passiveSupported=!1}}},{key:"initRequestIdleCallback",value:function(){!1 in window&&(window.requestIdleCallback=function(cb){var start=Date.now();return setTimeout(function(){cb({didTimeout:!1,timeRemaining:function(){return Math.max(0,50-(Date.now()-start))}})},1)}),!1 in window&&(window.cancelIdleCallback=function(id){return clearTimeout(id)})}},{key:"isDataSaverModeOn",value:function(){return"connection"in navigator&&!0===navigator.connection.saveData}},{key:"supportsLinkPrefetch",value:function(){var elem=document.createElement("link");return elem.relList&&elem.relList.supports&&elem.relList.supports("prefetch")&&window.IntersectionObserver&&"isIntersecting"in IntersectionObserverEntry.prototype}},{key:"isSlowConnection",value:function(){return"connection"in navigator&&"effectiveType"in navigator.connection&&("2g"===navigator.connection.effectiveType||"slow-2g"===navigator.connection.effectiveType)}}]),RocketBrowserCompatibilityChecker}();
//# sourceURL=rocket-browser-checker-js-after
</script>
<script id="rocket-preload-links-js-extra">
var RocketPreloadLinksConfig = {"excludeUris":"/resources/case-studies/|/(?:.+/)?feed(?:/(?:.+/?)?)?$|/(?:.+/)?embed/|/(index.php/)?(.*)wp-json(/.*|$)|/refer/|/go/|/recommend/|/recommends/","usesTrailingSlash":"1","imageExt":"jpg|jpeg|gif|png|tiff|bmp|webp|avif|pdf|doc|docx|xls|xlsx|php","fileExt":"jpg|jpeg|gif|png|tiff|bmp|webp|avif|pdf|doc|docx|xls|xlsx|php|html|htm","siteUrl":"https://citrine.io","onHoverDelay":"100","rateThrottle":"3"};
//# sourceURL=rocket-preload-links-js-extra
</script>
<script type="text/rocketlazyloadscript" id="rocket-preload-links-js-after">
(function() {
"use strict";var r="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},e=function(){function i(e,t){for(var n=0;n<t.length;n++){var i=t[n];i.enumerable=i.enumerable||!1,i.configurable=!0,"value"in i&&(i.writable=!0),Object.defineProperty(e,i.key,i)}}return function(e,t,n){return t&&i(e.prototype,t),n&&i(e,n),e}}();function i(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}var t=function(){function n(e,t){i(this,n),this.browser=e,this.config=t,this.options=this.browser.options,this.prefetched=new Set,this.eventTime=null,this.threshold=1111,this.numOnHover=0}return e(n,[{key:"init",value:function(){!this.browser.supportsLinkPrefetch()||this.browser.isDataSaverModeOn()||this.browser.isSlowConnection()||(this.regex={excludeUris:RegExp(this.config.excludeUris,"i"),images:RegExp(".("+this.config.imageExt+")$","i"),fileExt:RegExp(".("+this.config.fileExt+")$","i")},this._initListeners(this))}},{key:"_initListeners",value:function(e){-1<this.config.onHoverDelay&&document.addEventListener("mouseover",e.listener.bind(e),e.listenerOptions),document.addEventListener("mousedown",e.listener.bind(e),e.listenerOptions),document.addEventListener("touchstart",e.listener.bind(e),e.listenerOptions)}},{key:"listener",value:function(e){var t=e.target.closest("a"),n=this._prepareUrl(t);if(null!==n)switch(e.type){case"mousedown":case"touchstart":this._addPrefetchLink(n);break;case"mouseover":this._earlyPrefetch(t,n,"mouseout")}}},{key:"_earlyPrefetch",value:function(t,e,n){var i=this,r=setTimeout(function(){if(r=null,0===i.numOnHover)setTimeout(function(){return i.numOnHover=0},1e3);else if(i.numOnHover>i.config.rateThrottle)return;i.numOnHover++,i._addPrefetchLink(e)},this.config.onHoverDelay);t.addEventListener(n,function e(){t.removeEventListener(n,e,{passive:!0}),null!==r&&(clearTimeout(r),r=null)},{passive:!0})}},{key:"_addPrefetchLink",value:function(i){return this.prefetched.add(i.href),new Promise(function(e,t){var n=document.createElement("link");n.rel="prefetch",n.href=i.href,n.onload=e,n.onerror=t,document.head.appendChild(n)}).catch(function(){})}},{key:"_prepareUrl",value:function(e){if(null===e||"object"!==(void 0===e?"undefined":r(e))||!1 in e||-1===["http:","https:"].indexOf(e.protocol))return null;var t=e.href.substring(0,this.config.siteUrl.length),n=this._getPathname(e.href,t),i={original:e.href,protocol:e.protocol,origin:t,pathname:n,href:t+n};return this._isLinkOk(i)?i:null}},{key:"_getPathname",value:function(e,t){var n=t?e.substring(this.config.siteUrl.length):e;return n.startsWith("/")||(n="/"+n),this._shouldAddTrailingSlash(n)?n+"/":n}},{key:"_shouldAddTrailingSlash",value:function(e){return this.config.usesTrailingSlash&&!e.endsWith("/")&&!this.regex.fileExt.test(e)}},{key:"_isLinkOk",value:function(e){return null!==e&&"object"===(void 0===e?"undefined":r(e))&&(!this.prefetched.has(e.href)&&e.origin===this.config.siteUrl&&-1===e.href.indexOf("?")&&-1===e.href.indexOf("#")&&!this.regex.excludeUris.test(e.href)&&!this.regex.images.test(e.href))}}],[{key:"run",value:function(){"undefined"!=typeof RocketPreloadLinksConfig&&new n(new RocketBrowserCompatibilityChecker({capture:!0,passive:!0}),RocketPreloadLinksConfig).init()}}]),n}();t.run();
}());

//# sourceURL=rocket-preload-links-js-after
</script>
<script id="rocket_lazyload_css-js-extra">
var rocket_lazyload_css_data = {"threshold":"300"};
//# sourceURL=rocket_lazyload_css-js-extra
</script>
<script id="rocket_lazyload_css-js-after">
!function o(n,a,c){function l(t,e){if(!a[t]){if(!n[t]){var r="function"==typeof require&&require;if(!e&&r)return r(t,!0);if(u)return u(t,!0);throw(e=new Error("Cannot find module '"+t+"'")).code="MODULE_NOT_FOUND",e}r=a[t]={exports:{}},n[t][0].call(r.exports,function(e){return l(n[t][1][e]||e)},r,r.exports,o,n,a,c)}return a[t].exports}for(var u="function"==typeof require&&require,e=0;e<c.length;e++)l(c[e]);return l}({1:[function(e,t,r){{let r="undefined"==typeof rocket_pairs?[]:rocket_pairs,o=(("undefined"==typeof rocket_excluded_pairs?[]:rocket_excluded_pairs).map(t=>{var e=t.selector;document.querySelectorAll(e).forEach(e=>{e.setAttribute("data-rocket-lazy-bg-"+t.hash,"excluded")})}),document.querySelector("#wpr-lazyload-bg-container"));var a=rocket_lazyload_css_data.threshold||300;let n=new IntersectionObserver(e=>{e.forEach(t=>{t.isIntersecting&&r.filter(e=>t.target.matches(e.selector)).map(t=>{var e;t&&((e=document.createElement("style")).textContent=t.style,o.insertAdjacentElement("afterend",e),t.elements.forEach(e=>{n.unobserve(e),e.setAttribute("data-rocket-lazy-bg-"+t.hash,"loaded")}))})})},{rootMargin:a+"px"});function c(){0<(0<arguments.length&&void 0!==arguments[0]?arguments[0]:[]).length&&r.forEach(t=>{try{document.querySelectorAll(t.selector).forEach(e=>{"loaded"!==e.getAttribute("data-rocket-lazy-bg-"+t.hash)&&"excluded"!==e.getAttribute("data-rocket-lazy-bg-"+t.hash)&&(n.observe(e),(t.elements||=[]).push(e))})}catch(e){console.error(e)}})}c(),(()=>{let r=window.MutationObserver;return function(e,t){if(e&&1===e.nodeType)return(t=new r(t)).observe(e,{attributes:!0,childList:!0,subtree:!0}),t}})()(document.querySelector("body"),c)}},{}]},{},[1]);
//# sourceURL=rocket_lazyload_css-js-after
</script>
<script type="text/rocketlazyloadscript" id="child-js-js" data-rocket-src="https://citrine.io/wp-content/themes/citrine/js/built.min.js" data-rocket-defer defer></script>
<script type="text/rocketlazyloadscript" id="dd-slick-js" data-rocket-src="https://citrine.io/wp-content/themes/citrine/js/vendor/jquery.dd-slick.min.js" data-rocket-defer defer></script>
<script type="text/rocketlazyloadscript" id="tooltipster-js-js" data-rocket-src="https://citrine.io/wp-content/themes/citrine/js/vendor/tooltipster.bundle.min.js" data-rocket-defer defer></script>
<script type="text/rocketlazyloadscript" data-minify="1" id="fancybox-js-js" data-rocket-src="https://citrine.io/wp-content/cache/min/1/wp-content/themes/inn8ly-builder/js/vendor/fancyBox/jquery.fancybox.js?ver=1785874339" data-rocket-defer defer></script>
<script type="text/rocketlazyloadscript" data-minify="1" id="red8-navigation-js" data-rocket-src="https://citrine.io/wp-content/cache/min/1/wp-content/themes/inn8ly-builder/js/navigation.js?ver=1785874339" data-rocket-defer defer></script>
<script type="text/rocketlazyloadscript" data-minify="1" id="red8-skip-link-focus-fix-js" data-rocket-src="https://citrine.io/wp-content/cache/min/1/wp-content/themes/inn8ly-builder/js/skip-link-focus-fix.js?ver=1785874339" data-rocket-defer defer></script>
<script type="text/rocketlazyloadscript" id="red8-js-js" data-rocket-src="https://citrine.io/wp-content/themes/inn8ly-builder/js/built.min.js?ver=20180222" data-rocket-defer defer></script>
<script type="text/rocketlazyloadscript" id="swiper-js-js" data-rocket-src="https://citrine.io/wp-content/themes/inn8ly-builder/js/swiper/swiper.min.js" data-rocket-defer defer></script>
<script type="text/rocketlazyloadscript" id="slick-js-js" data-rocket-src="https://citrine.io/wp-content/themes/inn8ly-builder/js/vendor/slick.min.js?ver=7.0.4" data-rocket-defer defer></script>
<script type="text/rocketlazyloadscript" id="featherlight-js-js" data-rocket-src="https://citrine.io/wp-content/themes/inn8ly-builder/js/vendor/featherlight.min.js?ver=7.0.4" data-rocket-defer defer></script>
<script type="text/rocketlazyloadscript" data-minify="1" id="mmenu-js-js" data-rocket-src="https://citrine.io/wp-content/cache/min/1/wp-content/themes/inn8ly-builder/js/vendor/mmenu/js/jquery.mmenu.min.all.js?ver=1785874339" data-rocket-defer defer></script>
<script type="text/rocketlazyloadscript" id="waypoints-js" data-rocket-src="https://citrine.io/wp-content/themes/inn8ly-builder/js/vendor/jquery.waypoints.min.js?ver=7.0.4" data-rocket-defer defer></script>
<script type="text/rocketlazyloadscript" id="fancybox-purify-js" data-rocket-src="https://citrine.io/wp-content/plugins/easy-fancybox/vendor/purify.min.js?ver=1787781226" data-rocket-defer defer></script>
<script id="jquery-fancybox-js-extra">window.addEventListener('DOMContentLoaded', function() {
var efb_i18n = {"close":"Close","next":"Next","prev":"Previous","startSlideshow":"Start slideshow","toggleSize":"Toggle size"};
//# sourceURL=jquery-fancybox-js-extra
});</script>
<script type="text/rocketlazyloadscript" data-minify="1" id="jquery-fancybox-js" data-rocket-src="https://citrine.io/wp-content/cache/min/1/wp-content/plugins/easy-fancybox/fancybox/1.5.4/jquery.fancybox.js?ver=1785874339" data-rocket-defer defer></script>
<script type="text/rocketlazyloadscript" id="jquery-fancybox-js-after">window.addEventListener('DOMContentLoaded', function() {
var fb_timeout, fb_opts={'autoScale':true,'showCloseButton':true,'margin':20,'pixelRatio':'false','centerOnScroll':false,'enableEscapeButton':true,'overlayShow':true,'hideOnOverlayClick':true,'overlayColor':'#000000','overlayOpacity':.8,'minVpHeight':320,'disableCoreLightbox':'true','enableBlockControls':'true','fancybox_openBlockControls':'true' };
if(typeof easy_fancybox_handler==='undefined'){
var easy_fancybox_handler=function(){
jQuery([".nolightbox","a.wp-block-fileesc_html__button","a.pin-it-button","a[href*='pinterest.com\/pin\/create']","a[href*='facebook.com\/share']","a[href*='twitter.com\/share']"].join(',')).addClass('nofancybox');
jQuery('a.fancybox-close').on('click',function(e){e.preventDefault();jQuery.fancybox.close()});
/* IMG */
						var unlinkedImageBlocks=jQuery(".wp-block-image > img:not(.nofancybox,figure.nofancybox>img)");
						unlinkedImageBlocks.wrap(function() {
							var href = jQuery( this ).attr( "src" );
							return "<a href='" + href + "'></a>";
						});
var fb_IMG_select=jQuery('a[href*=".jpg" i]:not(.nofancybox,li.nofancybox>a,figure.nofancybox>a),area[href*=".jpg" i]:not(.nofancybox),a[href*=".jpeg" i]:not(.nofancybox,li.nofancybox>a,figure.nofancybox>a),area[href*=".jpeg" i]:not(.nofancybox),a[href*=".png" i]:not(.nofancybox,li.nofancybox>a,figure.nofancybox>a),area[href*=".png" i]:not(.nofancybox),a[href*=".webp" i]:not(.nofancybox,li.nofancybox>a,figure.nofancybox>a),area[href*=".webp" i]:not(.nofancybox)');
fb_IMG_select.addClass('fancybox image');
var fb_IMG_sections=jQuery('.gallery,.wp-block-gallery,.tiled-gallery,.wp-block-jetpack-tiled-gallery,.ngg-galleryoverview,.ngg-imagebrowser,.nextgen_pro_blog_gallery,.nextgen_pro_film,.nextgen_pro_horizontal_filmstrip,.ngg-pro-masonry-wrapper,.ngg-pro-mosaic-container,.nextgen_pro_sidescroll,.nextgen_pro_slideshow,.nextgen_pro_thumbnail_grid,.tiled-gallery');
fb_IMG_sections.each(function(){jQuery(this).find(fb_IMG_select).attr('rel','gallery-'+fb_IMG_sections.index(this));});
jQuery('a.fancybox,area.fancybox,.fancybox>a').each(function(){jQuery(this).fancybox(jQuery.extend(true,{},fb_opts,{'transition':'elastic','transitionIn':'none','transitionOut':'none','opacity':false,'hideOnContentClick':false,'titleShow':true,'titlePosition':'over','titleFromAlt':true,'showNavArrows':true,'enableKeyboardNav':true,'cyclic':false,'mouseWheel':'false'}))});
/* Vimeo */
jQuery('a[href*="vimeo.com/" i],area[href*="vimeo.com/" i]' ).filter(function(){return this.href.match(/\/(?:[0-9]+|video\/)/);}).not('.nofancybox,li.nofancybox>a').addClass('fancybox-vimeo');
jQuery('a.fancybox-vimeo,area.fancybox-vimeo,.fancybox-vimeo>a').each(function(){jQuery(this).fancybox(jQuery.extend(true,{},fb_opts,{'type':'iframe','width':900,'height':500,'keepRatio':1,'aspectRatio':1,'titleShow':false,'titlePosition':'float','titleFromAlt':true,'onStart':function(a,i,o){var splitOn=a[i].href.indexOf("?");var urlParms=(splitOn>-1)?a[i].href.substring(splitOn):"";o.allowfullscreen=(urlParms.indexOf("fullscreen=0")>-1)?false:true;o.href=a[i].href.replace(/https?:\/\/(?:www\.)?vimeo\.com\/([0-9]+)\??(.*)/gi,"https://player.vimeo.com/video/$1?$2&autoplay=1");}}))});
};};
jQuery(easy_fancybox_handler);jQuery(document).on('post-load',easy_fancybox_handler);

//# sourceURL=jquery-fancybox-js-after
});</script>
<script id="tc-caf-frontend-scripts-pro-js-extra">
var tc_caf_ajax = {"ajax_url":"https://citrine.io/wp-admin/admin-ajax.php","nonce":"3a0d0c465a","plugin_path":"https://citrine.io/wp-content/plugins/category-ajax-filter-pro/"};
//# sourceURL=tc-caf-frontend-scripts-pro-js-extra
</script>
<script type="text/rocketlazyloadscript" data-minify="1" id="tc-caf-frontend-scripts-pro-js" data-rocket-src="https://citrine.io/wp-content/cache/min/1/wp-content/plugins/category-ajax-filter-pro/assets/js/script.js?ver=1785874339" data-rocket-defer defer></script>
<script type="text/rocketlazyloadscript" id="hoverIntent-js" data-rocket-src="https://citrine.io/wp-includes/js/hoverIntent.min.js?ver=1.10.2" data-rocket-defer defer></script>
<script type="text/rocketlazyloadscript" data-minify="1" id="megamenu-js" data-rocket-src="https://citrine.io/wp-content/cache/min/1/wp-content/plugins/megamenu/js/maxmegamenu.js?ver=1785874339" data-rocket-defer defer></script>
<script type="text/rocketlazyloadscript" data-minify="1" id="announcer-js-js" data-rocket-src="https://citrine.io/wp-content/cache/min/1/wp-content/plugins/announcer/public/js/script.js?ver=1785874339" data-rocket-defer defer></script>
			<script type="text/rocketlazyloadscript" data-rocket-type="text/javascript" id="wpsp-script-frontend"></script>
			<script>window.lazyLoadOptions=[{elements_selector:"img[data-lazy-src],.rocket-lazyload,iframe[data-lazy-src]",data_src:"lazy-src",data_srcset:"lazy-srcset",data_sizes:"lazy-sizes",class_loading:"lazyloading",class_loaded:"lazyloaded",threshold:300,callback_loaded:function(element){if(element.tagName==="IFRAME"&&element.dataset.rocketLazyload=="fitvidscompatible"){if(element.classList.contains("lazyloaded")){if(typeof window.jQuery!="undefined"){if(jQuery.fn.fitVids){jQuery(element).parent().fitVids()}}}}}},{elements_selector:".rocket-lazyload",data_src:"lazy-src",data_srcset:"lazy-srcset",data_sizes:"lazy-sizes",class_loading:"lazyloading",class_loaded:"lazyloaded",threshold:300,}];window.addEventListener('LazyLoad::Initialized',function(e){var lazyLoadInstance=e.detail.instance;if(window.MutationObserver){var observer=new MutationObserver(function(mutations){var image_count=0;var iframe_count=0;var rocketlazy_count=0;mutations.forEach(function(mutation){for(var i=0;i<mutation.addedNodes.length;i++){if(typeof mutation.addedNodes[i].getElementsByTagName!=='function'){continue}
if(typeof mutation.addedNodes[i].getElementsByClassName!=='function'){continue}
images=mutation.addedNodes[i].getElementsByTagName('img');is_image=mutation.addedNodes[i].tagName=="IMG";iframes=mutation.addedNodes[i].getElementsByTagName('iframe');is_iframe=mutation.addedNodes[i].tagName=="IFRAME";rocket_lazy=mutation.addedNodes[i].getElementsByClassName('rocket-lazyload');image_count+=images.length;iframe_count+=iframes.length;rocketlazy_count+=rocket_lazy.length;if(is_image){image_count+=1}
if(is_iframe){iframe_count+=1}}});if(image_count>0||iframe_count>0||rocketlazy_count>0){lazyLoadInstance.update()}});var b=document.getElementsByTagName("body")[0];var config={childList:!0,subtree:!0};observer.observe(b,config)}},!1)</script><script data-no-minify="1" async src="https://citrine.io/wp-content/plugins/wp-rocket/assets/js/lazyload/17.8.3/lazyload.min.js"></script><script>function lazyLoadThumb(e,alt,l){var t='<img data-lazy-src="https://i.ytimg.com/vi/ID/hqdefault.jpg" alt="" width="480" height="360"><noscript><img src="https://i.ytimg.com/vi/ID/hqdefault.jpg" alt="" width="480" height="360"></noscript>',a='<button class="play" aria-label="Play Youtube video"></button>';if(l){t=t.replace('data-lazy-','');t=t.replace('loading="lazy"','');t=t.replace(/<noscript>.*?<\/noscript>/g,'');}t=t.replace('alt=""','alt="'+alt+'"');return t.replace("ID",e)+a}function lazyLoadYoutubeIframe(){var e=document.createElement("iframe"),t="ID?autoplay=1";t+=0===this.parentNode.dataset.query.length?"":"&"+this.parentNode.dataset.query;e.setAttribute("src",t.replace("ID",this.parentNode.dataset.src)),e.setAttribute("frameborder","0"),e.setAttribute("allowfullscreen","1"),e.setAttribute("allow","accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"),this.parentNode.parentNode.replaceChild(e,this.parentNode)}document.addEventListener("DOMContentLoaded",function(){var exclusions=["\/wp-content\/uploads\/2021\/11\/hero-hexagons.png","\/wp-content\/uploads\/2018\/07\/Citrine-informatics-logo.svg"];var e,t,p,u,l,a=document.getElementsByClassName("rll-youtube-player");for(t=0;t<a.length;t++)(e=document.createElement("div")),(u='https://i.ytimg.com/vi/ID/hqdefault.jpg'),(u=u.replace('ID',a[t].dataset.id)),(l=exclusions.some(exclusion=>u.includes(exclusion))),e.setAttribute("data-id",a[t].dataset.id),e.setAttribute("data-query",a[t].dataset.query),e.setAttribute("data-src",a[t].dataset.src),(e.innerHTML=lazyLoadThumb(a[t].dataset.id,a[t].dataset.alt,l)),a[t].appendChild(e),(p=e.querySelector(".play")),(p.onclick=lazyLoadYoutubeIframe)});</script>
<script>"use strict";function wprRemoveCPCSS(){var preload_stylesheets=document.querySelectorAll('link[data-rocket-async="style"][rel="preload"]');if(preload_stylesheets&&0<preload_stylesheets.length)for(var stylesheet_index=0;stylesheet_index<preload_stylesheets.length;stylesheet_index++){var media=preload_stylesheets[stylesheet_index].getAttribute("media")||"all";if(window.matchMedia(media).matches)return void setTimeout(wprRemoveCPCSS,200)}var elem=document.getElementById("rocket-critical-css");elem&&"remove"in elem&&elem.remove()}window.addEventListener?window.addEventListener("load",wprRemoveCPCSS):window.attachEvent&&window.attachEvent("onload",wprRemoveCPCSS);</script><noscript><link data-minify="1" rel='stylesheet' id='announcer-css-css' href='https://citrine.io/wp-content/cache/min/1/wp-content/plugins/announcer/public/css/style.css?ver=1785874338' media='all' /><link data-minify="1" rel='stylesheet' id='cookie-law-info-css' href='https://citrine.io/wp-content/cache/min/1/wp-content/plugins/cookie-law-info/legacy/public/css/cookie-law-info-public.css?ver=1785874338' media='all' /><link data-minify="1" rel='stylesheet' id='cookie-law-info-gdpr-css' href='https://citrine.io/wp-content/cache/min/1/wp-content/plugins/cookie-law-info/legacy/public/css/cookie-law-info-gdpr.css?ver=1785874338' media='all' /><link data-minify="1" rel='stylesheet' id='cta-kit-styles-css' href='https://citrine.io/wp-content/cache/min/1/wp-content/plugins/floating-button-call-to-action/assets/cta-kit.css?ver=1785874338' media='all' /><link data-minify="1" rel='stylesheet' id='dashicons-css' href='https://citrine.io/wp-content/cache/min/1/wp-includes/css/dashicons.min.css?ver=1785874338' media='all' /><link data-minify="1" rel='stylesheet' id='megamenu-css' href='https://citrine.io/wp-content/cache/min/1/wp-content/uploads/maxmegamenu/style.css?ver=1785874338' media='all' /><link data-minify="1" rel='stylesheet' id='red8-style-css' href='https://citrine.io/wp-content/cache/background-css/1/citrine.io/wp-content/cache/min/1/wp-content/themes/inn8ly-builder/style.css?ver=1785874338&wpr_t=1787766826' media='all' /><link data-minify="1" rel='stylesheet' id='child-style-css' href='https://citrine.io/wp-content/cache/background-css/1/citrine.io/wp-content/cache/min/1/wp-content/themes/citrine/style.css?ver=1785874338&wpr_t=1787766826' media='all' /><link rel='stylesheet' id='tooltipster-css-css' href='https://citrine.io/wp-content/themes/citrine/js/vendor/tooltipster.bundle.min.css?ver=7.0.4' media='all' /><link rel='stylesheet' id='tooltipster-shadow-css' href='https://citrine.io/wp-content/themes/citrine/js/vendor/tooltipster-sideTip-shadow.min.css?ver=7.0.4' media='all' /><link data-minify="1" rel='stylesheet' id='fancybox-css-css' href='https://citrine.io/wp-content/cache/background-css/1/citrine.io/wp-content/cache/min/1/wp-content/themes/inn8ly-builder/js/vendor/fancyBox/jquery.fancybox.css?ver=1785874338&wpr_t=1787766826' media='all' /><link rel='stylesheet' id='swiper-css' href='https://citrine.io/wp-content/themes/inn8ly-builder/css/swiper.min.css?ver=7.0.4' media='all' /><link data-minify="1" rel='stylesheet' id='slick-css-css' href='https://citrine.io/wp-content/cache/min/1/wp-content/themes/inn8ly-builder/css/slick.css?ver=1785874338' media='all' /><link data-minify="1" rel='stylesheet' id='slick-theme-css-css' href='https://citrine.io/wp-content/cache/background-css/1/citrine.io/wp-content/cache/min/1/wp-content/themes/inn8ly-builder/css/slick-theme.css?ver=1785874338&wpr_t=1787766826' media='all' /><link data-minify="1" rel='stylesheet' id='mmenu-css' href='https://citrine.io/wp-content/cache/min/1/wp-content/themes/inn8ly-builder/js/vendor/mmenu/css/jquery.mmenu.all.css?ver=1785874338' media='all' /><link rel='stylesheet' id='featherlight-css-css' href='https://citrine.io/wp-content/themes/inn8ly-builder/js/vendor/featherlight.min.css?ver=7.0.4' media='all' /><link data-minify="1" rel='stylesheet' id='fancybox-css' href='https://citrine.io/wp-content/cache/min/1/wp-content/plugins/easy-fancybox/fancybox/1.5.4/jquery.fancybox.css?ver=1785874338' media='screen' /><link data-minify="1" rel='stylesheet' id='tc-caf-pro-common-style-css' href='https://citrine.io/wp-content/cache/min/1/wp-content/plugins/category-ajax-filter-pro/assets/css/common/common.css?ver=1785874338' media='all' /></noscript><script>(function(){function c(){var b=a.contentDocument||(a.contentWindow&&a.contentWindow.document);if(b){var d=b.createElement('script');d.innerHTML="window.__CF$cv$params={r:'a316355eb928a5d9',t:'MTc4Nzc4MjY2Ng=='};var a=document.createElement('script');a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";b.getElementsByTagName('head')[0].appendChild(d)}}if(document.body){var a=document.createElement('iframe');a.height=1;a.width=1;a.style.position='absolute';a.style.top=0;a.style.left=0;a.style.border='none';a.style.visibility='hidden';document.body.appendChild(a);if('loading'!==document.readyState)c();else if(window.addEventListener)document.addEventListener('DOMContentLoaded',c);else{var e=document.onreadystatechange||function(){};document.onreadystatechange=function(b){e(b);'loading'!==document.readyState&&(document.onreadystatechange=e,c())}}}})();</script></body>
</html>

<!-- This website is like a Rocket, isn't it? Performance optimized by WP Rocket. Learn more: https://wp-rocket.me -->