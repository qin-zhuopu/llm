# Source: https://www.hongxiu.com

> 抓取日期: 2026-08-26

---

<!DOCTYPE html>
<html>
<head>
    
<script>
   var g_data = g_data || {};
   g_data.site = 'hongxiu'

   // 环境变量，会按照环境选择性打log
   g_data.envType = 'pro';

   //环境域名
   g_data.rootDomain = 'hongxiu.com';
   g_data.domain = '';
   g_data.domainPreFix = '';

   //静态资源域名
   g_data.staticPath = '//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease';

   //获取用户是否登录
   g_data.isLogin = 'false';

   // 导流相关
   g_data.appDownloadUrl = 'https://www.yuewen.com/app.html#appxx';
   g_data.guide2app = 'qd';
   g_data.guide2appXXLocationSite = '_hxpc';
   g_data.isQReaderNoFreeBook = false;

   // 是否支持登录
   g_data.enableLogin = true;

   // 是否支持充值 / 消费 / 打赏 / 投票等
   g_data.enableChargeAndConsume = true;
</script>

    <script>
      // 全局的通用数据都放g_data变量里
      // 用作统计PV
      g_data.pageId = 'hx_P_front';
    </script>
    <script>

  function setCookie(name, value, domain, path, expires){
    if(expires){
      expires = new Date(+new Date() + expires);
    }
    var tempcookie = name + '=' + escape(value) +
      ((expires) ? '; expires=' + expires.toGMTString() : '') +
      ((path) ? '; path=' + path : '') +
      ((domain) ? '; domain=' + domain : '');

    //Ensure the cookie's size is under the limitation
    if(tempcookie.length < 4096) {
      document.cookie = tempcookie;
    }
  }

  function setReferrer(referrerCookieName) {
    try {
      var reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
      var seoReferer = document.cookie.match(reg);
      console.log("get cookie referrer: ", seoReferer)
      if (seoReferer && seoReferer[2]) {
        Object.defineProperty(document, "referrer", {
          value: decodeURIComponent(seoReferer[2])
        });
        document.cookie = referrerCookieName + '=;domain=.' + g_data.rootDomain + ';path=/;expires=Thu, 01-Jan-1970 00:00:01 GMT';
      }
    } catch (error) {
      console.log(error);
    }
  }
  function isMobile() {
    return /(Android|iPhone|iPad|iPod|SymbianOS|Windows Phone|BlackBerry|OpenHarmony.*Mobile|Fennec|IEMobile)/i.test(navigator.userAgent);
  }
  function isSpider() {
    return /(bot|spider|crawl|slurp|archiver|facebook|googlebot|bingbot|yandexbot|duckduckgo|twitterbot)/i.test(navigator.userAgent);
  }

  function jumpIfMobile(mPathName, referrerCookieName) {
    //判断是移动设备 且 宽度小于1024 且 不是爬虫 后跳转到m站
    if (
      window.outerWidth <= 1024
      && isMobile()
      && !isSpider()
      && location.host.indexOf('.qq.com') === -1
    ) {
      var url = location.protocol + "//" + location.host.replace("www.", "m.") + (mPathName || location.pathname)
      var search = location.search.replace("?", "");
      if (search) {
        if (/source=m_jump/.test(search)) {
          search = search.replace("source=m_jump", "source=pc_jump")
        } else if (/source=pc_jump/.test(search)) {
          // do nothing
        } else {
          search = (search + "&source=pc_jump")
        }
      } else {
        search = "source=pc_jump"
      }
      url = url.indexOf("?") !== -1 ? (url + "&" + search) : (url + "?" + search);

      console.log("set cookie referrer: ", document.referrer)
      setCookie(referrerCookieName, document.referrer, '.' + g_data.rootDomain, '/', 60000);
      window.location.href = url;
    }
  }

  var referrerCookieName = "seo-jump-referrer";
  setReferrer(referrerCookieName);
  jumpIfMobile(window.mPath, referrerCookieName);
</script>


    <meta charset="UTF-8">
    

<title>红袖读书_好看的小说免费阅读 - 阅文集团旗下网站</title>
<meta name="keywords" content="免费小说, 言情小说, 小说排行榜, 小说阅读网, 全本小说, 完本小说, 小说下载, 红柚读书">
<meta name="description" content="又名“红袖添香”，国内知名网络文学原创小说门户。书城拥有海量完结全本小说，每日更新言情、都市、耽美、穿越、官场、重生、玄幻、女尊等小说的连载最新章节，定期发布阅读小说排行榜单，听有声小说推荐下载『红袖读书APP』。">

    <meta name="robots" content="all">
    <meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1">

    <meta name="renderer" content="webkit" />
    <link rel="shortcut icon" type="image/x-icon" href="//yuxseocdn.yuewen.com/favicon/hongxiu.ico">

    <script>document.domain = 'hongxiu.com';</script>

    
    <!-- start mobile and canonical link related -->


<meta http-equiv="mobile-agent" content="format=html5; url=https://m.hongxiu.com">
<link rel="alternate" href="https://m.hongxiu.com">
<link rel="canonical" href="https://www.hongxiu.com">


    <!-- start header 钩子 -->
    <meta name="applicable-device" content="pc">
<!-- 移动设备访问PC端跳转的代码被删除 -->
<!-- 跳转逻辑放在 static/component/mobileJump.js 中 -->
<link rel="shortcut icon" type="image/x-icon" href="//yuxseocdn.yuewen.com/favicon/hongxiu.ico">
<link rel="Bookmark" type="image/x-icon" href="//yuxseocdn.yuewen.com/favicon/hongxiu.ico">


    <!-- end header 钩子 -->

    <!-- 站点认证 S -->
    




    <meta name="sogou_site_verification" content="EAeeNWG0Ex" />
    <meta name="bytedance-verification-code" content="VlxASrHBF1czUccx9bpg" />
    <meta name="shenma-site-verification" content="5e0cef13cd202d339c9d04e55b5d1c48_1679292253">
    <meta name="google-site-verification" content="sB71wCgMYJsuziW4gl2SdOAy_i_jUrDnm4co-aCkmy4" />






    <!-- 站点认证 E -->

    <link rel="stylesheet" href="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/css/reset.1586d.css">
    <link rel="stylesheet" href="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/css/lbfUI/css/icon.10dd5.css">
    <link rel="stylesheet" href="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/css/font.918d2.css">
    <link rel="stylesheet" href="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/css/header.b687a.css">
    <link rel="stylesheet" href="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/css/module.beafa.css">
    <link rel="stylesheet" href="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/css/index.1fb18.css">
    <link rel="stylesheet" href="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/css/layout.c0894.css">
    <link rel="stylesheet" href="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/css/popup.74b40.css">
    <link rel="stylesheet" href="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/css/footer.6b6ba.css">
</head>
<body class="g_site_hongxiu">

<div class="wrap home">
    <!-- start 头部 -->
    <div class="header">
    
    <!-- start 顶部 -->
    <div class="top-head box-center cf">
        <!-- start Logo -->
        <div class="logo" title="红袖读书">
            <a href="/"><em></em></a>
        </div>
        <!-- end Logo -->

        <!-- start 搜索框 -->
        <div class="search-wrap">
            
            <form class="cf" id="formUrl" action="/so" method="get" target="_blank">
                <input class="search-box" id="s-box" name="kw" type="text" placeholder="傲气如我" autocomplete="off" value="">
                
                    <input class="submit-input" type="submit" id="searchSubmit" data-eid=""><a href="/search" id="search-a-btn"><label id="search-btn" class="search-btn" for="searchSubmit"><em class="iconfont" data-eid="">&#xe604;</em></label></a>
                
            </form>
        </div>
        <!-- end 搜索框 -->
        
        <!-- start 用户专区 -->
        <div class="user-wrap">
            <div class="avatar" id="j-userWrap"><a class="link" href="javascript:" id="j-avatar"><img src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/ico/account.1e031.png"></a>

                <!-- start 用户专区下拉框 -->
                <div class="down-drop" id="j-userDownDrop">
                    <dl>
                        <dd><a href="javascript:" id="sign-out">退出</a></dd>
                    </dl>
                </div>
                <!-- end 用户专区下拉框 -->
            </div>
            <ul>
                <li><a class="head-msg" href="javascript:" title="消息中心"><em class="iconfont">&#xe902;</em></a></li>
                <li><a class="head-shelf" href="javascript:"><em class="iconfont">&#xe62c;</em>我的书架</a></li>
            </ul>
        </div>
        <!-- end 用户专区 -->
        
    </div>
    <!-- end 顶部 -->
    
    
    <!-- start 顶部导航 -->
    <div class="top-nav-wrap">
        <div class="box-center cf">
            <div class="left-nav fl">
                <ul class="cf">
                    <li class="type " id="j-navType"><a href="/category"><em class="iconfont">&#xe612;</em>全部分类</a>
                        
                        <div class="type-list" id="j-typeList">
                            <cite></cite>
                            <dl>
                                <dd><a href="/category/30020_f1_f1_f1_f1_f1_0_1"><em class="iconfont">&#xe630;</em><i>现代言情</i></a></dd>
                                <dd><a href="/category/30013_f1_f1_f1_f1_f1_0_1"><em class="iconfont">&#xe632;</em><i>古代言情</i></a></dd>
                                <dd><a href="/category/30031_f1_f1_f1_f1_f1_0_1"><em class="iconfont">&#xe631;</em><i>浪漫青春</i></a></dd>
                                <dd><a href="/category/30001_f1_f1_f1_f1_f1_0_1"><em class="iconfont">&#xe637;</em><i>玄幻言情</i></a></dd>
                                <dd><a href="/category/30008_f1_f1_f1_f1_f1_0_1"><em class="iconfont">&#xe62e;</em><i>仙侠奇缘</i></a></dd>
                                <dd><a href="/category/30036_f1_f1_f1_f1_f1_0_1"><em class="iconfont">&#xe634;</em><i>悬疑</i></a></dd>
                                <dd><a href="/category/30042_f1_f1_f1_f1_f1_0_1"><em class="iconfont">&#xe62d;</em><i>科幻空间</i></a></dd>
                                <dd><a href="/category/30050_f1_f1_f1_f1_f1_0_1"><em class="iconfont">&#xe638;</em><i>游戏竞技</i></a></dd>
                                <dd><a href="/category/30083_f1_f1_f1_f1_f1_0_1"><em class="iconfont">&#xe63b;</em>短篇小说</a></dd>
                                <dd><a href="/category/30055_f1_f1_f1_f1_f1_0_1"><em class="iconfont">&#xe904;</em><i>轻小说</i></a></dd>
                            </dl>
                        </div>
                    </li>
                    <li class=""><a href="/rank">排行榜</a></li>
                    <li class=""><a href="/free">免费</a></li>
                    <li class=""><a href="/finish">完本</a></li>
                    <li class=""><a href="/baike">百科</a></li>
                    <li><a href="/gdyq">古言</a></li>
                    <li><a href="/xdyq">现言</a></li>
                    <li><a href="/xhxx">玄幻仙侠</a></li>
                    <li><a href="/lykh">悬疑科幻</a></li>
                    <li><a href="/qcyx">青春游戏</a></li>
                    <li><a href="/fsg">风尚阁</a></li>

                    

                        <!-- 临时将 版权专区 改为 动漫专区 （审核） -->
                        <li class=""><a href="/z/comic" rel="nofollow">动漫专区</a></li>
                        <!-- 临时将 版权专区 改为 动漫专区 （审核） -->
                    
                </ul>
            </div>
            <div class="right-nav fr">
                <!-- 删除 _blank 修复未登录时跳到空白页面 -->
<!--                <a class="j-goCharge" href="javascript:"><em class="iconfont">&#xe60f;</em>充值</a>-->
                <a href="//write.qq.com?siteid=6" target="_blank"><em class="iconfont">&#xe62a;</em>作家专区</a>
        </div>
    </div>
    </div>
    <!-- end 顶部导航 -->

    
</div>

    <!-- end 头部 -->

    <!-- start 首页内容容器 -->
    <div class="index-wrap">

    <div class="flower left"></div>
    <div class="flower right"></div>

        <!-- start 居中容器，主要内容结构 -->
    <div class="box-center">
        <!-- start 首屏焦点图区域 -->
        
    <div class="focus-wrap mb20 cf">
        <div class="focus-slider-wrap cf" data-l1="1">
            
                <!-- start 焦点图轮播 -->
                <div id="j-focus-slider" class="yx-rotaion fl">
                    <ul class="rotaion_list">
                        
                            <li style="display: none">
                                <a href="/book/33358861104391807" target="_blank"><img src="//bossaudioandcomic-1252317822.image.myqcloud.com/activity/document/344d7c9c177b5334a88083e8b15c6b5d.jpg" alt="重生换宗，小可怜"></a>
                            </li>
                            
                            <li style="display: none">
                                <a href="/book/32046313507749807" target="_blank"><img src="//bossaudioandcomic-1252317822.image.myqcloud.com/activity/document/b01cfb716adbdb8ee6b31ea12521d99d.jpg" alt="表姑娘回京后，未"></a>
                            </li>
                            
                            <li style="display: none">
                                <a href="/book/33271078404770808" target="_blank"><img src="//bossaudioandcomic-1252317822.image.myqcloud.com/activity/document/ac7af9456958839bb1553918f2e2fd1f.jpg" alt="在末日游戏里当农"></a>
                            </li>
                            
                            <li style="display: none">
                                <a href="/book/33485481603781808" target="_blank"><img src="//bossaudioandcomic-1252317822.image.myqcloud.com/activity/document/dfa851cd87548ff696a93a81d52263f3.jpg" alt="掀桌！唢呐一吹，"></a>
                            </li>
                            
                            <li style="display: none">
                                <a href="/book/33446341203028509" target="_blank"><img src="//bossaudioandcomic-1252317822.image.myqcloud.com/activity/document/ab9f288b9196a7370baf88d95eb4fbc7.jpg" alt="惊蛰无人生还"></a>
                            </li>
                            
                    </ul>
                    <div class="yx-rotation-focus">
                        <!-- <a class="hover" href="https://www.hongxiu.com/book/33358861104391807" target="_blank">重生换宗，小可怜</a> -->
                        
                            <a href="/book/33358861104391807" target="_blank">
                                重生换宗，小可怜
                            </a>
                            
                            <a href="/book/32046313507749807" target="_blank">
                                表姑娘回京后，未
                            </a>
                            
                            <a href="/book/33271078404770808" target="_blank">
                                在末日游戏里当农
                            </a>
                            
                            <a href="/book/33485481603781808" target="_blank">
                                掀桌！唢呐一吹，
                            </a>
                            
                            <a href="/book/33446341203028509" target="_blank">
                                惊蛰无人生还
                            </a>
                            
                    </div>
                </div>
                <!-- end 焦点图轮播 -->
                

                    <!-- start 公告 -->
                    <div class="focus-notice-wrap fr">
                        <h3><em class="iconfont">&#xe63a;</em><span>公告</span></h3>
                        
                            <div class="notice-list">
                                <ul>
                                    
                                        <li style="width: 210px;" class="rec"><a href="https://v.wjx.cn/vm/m9BRwRq.aspx" target="_blank" rel="nofollow"><span>[资讯]</span>中国数字阅读用户现状调研</a></li>
                                        
                                        <li style="width: 210px;" class=""><a href="https://mp.weixin.qq.com/s/4VeBev9GGxihH5MNVevfSg?mpshare=1&amp;scene=1&amp;srcid=0801zDxRpMpTTwRpb8djZYXr&amp;sharer_shareinfo=467c009cbe86e604c7fb12947fa1170b&amp;sharer_shareinfo_first=467c009cbe86e604c7fb12947fa1170b#wechat_redirect" target="_blank" rel="nofollow"><span>[资讯]</span>书写抗战精神作品联展</a></li>
                                        
                                        <li style="width: 210px;" class=""><a href="https://xinwen.bjd.com.cn/content/s68bf8845e4b0221b9bec988f.html" target="_blank" rel="nofollow"><span>[资讯]</span>25年专项海报公布！</a></li>
                                        
                                        <li style="width: 210px;" class=""><a href="/book/3756981504436501" target="_blank" rel="nofollow"><span>[公告]</span>《听说你喜欢我》原著</a></li>
                                        
                                        <li style="width: 210px;" class=""><a href="https://mp.weixin.qq.com/s/c1G3OQ6-lWh5qwQ-sejJcg" target="_blank" rel="nofollow"><span>[资讯]</span>25年绿书签行动来啦</a></li>
                                        
                                        <li style="width: 210px;" class=""><a href="https://write.qq.com/portal/college/editordetail?gender=2&amp;typeid=75457244950928251&amp;idx=75460605762836001" target="_blank" rel="nofollow"><span>[公告]</span>25年作家福利已上线</a></li>
                                        
                                </ul>
                            </div>
                            
                    </div>
                    <!-- end 公告 -->
        </div>

    </div>
        <!-- end 首屏焦点图区域 -->

        <!-- start 编辑推荐 -->
        
