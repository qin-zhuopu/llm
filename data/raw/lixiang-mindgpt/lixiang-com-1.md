# Source: https://www.lixiang.com

> 抓取日期: 2026-08-26

---

<!DOCTYPE html>
<html lang="zh-CN">
    <head>
        <meta charset="UTF-8" />
<title>理想汽车丨理想，给车和家赋予生命。</title>
<meta
    name="viewport"
    content="width=device-width,initial-scale=1.0,maximum-scale=1.0, user-scalable=no, viewport-fit=cover"
/>
<meta name="format-detection" content="telephone=no" />
<meta http-equiv="X-UA-Compatible" content="ie=edge" />
<meta name="renderer" content="webkit" />

<!-- 360搜索智能摘要 -->
<meta property="og:type" content="news" />
<meta property="og:title" content="理想汽车丨理想，给车和家赋予生命。" />
<meta
    property="og:description"
    content="理想汽车致力于成为全球领先的具身智能企业，产品布局包含智能汽车、智能眼镜、空间机器人和人形机器人，提供家一样的体验、具身智能的主动服务。"
/>
<meta
    property="og:image"
    content="https://p.ampmake.com/fed/image/png/d4e456eef7dbf961f28cba4f4c42b7a2.png"
/>

<meta
    name="keywords"
    content="理想汽车，理想，给车和家赋予生命。具身智能旗舰SUV，李想，车和家，理想5C，自研马赫芯片，智能电动车，增程电动车，混动SUV，理想社区，理想口碑，理想汽车怎么样，理想L9怎么样，理想MEGA怎么样，理想i6怎么样，理想L9，理想MEGA，理想L6，理想i6，理想i8"
/>
<meta
    name="description"
    content="理想汽车致力于成为全球领先的具身智能企业，产品布局包含智能汽车、智能眼镜、空间机器人和人形机器人，提供家一样的体验、具身智能的主动服务。"
/>
<meta name="sogou_site_verification" content="FYa4KKq8om" />

<meta name="mobile-web-app-capable" content="yes" />
<meta name="apple-mobile-web-app-status-bar-style" content="black" />
<meta
    name="apple-mobile-web-app-title"
    content="理想汽车丨理想，给车和家赋予生命。"
/>

<link
    rel="icon"
    href="https://www.lixiang.com/favicon.ico"
    type="image/vnd.microsoft.icon"
/>

<link
    rel="apple-touch-icon"
    href="https://s.ampmake.com/fed/m01/lixiang3/favicon.ico"
/>
<link
    href="https://www.lixiang.com/favicon.ico"
    rel="shortcut icon"
    type="image/x-icon"
/>
<link
    href="https://www.lixiang.com/favicon.ico"
    rel="icon"
    type="image/x-icon"
/>

<!--[if (lt IE 11) & (!IEMobile)]>
    <script>
        window.location = '/upgrade.html';
    </script>
<![endif]-->
<style>
    .fn-hide {
        display: none;
    }
</style>
<script>
    window.webViewRequestSend = false;
    var agent = navigator.userAgent;
    var html = document.documentElement;

    // 是否为低版本IE
    if (agent.indexOf('MSIE') > -1 && agent.indexOf('Trident') > -1) {
        if (window.ActiveXObject) window.location = '/upgrade.html';
    }

    // 是否为ie或edge浏览器
    var isIE = window.ActiveXObject || 'ActiveXObject' in window;
    var isEdge = agent.indexOf('Edge') > -1;

    if (isIE || isEdge) {
        html.classList.add('isms');
    }

    // 获取cookie
    function getCookie(name) {
        if (document.cookie.length > 0) {
            var start = document.cookie.indexOf(name + '=');
            if (start !== -1) {
                start = start + name.length + 1;
                var end = document.cookie.indexOf(';', start);
                if (end === -1) end = document.cookie.length;
                return unescape(document.cookie.substring(start, end));
            }
        }
        return '';
    }

    // 设置Cookie
    function setCookie(cname, cvalue, exdays) {
        var d = new Date();
        d.setTime(d.getTime() + exdays * 24 * 60 * 60 * 1000);
        var expires = exdays ? 'expires=' + d.toUTCString() : ''; // exdays传0 设置为临时session cookie
        if (location.host.indexOf('.lixiang.com') >= 0) {
            document.cookie =
                cname +
                '=' +
                cvalue +
                '; ' +
                expires +
                '; domain=.lixiang.com; path=/';
        } else {
            document.cookie =
                cname + '=' + cvalue + '; ' + expires + '; path=/';
        }
    }

    // 百度品专
    if (location.search.indexOf('from=baidu') >= 0) {
        var fromBaidu = getCookie('fromBaidu');
        if (!fromBaidu) {
            setCookie('fromBaidu', 1, 0);
        }
    }

    // 是否为理想汽车App客户端
    var isapp = /isapp=1/.test(document.cookie);
    if (isapp) {
        html.classList.add('isapp');
        // 安卓状态栏高度
        var statusbarHeight = getCookie('statusbarHeight');
        if (statusbarHeight) {
            html.classList.add('isandroid');
            var style = document.createElement('style');
            statusbarHeight = Number(statusbarHeight);
            statusbarHeight = Number.isNaN(statusbarHeight)
                ? 20
                : statusbarHeight;
            style.innerHTML =
                ':root { --statusbarHeight: ' + statusbarHeight + 'px; }';
            document.head.appendChild(style);
        }
    }

    // 是否为第三方小程序
    var isWxapp = /miniProgram/i.test(agent);
    var isBdapp = /swan\//.test(agent);
    var isDyapp = /dyapp=1/.test(document.cookie);
    var isThirdapp = isWxapp || isBdapp || isDyapp;
    if (isThirdapp) {
        html.classList.add('isthirdapp');
        document.title = document.title.replace(
            '理想汽车丨理想，给车和家赋予生命。丨',
            ''
        );
    }

    // 是否为百度小程序
    var isbaiduminapp = /baiduMinApp=1/i.test(document.cookie);
    if (isbaiduminapp) {
        html.classList.add('isbaiduminapp');
    }

    // webapp全屏
    if ('standalone' in window.navigator && window.navigator.standalone) {
        var noddy,
            remotes = false;
        document.addEventListener(
            'click',
            function(event) {
                noddy = event.target;
                if (noddy) {
                    while (noddy.nodeName !== 'A' && noddy.nodeName !== 'HTML')
                        noddy = noddy.parentNode;
                    if (
                        'href' in noddy &&
                        noddy.href.indexOf('http') !== -1 &&
                        (noddy.href.indexOf(document.location.host) !== -1 ||
                            remotes)
                    ) {
                        event.preventDefault();
                        document.location.href = noddy.href;
                    }
                }
            },
            false
        );
    }