<div class="index-book-wrap edit-rec-wrap mb20">
    <div class="inner-wrap cf">
        <!-- start 左侧 -->
        <div class="left-wrap fl hover-icon">
            <h3 class="lang"><em class="icon icon-edit_rec"></em></h3>
            <!-- <h3 class="lang">编辑强推<em class="icon icon-edit_rec"></em></h3> -->
            
            <div id="new-book-list">
                <div class="type-new-list cf" data-l2="1">
                  <div class="line l1"></div>
                  <div class="line l2"></div>
                    <ul>
                        
                        <li data-rid="1">
                            <div class="book-img">
                                <a href="/book/31725340403587408" data-eid="qd_F23" data-bid="31725340403587408" target="_blank"><img src="//bookcover.yuewen.com/qdbimg/349573/c_31725340403587408/90" alt="我靠种田经商养活三军"></a>
                            </div>
                            <div class="book-info"><h4>
                                <a href="/book/31725340403587408" data-eid="qd_F24" data-bid="31725340403587408" target="_blank" title="我靠种田经商养活三军">我靠种田经商养活三军</a>
                            </h4>
                                <p>新书《惨死？重生虐渣！白眼狼们跪着求！》已发布，宝宝们多多支持呀！新书《穿到大汉搞基建》已发布，请宝宝们支持呀唐昭是沪市商场上一颗冉冉升起的新星。一朝重生，成了魏国公府的嫡长女，被皇帝下旨赐婚给昏迷不醒的宣王五子冲喜。冲喜当日，昏迷半月有余的顾辞睁开了眼睛。唐昭对上那双凛冽逼人的双眼，就知道这是狼队友。皇帝大行后，唐昭随宣王府众人前往封地，开始展露锋芒。提高亩产，经营作坊，修建水利，改善医疗，赚钱</p>
                                <div class="state-box cf">
                                    <i>古代言情</i><a class="author default" data-eid="qd_F25" target="_blank"><img src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/ico/user.f22d3.png">牛顿不爱吃苹果</a>
                                </div>
                            </div>
                        </li>
                        
                        <li data-rid="2">
                            <div class="book-img">
                                <a href="/book/30549797907512407" data-eid="qd_F23" data-bid="30549797907512407" target="_blank"><img src="//bookcover.yuewen.com/qdbimg/349573/c_30549797907512407/90" alt="盛唐奇幻录"></a>
                            </div>
                            <div class="book-info"><h4>
                                <a href="/book/30549797907512407" data-eid="qd_F24" data-bid="30549797907512407" target="_blank" title="盛唐奇幻录">盛唐奇幻录</a>
                            </h4>
                                <p>【1V1，霸气机敏少女幻术师X温柔腹黑少年神探】盛世长安幻术风靡，无父无母的果儿自幼随师父苦研幻术，只为成为天下第一幻术师！长安是果儿的故土，却也是师父从不肯带她踏足的禁地。十五岁时，师父留下一封信便离奇失踪……为寻师父，也为成就梦想，果儿骑着一头白驴独闯长安，却在这里遭遇了光怪陆离的诡谲谜案……果儿披荆斩棘堪破迷案的过程中，邂逅了极致反差温柔腹黑的长安第一神探薛和沾。又陆续结识了贪财浪荡的市井神</p>
                                <div class="state-box cf">
                                    <i>古代言情</i><a class="author default" data-eid="qd_F25" target="_blank"><img src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/ico/user.f22d3.png">婆娑道姑</a>
                                </div>
                            </div>
                        </li>
                        
                        <li data-rid="3">
                            <div class="book-img">
                                <a href="/book/33841727603369708" data-eid="qd_F23" data-bid="33841727603369708" target="_blank"><img src="//bookcover.yuewen.com/qdbimg/349573/c_33841727603369708/90" alt="明争暗诱"></a>
                            </div>
                            <div class="book-info"><h4>
                                <a href="/book/33841727603369708" data-eid="qd_F24" data-bid="33841727603369708" target="_blank" title="明争暗诱">明争暗诱</a>
                            </h4>
                                <p>和谈斯屹结婚前，孟京攸只见过他三次。商业联姻，协议隐婚，为期三年。那时她刚失恋。满腔爱意追了多年的前男友，跟她说：“我们不合适。”同样爱而不得的，还有谈斯屹。据说：他有白月光，与孟京攸眉眼相似。敢情，就连联姻，也是找了个相似的替身。**婚后第二年，孟京攸生日，喝多了酒，竟当着众人的面，扯着他的领带，将他压在身下：“你长得……好像我老公。”谈家二爷理性薄情，那晚却被她撩红了眼，靠在她耳边低哄：“乖一</p>
                                <div class="state-box cf">
                                    <i>现代言情</i><a class="author default" data-eid="qd_F25" target="_blank"><img src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/ico/user.f22d3.png">月初姣姣</a>
                                </div>
                            </div>
                        </li>
                        
                        <li data-rid="4">
                            <div class="book-img">
                                <a href="/book/33634549004675407" data-eid="qd_F23" data-bid="33634549004675407" target="_blank"><img src="//bookcover.yuewen.com/qdbimg/349573/c_33634549004675407/90" alt="凌霄花上"></a>
                            </div>
                            <div class="book-info"><h4>
                                <a href="/book/33634549004675407" data-eid="qd_F24" data-bid="33634549004675407" target="_blank" title="凌霄花上">凌霄花上</a>
                            </h4>
                                <p>太和元年春，料峭寒夜，虞花凌浑身是血，虚软无力地靠在深巷一角，觉得这人生真是操蛋，千里追杀，她怕是进不了京就得死在路上。糟心昏沉之际，一人拎着酒从旁边酒肆出来，瞧见她，顿住，隔着三丈的距离，看了片刻，啧啧一声，“好好的一个小姑娘，怎么这么惨？我这里有半坛酒，要吗？”虞花凌厌厌地掀起眼皮，盯着这人看了一会儿，长身玉立的一位公子哥，她伸手，“要！”这人将半坛酒扔给她，转身走了。虞花凌靠着这半坛酒，一路</p>
                                <div class="state-box cf">
                                    <i>古代言情</i><a class="author default" data-eid="qd_F25" target="_blank"><img src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/ico/user.f22d3.png">西子情</a>
                                </div>
                            </div>
                        </li>
                        
                        <li data-rid="5">
                            <div class="book-img">
                                <a href="/book/33098954903350908" data-eid="qd_F23" data-bid="33098954903350908" target="_blank"><img src="//bookcover.yuewen.com/qdbimg/349573/c_33098954903350908/90" alt="荒野直播，毛茸茸带我屡破凶案"></a>
                            </div>
                            <div class="book-info"><h4>
                                <a href="/book/33098954903350908" data-eid="qd_F24" data-bid="33098954903350908" target="_blank" title="荒野直播，毛茸茸带我屡破凶案">荒野直播，毛茸茸带我屡破凶案</a>
                            </h4>
                                <p>被养父母当作“心脏容器”抛弃那天，穿越过来的阮未迟激活了探索系统。为了活命开启荒野直播，却不料直播间画风逐渐跑偏：挖蚯蚓挖到人头，流浪猫说凶手少根手指，鸽子指认知名女星被推下天台，还有废弃工厂悬挂着的半截尸体……网友以为是剧本，警方却连夜找上门：“阮小姐，麻烦协助调查连环杀人案。”从偏僻鱼塘的猫咪解密，到废旧工厂的狼王追凶，她的直播间成了破案现场。网友们听说最近有个新兴主播，只要和毛茸茸有关的事，</p>
                                <div class="state-box cf">
                                    <i>现代言情</i><a class="author default" data-eid="qd_F25" target="_blank"><img src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/ico/user.f22d3.png">白茶有猫饼</a>
                                </div>
                            </div>
                        </li>
                        
                        <li data-rid="6">
                            <div class="book-img">
                                <a href="/book/32905803903602809" data-eid="qd_F23" data-bid="32905803903602809" target="_blank"><img src="//bookcover.yuewen.com/qdbimg/349573/c_32905803903602809/90" alt="折金钗"></a>
                            </div>
                            <div class="book-info"><h4>
                                <a href="/book/32905803903602809" data-eid="qd_F24" data-bid="32905803903602809" target="_blank" title="折金钗">折金钗</a>
                            </h4>
                                <p>虞瑾重生到凌家登门退亲这日，前世，她为争一口气，拒不退婚，和凌木南做了一世怨侣，至死方休。如今重回当年岔路口……往前看，凌家，她那未婚夫的亲亲表妹肚子都大了，一堆乌糟事等着，往后看，自家门里也不清净，二姑娘一心谋算嫁权贵，三姑娘觊觎准姐夫，四姑娘正待择黄道吉日与情郎私奔……虞家长房无子，爵位传给二房败家子，家族很快就会衰败没落……既然大家都不争气，那就索性一起躺平摆烂，爱咋咋地吧！素来掐尖要强的掌</p>
                                <div class="state-box cf">
                                    <i>古代言情</i><a class="author default" data-eid="qd_F25" target="_blank"><img src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/ico/user.f22d3.png">叶阳岚</a>
                                </div>
                            </div>
                        </li>
                        
                        <li data-rid="7">
                            <div class="book-img">
                                <a href="/book/33481219107866808" data-eid="qd_F23" data-bid="33481219107866808" target="_blank"><img src="//bookcover.yuewen.com/qdbimg/349573/c_33481219107866808/90" alt="胎穿后我掌管全家气运"></a>
                            </div>
                            <div class="book-info"><h4>
                                <a href="/book/33481219107866808" data-eid="qd_F24" data-bid="33481219107866808" target="_blank" title="胎穿后我掌管全家气运">胎穿后我掌管全家气运</a>
                            </h4>
                                <p>睡梦中猝死的孟皎月直接投胎了，好在她掌控运道的一黑一白两个小本本还在。大御帝国文人第一世家孟家几百年底蕴，翰墨书院培养出无数学子，可惜代代无女，她一出生就成了唯一。祖父把大御开国皇帝御赐的一块蓝田玉花重金请第一玉雕大师雕刻成玉坠，在她百日宴上亲手给她戴上，说将来谁戴上这枚玉坠谁就是孟家婿。实打实的孟家掌上明珠。百日宴上四大家族、皇帝、各大世家都把自家的适龄男孩儿带来了。孟皎月礼物收了一大堆不算，刚</p>
                                <div class="state-box cf">
                                    <i>玄幻言情</i><a class="author default" data-eid="qd_F25" target="_blank"><img src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/ico/user.f22d3.png">午日阳光</a>
                                </div>
                            </div>
                        </li>
                        
                        <li data-rid="8">
                            <div class="book-img">
                                <a href="/book/33790178503934708" data-eid="qd_F23" data-bid="33790178503934708" target="_blank"><img src="//bookcover.yuewen.com/qdbimg/349573/c_33790178503934708/90" alt="反派庶女不好惹"></a>
                            </div>
                            <div class="book-info"><h4>
                                <a href="/book/33790178503934708" data-eid="qd_F24" data-bid="33790178503934708" target="_blank" title="反派庶女不好惹">反派庶女不好惹</a>
                            </h4>
                                <p>穿成小官家的庶女，韩胜玉一直以为自己拿的是自强不息励志剧本。直到一纸来信让她们进京，抵达金城后，她才知道自己穿书了，拿的是反派祭天剧本。包括不限于自己为了男女主惊天地泣鬼神的爱情奉献自己的倾城美貌，顶尖智商，人格尊严以及珍贵的生命。韩胜玉冷笑一声撸袖子掀桌，我人美心善，怎么可能是智障反派！去他的男女主，让你们知道反派庶女不好惹。顺我者昌，逆我者亡。</p>
                                <div class="state-box cf">
                                    <i>古代言情</i><a class="author default" data-eid="qd_F25" target="_blank"><img src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/ico/user.f22d3.png">暗香</a>
                                </div>
                            </div>
                        </li>
                        
                        <li data-rid="9">
                            <div class="book-img">
                                <a href="/book/34021220204341608" data-eid="qd_F23" data-bid="34021220204341608" target="_blank"><img src="//bookcover.yuewen.com/qdbimg/349573/c_34021220204341608/90" alt="假孕成真，阴鸷反派求放过"></a>
                            </div>
                            <div class="book-info"><h4>
                                <a href="/book/34021220204341608" data-eid="qd_F24" data-bid="34021220204341608" target="_blank" title="假孕成真，阴鸷反派求放过">假孕成真，阴鸷反派求放过</a>
                            </h4>
                                <p>云昭渺穿书了，醒来时浑身酸疼，身旁是被她“睡”失忆的魔尊。魔尊眸色阴鸷，捏着她下巴逼问：“你是谁？”为了保命，她捂着小腹，眼底泛起水雾，幽怨委屈地埋怨道：“阿沉，你竟不记得我了。”眼泪涌出，自脸颊滑落：“你不记得我就算了，竟然连我们的孩子都忘了……他才两个月大……”宫厌沉手指一顿，杀意收敛，茫然地看向她平坦的小腹。自此，她被迫踏上演戏之路，谁知演着演着……真怀了？？？——宫厌沉失忆后捡到一个女人。</p>
                                <div class="state-box cf">
                                    <i>玄幻言情</i><a class="author default" data-eid="qd_F25" target="_blank"><img src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/ico/user.f22d3.png">沈烟渚</a>
                                </div>
                            </div>
                        </li>
                        
                    </ul>
                </div>
            </div>
            
        </div>
        <!-- end 左侧-->
        <!-- start 右侧-->
        <div class="right-wrap mb6 hover-icon fr">
            <div class="book-list-wrap fr" data-l1="10">
                <h3 class="lang"><a href="/fsg"></a><em class="icon icon-fsg"></em></h3>
                <!-- <h3 class="lang"><a href="/fsg">风尚阁</a><em class="icon icon-fsg"></em></h3> -->
                
                <div class="book-list">
                    <ul>
                        
                        <li data-rid="1">
                            <a class="channel" href="/category/30020_f1_f1_f1_f1_f1_0_1" data-eid="qd_A112" target="_blank"><em>「</em>现代言情<em>」</em></a><a class="name" href="/book/30484150803175209" data-eid="qd_A113" target="_blank" data-bid="30484150803175209" title="离婚后夫人另嫁，陆总他疯了">离婚后夫人另嫁，陆总他疯了</a>
                        </li>
                        
                        <li data-rid="2">
                            <a class="channel" href="/category/30020_f1_f1_f1_f1_f1_0_1" data-eid="qd_A112" target="_blank"><em>「</em>现代言情<em>」</em></a><a class="name" href="/book/33030516703645107" data-eid="qd_A113" target="_blank" data-bid="33030516703645107" title="甲方的春天">甲方的春天</a>
                        </li>
                        
                        <li data-rid="3">
                            <a class="channel" href="/category/30013_f1_f1_f1_f1_f1_0_1" data-eid="qd_A112" target="_blank"><em>「</em>古代言情<em>」</em></a><a class="name" href="/book/34168362803862509" data-eid="qd_A113" target="_blank" data-bid="34168362803862509" title="隔壁童养媳上岸日常">隔壁童养媳上岸日常</a>
                        </li>
                        
                        <li data-rid="4">
                            <a class="channel" href="/category/30020_f1_f1_f1_f1_f1_0_1" data-eid="qd_A112" target="_blank"><em>「</em>现代言情<em>」</em></a><a class="name" href="/book/32624795204536409" data-eid="qd_A113" target="_blank" data-bid="32624795204536409" title="带着空间穿年代，科研大佬有点甜">带着空间穿年代，科研大佬有点甜</a>
                        </li>
                        
                        <li data-rid="5">
                            <a class="channel" href="/category/30013_f1_f1_f1_f1_f1_0_1" data-eid="qd_A112" target="_blank"><em>「</em>古代言情<em>」</em></a><a class="name" href="/book/33446341203028509" data-eid="qd_A113" target="_blank" data-bid="33446341203028509" title="惊蛰无人生还">惊蛰无人生还</a>
                        </li>
                        
                        <li data-rid="6">
                            <a class="channel" href="/category/30020_f1_f1_f1_f1_f1_0_1" data-eid="qd_A112" target="_blank"><em>「</em>现代言情<em>」</em></a><a class="name" href="/book/29327970807629604" data-eid="qd_A113" target="_blank" data-bid="29327970807629604" title="我在海拔三千米的高原开渔场">我在海拔三千米的高原开渔场</a>
                        </li>
                        
                        <li data-rid="7">
                            <a class="channel" href="/category/30013_f1_f1_f1_f1_f1_0_1" data-eid="qd_A112" target="_blank"><em>「</em>古代言情<em>」</em></a><a class="name" href="/book/34329331304540108" data-eid="qd_A113" target="_blank" data-bid="34329331304540108" title="和离后，清冷权臣红眼喊我小祖宗">和离后，清冷权臣红眼喊我小祖宗</a>
                        </li>
                        
                        <li data-rid="8">
                            <a class="channel" href="/category/30036_f1_f1_f1_f1_f1_0_1" data-eid="qd_A112" target="_blank"><em>「</em>悬疑侦探<em>」</em></a><a class="name" href="/book/33450667303301309" data-eid="qd_A113" target="_blank" data-bid="33450667303301309" title="髻杀">髻杀</a>
                        </li>
                        
                        <li data-rid="9">
                            <a class="channel" href="/category/30020_f1_f1_f1_f1_f1_0_1" data-eid="qd_A112" target="_blank"><em>「</em>现代言情<em>」</em></a><a class="name" href="/book/33613005204776607" data-eid="qd_A113" target="_blank" data-bid="33613005204776607" title="江州囍事">江州囍事</a>
                        </li>
                        
                        <li data-rid="10">
                            <a class="channel" href="/category/30020_f1_f1_f1_f1_f1_0_1" data-eid="qd_A112" target="_blank"><em>「</em>现代言情<em>」</em></a><a class="name" href="/book/34287030603324308" data-eid="qd_A113" target="_blank" data-bid="34287030603324308" title="读心替身小保姆，反派修罗场争宠">读心替身小保姆，反派修罗场争宠</a>
                        </li>
                        
                        <li data-rid="11">
                            <a class="channel" href="/category/30055_f1_f1_f1_f1_f1_0_1" data-eid="qd_A112" target="_blank"><em>「</em>轻小说<em>」</em></a><a class="name" href="/book/32422206303433009" data-eid="qd_A113" target="_blank" data-bid="32422206303433009" title="斗罗叶骨衣：穿回过去，还称帝？">斗罗叶骨衣：穿回过去，还称帝？</a>
                        </li>
                        
                    </ul>
                </div>
                
            </div>
        </div>
        <!-- end 右侧 -->
    </div>
</div>

        <!-- end 编辑推荐 -->

        <!-- start 红文馆 -->
        <div class="red-shop cf mb20">
    <h3 title="红文馆"></h3>
    
    <div class="book-slide-wrap box">
        <div id="j-bookSlide">
            <ul class="cf">
                
                <li>
                    <div class="book-img">
                        <a href="/book/33251016704660509" target="_blank">
                            <img class="lazy" src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/common/default_book.5968b.png" data-original="//bookcover.yuewen.com/qdbimg/349573/c_33251016704660509/90">
                        </a>
                    </div>
                    <h4><a href="/book/33251016704660509" target="_blank">大小姐她一心只想上位</a></h4>
                    <p>天泠</p>
                </li>
                
                <li>
                    <div class="book-img">
                        <a href="/book/33878206307202507" target="_blank">
                            <img class="lazy" src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/common/default_book.5968b.png" data-original="//bookcover.yuewen.com/qdbimg/349573/c_33878206307202507/90">
                        </a>
                    </div>
                    <h4><a href="/book/33878206307202507" target="_blank">流放神级生育力？摆摊养崽兽夫宠</a></h4>
                    <p>虞木京</p>
                </li>
                
                <li>
                    <div class="book-img">
                        <a href="/book/32271051507422309" target="_blank">
                            <img class="lazy" src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/common/default_book.5968b.png" data-original="//bookcover.yuewen.com/qdbimg/349573/c_32271051507422309/90">
                        </a>
                    </div>
                    <h4><a href="/book/32271051507422309" target="_blank">拈花问鼎</a></h4>
                    <p>凤轻</p>
                </li>
                
                <li>
                    <div class="book-img">
                        <a href="/book/32149202104965508" target="_blank">
                            <img class="lazy" src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/common/default_book.5968b.png" data-original="//bookcover.yuewen.com/qdbimg/349573/c_32149202104965508/90">
                        </a>
                    </div>
                    <h4><a href="/book/32149202104965508" target="_blank">全球穿越：我能听见异植心声</a></h4>
                    <p>舒长歌</p>
                </li>
                
                <li>
                    <div class="book-img">
                        <a href="/book/31346356603368008" target="_blank">
                            <img class="lazy" src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/common/default_book.5968b.png" data-original="//bookcover.yuewen.com/qdbimg/349573/c_31346356603368008/90">
                        </a>
                    </div>
                    <h4><a href="/book/31346356603368008" target="_blank">闪婚七零：随军养崽暴富了</a></h4>
                    <p>花鹿呦呦</p>
                </li>
                
                <li>
                    <div class="book-img">
                        <a href="/book/32382523204555609" target="_blank">
                            <img class="lazy" src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/common/default_book.5968b.png" data-original="//bookcover.yuewen.com/qdbimg/349573/c_32382523204555609/90">
                        </a>
                    </div>
                    <h4><a href="/book/32382523204555609" target="_blank">酿秋实</a></h4>
                    <p>前后卿</p>
                </li>
                
                <li>
                    <div class="book-img">
                        <a href="/book/32647852503845207" target="_blank">
                            <img class="lazy" src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/common/default_book.5968b.png" data-original="//bookcover.yuewen.com/qdbimg/349573/c_32647852503845207/90">
                        </a>
                    </div>
                    <h4><a href="/book/32647852503845207" target="_blank">被夺一切后我成了仙道魁首</a></h4>
                    <p>盛唐无夜</p>
                </li>
                
                <li>
                    <div class="book-img">
                        <a href="/book/33713710307788109" target="_blank">
                            <img class="lazy" src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/common/default_book.5968b.png" data-original="//bookcover.yuewen.com/qdbimg/349573/c_33713710307788109/90">
                        </a>
                    </div>
                    <h4><a href="/book/33713710307788109" target="_blank">错嫁反派大佬，随军养崽躺赢了</a></h4>
                    <p>姬朔</p>
                </li>
                
                <li>
                    <div class="book-img">
                        <a href="/book/34384315907247108" target="_blank">
                            <img class="lazy" src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/common/default_book.5968b.png" data-original="//bookcover.yuewen.com/qdbimg/349573/c_34384315907247108/90">
                        </a>
                    </div>
                    <h4><a href="/book/34384315907247108" target="_blank">软萌人鱼幼崽，治愈全星际被团宠</a></h4>
                    <p>垚垚不吃土</p>
                </li>
                
            </ul>
        </div>
        <a class="prev jcarousel-control-prev" href="javascript:" id="j-LeftBtn"><em class="iconfont">&#xe628;</em></a>
        <a class="next jcarousel-control-next" href="javascript:" id="j-RightBtn"><em class="iconfont">&#xe621;</em></a>
        <p class="jcarousel-pagination"></p>
    </div>
    
</div>
        <!-- end 红文馆 -->

        

        <!-- start 书单排行榜 -->
        