</script>
<script>
    var globalData = {"isServerEnv":true,"apiPrefix":"https://api-web.lixiang.com","env":"prod"};
</script>


<link href="https://p.ampmake.com/fed/m01/chunk-2608/css/4842.c6a71dba.css" rel="stylesheet" />
<link href="https://p.ampmake.com/fed/m01/chunk-2608/css/9259.c1bb4082.css" rel="stylesheet" />
<link href="https://p.ampmake.com/fed/m01/chunk-2608/css/4370.d9ab91ed.css" rel="stylesheet" />
<link href="https://p.ampmake.com/fed/m01/chunk-2608/css/home.9f32af69.css" rel="stylesheet" />
<!-- 顶象无感验证SDK -->
<script>
    (function() {
        const dxUrl =
            'https://p.ampmake.com/fed/text/javascript/86624a0b0bd9daf1ad5e38fc352e23af.js';
        !(function() {
            var head = document.getElementsByTagName('head')[0];
            var script = document.createElement('script');
            script.async = true;
            script.type = 'text/javascript';
            script.src = dxUrl;
            head.appendChild(script);
        })();
    })();
</script>

    </head>
    <body class="lx-font">
        <img
            src="https://p.ampmake.com/fed/image/png/d4e456eef7dbf961f28cba4f4c42b7a2.png"
            alt="理想"
            style="display: none;"
        />
        <div id="chj-header">
    <header style="opacity: 0">
        <div class="pcHeader-inner">
            <div
                class="pcHeader-aside pcHeader-logo"
                lxtrack-event="header_logo"
            >
                <a href="/" class="header-logo-image"></a>
            </div>
            <ul class="pcHeader-menu loginHide">
                <li
                    lxtrack-event="click_5dx170BH37"
                    class="key0click_5dx170BH37"
                >
                    <a href="/L7">理想L7</a>
                </li>
                <li
                    lxtrack-event="click_w4i57365i7"
                    class="key1click_w4i57365i7"
                >
                    <a href="/L8">理想L8</a>
                </li>
                <li
                    lxtrack-event="c_default_2Ks229A7pb"
                    class="key2c_default_2Ks229A7pb"
                >
                    <a href="/L9">理想L9</a>
                </li>
                <li
                    lxtrack-event="c_default_2Ks229A7pb"
                    class="key2c_default_2Ks229A7pb"
                >
                    <a href="/mega">理想MEGA</a>
                </li>
                <li
                    lxtrack-event="c_default_Q5226302Jm"
                    class="key5c_default_Q5226302Jm"
                >
                    <a href="/support/store/findus">门店</a>
                </li>
                <li
                    lxtrack-event="c_default_2HqxlMSUbx"
                    class="key6c_default_2HqxlMSUbx"
                >
                    <a href="/community/list">社区</a>
                </li>
                <li
                    lxtrack-event="c_default_3938vT40fk"
                    class="key7c_default_3938vT40fk"
                >
                    <a href="/koubei/list">口碑</a>
                </li>
                <li
                    lxtrack-event="c_default_s5uk6HhR7S"
                    class="key8c_default_s5uk6HhR7S"
                >
                    <div class="pcHeader-submenu">
                        <span
                            >关于我们<i
                                class="lxiconfont lxiconfont-arrowdown-small"
                            ></i
                        ></span>
                        <ul class="pcHeader-submenu-list">
                            <li lxtrack-event="c_default_8vb9F7Z5r8" class="">
                                <a href="/about.html">理想汽车</a>
                            </li>
                            <li lxtrack-event="c_default_26x5T09sv4" class="">
                                <a href="/employ.html">加入我们</a>
                            </li>
                            <li lxtrack-event="c_default_d4d1d74g55" class="">
                                <a href="/news.html">媒体中心</a>
                            </li>
                            <li lxtrack-event="c_default_H5K06sQ709" class="">
                                <a href="/help.html">帮助中心</a>
                            </li>
                            <li lxtrack-event="c_default_2i4MH33VS6" class="">
                                <a href="https://ir.lixiang.com/">投资者关系</a>
                            </li>
                        </ul>
                    </div>
                </li>
            </ul>
            <div class="pcHeader-aside loginHide">
                <div
                    class="pcHeader-drive"
                    lxtrack-event="c_default_F3P2f0gBr2"
                >
                    <a href="/drive/shop.html">预约体验</a>
                </div>
                <div class="pcHeader-login" lxtrack-event="header_login">
                    <span>登录</span>
                </div>
                <div class="pcHeader-language" lxtrack-event="header_language">
                    <ul class="pcHeader-menu">
                        <li>
                            <div class="pcHeader-submenu">
                                <span
                                    >语言<i
                                        class="lxiconfont lxiconfont-arrowdown-small"
                                    ></i
                                ></span>
                                <ul class="pcHeader-submenu-list">
                                    <li>
                                        <a class="disabled" href="javascript:;"
                                            >中文</a
                                        >
                                    </li>
                                    <li>
                                        <a href="https://www.lixiang.com/en"
                                            >EN</a
                                        >
                                    </li>
                                </ul>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </header>