<div class="rank-wrap mb20" data-l1="11">
    <div id="rank-list-row" class="rank-list-row inner-wrap cf">
        <div class="rank-list" data-l2="1">
            <h3 class="wrap-title lang">华语言情风云榜<a class="more" href="/rank/hxyuepiao" target="_blank">更多<em class="iconfont">&#xe621;</em></a></h3>
            
            <div class="book-list">
                <ul>
                    <li class="unfold" data-rid="1">
                        <div class="book-wrap cf">
                            <div class="book-info fl"><h3>NO.1</h3><h4>
                                <a href="/book/11281255704829603" target="_blank" data-eid="qd_A117" data-bid="11281255704829603" title="总裁狼性">总裁狼性</a>
                            </h4>
                                <p class="month"><i>150</i>月票</p>
                                <p class="author">
                                    <a class="type" href="/category/30020_f1_f1_f1_f1_f1_0_1" target="_blank">现代言情</a><i>·</i><a class="writer default">爱做噩梦的猫</a>
                                </p></div>
                            <div class="book-cover">
                                <a class="link" href="/book/11281255704829603" data-eid="qd_A117" target="_blank" data-bid="11281255704829603"><img src="//bookcover.yuewen.com/qdbimg/349573/c_11281255704829603/90" alt="总裁狼性"></a><span></span>
                            </div>
                        </div>
                    </li>
                    
                    <li data-rid="2">
                        <div class="num-box"><span class="num2">2</span></div>
                        <div class="name-box">
                            <a class="name middle" href="/book/10194680803837303" target="_blank" data-eid="qd_A117" data-bid="10194680803837303" title="顾忘西川">顾忘西川</a><i class="num">120</i>
                        </div>
                    </li>
                    
                    <li data-rid="3">
                        <div class="num-box"><span class="num3">3</span></div>
                        <div class="name-box">
                            <a class="name middle" href="/book/20724092001596504" target="_blank" data-eid="qd_A117" data-bid="20724092001596504" title="美食大佬在星际只想赚钱">美食大佬在星际只想赚钱</a><i class="num">42</i>
                        </div>
                    </li>
                    
                    <li data-rid="4">
                        <div class="num-box"><span class="num4">4</span></div>
                        <div class="name-box">
                            <a class="name middle" href="/book/17215945505470204" target="_blank" data-eid="qd_A117" data-bid="17215945505470204" title="南风雨后">南风雨后</a><i class="num">36</i>
                        </div>
                    </li>
                    
                    <li data-rid="5">
                        <div class="num-box"><span class="num5">5</span></div>
                        <div class="name-box">
                            <a class="name middle" href="/book/8351242704606903" target="_blank" data-eid="qd_A117" data-bid="8351242704606903" title="呆萌世子妃：竹马夫君咬一口">呆萌世子妃：竹马夫君咬一口</a><i class="num">35</i>
                        </div>
                    </li>
                    
                    <li data-rid="6">
                        <div class="num-box"><span class="num6">6</span></div>
                        <div class="name-box">
                            <a class="name middle" href="/book/17327871604465704" target="_blank" data-eid="qd_A117" data-bid="17327871604465704" title="毒妇和她的死对头重生了">毒妇和她的死对头重生了</a><i class="num">18</i>
                        </div>
                    </li>
                    
                    <li data-rid="7">
                        <div class="num-box"><span class="num7">7</span></div>
                        <div class="name-box">
                            <a class="name middle" href="/book/5458228603893201" target="_blank" data-eid="qd_A117" data-bid="5458228603893201" title="钻石小春耀晶明坚梦">钻石小春耀晶明坚梦</a><i class="num">18</i>
                        </div>
                    </li>
                    
                    <li data-rid="8">
                        <div class="num-box"><span class="num8">8</span></div>
                        <div class="name-box">
                            <a class="name middle" href="/book/18687000008784404" target="_blank" data-eid="qd_A117" data-bid="18687000008784404" title="对谢哥哥撒个娇">对谢哥哥撒个娇</a><i class="num">8</i>
                        </div>
                    </li>
                    
                    <li data-rid="9">
                        <div class="num-box"><span class="num9">9</span></div>
                        <div class="name-box">
                            <a class="name middle" href="/book/18925228008299004" target="_blank" data-eid="qd_A117" data-bid="18925228008299004" title="快穿之干了这碗狗粮">快穿之干了这碗狗粮</a><i class="num">6</i>
                        </div>
                    </li>
                    
                    <li data-rid="10">
                        <div class="num-box"><span class="num10">10</span></div>
                        <div class="name-box">
                            <a class="name middle" href="/book/5457341603385901" target="_blank" data-eid="qd_A117" data-bid="5457341603385901" title="女人心">女人心</a><i class="num">6</i>
                        </div>
                    </li>
                    
                    <li data-rid="11">
                        <div class="num-box"><span class="num11">11</span></div>
                        <div class="name-box">
                            <a class="name middle" href="/book/20934168208615604" target="_blank" data-eid="qd_A117" data-bid="20934168208615604" title="陆总，夫人又传您八卦了">陆总，夫人又传您八卦了</a><i class="num">5</i>
                        </div>
                    </li>
                    
                    <li data-rid="12">
                        <div class="num-box"><span class="num12">12</span></div>
                        <div class="name-box">
                            <a class="name middle" href="/book/17755279506421504" target="_blank" data-eid="qd_A117" data-bid="17755279506421504" title="致命偏宠">致命偏宠</a><i class="num">5</i>
                        </div>
                    </li>
                    
                    <li data-rid="13">
                        <div class="num-box"><span class="num13">13</span></div>
                        <div class="name-box">
                            <a class="name middle" href="/book/14433859204078004" target="_blank" data-eid="qd_A117" data-bid="14433859204078004" title="摄政王的小闲妻">摄政王的小闲妻</a><i class="num">5</i>
                        </div>
                    </li>
                    
                    <li data-rid="14">
                        <div class="num-box"><span class="num14">14</span></div>
                        <div class="name-box">
                            <a class="name middle" href="/book/16792364604322104" target="_blank" data-eid="qd_A117" data-bid="16792364604322104" title="嫡长女她又美又飒">嫡长女她又美又飒</a><i class="num">4</i>
                        </div>
                    </li>
                    
                    <li data-rid="15">
                        <div class="num-box"><span class="num15">15</span></div>
                        <div class="name-box">
                            <a class="name middle" href="/book/19931432208400404" target="_blank" data-eid="qd_A117" data-bid="19931432208400404" title="末日经营游戏">末日经营游戏</a><i class="num">3</i>
                        </div>
                    </li>
                    
                    <li data-rid="16">
                        <div class="num-box"><span class="num16">16</span></div>
                        <div class="name-box">
                            <a class="name middle" href="/book/18564721708225304" target="_blank" data-eid="qd_A117" data-bid="18564721708225304" title="快穿之奶猫宿主甜又软">快穿之奶猫宿主甜又软</a><i class="num">3</i>
                        </div>
                    </li>
                    
                    <li data-rid="17">
                        <div class="num-box"><span class="num17">17</span></div>
                        <div class="name-box">
                            <a class="name middle" href="/book/13899265303683904" target="_blank" data-eid="qd_A117" data-bid="13899265303683904" title="暖婚甜入骨">暖婚甜入骨</a><i class="num">3</i>
                        </div>
                    </li>
                    
                    <li data-rid="18">
                        <div class="num-box"><span class="num18">18</span></div>
                        <div class="name-box">
                            <a class="name middle" href="/book/13641088905154304" target="_blank" data-eid="qd_A117" data-bid="13641088905154304" title="女配表示很无辜">女配表示很无辜</a><i class="num">3</i>
                        </div>
                    </li>
                    
                    <li data-rid="19">
                        <div class="num-box"><span class="num19">19</span></div>
                        <div class="name-box">
                            <a class="name middle" href="/book/12110374803718803" target="_blank" data-eid="qd_A117" data-bid="12110374803718803" title="大宋宠妃陈三娘">大宋宠妃陈三娘</a><i class="num">3</i>
                        </div>
                    </li>
                    
                    <li data-rid="20">
                        <div class="num-box"><span class="num20">20</span></div>
                        <div class="name-box">
                            <a class="name middle" href="/book/6392131203396901" target="_blank" data-eid="qd_A117" data-bid="6392131203396901" title="神医药香：山里汉子农家妻">神医药香：山里汉子农家妻</a><i class="num">3</i>
                        </div>
                    </li>
                    
                </ul>
            </div>
            
        </div>


        <!-- start 热销榜 -->
        <div class="rank-list width" data-l2="1">
            <h3 class="wrap-title lang">热销榜<a class="more" href="/rank/hotsales" target="_blank">更多<em class="iconfont">&#xe621;</em></a></h3>
            
            <div class="book-list">
                <ul>
                    <li class="unfold" data-rid="1">
                        <div class="book-wrap cf">
                            <div class="book-info fl"><h3>NO.1</h3><h4>
                                <a href="/book/8263527304935303" target="_blank" data-eid="qd_A117" data-bid="8263527304935303" title="恰似寒光遇骄阳">恰似寒光遇骄阳</a>
                            </h4>
                                <p class="strong">销量冠军</p>
                                <p class="author">
                                    <a class="type" href="/category/30020_f1_f1_f1_f1_f1_0_1" target="_blank">现代言情</a><i>·</i><a class="writer default">囧囧有妖</a>
                                </p></div>
                            <div class="book-cover">
                                <a class="link" href="/book/8263527304935303" data-eid="qd_A117" target="_blank" data-bid="8263527304935303"><img src="//bookcover.yuewen.com/qdbimg/349573/c_8263527304935303/90" alt="恰似寒光遇骄阳"></a><span></span>
                            </div>
                        </div>
                    </li>
                    
                    <li data-rid="2">
                        <div class="num-box"><span class="num2">2</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/21855922801825904" target="_blank" data-eid="qd_A117" data-bid="21855922801825904" title="摄政王他又在掐我桃花">摄政王他又在掐我桃花</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="3">
                        <div class="num-box"><span class="num3">3</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/24125475801715104" target="_blank" data-eid="qd_A117" data-bid="24125475801715104" title="穿成权臣的首富娇妻">穿成权臣的首富娇妻</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="4">
                        <div class="num-box"><span class="num4">4</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/17536776207350304" target="_blank" data-eid="qd_A117" data-bid="17536776207350304" title="夫人她马甲又轰动全城了">夫人她马甲又轰动全城了</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="5">
                        <div class="num-box"><span class="num5">5</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/25001510901180504" target="_blank" data-eid="qd_A117" data-bid="25001510901180504" title="欢迎来到我的地狱">欢迎来到我的地狱</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="6">
                        <div class="num-box"><span class="num6">6</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/23668280201484904" target="_blank" data-eid="qd_A117" data-bid="23668280201484904" title="宋檀记事">宋檀记事</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="7">
                        <div class="num-box"><span class="num7">7</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/24604915301478504" target="_blank" data-eid="qd_A117" data-bid="24604915301478504" title="大小姐她总是不求上进">大小姐她总是不求上进</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="8">
                        <div class="num-box"><span class="num8">8</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/23745323301951404" target="_blank" data-eid="qd_A117" data-bid="23745323301951404" title="大理寺小饭堂">大理寺小饭堂</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="9">
                        <div class="num-box"><span class="num9">9</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/22455842509184904" target="_blank" data-eid="qd_A117" data-bid="22455842509184904" title="长安好">长安好</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="10">
                        <div class="num-box"><span class="num10">10</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/15953225505698104" target="_blank" data-eid="qd_A117" data-bid="15953225505698104" title="十万个氪金的理由">十万个氪金的理由</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="11">
                        <div class="num-box"><span class="num11">11</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/7036260604114001" target="_blank" data-eid="qd_A117" data-bid="7036260604114001" title="惊世医妃">惊世医妃</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="12">
                        <div class="num-box"><span class="num12">12</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/17755279506421504" target="_blank" data-eid="qd_A117" data-bid="17755279506421504" title="致命偏宠">致命偏宠</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="13">
                        <div class="num-box"><span class="num13">13</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/22436946000359002" target="_blank" data-eid="qd_A117" data-bid="22436946000359002" title="南朝春色">南朝春色</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="14">
                        <div class="num-box"><span class="num14">14</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/22273571609884704" target="_blank" data-eid="qd_A117" data-bid="22273571609884704" title="重生年代：炮灰长姐带妹逆袭">重生年代：炮灰长姐带妹逆袭</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="15">
                        <div class="num-box"><span class="num15">15</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/24533758901917904" target="_blank" data-eid="qd_A117" data-bid="24533758901917904" title="八零大院小可怜是玄学大佬">八零大院小可怜是玄学大佬</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="16">
                        <div class="num-box"><span class="num16">16</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/22567716000017202" target="_blank" data-eid="qd_A117" data-bid="22567716000017202" title="全能修炼师：废柴二小姐">全能修炼师：废柴二小姐</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="17">
                        <div class="num-box"><span class="num17">17</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/7200532503839703" target="_blank" data-eid="qd_A117" data-bid="7200532503839703" title="慕少你老婆虐渣了">慕少你老婆虐渣了</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="18">
                        <div class="num-box"><span class="num18">18</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/7738325503169203" target="_blank" data-eid="qd_A117" data-bid="7738325503169203" title="穿成王爷的小仙女">穿成王爷的小仙女</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="19">
                        <div class="num-box"><span class="num19">19</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/13405417003238804" target="_blank" data-eid="qd_A117" data-bid="13405417003238804" title="重生异能俏娇妻">重生异能俏娇妻</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="20">
                        <div class="num-box"><span class="num20">20</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/18657815901379604" target="_blank" data-eid="qd_A117" data-bid="18657815901379604" title="表哥万福">表哥万福</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                </ul>
            </div>
            
        </div>
        <!-- end 热销榜 -->

        <!-- start 礼物榜 -->
        <div class="rank-list" data-l2="1">
            <h3 class="wrap-title lang">礼物榜<a class="more" href="/rank/reward" target="_blank">更多<em class="iconfont">&#xe621;</em></a></h3>
            
            <div class="book-list">
                <ul>
                    <li class="unfold" data-rid="1">
                        <div class="book-wrap cf">
                            <div class="book-info fl"><h3>NO.1</h3><h4>
                                <a href="/book/8263527304935303" target="_blank" data-eid="qd_A117" data-bid="8263527304935303" title="恰似寒光遇骄阳">恰似寒光遇骄阳</a>
                            </h4>
                                <p class="strong">读者最爱</p>
                                <p class="author">
                                    <a class="type" href="/category/30020_f1_f1_f1_f1_f1_0_1" target="_blank">现代言情</a><i>·</i><a class="writer default">囧囧有妖</a>
                                </p></div>
                            <div class="book-cover">
                                <a class="link" href="/book/8263527304935303" data-eid="qd_A117" target="_blank" data-bid="8263527304935303"><img src="//bookcover.yuewen.com/qdbimg/349573/c_8263527304935303/90" alt="恰似寒光遇骄阳"></a><span></span>
                            </div>
                        </div>
                    </li>
                    
                    <li data-rid="2">
                        <div class="num-box"><span class="num2">2</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/21855922801825904" target="_blank" data-eid="qd_A117" data-bid="21855922801825904" title="摄政王他又在掐我桃花">摄政王他又在掐我桃花</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="3">
                        <div class="num-box"><span class="num3">3</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/22116362000978402" target="_blank" data-eid="qd_A117" data-bid="22116362000978402" title="绝世神医：腹黑大小姐">绝世神医：腹黑大小姐</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="4">
                        <div class="num-box"><span class="num4">4</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/24125475801715104" target="_blank" data-eid="qd_A117" data-bid="24125475801715104" title="穿成权臣的首富娇妻">穿成权臣的首富娇妻</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="5">
                        <div class="num-box"><span class="num5">5</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/3675832204934203" target="_blank" data-eid="qd_A117" data-bid="3675832204934203" title="天医凤九">天医凤九</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="6">
                        <div class="num-box"><span class="num6">6</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/21967813308221904" target="_blank" data-eid="qd_A117" data-bid="21967813308221904" title="国师，陛下又不乖">国师，陛下又不乖</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="7">
                        <div class="num-box"><span class="num7">7</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/25587167609305404" target="_blank" data-eid="qd_A117" data-bid="25587167609305404" title="退婚后咸鱼美人拿了反派剧本">退婚后咸鱼美人拿了反派剧本</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="8">
                        <div class="num-box"><span class="num8">8</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/21942288508637804" target="_blank" data-eid="qd_A117" data-bid="21942288508637804" title="钓系美人在恋综成了万人迷">钓系美人在恋综成了万人迷</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="9">
                        <div class="num-box"><span class="num9">9</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/15903587405066104" target="_blank" data-eid="qd_A117" data-bid="15903587405066104" title="全能大佬又被拆马甲了">全能大佬又被拆马甲了</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="10">
                        <div class="num-box"><span class="num10">10</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/16376378805497104" target="_blank" data-eid="qd_A117" data-bid="16376378805497104" title="打职业后成了团宠">打职业后成了团宠</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="11">
                        <div class="num-box"><span class="num11">11</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/22597403301568004" target="_blank" data-eid="qd_A117" data-bid="22597403301568004" title="我在古代当名师">我在古代当名师</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="12">
                        <div class="num-box"><span class="num12">12</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/10014439503142903" target="_blank" data-eid="qd_A117" data-bid="10014439503142903" title="嘿我来教你谈恋爱">嘿我来教你谈恋爱</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="13">
                        <div class="num-box"><span class="num13">13</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/7200532503839703" target="_blank" data-eid="qd_A117" data-bid="7200532503839703" title="慕少你老婆虐渣了">慕少你老婆虐渣了</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="14">
                        <div class="num-box"><span class="num14">14</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/13992296405132004" target="_blank" data-eid="qd_A117" data-bid="13992296405132004" title="笛上春行录">笛上春行录</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="15">
                        <div class="num-box"><span class="num15">15</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/17155104204051104" target="_blank" data-eid="qd_A117" data-bid="17155104204051104" title="夜寒深深醉思量">夜寒深深醉思量</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="16">
                        <div class="num-box"><span class="num16">16</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/25001510901180504" target="_blank" data-eid="qd_A117" data-bid="25001510901180504" title="欢迎来到我的地狱">欢迎来到我的地狱</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="17">
                        <div class="num-box"><span class="num17">17</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/15496132504523304" target="_blank" data-eid="qd_A117" data-bid="15496132504523304" title="对门的猫爷很高冷">对门的猫爷很高冷</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="18">
                        <div class="num-box"><span class="num18">18</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/4818982104534803" target="_blank" data-eid="qd_A117" data-bid="4818982104534803" title="许你万丈光芒好">许你万丈光芒好</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="19">
                        <div class="num-box"><span class="num19">19</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/16748549005028004" target="_blank" data-eid="qd_A117" data-bid="16748549005028004" title="猕猴桃那些事儿">猕猴桃那些事儿</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                    <li data-rid="20">
                        <div class="num-box"><span class="num20">20</span></div>
                        <div class="name-box">
                            <a class="name long" href="/book/18181204801100204" target="_blank" data-eid="qd_A117" data-bid="18181204801100204" title="剧情都崩了还快什么穿">剧情都崩了还快什么穿</a>
                            <i class="trend">
                                
                                <em class="iconfont">&#xe907;</em>
                                
                            </i>
                        </div>
                    </li>
                    
                </ul>
            </div>
            
        </div>
        <!-- end 礼物榜 -->

        <!-- start 新书点击榜 -->
        <div class="rank-list" data-l2="1">
            <h3 class="wrap-title lang">更新榜<a class="more" href="/rank/update" target="_blank">更多<em class="iconfont">&#xe621;</em></a></h3>
            
            <div class="book-list">
                <ul>
                    <li class="unfold" data-rid="1">
                        <div class="book-wrap cf">
                            <div class="book-info fl"><h3>NO.1</h3><h4>
                                <a href="/book/16234750005145304" target="_blank" data-eid="qd_A117" data-bid="16234750005145304" title="红妆十里花期十年">红妆十里花期十年</a>
                            </h4>
                                <p class="strong">勤更明星</p>
                                <p class="author">
                                    <a class="type" href="/category/30013_f1_f1_f1_f1_f1_0_1" target="_blank">古代言情</a><i>·</i><a class="writer default">明月晞</a>
                                </p></div>
                            <div class="book-cover">
                                <a class="link" href="/book/16234750005145304" data-eid="qd_A117" target="_blank" data-bid="16234750005145304"><img src="//bookcover.yuewen.com/qdbimg/349573/c_16234750005145304/90" alt="红妆十里花期十年"></a><span></span>
                            </div>
                        </div>
                    </li>
                    
                    <li data-rid="2">
                        <div class="num-box"><span class="num2">2</span></div>
                        <div class="name-box">
                            <a class="name" href="/book/26516628909890004" target="_blank" data-eid="qd_A117" data-bid="26516628909890004" title="斗罗之不想成神的我居然成神了">斗罗之不想成神的我居然成神了</a><i class="author">奔跑的椅子</i>
                        </div>
                    </li>
                    
                    <li data-rid="3">
                        <div class="num-box"><span class="num3">3</span></div>
                        <div class="name-box">
                            <a class="name" href="/book/22539098009399204" target="_blank" data-eid="qd_A117" data-bid="22539098009399204" title="国公府大小姐她又美又狂">国公府大小姐她又美又狂</a><i class="author">池上当歌</i>
                        </div>
                    </li>
                    
                    <li data-rid="4">
                        <div class="num-box"><span class="num4">4</span></div>
                        <div class="name-box">
                            <a class="name" href="/book/20406712808675204" target="_blank" data-eid="qd_A117" data-bid="20406712808675204" title="锦鲤弃妇：随身空间养萌娃">锦鲤弃妇：随身空间养萌娃</a><i class="author">轻妩媚</i>
                        </div>
                    </li>
                    
                    <li data-rid="5">
                        <div class="num-box"><span class="num5">5</span></div>
                        <div class="name-box">
                            <a class="name" href="/book/24460101601274904" target="_blank" data-eid="qd_A117" data-bid="24460101601274904" title="穿越星际：我靠能吃喜提上将">穿越星际：我靠能吃喜提上将</a><i class="author">俗人某</i>
                        </div>
                    </li>
                    
                    <li data-rid="6">
                        <div class="num-box"><span class="num6">6</span></div>
                        <div class="name-box">
                            <a class="name" href="/book/16105470104653804" target="_blank" data-eid="qd_A117" data-bid="16105470104653804" title="嫡女虞后">嫡女虞后</a><i class="author">钗娘</i>
                        </div>
                    </li>
                    
                    <li data-rid="7">
                        <div class="num-box"><span class="num7">7</span></div>
                        <div class="name-box">
                            <a class="name" href="/book/24123113709330504" target="_blank" data-eid="qd_A117" data-bid="24123113709330504" title="只对你服软">只对你服软</a><i class="author">圆子儿</i>
                        </div>
                    </li>
                    
                    <li data-rid="8">
                        <div class="num-box"><span class="num8">8</span></div>
                        <div class="name-box">
                            <a class="name" href="/book/26026681401611404" target="_blank" data-eid="qd_A117" data-bid="26026681401611404" title="养猪百头，不如逼太子殿下还钱">养猪百头，不如逼太子殿下还钱</a><i class="author">山人钠thing</i>
                        </div>
                    </li>
                    
                    <li data-rid="9">
                        <div class="num-box"><span class="num9">9</span></div>
                        <div class="name-box">
                            <a class="name" href="/book/11780665304553203" target="_blank" data-eid="qd_A117" data-bid="11780665304553203" title="祥符洞秘闻">祥符洞秘闻</a><i class="author">人生倒师</i>
                        </div>
                    </li>
                    
                    <li data-rid="10">
                        <div class="num-box"><span class="num10">10</span></div>
                        <div class="name-box">
                            <a class="name" href="/book/16097030504861304" target="_blank" data-eid="qd_A117" data-bid="16097030504861304" title="未惊">未惊</a><i class="author">愿卿na</i>
                        </div>
                    </li>
                    
                    <li data-rid="11">
                        <div class="num-box"><span class="num11">11</span></div>
                        <div class="name-box">
                            <a class="name" href="/book/24125475801715104" target="_blank" data-eid="qd_A117" data-bid="24125475801715104" title="穿成权臣的首富娇妻">穿成权臣的首富娇妻</a><i class="author">巧克力派</i>
                        </div>
                    </li>
                    
                    <li data-rid="12">
                        <div class="num-box"><span class="num12">12</span></div>
                        <div class="name-box">
                            <a class="name" href="/book/25506591609037904" target="_blank" data-eid="qd_A117" data-bid="25506591609037904" title="斗罗：唐三带我加入武魂殿">斗罗：唐三带我加入武魂殿</a><i class="author">迷迷瞪瞪呀</i>
                        </div>
                    </li>
                    
                    <li data-rid="13">
                        <div class="num-box"><span class="num13">13</span></div>
                        <div class="name-box">
                            <a class="name" href="/book/13044253003285403" target="_blank" data-eid="qd_A117" data-bid="13044253003285403" title="遗落沧桑">遗落沧桑</a><i class="author">Z沉心</i>
                        </div>
                    </li>
                    
                    <li data-rid="14">
                        <div class="num-box"><span class="num14">14</span></div>
                        <div class="name-box">
                            <a class="name" href="/book/21007922701148404" target="_blank" data-eid="qd_A117" data-bid="21007922701148404" title="拒嫁千金是满级宠夫大佬">拒嫁千金是满级宠夫大佬</a><i class="author">花花果</i>
                        </div>
                    </li>
                    
                    <li data-rid="15">
                        <div class="num-box"><span class="num15">15</span></div>
                        <div class="name-box">
                            <a class="name" href="/book/22790916001388004" target="_blank" data-eid="qd_A117" data-bid="22790916001388004" title="甜疯！冷冰冰的宋律师英年早婚了">甜疯！冷冰冰的宋律师英年早婚了</a><i class="author">果糖酸</i>
                        </div>
                    </li>
                    
                    <li data-rid="16">
                        <div class="num-box"><span class="num16">16</span></div>
                        <div class="name-box">
                            <a class="name" href="/book/13334043403479304" target="_blank" data-eid="qd_A117" data-bid="13334043403479304" title="婚后那几年">婚后那几年</a><i class="author">Y落落</i>
                        </div>
                    </li>
                    
                    <li data-rid="17">
                        <div class="num-box"><span class="num17">17</span></div>
                        <div class="name-box">
                            <a class="name" href="/book/5457374104142201" target="_blank" data-eid="qd_A117" data-bid="5457374104142201" title="铁雪云烟">铁雪云烟</a><i class="author">庞钠文</i>
                        </div>
                    </li>
                    
                    <li data-rid="18">
                        <div class="num-box"><span class="num18">18</span></div>
                        <div class="name-box">
                            <a class="name" href="/book/15376095004100504" target="_blank" data-eid="qd_A117" data-bid="15376095004100504" title="当穿越女重生后">当穿越女重生后</a><i class="author">清绝梦魇</i>
                        </div>
                    </li>
                    
                </ul>
            </div>
            
        </div>
        <!-- end 新书点击榜 -->
    </div>
</div>
        <!-- end 书单排行榜 -->

        <!-- start 新书榜 -->
        
<div class="index-book-wrap finish-rank mb20">
    <div class="inner-wrap cf">
        <!-- start 左侧 -->
        <div class="left-wrap fl">
            <h3 class="wrap-title lang">新书推荐</h3>
            
            <div class="left-info fl" data-l2="1">
                <div class="slide-box">
                    <!-- start 预加载 -->
                    <div class="la-ball-pulse">
                        <span></span>
                        <span></span>
                        <span></span>
                    </div>
                    <!-- end 预加载 -->
                    <ul id="left-slide-01" class="roundabout">
                        
                    </ul>
                </div>
                <!-- start 轮播书介绍 -->
                <div class="info-text">
                    <dl>
                        
                    </dl>
                </div>
                <!-- end 轮播书介绍 -->
            </div>
            <div class="center-book-list fl" data-l2="2">
                <div class="line line1"></div>
                <div class="line line2"></div>
                <ul>
                    
                    <li data-rid="4">
                        <div class="book-img">
                            <a href="/book/34535527007127208" target="_blank" data-eid="qd_A142" data-bid="34535527007127208"><img class="lazy" src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/common/default_book.5968b.png" data-original="//bookcover.yuewen.com/qdbimg/349573/c_34535527007127208/90" alt="替身她掀翻虐恋，霸总他卷爆恋综"></a>
                        </div>
                        <div class="book-info"><h3>
                            <a href="/book/34535527007127208" target="_blank" data-eid="qd_A143" data-bid="34535527007127208" title="替身她掀翻虐恋，霸总他卷爆恋综">替身她掀翻虐恋，霸总他卷爆恋综</a>
                        </h3>
                            <p>【娱乐圈+求生恋综直播+男女主双穿书+发疯抽象+沙雕玩梗+胡言乱语+打脸】【女主全网黑变万人迷+男主从霸总穿成穷光蛋】【脑子有点大病的女明星VS同样脑回路清奇的霸总】霸总贺郢遒穿书了。穿成了一本娱乐圈虐文里的深情男二，刚穿书就被赶出豪门，开局秒变穷光蛋。由俭入奢易，由奢入俭难。为了养活自己，他只能四处打工。没想到接连碰壁，cos司机凶哭了哑巴小姑娘被人呲哒一通就算了。结果在cos牙医给她拔智齿的时</p>
                            <div class="state-box cf">
                                <i>现代言情</i><a class="author default" data-eid="qd_A144"><img src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/ico/user.f22d3.png">卖炸弹的小女孩</a>
                            </div>
                        </div>
                    </li>
                    
                    <li data-rid="5">
                        <div class="book-img">
                            <a href="/book/32936166607247707" target="_blank" data-eid="qd_A142" data-bid="32936166607247707"><img class="lazy" src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/common/default_book.5968b.png" data-original="//bookcover.yuewen.com/qdbimg/349573/c_32936166607247707/90" alt="打赏返现，男神们争着让我当榜一"></a>
                        </div>
                        <div class="book-info"><h3>
                            <a href="/book/32936166607247707" target="_blank" data-eid="qd_A143" data-bid="32936166607247707" title="打赏返现，男神们争着让我当榜一">打赏返现，男神们争着让我当榜一</a>
                        </h3>
                            <p>【多男主、bg、雄竞、非传统神豪文，系统占比不大】你以为这是攻略游戏？不，这是她的理财项目！只因沈昭意绑定了一个离谱系统——给异性花钱就能暴富，但返现比例居然按颜值计算！于是，她被迫开启了一场幕后“精致养鱼，养精致鱼”的实验。在不露脸的赛车手那儿试探性消费，却被对方当成未成年，手把手教她如何申请退款；给高冷禁欲的医学博主刷个华子，换来一句“冲动消费是不正确行为，建议预约一下精神科”；打赏语音厅哄睡</p>
                            <div class="state-box cf">
                                <i>现代言情</i><a class="author default" data-eid="qd_A144"><img src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/ico/user.f22d3.png">眉东</a>
                            </div>
                        </div>
                    </li>
                    
                    <li data-rid="6">
                        <div class="book-img">
                            <a href="/book/34264053204908207" target="_blank" data-eid="qd_A142" data-bid="34264053204908207"><img class="lazy" src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/common/default_book.5968b.png" data-original="//bookcover.yuewen.com/qdbimg/349573/c_34264053204908207/90" alt="女帝成长手册"></a>
                        </div>
                        <div class="book-info"><h3>
                            <a href="/book/34264053204908207" target="_blank" data-eid="qd_A143" data-bid="34264053204908207" title="女帝成长手册">女帝成长手册</a>
                        </h3>
                            <p>穿越成一个爹不疼娘不爱的小可怜，还差点被卖给一个屠夫当填房的时候，国公府来人说她是他们家丢失多年的嫡长女。家里还有一个被收养的假千金。郑清书刚刚打算撸袖子和假千金大战三百回合的时候，结果她成了和皇长子一母同胞的长公主，还拥有开国皇帝才有的天生神力。既然距离皇位那么近了，那她就勉为其难的坐上去吧。</p>
                            <div class="state-box cf">
                                <i>古代言情</i><a class="author default" data-eid="qd_A144"><img src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/ico/user.f22d3.png">熠星宁</a>
                            </div>
                        </div>
                    </li>
                    
                </ul>
            </div>
            
        </div>
        <!-- end 左侧 -->

        <!-- start 右侧 -->
        <div class="right-wrap recent-finish-wrap fr">
            <div class="rank-list" data-l2="3"><h3 class="wrap-title lang">签约作者新书榜<a class="more" href="/rank/newsign" target="_blank">更多<em class="iconfont">&#xe621;</em></a></h3>
                
                <div class="book-list">
                    <ul>
                        <li class="unfold" data-rid="1">
                            <div class="book-wrap cf">
                                <div class="book-info fl">
                                    <h3>NO.1</h3>
                                    <h4>
                                    <a href="/book/26516628909890004" target="_blank" data-eid="qd_A136" data-bid="26516628909890004" title="斗罗之不想成神的我居然成神了">斗罗之不想成神的我居然成神了</a>
                                </h4>
                                    <p class="author">
                                        <a class="type" href="/category/30055_f1_f1_f1_f1_f1_0_1" target="_blank">同人衍生</a><i>·</i><a class="writer default">奔跑的椅子</a>
                                    </p>
                                </div>
                                <div class="book-cover">
                                    <a class="link" href="/book/26516628909890004" target="_blank" data-eid="qd_A136" data-bid="3323048"><img src="//bookcover.yuewen.com/qdbimg/349573/c_26516628909890004/90" alt="斗罗之不想成神的我居然成神了"></a><span></span>
                                </div>
                            </div>
                        </li>
                        
                    </ul>
                </div>
                
            </div>
        </div>
        <!-- end 右侧 -->

    </div>
</div>

        <!-- end 新书榜 -->

        

        <!-- start 人气完本 -->
        