</div>

        <div class="chj-content">
            <div id="app"></div>
        </div>
        <footer id="chj-footer" class="chj-footer" :class="footerClass">
    <div id="chj-footer-nav"></div>
    <div id="chj-footer-bottom">
        <div class="chj-footer-inner">
            <div class="chj-footer-inner-cell cell-top">
                <div class="chj-footer-link">
                    <a class="mobile-hide" href="/autoinfo/index.html"
                        >维修与环保信息</a
                    >
                    <a href="/agreement/legal.html">法律与安全</a>
                    <a href="/agreement/privacy.html">隐私政策</a>
                    <a href="/help/topic/spray.html">钣喷中心</a>
                </div>
                <div class="chj-footer-icon" ref="footerIcon">
                    <a
                        class="chj-footer-icon-app"
                        href="javascript:;"
                        @click.stop="popshow('app')"
                    >
                        <div
                            class="chj-footer-popover"
                            :class="{'popshow': popshow_app}"
                            @click.stop
                        >
                            <div class="popover-qrcode">
                                <img alt="理想汽车App" />
                            </div>
                            <div class="popover-text">扫码下载理想汽车App</div>
                        </div>
                        <i
                            class="iconfont iconfont-app"
                            :class="{'popshow': popshow_app}"
                        ></i>
                    </a>
                    <a
                        class="chj-footer-icon-weixin"
                        href="javascript:;"
                        @click.stop="popshow('weixin')"
                    >
                        <div
                            class="chj-footer-popover"
                            :class="{'popshow': popshow_weixin}"
                            @click.stop
                        >
                            <div class="popover-qrcode">
                                <img alt="理想汽车公众号" />
                            </div>
                            <div class="popover-text">
                                扫码关注理想汽车公众号
                            </div>
                        </div>
                        <i
                            class="iconfont iconfont-weixin"
                            :class="{'popshow': popshow_weixin}"
                        ></i>
                    </a>
                    <a
                        class="chj-footer-icon-weibo"
                        target="_blank"
                        href="https://weibo.com/u/6001272153"
                    >
                        <i class="iconfont iconfont-weibo"></i>
                    </a>
                </div>
            </div>
            <div class="chj-footer-inner-cell cell-bottom">
                <div class="chj-footer-text">
                    <p>
                        <span class="chj-footer-text-callIM" @click="callIM"
                            >在线客服</span
                        >
                        <span
                            ><a href="tel:4006860900"
                                >客服电话 400-686-0900</a
                            ></span
                        >
                        <span
                            ><a href="mailto:press@lixiang.com"
                                >媒体咨询 press@lixiang.com</a
                            ></span
                        >
                    </p>
                    <!-- <span class="last"><a href="mailto:press@lixiang.com">媒体咨询 press@lixiang.com</a></span> -->
                </div>
                <div class="chj-footer-copyright">
                    <div class="chj-footer-copyright-top">
                        <span
                            ><a
                                target="_blank"
                                href="https://beian.miit.gov.cn/"
                                >©2020 京ICP备19003172号</a
                            ></span
                        >
                        <span
                            ><i class="emblem"></i
                            ><a
                                target="_blank"
                                href="https://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11011302001865"
                                >京公网安备11011302001865号</a
                            ></span
                        >
                        <span>北京车励行信息技术有限公司@版权所有</span>
                        <span
                            >增值电信业务经营许可证：编号京B2-20191092/编号B2-20196074</span
                        >
                        <span>
                            <a
                                target="_blank"
                                rel="noopener noreferrer"
                                href="https://www.lixiang.com/picture/preview.html?path=https://p.ampmake.com/fed/image/png/bf2586abadf6d4ce70338b8b3dd6f906.png"
                            >
                                营业执照
                            </a>
                        </span>
                        <span>
                            <a
                                target="_blank"
                                rel="noopener noreferrer"
                                href="https://www.lixiang.com/picture/preview.html?path=https://p.ampmake.com/fed/image/png/87a77c4fc13e7bc3a98b402abd6c7695.png"
                            >
                                广播电视节目制作经营许可证（京）字第18667号
                            </a>
                        </span>
                        <span
                            >北京市顺义区高丽营镇恒兴路4号院1幢105室(科技创新功能区)</span
                        >
                    </div>
                    <!-- <div class="chj-footer-copyright-bottom">
    
                    </div> -->
                    <!-- <span>©2019 京ICP备19003172号</span>
                    <span><i class="emblem"></i><a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502036860">京公网安备11010502036860号</a></span> -->
                </div>
            </div>
        </div>
    </div>