<div class="index-book-wrap finish-rank mb20">
    <div class="inner-wrap cf">
        <!-- start 左侧 -->
        <div class="left-wrap fl">
            <h3 class="wrap-title lang">人气完本</h3>
            
            <div class="left-info fl" data-l2="1">
                <div class="slide-box">
                    <!-- start 预加载 -->
                    <div class="la-ball-pulse">
                        <span></span>
                        <span></span>
                        <span></span>
                    </div>
                    <!-- end 预加载 -->
                    <ul id="left-slide-02" class="roundabout">
                        
                        <li class="book1" data-id="1" data-type="1" data-height="100%" data-rid="1">
                            <a href="/book/29754400704255704" target="_blank"><img class="lazy" src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/common/default_book.5968b.png" data-original="//bookcover.yuewen.com/qdbimg/349573/c_29754400704255704/90" alt="十里芳菲"></a>
                        </li>
                        
                        <li class="book2" data-id="2" data-type="1" data-height="100%" data-rid="2">
                            <a href="/book/31943077703862007" target="_blank"><img class="lazy" src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/common/default_book.5968b.png" data-original="//bookcover.yuewen.com/qdbimg/349573/c_31943077703862007/90" alt="宠妾娇媚，疯批首辅病态占有"></a>
                        </li>
                        
                        <li class="book3" data-id="3" data-type="1" data-height="100%" data-rid="3">
                            <a href="/book/31859940603899908" target="_blank"><img class="lazy" src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/common/default_book.5968b.png" data-original="//bookcover.yuewen.com/qdbimg/349573/c_31859940603899908/90" alt="出马诡契：我的当铺通阴阳"></a>
                        </li>
                        
                    </ul>
                </div>
                <!-- start 轮播书介绍 -->
                <div class="info-text">
                    <dl>
                        
                        <dd data-rid="1">
                            <h3>
                                <a href="/book/29754400704255704" target="_blank" title="十里芳菲">十里芳菲</a>
                            </h3>
                            <p class="author">
                                <a class="default" href="javascript:" target="_blank">西子情</a>
                            </p>
                            <p class="tag"><span class="org">玄幻言情</span><span class="red">已完结</span><span class="blue">152万</span>
                            </p>
                            <p class="intro">
                                昆仑有两宝，一宝玄天境，可预知百年，一宝卫轻蓝，少年天才，承宗门重任。昆仑将这两宝护的紧，跟眼珠子一般。江离声是个修炼废柴，什么都会，什么都不精通，哪一种道，她也修不好，这也就罢了，偏偏她还是个惹事儿精，将宗门上下搅的日夜不得安宁。她师傅护犊子，在她引起众怒，众人发誓要将她踢出宗门时，直接将她送去了昆仑，美其名曰：昆仑规矩严，会教弟子，她去了一定能改造好。后来，江离声不但没被改造好，还闯了大祸，被
                            </p>
                            <a class="red-btn" href="/book/29754400704255704" target="_blank" data-eid="qd_A124" data-bid="">书籍详情</a>
                        </dd>
                        
                        <dd data-rid="2">
                            <h3>
                                <a href="/book/31943077703862007" target="_blank" title="宠妾娇媚，疯批首辅病态占有">宠妾娇媚，疯批首辅病态占有</a>
                            </h3>
                            <p class="author">
                                <a class="default" href="javascript:" target="_blank">沐玖梨</a>
                            </p>
                            <p class="tag"><span class="org">古代言情</span><span class="red">已完结</span><span class="blue">132.74万</span>
                            </p>
                            <p class="intro">
                                【年龄差+地位差+蓄谋已久】尚书府千金苏杳生的美若天仙，却不知道早被当今首辅觊觎多年。世人都以为首辅大人陆怀瑾禁欲高冷，是谪仙般无人可染指的高岭之花。只有苏杳知道，他的皮囊下是疯狂偏执的灵魂。他的骨子里是掠夺，是欲望，是蓄谋已久的强取豪夺。从前，他是恩人，照顾有佳。如今，他是男人，肆意折辱。苏杳衣衫褴褛，双眼恶狠狠瞪着陆怀瑾。“第九十九次了。苏杳，你的记性总是不好。”苏杳嘶吼，“三年了！陆怀瑾！三
                            </p>
                            <a class="red-btn" href="/book/31943077703862007" target="_blank" data-eid="qd_A124" data-bid="">书籍详情</a>
                        </dd>
                        
                        <dd data-rid="3">
                            <h3>
                                <a href="/book/31859940603899908" target="_blank" title="出马诡契：我的当铺通阴阳">出马诡契：我的当铺通阴阳</a>
                            </h3>
                            <p class="author">
                                <a class="default" href="javascript:" target="_blank">葵花岛主阿</a>
                            </p>
                            <p class="tag"><span class="org">悬疑侦探</span><span class="red">已完结</span><span class="blue">99.21万</span>
                            </p>
                            <p class="intro">
                                精神病院的符咒贴了十二年，我成了弟弟续命的“人肉护身符”。直到他18岁考验失败，家里老仙拿来一架天平…“简熹瑶，该你继承祖业了。”接手当铺第一天，客户有点棘手：孕妇鬼没钱还要缝尸，胖鬼典当轮回权只为泡蜘蛛精，最离谱的我爷爷的掌堂狐仙，它竟要抛下我，割尾换姻缘！渐渐我发现，爷爷的堂口供着的是与炼狱的契约，弟弟和家人死后魂魄皆变成了炼狱奴仆。去他的功德！去他的契约！我掀了当铺的天秤，把炼狱凶兽挨个收编
                            </p>
                            <a class="red-btn" href="/book/31859940603899908" target="_blank" data-eid="qd_A124" data-bid="">书籍详情</a>
                        </dd>
                        
                    </dl>
                </div>
                <!-- end 轮播书介绍 -->
            </div>
            <div class="center-book-list fl" data-l2="2">
                <div class="line line1"></div>
                <div class="line line2"></div>
                <ul>
                    
                    <li data-rid="4">
                        <div class="book-img">
                            <a href="/book/23522543001006104" target="_blank" data-eid="qd_A142" data-bid="23522543001006104"><img class="lazy" src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/common/default_book.5968b.png" data-original="//bookcover.yuewen.com/qdbimg/349573/c_23522543001006104/90" alt="我在诡异世界继承神位后"></a>
                        </div>
                        <div class="book-info"><h3>
                            <a href="/book/23522543001006104" target="_blank" data-eid="qd_A143" data-bid="23522543001006104" title="我在诡异世界继承神位后">我在诡异世界继承神位后</a>
                        </h3>
                            <p>【无cp、高智女主、算无遗策、套娃似多马甲、诡怪异世、微克】是作为人去死，还是作为神去浪？这还需要考虑吗？宓八月一直以为穿的是古代种田，某天收获一份神遗才发现是神鬼灵异。得知养了半年的女孩是个未来献身救世的救世主，自己则在收到神遗的当天就会死。宓八月微微一笑，当天就手刃了会害自己身死的罪魁祸首，用阴神的马甲游走灵凡、阴阳各界倒运资源，不断壮大自身和势力。一开始世人眼里，宓八月是一个出身凡俗乡下，穷</p>
                            <div class="state-box cf">
                                <i>玄幻言情</i><a class="author default" data-eid="qd_A144"><img src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/ico/user.f22d3.png">水千澈</a>
                            </div>
                        </div>
                    </li>
                    
                    <li data-rid="5">
                        <div class="book-img">
                            <a href="/book/24055465809174104" target="_blank" data-eid="qd_A142" data-bid="24055465809174104"><img class="lazy" src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/common/default_book.5968b.png" data-original="//bookcover.yuewen.com/qdbimg/349573/c_24055465809174104/90" alt="花醉满堂"></a>
                        </div>
                        <div class="book-info"><h3>
                            <a href="/book/24055465809174104" target="_blank" data-eid="qd_A143" data-bid="24055465809174104" title="花醉满堂">花醉满堂</a>
                        </h3>
                            <p>初时，他说：“江宁郡的小庶女啊，这什么破身份，我不娶！”见过后，他啧啧：“弱不禁风，不堪一折，太弱了，我不要！”当她孤身一人拿着婚书上门，他倚门而立，欠扁地笑，“来让我娶你啊？可是小爷不想英年早婚！”得知她是前来退婚，他脸色彻底黑了，阴沉沉要杀人，“谁给你的胆子敢退小爷的婚？”……苏容觉得，端华郡主怕是眼瞎，这人一身娇纵，哪里值得她为了他要死要活？早知道，她第一次见他时，就把退婚书甩他脸上。———</p>
                            <div class="state-box cf">
                                <i>古代言情</i><a class="author default" data-eid="qd_A144"><img src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/ico/user.f22d3.png">西子情</a>
                            </div>
                        </div>
                    </li>
                    
                    <li data-rid="6">
                        <div class="book-img">
                            <a href="/book/27399823707515004" target="_blank" data-eid="qd_A142" data-bid="27399823707515004"><img class="lazy" src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/common/default_book.5968b.png" data-original="//bookcover.yuewen.com/qdbimg/349573/c_27399823707515004/90" alt="独占偏宠：陆医生他蓄谋已久"></a>
                        </div>
                        <div class="book-info"><h3>
                            <a href="/book/27399823707515004" target="_blank" data-eid="qd_A143" data-bid="27399823707515004" title="独占偏宠：陆医生他蓄谋已久">独占偏宠：陆医生他蓄谋已久</a>
                        </h3>
                            <p>机缘巧合之下，唐苏发现她曾经暗恋的高冷男神就住对门，八年了，他根本不记得她，唐苏只好把小心思收敛起来，装不认识。每次见面，她都中规中矩地喊他陆医生。……某一天，陆寒在午休，唐苏溜进了他办公室。值班护士惊坐起，冲着唐苏一边喊“站住”一边跟了过去。等护士赶到，唐苏坐在椅子上，伸腿勾了下陆寒的腿，撒娇：“陆医生，我腿疼，你给看看？”陆寒退后一步，转头对护士说：“你先出去，我会处理。”护士点头，还体贴地帮</p>
                            <div class="state-box cf">
                                <i>现代言情</i><a class="author default" data-eid="qd_A144"><img src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/ico/user.f22d3.png">格子虫</a>
                            </div>
                        </div>
                    </li>
                    
                    <li data-rid="7">
                        <div class="book-img">
                            <a href="/book/31059868607257307" target="_blank" data-eid="qd_A142" data-bid="31059868607257307"><img class="lazy" src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/common/default_book.5968b.png" data-original="//bookcover.yuewen.com/qdbimg/349573/c_31059868607257307/90" alt="重生年代，福气包在厂区吃瓜看戏"></a>
                        </div>
                        <div class="book-info"><h3>
                            <a href="/book/31059868607257307" target="_blank" data-eid="qd_A143" data-bid="31059868607257307" title="重生年代，福气包在厂区吃瓜看戏">重生年代，福气包在厂区吃瓜看戏</a>
                        </h3>
                            <p>晴天一声响，天空掉下个罗妹妹。罗妹妹爹不亲妈不爱，家中七个娃她是小可怜儿。罗钰一脸懵逼。“我就是穿个马路而已，咋就跑到了吃不饱穿不暖的岁月里？”想想可怜的前世，罗钰淡定地挥手告别。不就是重生么，这有啥，上千本小说她可不是白看的，她经验十足。空间没有系统来凑，就是这个系统有点不太给力，但让她躺平还是没问题的。罗钰挥挥小手离开吸血的小家，快速融入煤矿的大家庭，每天打毛衣快乐地吃瓜看戏，有时还会给自己加</p>
                            <div class="state-box cf">
                                <i>现代言情</i><a class="author default" data-eid="qd_A144"><img src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/ico/user.f22d3.png">爱杀</a>
                            </div>
                        </div>
                    </li>
                    
                    <li data-rid="8">
                        <div class="book-img">
                            <a href="/book/31940915907088808" target="_blank" data-eid="qd_A142" data-bid="31940915907088808"><img class="lazy" src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/common/default_book.5968b.png" data-original="//bookcover.yuewen.com/qdbimg/349573/c_31940915907088808/90" alt="废土种田，分配的对象超给力"></a>
                        </div>
                        <div class="book-info"><h3>
                            <a href="/book/31940915907088808" target="_blank" data-eid="qd_A143" data-bid="31940915907088808" title="废土种田，分配的对象超给力">废土种田，分配的对象超给力</a>
                        </h3>
                            <p>江淼穿越到天灾十年后的废土三年，成了一个孤苦无依的十八岁少女，获得金手指“每日一签”，同时被政府强行分配对象——苏毅。系统要求她建设家园，根据进度解锁不同等级的签到礼物。政府要求他们在外城区生活，每天必须出门淘荒寻找食物或者其他有用的物品卖给交易中心，从而换取积分，积分用来购买政府的食物。江淼——现在的生活比以前好多了，只要努力淘荒，耕种养殖，也不是活不下去，只要这个没见过面的对象不拖后腿就行，实</p>
                            <div class="state-box cf">
                                <i>科幻空间</i><a class="author default" data-eid="qd_A144"><img src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/ico/user.f22d3.png">竹篱清茶</a>
                            </div>
                        </div>
                    </li>
                    
                    <li data-rid="9">
                        <div class="book-img">
                            <a href="/book/32752394307499808" target="_blank" data-eid="qd_A142" data-bid="32752394307499808"><img class="lazy" src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/common/default_book.5968b.png" data-original="//bookcover.yuewen.com/qdbimg/349573/c_32752394307499808/90" alt="当我撞了甲方老板的车"></a>
                        </div>
                        <div class="book-info"><h3>
                            <a href="/book/32752394307499808" target="_blank" data-eid="qd_A143" data-bid="32752394307499808" title="当我撞了甲方老板的车">当我撞了甲方老板的车</a>
                        </h3>
                            <p>祝曲祺中了个大奖。老板听说以后，觉得这姑娘运气好，吉利，于是钦点她陪自己去见客户，洽谈重要合作项目。祝曲祺右眼皮跳个不停，总感觉有什么灾祸等着自己。果不其然——她出车祸了。好消息是，本人毫发无伤。坏消息是，她创了辆劳斯莱斯。事故发生的时候，祝曲祺吓傻了，回过神来赶紧下车去跟人道歉。司机看到惨不忍睹的车尾：“这……怎么处理我也做不了主，得请示老板。”下一瞬，后排的车窗落下，露出一张英俊逼人的脸。祝曲</p>
                            <div class="state-box cf">
                                <i>现代言情</i><a class="author default" data-eid="qd_A144"><img src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/ico/user.f22d3.png">三月棠墨</a>
                            </div>
                        </div>
                    </li>
                    
                </ul>
            </div>
            
        </div>
        <!-- end 左侧 -->

        <!-- start 右侧 -->
        <div class="right-wrap recent-finish-wrap fr">
            <div class="rank-list" data-l2="3"><h3 class="wrap-title lang">完本榜<a class="more" href="/rank/finish" target="_blank">更多<em class="iconfont">&#xe621;</em></a></h3>
                
                <div class="book-list" style="height: 396px; overflow: hidden">
                    <ul>
                        <li class="unfold" data-rid="1">
                            <div class="book-wrap cf">
                                <div class="book-info fl">
                                    <h3>NO.1</h3>
                                    <h4>
                                        <a href="/book/8263527304935303" target="_blank" data-eid="qd_A136" data-bid="8263527304935303" title="恰似寒光遇骄阳">恰似寒光遇骄阳</a>
                                    </h4>
                                    <p class="author">
                                        <a class="type" href="/category/30020_f1_f1_f1_f1_f1_0_1" target="_blank">豪门世家</a><i>·</i><a class="writer default">囧囧有妖</a>
                                    </p>
                                </div>
                                <div class="book-cover">
                                    <a class="link" href="/book/8263527304935303" target="_blank" data-eid="qd_A136" data-bid="3323048"><img src="//bookcover.yuewen.com/qdbimg/349573/c_8263527304935303/90" alt="恰似寒光遇骄阳"></a><span></span>
                                </div>
                            </div>
                        </li>
                        
                        <li data-rid="2">
                            <div class="num-box"><span class="num2">2</span></div>
                            <div class="name-box">
                                <a class="name" href="/book/21855922801825904" target="_blank" data-eid="qd_A117" data-bid="21855922801825904" title="摄政王他又在掐我桃花">摄政王他又在掐我桃花</a><i class="author">花匪</i>
                            </div>
                        </li>
                        
                        <li data-rid="3">
                            <div class="num-box"><span class="num3">3</span></div>
                            <div class="name-box">
                                <a class="name" href="/book/15953225505698104" target="_blank" data-eid="qd_A117" data-bid="15953225505698104" title="十万个氪金的理由">十万个氪金的理由</a><i class="author">墨泠</i>
                            </div>
                        </li>
                        
                        <li data-rid="4">
                            <div class="num-box"><span class="num4">4</span></div>
                            <div class="name-box">
                                <a class="name" href="/book/7036260604114001" target="_blank" data-eid="qd_A117" data-bid="7036260604114001" title="惊世医妃">惊世医妃</a><i class="author">绿依</i>
                            </div>
                        </li>
                        
                        <li data-rid="5">
                            <div class="num-box"><span class="num5">5</span></div>
                            <div class="name-box">
                                <a class="name" href="/book/17755279506421504" target="_blank" data-eid="qd_A117" data-bid="17755279506421504" title="致命偏宠">致命偏宠</a><i class="author">漫西</i>
                            </div>
                        </li>
                        
                        <li data-rid="6">
                            <div class="num-box"><span class="num6">6</span></div>
                            <div class="name-box">
                                <a class="name" href="/book/22436946000359002" target="_blank" data-eid="qd_A117" data-bid="22436946000359002" title="南朝春色">南朝春色</a><i class="author">林家成</i>
                            </div>
                        </li>
                        
                        <li data-rid="7">
                            <div class="num-box"><span class="num7">7</span></div>
                            <div class="name-box">
                                <a class="name" href="/book/24533758901917904" target="_blank" data-eid="qd_A117" data-bid="24533758901917904" title="八零大院小可怜是玄学大佬">八零大院小可怜是玄学大佬</a><i class="author">沸腾的咖啡</i>
                            </div>
                        </li>
                        
                        <li data-rid="8">
                            <div class="num-box"><span class="num8">8</span></div>
                            <div class="name-box">
                                <a class="name" href="/book/22567716000017202" target="_blank" data-eid="qd_A117" data-bid="22567716000017202" title="全能修炼师：废柴二小姐">全能修炼师：废柴二小姐</a><i class="author">阿谁</i>
                            </div>
                        </li>
                        
                        <li data-rid="9">
                            <div class="num-box"><span class="num9">9</span></div>
                            <div class="name-box">
                                <a class="name" href="/book/7738325503169203" target="_blank" data-eid="qd_A117" data-bid="7738325503169203" title="穿成王爷的小仙女">穿成王爷的小仙女</a><i class="author">冰婶</i>
                            </div>
                        </li>
                        
                        <li data-rid="10">
                            <div class="num-box"><span class="num10">10</span></div>
                            <div class="name-box">
                                <a class="name" href="/book/13405417003238804" target="_blank" data-eid="qd_A117" data-bid="13405417003238804" title="重生异能俏娇妻">重生异能俏娇妻</a><i class="author">晏辽</i>
                            </div>
                        </li>
                        
                        <li data-rid="11">
                            <div class="num-box"><span class="num11">11</span></div>
                            <div class="name-box">
                                <a class="name" href="/book/18657815901379604" target="_blank" data-eid="qd_A117" data-bid="18657815901379604" title="表哥万福">表哥万福</a><i class="author">犹似</i>
                            </div>
                        </li>
                        
                        <li data-rid="12">
                            <div class="num-box"><span class="num12">12</span></div>
                            <div class="name-box">
                                <a class="name" href="/book/15488011805011204" target="_blank" data-eid="qd_A117" data-bid="15488011805011204" title="夫人每天都在线打脸">夫人每天都在线打脸</a><i class="author">南之情</i>
                            </div>
                        </li>
                        
                        <li data-rid="13">
                            <div class="num-box"><span class="num13">13</span></div>
                            <div class="name-box">
                                <a class="name" href="/book/6649032704756503" target="_blank" data-eid="qd_A117" data-bid="6649032704756503" title="华姝">华姝</a><i class="author">若相姒</i>
                            </div>
                        </li>
                        
                        <li data-rid="14">
                            <div class="num-box"><span class="num14">14</span></div>
                            <div class="name-box">
                                <a class="name" href="/book/13641088905154304" target="_blank" data-eid="qd_A117" data-bid="13641088905154304" title="女配表示很无辜">女配表示很无辜</a><i class="author">一颗小豌豆呀</i>
                            </div>
                        </li>
                        
                        <li data-rid="15">
                            <div class="num-box"><span class="num15">15</span></div>
                            <div class="name-box">
                                <a class="name" href="/book/3675832204934203" target="_blank" data-eid="qd_A117" data-bid="3675832204934203" title="天医凤九">天医凤九</a><i class="author">凤炅</i>
                            </div>
                        </li>
                        
                        <li data-rid="16">
                            <div class="num-box"><span class="num16">16</span></div>
                            <div class="name-box">
                                <a class="name" href="/book/22148996000646402" target="_blank" data-eid="qd_A117" data-bid="22148996000646402" title="傲娇帝君是神坑">傲娇帝君是神坑</a><i class="author">梵缺</i>
                            </div>
                        </li>
                        
                        <li data-rid="17">
                            <div class="num-box"><span class="num17">17</span></div>
                            <div class="name-box">
                                <a class="name" href="/book/14161390003600304" target="_blank" data-eid="qd_A117" data-bid="14161390003600304" title="反派国师想转正">反派国师想转正</a><i class="author">乌里丑丑</i>
                            </div>
                        </li>
                        
                        <li data-rid="18">
                            <div class="num-box"><span class="num18">18</span></div>
                            <div class="name-box">
                                <a class="name" href="/book/13191263205723504" target="_blank" data-eid="qd_A117" data-bid="13191263205723504" title="本王命不久矣">本王命不久矣</a><i class="author">白小圆</i>
                            </div>
                        </li>
                        
                        <li data-rid="19">
                            <div class="num-box"><span class="num19">19</span></div>
                            <div class="name-box">
                                <a class="name" href="/book/5587047903584103" target="_blank" data-eid="qd_A117" data-bid="5587047903584103" title="锦绣深宫">锦绣深宫</a><i class="author">半枝雪</i>
                            </div>
                        </li>
                        
                        <li data-rid="20">
                            <div class="num-box"><span class="num20">20</span></div>
                            <div class="name-box">
                                <a class="name" href="/book/4532471304373203" target="_blank" data-eid="qd_A117" data-bid="4532471304373203" title="荣医">荣医</a><i class="author">沉舟钓雪</i>
                            </div>
                        </li>
                        
                    </ul>
                </div>
                
            </div>
        </div>
        <!-- end 右侧 -->

    </div>