</footer>

        <script>
            var pmsData = {"pageId":"100409721131084554","versionId":"BWoj8fb6gtjLfR0fj4","code":"web-home","logined":0,"refreshed":0,"refreshInterval":5,"track":{"show":"p_default_u7S0I263eP"},"components":[{"versionId":"BWoj8fb6gtjLfR0fj4","componentId":"SceneMarketing","componentVersionId":"zTaMBq0NroRZS4eq2F","componentVersionName":"2","sort":1,"pageComponentRemark":"预热","code":"SceneMarketing","type":"SceneMarketing","showDevice":"PC+M","list":[{"bgPadV":"https://p.ampmake.com/lilibrary/65059338797608/76736d05-5472-4f2a-8437-c4abbff000bf.jpg","videoUrlPc":{"hd":"","sd":""},"previewVideoUrlPc":{"hd":"","sd":""},"link":{"text":"","action":"","track":"","params":{},"paramsNew":{}},"bgM":"https://p.ampmake.com/lilibrary/650621313396036/fed8ca73-e5f8-4293-a9f0-63ff18b4c450.jpg","videoUrlM":{"hd":"","sd":""},"titleListM":[{"margin":"80","text":"新一代理想MEGA产品发布会","font":"big"},{"text":"9月2日19:30见","font":"small"}],"buttonList":[{"button":{"text":"预约直播","action":"preorderLive","track":"click_22bXvD3u9Q","params":{},"paramsNew":{}},"type":"main"}],"type":"None","titleListPc":[{"text":"新一代理想MEGA产品发布会","font":"big"},{"text":"9月2日19:30见","font":"small"}],"bgPc":"https://p.ampmake.com/lilibrary/650611208870060/ab117b7e-b3ce-48fd-b983-f2018cdc39a6.jpg","bgPadH":"https://p.ampmake.com/lilibrary/650602196491025/bc76f7af-a755-4c27-8125-6fbac8650826.jpg","previewVideoUrlM":{"hd":"","sd":""},"fontColor":"white"}],"fullScreen":true,"showTrack":"show_GMyg0210Em"},{"versionId":"BWoj8fb6gtjLfR0fj4","componentId":"SceneMultiGrid","componentVersionId":"BRL0NXArtsez8LRvYe","componentVersionName":"4","sort":2,"pageComponentRemark":"pc","code":"SceneMultiGrid","type":"SceneMultiGrid","showDevice":"PC","chargingText2":"","chargingDesc":"充电比加油更方便。","chargingText1":"{number}个<br>理想超充站","chargingSize":"small","chargingBg":"https://p.ampmake.com/lilibrary/233775511860885/e6ba1512-01ad-48fa-85ca-24e9cba2e226.jpg","chargingButton":{"text":"了解更多","action":"goToSupportCharging","track":"click_R9j2j84875","params":{},"paramsNew":{}},"imageList":[{"button2":{"text":"定购","action":"goToBuy","track":"click_4924IsWo9r","params":{},"paramsNew":{"carModel":"X04"}},"size":"big","car":"X04","bg":"https://p.ampmake.com/lilibrary/193283690426/a1494793-98cc-4157-9653-43f9131e7575.jpg","logo":"https://p.ampmake.com/lilibrary/504619010204269/c840a0b5-8327-4fea-a673-758f8953b4ed.png","button1":{"text":"详情","action":"goToProduct","track":"click_74gu3J3NTH","params":{},"paramsNew":{"carModel":"X04"}}},{"button2":{"text":"定购","action":"goToBuy_L8","track":"click_423adN4Ur7","params":{},"paramsNew":{}},"size":"small","car":"X02","bg":"https://p.ampmake.com/lilibrary/182087189562825/51512336-02d2-4759-a44c-8c3ac59133b9.jpg","logo":"https://p.ampmake.com/lilibrary/983673397949358/26b04ecc-d5bc-45ce-95a6-987202e1cda1.png","button1":{"text":"详情","action":"goToProduct_L8","track":"click_N9kf42291X","params":{},"paramsNew":{}}},{"button2":{"text":"定购","action":"goToBuy","track":"c_default_017S2n3l34","params":{},"paramsNew":{"carModel":"X01"}},"size":"small","car":"X01","bg":"https://p.ampmake.com/lilibrary/182087726120157/3161c3be-9d4a-4716-80dc-860daa917750.jpg","logo":"https://p.ampmake.com/lilibrary/662019791898108/fac80fbc-0944-4824-afde-44222235fcab.png","button1":{"text":"详情","action":"goToProduct","track":"c_default_D0370r07OP","params":{},"paramsNew":{"carModel":"X01"}}},{"button2":{"text":"定购","action":"goToBuy_i6","track":"click_7ud3e7H5M7","params":{},"paramsNew":{}},"size":"big","car":"W04","bg":"https://p.ampmake.com/lilibrary/182086101769617/939c10f5-9ac7-4307-8eaf-1a590be73dec.jpg","logo":"https://p.ampmake.com/lilibrary/916544111512428/f8006029-9173-4282-8846-9ca4264daae9.png","button1":{"text":"详情","action":"goToProduct_i6","track":"click_rm71wV3XFh","params":{},"paramsNew":{}}},{"button2":{"text":"定购","action":"goToBuy_i8","track":"click_6389593z61","params":{},"paramsNew":{}},"size":"small","car":"W02","bg":"https://p.ampmake.com/lilibrary/824481931601706/8af58076-6847-44d0-809f-e81b53aafb07.jpg","logo":"https://p.ampmake.com/lilibrary/41230825389753/1cf7fbce-0dfd-4732-86b7-adf6afa23071.png","button1":{"text":"详情","action":"goToProduct_i8","track":"click_970QW92S8m","params":{},"paramsNew":{}}},{"button2":{"text":"","action":"goToBuy_MEGA","track":"click_3BI35931x7","params":{},"paramsNew":{}},"size":"small","car":"W01","bg":"https://p.ampmake.com/lilibrary/650630024958450/e9492c48-86cb-4a5a-b501-978f95970602.jpg","logo":"https://p.ampmake.com/lilibrary/637664511647482/f2f29f94-7e54-4535-9159-9debb7d58176.png","button1":{"text":"详情","action":"goToProduct_MEGA","track":"click_oX94D2V24G","params":{},"paramsNew":{}}}],"newStyle":false,"showTrack":"show_405r1079I3","chargingTitle":"理想充电站"},{"versionId":"BWoj8fb6gtjLfR0fj4","componentId":"SceneMultiBanner","componentVersionId":"Qf3QBOkn43XQH9M90u","componentVersionName":"7","sort":3,"pageComponentRemark":"m","code":"SceneMultiBanner","type":"SceneMultiBanner","showDevice":"M","enHide":true,"clickTrackM":"click_a0cO9I8kY3","bannerList":[{"button2":{"text":"","action":"goToProduct_i6","track":"","params":{},"paramsNew":{}},"bg":"https://p.ampmake.com/lilibrary/198253597421095/a3e43022-44e4-4dc8-8e2a-31909c2aaafd.jpg","link":{"text":"","action":"goToPublishVideo","track":"","params":{},"paramsNew":{}},"logo":"https://p.ampmake.com/lilibrary/495339656991613/53b8018d-a62b-4e37-a586-3655aa8c9a2f.png","type":"X04","button1":{"text":"","action":"","track":"","params":{},"paramsNew":{}}},{"button2":{"text":"","action":"","track":"","params":{},"paramsNew":{}},"bg":"https://p.ampmake.com/lilibrary/859835366401743/5d25cae2-28ec-4815-b09c-98695a7e00b6.png","link":{"text":"","action":"","track":"","params":{},"paramsNew":{}},"logo":"https://p.ampmake.com/lilibrary/916583926994284/5b3828cc-a793-49fe-995b-ba82f9ade4ef.png","type":"W04","button1":{"text":"","action":"","track":"","params":{},"paramsNew":{}}}],"showTrack":"show_P93W28Ly53"},{"versionId":"BWoj8fb6gtjLfR0fj4","componentId":"SceneMultiGrid","componentVersionId":"Ejs7G8BsgpzcVsgfrX","componentVersionName":"3","sort":4,"pageComponentRemark":"m","code":"SceneMultiGrid","type":"SceneMultiGrid","showDevice":"M","clickTrackM":"click_4zl6U7533R","chargingText2":"","chargingDesc":"充电比加油更方便。","chargingText1":"{number}个<br>理想超充站","chargingSize":"small","chargingBg":"https://p.ampmake.com/lilibrary/178808938556848/3795484a-11fd-4e70-932c-d5dde58a73c7.jpg","chargingButton":{"text":"","action":"","track":"","params":{},"paramsNew":{}},"imageList":[{"button2":{"text":"","action":"","track":"","params":{},"paramsNew":{}},"size":"small","car":"X02","bg":"https://p.ampmake.com/lilibrary/520198019727587/6879bc6f-eb21-4de3-b3c1-350258a733bf.jpg","logo":"https://p.ampmake.com/lilibrary/145194958700160/3a459d9d-8c20-4904-8a23-b4af1e44ddc2.png","button1":{"text":"","action":"","track":"","params":{},"paramsNew":{}}},{"button2":{"text":"","action":"","track":"","params":{},"paramsNew":{}},"size":"small","car":"X01","bg":"https://p.ampmake.com/lilibrary/097655288971158/6be99f0e-f90e-41dc-91e0-6fa0818bd7c0.jpg","logo":"https://p.ampmake.com/lilibrary/661928104782469/575dac4c-8c77-4bd4-a8d3-da1bcfd36e84.png","button1":{"text":"","action":"goToBuyPre","track":"","params":{},"paramsNew":{}}},{"button2":{"text":"","action":"","track":"","params":{},"paramsNew":{}},"car":"W04","bg":"https://p.ampmake.com/lilibrary/198245919455429/97a1ed71-2337-4f19-90b4-856c18842948.jpg","logo":"https://p.ampmake.com/lilibrary/916583926994284/5b3828cc-a793-49fe-995b-ba82f9ade4ef.png","button1":{"text":"","action":"","track":"","params":{},"paramsNew":{}}},{"button2":{"text":"","action":"","track":"","params":{},"paramsNew":{}},"size":"small","car":"W02","bg":"https://p.ampmake.com/lilibrary/824590092865485/5f180389-d2ce-488b-b0aa-d871c02c169e.jpg","logo":"https://p.ampmake.com/lilibrary/567951673287468/ddb2c186-436f-4346-9375-9f90a14cf511.png","button1":{"text":"","action":"","track":"","params":{},"paramsNew":{}}},{"button2":{"text":"","action":"","track":"","params":{},"paramsNew":{}},"size":"small","car":"W01","bg":"https://p.ampmake.com/lilibrary/650582584948171/dbe0d726-35c1-45da-9e86-87e7e7209960.jpg","logo":"https://p.ampmake.com/lilibrary/62859106718451/85f4d185-e340-424f-8590-ce6046cbae65.png","button1":{"text":"","action":"","track":"","params":{},"paramsNew":{}}}],"showTrack":"show_3PjGs21910","chargingTitle":"理想充电站"},{"versionId":"BWoj8fb6gtjLfR0fj4","componentId":"SceneMultiBanner","componentVersionId":"wyuQvfOxONCkKtaGPd","componentVersionName":"8","sort":5,"pageComponentRemark":"pc","code":"SceneMultiBanner","type":"SceneMultiBanner","showDevice":"PC","enHide":false,"swiperTrack":"show_60z03d16P5","bannerList":[{"button2":{"text":"立即定购","action":"goToBuy","track":"click_mr1t8f8S8E","params":{},"paramsNew":{"carModel":"X01"}},"enHide":true,"bg":"https://p.ampmake.com/lilibrary/758996069792024/39d96274-4326-444a-9800-fed5466904aa.jpg","link":{"text":"","action":"","track":"","params":{},"paramsNew":{}},"logo":"https://p.ampmake.com/lilibrary/661928104782469/575dac4c-8c77-4bd4-a8d3-da1bcfd36e84.png","type":"X01","button1":{"text":"了解详情","action":"goToProduct","track":"click_N95250vl6O","params":{},"paramsNew":{"carModel":"X01"}}},{"button2":{"text":"定购","action":"goToBuy","track":"click_S418Eq2127","params":{},"paramsNew":{"carModel":"W04"}},"bg":"https://p.ampmake.com/lilibrary/859468035916039/0ce0526f-c1da-46f4-bda8-7a1f7f580eeb.png","link":{"text":"","action":"","track":"","params":{},"paramsNew":{}},"logo":"https://p.ampmake.com/lilibrary/916544111512428/f8006029-9173-4282-8846-9ca4264daae9.png","type":"W04","button1":{"text":"详情","action":"goToProduct","track":"click_G50k79OG07","params":{},"paramsNew":{"carModel":"W04"}}},{"button2":{"text":"","action":"goToBuyTerminal","track":"","params":{},"paramsNew":{"type":"livis"}},"enHide":true,"bg":"https://p.ampmake.com/lilibrary/56515135560020/465825e6-ec91-4871-82d8-974c23e969d7.jpg","link":{"text":"","action":"","track":"","params":{},"paramsNew":{}},"logo":"https://p.ampmake.com/lilibrary/145194958700160/3a459d9d-8c20-4904-8a23-b4af1e44ddc2.png","type":"X02","button1":{"text":"了解详情","action":"goToProduct","track":"click_566sd39SS8","params":{},"paramsNew":{"carModel":"X02"}}}],"videoRatioPC":"2.35/1","showTrack":"show_yo25cVZ9N0"},{"versionId":"BWoj8fb6gtjLfR0fj4","componentId":"SceneTableHorizontal2","componentVersionId":"h0dqtZhJHnOzhzgzvT","componentVersionName":"5","sort":6,"pageComponentRemark":"用户视频","code":"SceneTableHorizontal2","type":"SceneTableHorizontal2","topGap":"big","bottomGap":"small","tagM":"品牌定位","titleM":"&nbsp; &nbsp;理想，<br>&nbsp; &nbsp;给车和家赋予生命。","link":{"text":"","action":"goToPublishNews","track":"","params":{},"paramsNew":{}},"title":"理想，给车和家赋予生命。","descM":"","list":[{"videoM":{"hd":"https://p.ampmake.com/lilibrary/hd/060930023697823/c3fc1457-31bb-46c9-92bd-bd1915042cbd.mp4","sd":"https://p.ampmake.com/lilibrary/sd/060930023697823/c3fc1457-31bb-46c9-92bd-bd1915042cbd.mp4"},"fullVideoM":{"hd":"https://p.ampmake.com/lilibrary/hd/773340487374215/b0a3e5e8-8bae-4d2e-937c-aa53fede73ac.mp4","sd":"https://p.ampmake.com/lilibrary/sd/773340487374215/b0a3e5e8-8bae-4d2e-937c-aa53fede73ac.mp4"},"videoPc":{"hd":"https://p.ampmake.com/lilibrary/hd/060930023697823/c3fc1457-31bb-46c9-92bd-bd1915042cbd.mp4","sd":"https://p.ampmake.com/lilibrary/sd/060930023697823/c3fc1457-31bb-46c9-92bd-bd1915042cbd.mp4"},"fullVideoBtn":"观看完整视频","titleM":"","bgPc":"https://p.ampmake.com/lilibrary/654502145482701/9b01720c-b372-40b1-acec-842b8cad56a3.jpg","link":{"text":"","action":"","track":"","params":{},"paramsNew":{}},"bgM":"https://p.ampmake.com/lilibrary/654502145482701/9b01720c-b372-40b1-acec-842b8cad56a3.jpg","contentM":"","title":"&nbsp; &nbsp;家是私有的空间，<br>&nbsp; &nbsp;亲密的关系，幸福的体验。","fullVideoPc":{"hd":"https://p.ampmake.com/lilibrary/hd/773340487374215/b0a3e5e8-8bae-4d2e-937c-aa53fede73ac.mp4","sd":"https://p.ampmake.com/lilibrary/sd/773340487374215/b0a3e5e8-8bae-4d2e-937c-aa53fede73ac.mp4"},"content":""},{"videoM":{"hd":"https://p.ampmake.com/lilibrary/hd/389767072244933/e69fff13-9006-4417-9cad-5a2232e87d26.mp4","sd":"https://p.ampmake.com/lilibrary/sd/389767072244933/e69fff13-9006-4417-9cad-5a2232e87d26.mp4"},"fullVideoM":{"hd":"https://p.ampmake.com/lilibrary/hd/389414734894972/7fd6adbc-67e8-4d27-8404-3b090a7351b8.mp4","sd":"https://p.ampmake.com/lilibrary/sd/389414734894972/7fd6adbc-67e8-4d27-8404-3b090a7351b8.mp4"},"titleM":"","link":{"text":"","action":"","track":"","params":{},"paramsNew":{}},"bgM":"https://p.ampmake.com/lilibrary/654503923697180/93a68b8e-d7c4-4389-b301-4399cb5139d6.jpg","title":"&nbsp; &nbsp;面对面，\n<br>&nbsp; &nbsp;看见最大的幸福。","content":"","videoPc":{"hd":"https://p.ampmake.com/lilibrary/hd/389767072244933/e69fff13-9006-4417-9cad-5a2232e87d26.mp4","sd":"https://p.ampmake.com/lilibrary/sd/389767072244933/e69fff13-9006-4417-9cad-5a2232e87d26.mp4"},"fullVideoBtn":"观看完整视频","bgPc":"https://p.ampmake.com/lilibrary/654503923697180/93a68b8e-d7c4-4389-b301-4399cb5139d6.jpg","fullVideoBtnTrack":"click_j6B6VmE991","contentM":"","fullVideoPc":{"hd":"https://p.ampmake.com/lilibrary/hd/389414734894972/7fd6adbc-67e8-4d27-8404-3b090a7351b8.mp4","sd":"https://p.ampmake.com/lilibrary/sd/389414734894972/7fd6adbc-67e8-4d27-8404-3b090a7351b8.mp4"}},{"videoM":{"hd":"https://p.ampmake.com/lilibrary/hd/389781775975351/6018ac60-2e6b-41a3-9865-6974c1fc3cac.mp4","sd":"https://p.ampmake.com/lilibrary/sd/389781775975351/6018ac60-2e6b-41a3-9865-6974c1fc3cac.mp4"},"fullVideoM":{"hd":"https://p.ampmake.com/lilibrary/hd/389781756725482/d0c66b66-02fc-4825-8e92-a0eb601f32f7.mp4","sd":"https://p.ampmake.com/lilibrary/sd/389781756725482/d0c66b66-02fc-4825-8e92-a0eb601f32f7.mp4"},"titleM":"","link":{"text":"","action":"","track":"","params":{},"paramsNew":{}},"bgM":"https://p.ampmake.com/lilibrary/654503106469529/58d9423e-3e98-4075-841d-6bb5a23c6292.jpg","title":"&nbsp; &nbsp;成长的旅途，<br>&nbsp; &nbsp;更近的幸福。\n","content":"","videoPc":{"hd":"https://p.ampmake.com/lilibrary/hd/389781775975351/6018ac60-2e6b-41a3-9865-6974c1fc3cac.mp4","sd":"https://p.ampmake.com/lilibrary/sd/389781775975351/6018ac60-2e6b-41a3-9865-6974c1fc3cac.mp4"},"fullVideoBtn":"观看完整视频","bgPc":"https://p.ampmake.com/lilibrary/654503106469529/58d9423e-3e98-4075-841d-6bb5a23c6292.jpg","fullVideoBtnTrack":"click_8mjfaJQXFF","contentM":"","fullVideoPc":{"hd":"https://p.ampmake.com/lilibrary/hd/389781756725482/d0c66b66-02fc-4825-8e92-a0eb601f32f7.mp4","sd":"https://p.ampmake.com/lilibrary/sd/389781756725482/d0c66b66-02fc-4825-8e92-a0eb601f32f7.mp4"}}],"bottomGapM":"big","enableHover":false,"tag":"品牌定位","showTrack":"show_Th9J2796kq","desc":""},{"versionId":"BWoj8fb6gtjLfR0fj4","componentId":"product-home-produce-list","componentVersionId":"ipCXDovrfdL2KTGttU","componentVersionName":"5","sort":7,"pageComponentRemark":"了解理想汽车","code":"product-home-produce-list","type":"product-home-produce-list","topGap":"zero","bottomGap":"zero","subtitle":"","tag":"","title":"","produceListItem":[{"bgImageUrl-m":"https://p.ampmake.com/lilibrary/414616797989077/2ea1d15c-708d-4fbb-b1ca-d230c78262da.jpg","list-button1":{"text":"了解更多","action":"goToAbout","track":"click_8Ca378Mer2","params":{"jumpId":"movehome"}},"subtitle":"","bgImageUrl-pc":"https://p.ampmake.com/lilibrary/414616797989077/2ea1d15c-708d-4fbb-b1ca-d230c78262da.jpg","title":"创造独一无二的产品"},{"bgImageUrl-m":"https://p.ampmake.com/lilibrary/414608377278648/31cd3d79-d8c5-4757-b7a0-9568ca2de665.jpg","list-button1":{"text":"了解更多","action":"goToAbout","track":"click_A5ccHz03F8","params":{"jumpId":"happyhome"}},"subtitle":"","bgImageUrl-pc":"https://p.ampmake.com/lilibrary/414608377278648/31cd3d79-d8c5-4757-b7a0-9568ca2de665.jpg","title":"百万家庭的选择"}],"showTrack":"show_gk616B1CQ3","hideInEn":false},{"versionId":"BWoj8fb6gtjLfR0fj4","componentId":"SceneTableHorizontal2","componentVersionId":"WYg5WRfU6uTM9cG5aN","componentVersionName":"6","sort":8,"pageComponentRemark":"探索理想科技","code":"SceneTableHorizontal2","type":"SceneTableHorizontal2","topGap":"big","bottomGap":"small","tagM":"","titleM":"","link":{"text":"","action":"goToPublishVideo","track":"","params":{},"paramsNew":{}},"title":"探索理想科技","descM":"","list":[{"videoM":{"hd":"","sd":""},"fullVideoM":{"hd":"","sd":""},"videoPc":{"hd":"","sd":""},"fullVideoBtn":"","titleM":"","bgPc":"https://p.ampmake.com/lilibrary/759131752331648/a3b770d7-0900-4a88-ae26-a6d719b27a68.jpg","link":{"text":"了解更多","action":"goToTech","track":"click_Z90r7MQTO0","params":{},"paramsNew":{"techPage":"chassis"}},"bgM":"https://p.ampmake.com/lilibrary/759131752331648/a3b770d7-0900-4a88-ae26-a6d719b27a68.jpg","contentM":"","title":"&nbsp; &nbsp;完全体线控底盘，<br>&nbsp; &nbsp;为全尺寸SUV量身打造。","fullVideoPc":{"hd":"","sd":""},"content":""},{"videoM":{"hd":"","sd":""},"fullVideoM":{"hd":"","sd":""},"videoPc":{"hd":"","sd":""},"fullVideoBtn":"","titleM":"","bgPc":"https://p.ampmake.com/lilibrary/754149056258163/1a7a89b9-a0c1-4e86-9e0b-2b3fec055ab5.jpg","link":{"text":"了解更多","action":"goToTech","track":"click_5C2x64O1z6","params":{},"paramsNew":{"techPage":"extendrange"}},"bgM":"https://p.ampmake.com/lilibrary/754149056258163/1a7a89b9-a0c1-4e86-9e0b-2b3fec055ab5.jpg","contentM":"","title":"&nbsp; &nbsp;王牌增程与王牌5C，<br>&nbsp; &nbsp;合二为一。","fullVideoPc":{"hd":"","sd":""},"content":""},{"videoM":{"hd":"","sd":""},"fullVideoM":{"hd":"","sd":""},"videoPc":{"hd":"","sd":""},"fullVideoBtn":"","titleM":"","bgPc":"https://p.ampmake.com/lilibrary/759140000718041/1d3ace41-88a7-4645-9a78-1489b445de3d.jpg","link":{"text":"了解更多","action":"goToTech","track":"click_WXENi0t100","params":{},"paramsNew":{"techPage":"eea"}},"bgM":"https://p.ampmake.com/lilibrary/759140000718041/1d3ace41-88a7-4645-9a78-1489b445de3d.jpg","contentM":"","title":"&nbsp; &nbsp;全新一代电子电气架构，<br>&nbsp; &nbsp;更高效、更安全、更聪明。","fullVideoPc":{"hd":"","sd":""},"content":""},{"videoM":{"hd":"","sd":""},"fullVideoM":{"hd":"","sd":""},"videoPc":{"hd":"","sd":""},"fullVideoBtn":"","titleM":"","bgPc":"https://p.ampmake.com/lilibrary/759103844528398/70f05f7b-7006-4895-bb33-3195e23d9110.jpg","link":{"text":"了解更多","action":"goToTechAutodrive","track":"click_U2O8Sq33O3","params":{},"paramsNew":{}},"bgM":"https://p.ampmake.com/lilibrary/759103844528398/70f05f7b-7006-4895-bb33-3195e23d9110.jpg","contentM":"","title":"&nbsp; &nbsp;全场景高级辅助驾驶，<br>&nbsp; &nbsp;终身零订阅费。","fullVideoPc":{"hd":"","sd":""},"content":""},{"videoM":{"hd":"","sd":""},"fullVideoM":{"hd":"","sd":""},"videoPc":{"hd":"","sd":""},"fullVideoBtn":"","titleM":"","bgPc":"https://p.ampmake.com/lilibrary/812296010212758/4d80928c-9ae2-403f-a0be-456ad4b48acb.jpg","link":{"text":"了解更多","action":"goToTechSmartspace","track":"click_2F73cmywMr","params":{},"paramsNew":{}},"bgM":"https://p.ampmake.com/lilibrary/812296010212758/4d80928c-9ae2-403f-a0be-456ad4b48acb.jpg","contentM":"","title":"&nbsp; &nbsp;理想智能空间，<br>&nbsp; &nbsp;创新五屏三维空间交互。","fullVideoPc":{"hd":"","sd":""},"content":""},{"videoM":{"hd":"","sd":""},"fullVideoM":{"hd":"","sd":""},"videoPc":{"hd":"","sd":""},"fullVideoBtn":"","titleM":"","bgPc":"https://p.ampmake.com/lilibrary/759094502383540/f32a1115-0bb0-4799-a974-244505adc72e.jpg","link":{"text":"了解更多","action":"goToTechMindgpt","track":"click_14595aLtVP","params":{},"paramsNew":{}},"bgM":"https://p.ampmake.com/lilibrary/759094502383540/f32a1115-0bb0-4799-a974-244505adc72e.jpg","contentM":"","title":"&nbsp; &nbsp;AI理想同学，<br>&nbsp; &nbsp;车里、家里都能用。","fullVideoPc":{"hd":"","sd":""},"content":""},{"videoM":{"hd":"","sd":""},"fullVideoM":{"hd":"","sd":""},"videoPc":{"hd":"","sd":""},"fullVideoBtn":"","titleM":"","bgPc":"https://p.ampmake.com/lilibrary/759113576445590/cf030240-7d1c-4c02-80ff-409ec736333e.jpg","link":{"text":"了解更多","action":"goToTech","track":"click_5568h79t7X","params":{},"paramsNew":{"techPage":"fortress"}},"bgM":"https://p.ampmake.com/lilibrary/759113576445590/cf030240-7d1c-4c02-80ff-409ec736333e.jpg","contentM":"","title":"&nbsp; &nbsp;堡垒安全车身，<br>&nbsp; &nbsp;360°保护每一位家人的安全。","fullVideoPc":{"hd":"","sd":""},"content":""}],"bottomGapM":"small","enableHover":true,"tag":"理想科技","showTrack":"show_x88459Qh8f","desc":""},{"versionId":"BWoj8fb6gtjLfR0fj4","componentId":"product-home-produce-list","componentVersionId":"ipCXDovrfdL2KTGttU","componentVersionName":"5","sort":9,"pageComponentRemark":"理想服务","code":"product-home-produce-list","type":"product-home-produce-list","topGap":"small","bottomGap":"zero","subtitle":"快速找到您需要的信息","tag":"直营服务","title":"完备的服务生态","produceListItem":[{"bgImageUrl-m":"https://p.ampmake.com/lilibrary/083012944421647/c709f621-f7ff-4b92-9d76-52df4279a49b.jpg","list-button1":{"text":"了解更多","action":"goToSupportCharging","track":"click_F5RT4A7YgY","params":{"jumpId":""}},"subtitle":"将充电速度代入“5G时代”，实现真正的充电自由。","bgImageUrl-pc":"https://p.ampmake.com/lilibrary/082546373332279/a098b25e-45ee-47d1-b069-04a7dadeb72c.jpg","title":"充电服务"}],"showTrack":"show_Y1e9480Oh8","hideInEn":true},{"versionId":"BWoj8fb6gtjLfR0fj4","componentId":"product-home-produce-list","componentVersionId":"ipCXDovrfdL2KTGttU","componentVersionName":"5","sort":10,"pageComponentRemark":"购车服务","code":"product-home-produce-list","type":"product-home-produce-list","topGap":"multi","bottomGap":"zero","subtitle":"","name":"scene-producelist-buy","tag":"","title":"","produceListItem":[{"bgImageUrl-m":"https://p.ampmake.com/lilibrary/438167434846489/6693bad1-bc56-429d-a8a0-eca5d4cc9e61.jpg","list-button1":{"text":"了解更多","action":"goToSupportStore","track":"click_6e2Vk6Z61T","params":{"jumpId":""},"paramsNew":{}},"subtitle":"透明、便捷、高效","bgImageUrl-pc":"https://p.ampmake.com/lilibrary/438167434846489/6693bad1-bc56-429d-a8a0-eca5d4cc9e61.jpg","title":"直营销售"},{"bgImageUrl-m":"https://p.ampmake.com/lilibrary/438163842696211/65932232-2aeb-4208-869f-6ecda5e23b7b.jpg","list-button1":{"text":"了解更多","action":"goToSupportService","track":"click_Yp13i5h769","params":{"jumpId":""},"paramsNew":{}},"subtitle":"专业、高效、贴心","bgImageUrl-pc":"https://p.ampmake.com/lilibrary/438163842696211/65932232-2aeb-4208-869f-6ecda5e23b7b.jpg","title":"理想服务"}],"showTrack":"show_77254915Yz","hideInEn":true},{"versionId":"BWoj8fb6gtjLfR0fj4","componentId":"product-home-linklist","componentVersionId":"rqooFTvugU2Q0nit7e","componentVersionName":"3","sort":11,"pageComponentRemark":"四联小入口（置换服务、金融试算器、帮助中心、参数配置）","code":"product-home-linklist","type":"product-home-linklist","name":"scene-operate","list":[{"button":{"text":"查看更多 >","action":"goToReplacement","track":"c_default_6N1N7izuOl"},"icon":"https://p.ampmake.com/lilibrary/839273181716267/a563f016-e9e9-4793-87fd-27bd5a6c700e.png","description":"","title":"置换服务"},{"button":{"text":"查看更多 >","action":"goToCalc_L6","track":"c_default_X831b686m9"},"icon":"https://p.ampmake.com/lilibrary/912003642518054/7d95a92d-4656-4f01-8967-619bc14485b5.png","description":"","title":"金融试算器"},{"button":{"text":"查看更多 >","action":"goToHelp","track":"c_default_pM35MFP659"},"icon":"https://p.ampmake.com/lilibrary/839272767853262/9f55e018-ab5e-4513-a3f5-32449e087968.png","description":"","title":"帮助中心"},{"button":{"text":"查看更多 >","action":"goToConfig_L6","track":"click_qLK6s97CQX"},"icon":"https://p.ampmake.com/lilibrary/839273395849341/405d4d10-9ff2-41cd-8b9d-4d10624b5954.png","description":"","title":"参数配置"}],"showTrack":"c_default_1mx2xc276c"},{"versionId":"BWoj8fb6gtjLfR0fj4","componentId":"product-download","componentVersionId":"4xKo21AycSnKwrz4k3","componentVersionName":"5","sort":12,"pageComponentRemark":"下载app","code":"product-download","type":"product-download","name":"scene-download","theme":"white"}],"lxCdnUrl":"https://live-status.ampmake.com/prodpagecdn/453aae01ed4e4122b769da62d7f0972e/30715886-42ea-4cf6-8f62-e025a1376798.json"};
            var liveUrl = 'https://live-status.ampmake.com/prodpagecdn/web-home.json';
        </script>
        <input
    type="hidden"
    id="timestamp"
    date-timestamp="8/27/2026, 6:14:59 AM"
    value="1787782499381"