</div>

        <!-- end 人气完本 -->

        <!-- start 限时免费 -->
        
        <!-- end 限时免费 -->

        <!-- start 热门分类 -->
        
<div class="row-book-wrap mb20">
    <div class="inner-wrap">
        <h3 class="wrap-title lang"></h3>
        <!-- start 热门分类榜单容器 -->
        <div class="hot-book-list-wrap">
            <ul class="mb30 cf">
                <li class="hover-icon">
                    
                    <dl>
                        <dd class="top" data-rid="1">
                            <h6><a href="/xdyq">现代言情</a></h6>
                            <div class="book-wrap cf">
                                <div class="book-info fl">
                                    <h4>
                                        <a href="/book/33902925504420809" target="_blank" data-eid="qd_A117" data-bid="33902925504420809" title="七零娇美人，绑定客运系统开大巴">七零娇美人，绑定客运系统开大巴</a>
                                    </h4>
                                    <p>苗云薇重生回到1976年被设计换掉工作的时候，上辈子她涉世未深，大吵大闹，不仅丢了工作，还被坏人倒打一耙，最终被迫离开城里，蹉跎一生。重生后，她咬牙蛰伏，步步为营，替自己铺一条路，顺道再找个志同道合的男人携手同行。心机堂姐悔得肠子都青了。暗恋对象偷偷找上门，“云薇，其实我最喜欢的是你，是我妈不同意我们在一起我才被迫放弃你，娶了苗雪薇。”苗云薇：“哪来的疯狗乱咬人！别碰瓷！本小姐早就有对象了！”在亲</p>
                                </div>
                                <div class="book-cover">
                                    <a class="link" href="/book/33902925504420809" data-eid="qd_A117" target="_blank" data-bid="/book/33902925504420809"><img src="//bookcover.yuewen.com/qdbimg/349573/c_33902925504420809/90" alt="七零娇美人，绑定客运系统开大巴"></a><span></span>
                                </div>
                            </div>
                        </dd>
                        
                        <dd data-rid="2"><i><a href="/book/34451727903119809" target="_blank">怀了死对头的崽怎么办</a></i></dd>
                        
                        <dd data-rid="3"><i><a href="/book/34268168304005009" target="_blank">暗宠入骨</a></i></dd>
                        
                        <dd data-rid="4"><i><a href="/book/33297668407187507" target="_blank">穿越年代，带着爹妈回乡当宠宝</a></i></dd>
                        
                        <dd data-rid="5"><i><a href="/book/34239097604729507" target="_blank">找回来的大小姐，她是真公主！</a></i></dd>
                        
                    </dl>
                    
                </li>

                <li class="hover-icon">
                    
                    <dl>
                        <dd class="top" data-rid="1">
                            <h6><a href="/gdyq">古代言情</a></h6>
                            <div class="book-wrap cf">
                                <div class="book-info fl">
                                    <h4>
                                        <a href="/book/31943077703862007" target="_blank" data-eid="qd_A117" data-bid="31943077703862007" title="宠妾娇媚，疯批首辅病态占有">宠妾娇媚，疯批首辅病态占有</a>
                                    </h4>
                                    <p>【年龄差+地位差+蓄谋已久】尚书府千金苏杳生的美若天仙，却不知道早被当今首辅觊觎多年。世人都以为首辅大人陆怀瑾禁欲高冷，是谪仙般无人可染指的高岭之花。只有苏杳知道，他的皮囊下是疯狂偏执的灵魂。他的骨子里是掠夺，是欲望，是蓄谋已久的强取豪夺。从前，他是恩人，照顾有佳。如今，他是男人，肆意折辱。苏杳衣衫褴褛，双眼恶狠狠瞪着陆怀瑾。“第九十九次了。苏杳，你的记性总是不好。”苏杳嘶吼，“三年了！陆怀瑾！三</p>
                                </div>
                                <div class="book-cover">
                                    <a class="link" href="/book/31943077703862007" data-eid="qd_A117" target="_blank" data-bid="31943077703862007"><img src="//bookcover.yuewen.com/qdbimg/349573/c_31943077703862007/90" alt="宠妾娇媚，疯批首辅病态占有"></a><span></span>
                                </div>
                            </div>
                        </dd>
                        
                        <dd data-rid="2"><i><a href="/book/33070313504754209" target="_blank">佞娇</a></i></dd>
                        
                        <dd data-rid="3"><i><a href="/book/33487776204601308" target="_blank">殿下，你抢的王妃是顶级大佬</a></i></dd>
                        
                        <dd data-rid="4"><i><a href="/book/33998578304188609" target="_blank">错把福星当炮灰？全家跪求我回头</a></i></dd>
                        
                        <dd data-rid="5"><i><a href="/book/33358861104391807" target="_blank">重生换宗，小可怜被大佬们团宠了</a></i></dd>
                        
                    </dl>
                    
                </li>

                <li class="hover-icon">
                    
                    <dl>
                        <dd class="top" data-rid="1">
                            <h6><a href="/xdyq">豪门总裁</a></h6>
                            <div class="book-wrap cf">
                                <div class="book-info fl">
                                    <h4>
                                        <a href="/book/31701160804734608" target="_blank" data-eid="qd_A117" data-bid="31701160804734608" title="入狱三年后，傅总跪着求原谅">入狱三年后，傅总跪着求原谅</a>
                                    </h4>
                                    <p>她本是豪门千金，从小骄纵妄为，大胆追爱，却被有心之人算计，家族破产，自己锒铛入狱。五年牢狱之灾，让曾经明媚的骄阳大小姐变得懦弱卑贱。出狱后，再度见到那个亲手将她送进监狱的男人——傅钧霆。安诺卑躬屈膝，瑟瑟发抖，只求放过。“傅先生，安诺错了，求您放过。”男人冷漠孤傲。“放过？你杀害欣云的时候，为什么没想过放过她？”“我没有……”男人扼住她的咽喉，一字一句。“安诺，我这辈子都不会放过你！”……可当真相</p>
                                </div>
                                <div class="book-cover">
                                    <a class="link" href="/book/31701160804734608" data-eid="qd_A117" target="_blank" data-bid="/book/31701160804734608"><img src="//bookcover.yuewen.com/qdbimg/349573/c_31701160804734608/90" alt="入狱三年后，傅总跪着求原谅"></a><span></span>
                                </div>
                            </div>
                        </dd>
                        
                        <dd data-rid="2"><i><a href="/book/33841727603369708" target="_blank">明争暗诱</a></i></dd>
                        
                        <dd data-rid="3"><i><a href="/book/33720952303797208" target="_blank">你犯贱我发癫！真千金爆火娱乐圈</a></i></dd>
                        
                        <dd data-rid="4"><i><a href="/book/32399574304205308" target="_blank">京圈太子爷求我给他一个名分</a></i></dd>
                        
                        <dd data-rid="5"><i><a href="/book/34475456603941107" target="_blank">开局离婚，一手烂牌打成王炸</a></i></dd>
                        
                    </dl>
                    
                </li>

                <li class="hover-icon">
                    
                    <dl>
                        <dd class="top" data-rid="1">
                            <h6><a href="/xhxx">玄幻言情</a></h6>
                            <div class="book-wrap cf">
                                <div class="book-info fl">
                                    <h4>
                                        <a href="/book/33878206307202507" target="_blank" data-eid="qd_A117" data-bid="33878206307202507" title="流放神级生育力？摆摊养崽兽夫宠">流放神级生育力？摆摊养崽兽夫宠</a>
                                    </h4>
                                    <p>新书《假扮凶兽白月光，揣崽跑路被亲哭》，欢迎宝宝们入坑～【雄竞修罗场+摆摊+美食+好孕】一觉醒来，末世厨神虞桉穿成兽世恶毒丑雌，不仅把顶级兽人吃干抹净，还孕气爆棚怀上三崽。坏消息：揣着崽即将流放。更坏的消息：流放途中，被迫与她绑定的黑蛇日日想勒死她！天崩开局，好在前世的木系异能和厨神空间跟着来了。看着嗷嗷待哺的崽崽，还有穷到住山洞的一家人，虞桉重操旧业，撸起袖子找食材到处摆摊，打算给美食荒漠的兽世</p>
                                </div>
                                <div class="book-cover">
                                    <a class="link" href="/book/33878206307202507" data-eid="qd_A117" target="_blank" data-bid="/book/33878206307202507"><img src="//bookcover.yuewen.com/qdbimg/349573/c_33878206307202507/90" alt="流放神级生育力？摆摊养崽兽夫宠"></a><span></span>
                                </div>
                            </div>
                        </dd>
                        
                        <dd data-rid="2"><i><a href="/book/33368358307211007" target="_blank">炼银劫</a></i></dd>
                        
                        <dd data-rid="3"><i><a href="/book/33487467507260308" target="_blank">荒古，我助姐姐成荒帝</a></i></dd>
                        
                        <dd data-rid="4"><i><a href="/book/32987172204842907" target="_blank">斗罗2：穿越斗罗之重振天使荣光</a></i></dd>
                        
                        <dd data-rid="5"><i><a href="/book/34021220204341608" target="_blank">假孕成真，阴鸷反派求放过</a></i></dd>
                        
                    </dl>
                    
                </li>
            </ul>

            <ul class="cf">
                <li class="hover-icon">
                    
                    <dl>
                        <dd class="top" data-rid="1">
                            <h6><a href="/gdyq">穿越架空</a></h6>
                            <div class="book-wrap cf">
                                <div class="book-info fl">
                                    <h4>
                                        <a href="/book/32716218104188909" target="_blank" data-eid="qd_A117" data-bid="32716218104188909" title="符针问骨">符针问骨</a>
                                    </h4>
                                    <p>【悬疑推理】➕【大女主】➕【古代法医】➕【朝堂斗争】➕【intj人设】➕【探案烧脑】大周朝唯一的女仵作，楚潇潇，手握“天驼尸刀”，指捻“白骨银针”，以尸骨为证，替亡灵诉语。一具刻满符文的洛阳遗骨，牵扯出父亲枉死的毒草之谜。桩桩诡案背后，皆是权谋倾轧的惊天布局。她剖尸骨，他拆迷局。从长安血莲到南疆蛊影，从玉门冰花到龟兹亡曲……八桩诡谲迷案，步步惊心。且看冷面女仵作携手莽撞王爷，剖开盛世下那不见光的阴</p>
                                </div>
                                <div class="book-cover">
                                    <a class="link" href="/book/32716218104188909" data-eid="qd_A117" target="_blank" data-bid="/book/32716218104188909"><img src="//bookcover.yuewen.com/qdbimg/349573/c_32716218104188909/90" alt="符针问骨"></a><span></span>
                                </div>
                            </div>
                        </dd>
                        
                        <dd data-rid="2"><i><a href="/book/33678225607264009" target="_blank">天降福星，荒年带领全家逆风翻盘</a></i></dd>
                        
                        <dd data-rid="3"><i><a href="/book/34179390403869307" target="_blank">六零年代当圣母？退退退</a></i></dd>
                        
                        <dd data-rid="4"><i><a href="/book/34384315907247108" target="_blank">软萌人鱼幼崽，治愈全星际被团宠</a></i></dd>
                        
                        <dd data-rid="5"><i><a href="/book/33506420507905908" target="_blank">绣卷裁刑</a></i></dd>
                        
                    </dl>
                    
                </li>

                <li class="hover-icon">
                    
                    <dl>
                        <dd class="top" data-rid="1">
                            <h6><a href="/xhxx">仙侠奇缘</a></h6>
                            <div class="book-wrap cf">
                                <div class="book-info fl">
                                    <h4>
                                        <a href="/book/33065112907573409" target="_blank" data-eid="qd_A117" data-bid="33065112907573409" title="悍玉掌宅">悍玉掌宅</a>
                                    </h4>
                                    <p>母仇未雪，渣爹继母虎视眈眈，婆家还想拿捏我这“悍名在外”的准媳妇？笑死，真当我是软柿子？深扒礼法漏洞化身“规则刺客”，钞能力+权谋双开大，锤爆魑魅魍魉！退婚？不，是我踩着他们脸面上青云！直到撞上那位想拿我当棋子的权谋大佬——呵，男人，你想利用的样子真下头。且看虎妻如何反驯“顶级掠食者”，在宅斗权谋场玩出致命心跳！礼法刺客+虎妻驯狼+黑莲花反杀教科书</p>
                                </div>
                                <div class="book-cover">
                                    <a class="link" href="/book/33065112907573409" data-eid="qd_A117" target="_blank" data-bid="/book/33065112907573409"><img src="//bookcover.yuewen.com/qdbimg/349573/c_33065112907573409/90" alt="悍玉掌宅"></a><span></span>
                                </div>
                            </div>
                        </dd>
                        
                        <dd data-rid="2"><i><a href="/book/34300875807228607" target="_blank">奶团上交修仙界，国家爸爸宠上天</a></i></dd>
                        
                        <dd data-rid="3"><i><a href="/book/26825884809236204" target="_blank">师妹的修炼方法它不科学</a></i></dd>
                        
                        <dd data-rid="4"><i><a href="/book/33358861104391807" target="_blank">重生换宗，小可怜被大佬们团宠了</a></i></dd>
                        
                        <dd data-rid="5"><i><a href="/book/33359394903242108" target="_blank">重生嫡女不好惹，她又娇又飒</a></i></dd>
                        
                    </dl>
                    
                </li>

                <li class="hover-icon">
                    
                    <dl>
                        <dd class="top" data-rid="1">
                            <h6><a href="/qcyx">青春游戏</a></h6>
                            <div class="book-wrap cf">
                                <div class="book-info fl">
                                    <h4>
                                        <a href="/book/34487613903355607" target="_blank" data-eid="qd_A117" data-bid="34487613903355607" title="被祖传木阁缩小后，我穿梭时空了">被祖传木阁缩小后，我穿梭时空了</a>
                                    </h4>
                                    <p>即将流落街头的准毕业生陆离，忽然发现了祖传木阁的秘密。穿越到南宋寻找发财机会，莫名成了四明山百姓数代供奉的山神。传说四明山有真神，十里八乡皆知。只是数百年来没人见过山神显灵，山庙渐渐破落。鄞县楼氏楼子义家中数位亲眷相继染上重病，命在旦夕，走投无路之下，想起山神传说。虽君子需敬鬼神而远之，但平生第一次，楼子义希望山神是真有。楼子义带足金银财宝跪在山前许愿：“祈求山神救我楼氏性命。”穷鬼陆离往嘴里塞了</p>
                                </div>
                                <div class="book-cover">
                                    <a class="link" href="/book/34487613903355607" data-eid="qd_A117" target="_blank" data-bid="/book/34487613903355607"><img src="//bookcover.yuewen.com/qdbimg/349573/c_34487613903355607/90" alt="被祖传木阁缩小后，我穿梭时空了"></a><span></span>
                                </div>
                            </div>
                        </dd>
                        
                        <dd data-rid="2"><i><a href="/book/33272127203855009" target="_blank">当怂包穿进现代灵异文中</a></i></dd>
                        
                        <dd data-rid="3"><i><a href="/book/33677264604981408" target="_blank">带着农场去海岛，路人甲她赢麻了</a></i></dd>
                        
                        <dd data-rid="4"><i><a href="/book/33864765103089807" target="_blank">女承母业，我在高校男寝当宿管</a></i></dd>
                        
                        <dd data-rid="5"><i><a href="/book/34459281904034407" target="_blank">神豪千倍返还系统加身的我爽了</a></i></dd>
                        
                    </dl>
                    
                </li>

                <li class="hover-icon">
                    
                    <dl>
                        <dd class="top" data-rid="1">
                            <h6><a href="/lykh">悬疑科幻</a></h6>
                            <div class="book-wrap cf">
                                <div class="book-info fl">
                                    <h4>
                                        <a href="/book/34039794804392909" target="_blank" data-eid="qd_A117" data-bid="34039794804392909" title="我为末世净秽土">我为末世净秽土</a>
                                    </h4>
                                    <p>宁析醒后听到的第一句话就是：“克隆体唤醒成功”—你的存在是为了赎罪……—你的核心使命是净化秽土世界……赎罪？替谁赎罪？原来是200年前的一位姐，觉醒撕裂空间的异能，肆无忌惮的使用，导致联邦的土地上处处都是小世界。宁析穿进小世界哼哧哼哧搞净化。小世界的NPC一句：姐，你回来了？宁析猛然抬头，不对！十二万分的不对！……此书又名《灾变后我长生不死》《人类觉醒从我开始》《克隆人也有春天》《重生后我成了环卫</p>
                                </div>
                                <div class="book-cover">
                                    <a class="link" href="/book/34039794804392909" data-eid="qd_A117" target="_blank" data-bid="/book/34039794804392909"><img src="//bookcover.yuewen.com/qdbimg/349573/c_34039794804392909/90" alt="我为末世净秽土"></a><span></span>
                                </div>
                            </div>
                        </dd>
                        
                        <dd data-rid="2"><i><a href="/book/33733539007278209" target="_blank">天幕直播：带着老祖宗们玩遍诸天</a></i></dd>
                        
                        <dd data-rid="3"><i><a href="/book/33272127203855009" target="_blank">当怂包穿进现代灵异文中</a></i></dd>
                        
                        <dd data-rid="4"><i><a href="/book/33172140007468109" target="_blank">妖书诡闻</a></i></dd>
                        
                        <dd data-rid="5"><i><a href="/book/33298553307684407" target="_blank">意识托管班</a></i></dd>
                        
                    </dl>
                    
                </li>
            </ul>
        </div>
        <!-- start 热门分类榜单容器 -->
    </div>