/>
<script>
    var disableInitWx = true;
    var pageName = 'home';
    var mobileRefresh = true;
    window.trackPageName = 'home';
</script>
<script>
    (function() {
        if (globalData.env !== 'prod') {
            var head = document.getElementsByTagName('head')[0];
            var script = document.createElement('script');
            script.type = 'text/javascript';
            script.src =
                'https://p.ampmake.com/fed//tmp/egg-multipart-tmp/fed-server-api/2025/03/28/18/accbed5d-240b-4e19-81ba-19065cfa8877.js';
            head.appendChild(script);
            script.onload = function() {
                localStorage.setItem('develop_mode', false);
                var c = 0;
                var timer = null;
                var f = false;
                var show = false;
                var active = '';
                ['click', 'touchstart'].forEach(function(item) {
                    window.addEventListener(item, () => {
                        if (active && active !== item) {
                            return;
                        }
                        active = item;
                        f = true;
                        if (c === 0) {
                            clearTimeout(timer);
                        }
                        if (f) {
                            c++;
                        }
                        if (!timer) {
                            timer = setTimeout(() => {
                                if (c > 10 && !show) {
                                    show = true;
                                    var vConsole = new VConsole();
                                }
                                clearTimeout(timer);
                                timer = null;
                                c = 0;
                                f = false;
                            }, 2000);
                        }
                    });
                });
            };
        }
    })();
</script>
<!-- chunks begin -->

<script src="https://p.ampmake.com/fed/m01/chunk-2608/js/9991.2c7d575e.js"></script>

<script src="https://p.ampmake.com/fed/m01/chunk-2608/js/2837.686d8f6f.js"></script>

<script src="https://p.ampmake.com/fed/m01/chunk-2608/js/3068.a2ed22d2.js"></script>

<script src="https://p.ampmake.com/fed/m01/chunk-2608/js/3611.e553b3a1.js"></script>

<script src="https://p.ampmake.com/fed/m01/chunk-2608/js/9712.acdb2e4f.js"></script>

<script src="https://p.ampmake.com/fed/m01/chunk-2608/js/7394.03e4cda8.js"></script>

<script src="https://p.ampmake.com/fed/m01/chunk-2608/js/8288.c2db680c.js"></script>

<script src="https://p.ampmake.com/fed/m01/chunk-2608/js/4842.0df9bedb.js"></script>

<script src="https://p.ampmake.com/fed/m01/chunk-2608/js/9259.762006ad.js"></script>

<script src="https://p.ampmake.com/fed/m01/chunk-2608/js/4762.16f404c8.js"></script>

<script src="https://p.ampmake.com/fed/m01/chunk-2608/js/339.6e04d9c8.js"></script>

<script src="https://p.ampmake.com/fed/m01/chunk-2608/js/4370.199be2eb.js"></script>

<script src="https://p.ampmake.com/fed/m01/chunk-2608/js/4388.84be3677.js"></script>

<script src="https://p.ampmake.com/fed/m01/chunk-2608/js/home.fbbd0a25.js"></script>
<!-- chunks end -->

    </body>
</html>