</div>
        <!-- end 热门分类 -->

        <!-- start 举报 banner -->
        <div class="banner-wrap mb20">
            <a href="https://www.12377.cn" target="_blank" rel="nofollow">
                <img src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/index/report.ca1c9.jpg">
            </a>
        </div>
        <!-- end 举报 banner -->

        <!-- Start 第六屏:最近更新  -->
        
        <!-- End 第六屏:最近更新  -->
    </div>
    <!-- end 首页内容容器 -->

    <!-- start 页脚 -->
    <!--
 * @Author: tangtianlai@tal.com
 * @Date: 2021-10-12 15:07:40
 * @LastEditors: tangtianlai
 * @LastEditTime: 2021-11-25 10:28:07
 * @FilePath: /hongxiu_pc_proj/src/views/layout/footer_index.html
-->
<!-- start 页脚 -->
<div class="footer">
    <!--start 友情链接-->
    <div class="box-center cf">
        <div class="friend-link">
            <em>阅文集团旗下网站：</em>
            <a href="https://www.qidian.com" target="_blank">起点中文网</a>
            <a href="https://book.qq.com" target="_blank">QQ阅读小说</a>
            <a href="https://www.qdmm.com" target="_blank">起点女生网</a>
            <a href="https://chuangshi.qq.com" target="_blank">创世中文网</a>
            <a href="https://yunqi.qq.com" target="_blank">云起书院</a>
            <a href="https://www.hongxiu.com">红袖添香</a>
            <a href="https://www.readnovel.com" target="_blank">小说阅读网</a>
            <a href="https://www.xs8.cn" target="_blank">言情小说吧</a>
            <a href="https://www.xxsy.net" target="_blank">潇湘书院</a>
            <a href="https://m.xiaoshuo.qq.com" target="_blank">QQ阅读男生网</a>
            <a href="https://www.rongshuxia.com" target="_blank">榕树下</a>
            <a href="https://www.xs.cn" target="_blank">小说网</a>
            <a href="https://www.tingbook.com" target="_blank" rel="nofollow">天方听书网</a>
            <a href="https://www.yuewen.com/app.html#appqq" target="_blank" rel="nofollow">QQ阅读</a>
            <a href="https://www.yuewen.com/app.html#appqd" target="_blank" rel="nofollow">起点读书</a>
            <a href="https://www.yuewen.com/app.html#appzj" target="_blank" rel="nofollow">作家助手</a>
            <a href="https://www.webnovel.com" target="_blank" title="起点中文网国际版" rel="nofollow">Webnovel</a>
            <a href="https://aicomic.yuewen.com" target="_blank" title="漫剧助手">漫剧助手</a>
            <a href="https://ac.qq.com" target="_blank" title="腾讯动漫">腾讯动漫</a>
            <a href="/recommendbooklist"></a>
            <a href="/kolquerylist"></a>
        </div>
        <!--end 友情链接-->
        <!--start 页脚菜单-->
        <div class="footer-menu dib-wrap">
            <a href="https://www.yuewen.com" target="_blank" rel="nofollow">关于我们</a>
            <a href="https://www.yuewen.com/#&contact" target="_blank" rel="nofollow">联系我们</a>
            
                <a href="https://help.yuewen.com/helpcenter/pc/menu?siteId=8&amp;cateId=1" target="_blank" rel="nofollow">帮助中心</a>
            
            <a href="https://www.yuewen.com/service.html" target="_blank" rel="nofollow">客服中心</a>
            <a href="https://join.yuewen.com" target="_blank" rel="nofollow">加入我们</a>
            <a href="https://write.qq.com/public/login.html?siteid=6" target="_blank" rel="nofollow">作家专区</a>
            <a href="https://jubao.yuewen.com" target="_blank" rel="nofollow">举报中心</a>
            <a href="https://security.tencent.com/" target="_blank" rel="nofollow">漏洞提交</a>
        </div>
        <!--end 页脚菜单-->
        <!--start 版权-->
        







<div class="copy-right">
    <p><span>Copyright &copy; 1999-2026 www.hongxiu.com All Rights Reserved</span>版权所有 北京红袖添香科技发展有限公司</p>
    <p><a href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502030109" style="display: inline-block;" target="_blank" rel="nofollow"><img src="//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/images/beian.d0289.png" style="float: left;">京公网安备 11010502030109号</a> <a href="https://imgservices-1252317822.image.myqcloud.com/coco/b12102024/2a23647f.9y9f9r.png">增值电信业务经营许可证：京ICP证090200号</a><a href="http://beian.miit.gov.cn/publish/query/indexFirst.action" target="_blank" rel="nofollow">互联网ICP备案号：京ICP备09093681号-1</a> 出版物经营许可证：新出发京零字第 朝180153 号
    </p>
    <p><a href="https://imgservices-1252317822.image.myqcloud.com/coco/b12102024/4cc0ace8.m670gd.png">网络文化经营许可证：京网文〔2024〕1504-075号</a> <a href="https://imgservices-1252317822.image.myqcloud.com/coco/b03042026/869ddf6d.gjxt8r.png" target="_blank">网络出版服务许可证：（署）网出证（京）字第140号</a><a target="_blank" href="https://imgservices-1252317822.image.myqcloud.com/coco/b12102024/6c3a33ff.6fp0yh.png"><span>营业执照</span></a>
    </p>
    <p>请所有作者发布作品时务必遵守国家互联网信息管理办法规定，我们拒绝任何色情小说，一经发现，即作删除！举报电话：010-59357051 举报邮箱：<a href="mailto:ywjubao@yuewen.com">ywjubao@yuewen.com</a></p>
    <p>本站所收录的作品、社区话题、用户评论、用户上传内容或图片等均属用户个人行为。如前述内容侵害您的权益，欢迎举报投诉，一经核实，立即删除，本站不承担任何责任</p>
    <p>联系方式 总机 010-83050798-6000 地址：北京市朝阳区东三环北路27号楼23层(20)2302内05单元</p>
</div>






        <!--end 版权-->

        <!--start 安全中心-->
        
        <div class="safety-box">
            <div class="safety-img dib-wrap">
                <a class="site4" href="http://cyberpolice.mps.gov.cn/wfjb/" target="_blank" rel="nofollow"></a>
                
                <a class="site3" href="https://ss.knet.cn/verifyseal.dll?sn=e17103011010869321wsdl000000&a=1&pa=0.8369620393163408" target="_blank" rel="nofollow"></a>
                
                <a class="site1" href="https://www.12377.cn" target="_blank" rel="nofollow"></a>
                <a class="site2" href="http://www.bjjubao.org.cn/index.html" target="_blank" rel="nofollow"></a>
            </div>
        </div>
        

        

        
        <!--end 安全中心-->
    </div>
</div>
<!-- end 页脚 -->

    <!-- end 页脚 -->
</div>

<!-- start LBF lib -->
<script data-ignore="true" src="//yuxseocdn.yuewen.com/lbf/1.0.4.1/LBF.js?max_age=31536000"></script>

<script>
    LBF.config({"paths":{"site":"//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease/js","static":"//yuxseocdn.yuewen.com/pro/hongxiu_pc/_prelease","common":"//qidian.gtimg.com/common/1.0.1"},"vars":{"theme":"//qidian.gtimg.com/hongxiu/css"},"combo":false,"debug":false});
    LBF.use(['lib.jQuery', 'static/js/index/index.f06f0.js'], function ($, Index) {
        // 页面逻辑入口
        new Index({});
    });
</script>
<!-- end LBF lib -->

<!-- 页面置灰 -->
<!-- <script>
  var time = +new Date()
  if (time < 1672502400000) { // - 2023-1-1
    document.getElementsByTagName('html')[0].style.filter = 'grayscale(100%)'
    document.getElementsByTagName('html')[0].style['-webkit-filter'] = 'grayscale(100%)'
  }
</script> -->

<!--【新增】百度统计配置 -->
<script>
    var _hmt = _hmt || [];
    (function() {
        var hm = document.createElement("script");
        hm.src = "https://hm.baidu.com/hm.js?3ba92f5fe7e3e5ecd3c37df261beed8a";
        var s = document.getElementsByTagName("script")[0]; 
        s.parentNode.insertBefore(hm, s);
    })();
</script>




</body>
</html>
