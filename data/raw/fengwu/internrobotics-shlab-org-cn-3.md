# Source: https://internrobotics.shlab.org.cn/

> 抓取日期: 2026-08-26

---

<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="utf-8" />
	<title>Intern Robotics</title>
	<meta name="keywords" content="Intern Robotics" />
	<meta name="description" content="Intern Robotics" />
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
	<meta name="viewport"
		content="width=device-width,initial-scale=1,maximum-scale=1,minimum-scale=1,user-scalable=no,viewport-fit=cover">
	<meta name="format-detection" content="telephone=no">
	<!-- animate动画 -->
	<link rel="stylesheet" href="css/animate.min.css">
	<!-- 样式初始化 -->
	<link rel="stylesheet" href="css/reset.css">
	<!-- flex布局 -->
	<link rel="stylesheet" href="css/flex.css">
	<!-- swiper -->
	<link rel="stylesheet" href="plugins/swiper/swiper-bundle.min.css">
	<!-- aos -->
	<link rel="stylesheet" href="plugins/aos/aos.css">
	<!-- 自定义样式 -->
	<script>
		document.write('<link rel="stylesheet" href="css/style.css?' + Math.floor(Date.now() / 1000) + '">');
	</script>
	<!-- 暗黑模式 -->
	<script>
		document.write('<link rel="stylesheet" href="css/style-black.css?' + Math.floor(Date.now() / 1000) + '">');
	</script>
	<!-- wap端兼容样式 -->
	<script>
		document.write('<link rel="stylesheet" href="css/style-wap.css?' + Math.floor(Date.now() / 1000) + '">');
	</script>
	<!-- <link rel="shortcut icon" type="image/png" href="favicon.ico" /> -->
	<!-- 图片懒加载 -->
	<script src="plugins/lazy/lazysizes.min.js"></script>
	<!-- gsap -->
	<script src="plugins/gsap/gsap.min.js"></script>
	<script src="plugins/gsap/ScrollTrigger.min.js"></script>
</head>

<body name="black">
	<div class="g-doc">
		<!-- 头部 -->
		<div id="header" class="g-hd">
			<!-- logo -->
			<div class="m-logo ">
				<a href="index.html"><img class="u-logo lazyload" data-src="imgs/logo.webp"></a>
				<div class="m-pc m-pc-menu">
					<div class="menu">
						<ul>
							<li><a class="first haslink" href="index.html">首页</a></li>
							<li><a class="first haslink" href="viewpoint.html">NEWS</a></li>
							<li><a class="first" href="javascript:void()">科学研究</a>
								<div class="submenu">
									<a href="aigc.html">具身AIGC</a>
									<a href="largemodel.html">具身大模型</a>
								</div>
							</li>

							<li><a class="first" href="javascript:void()">全栈引擎</a>
								<div class="submenu">
									<a href="platform.html">仿真引擎</a>
									<a href="opendataset.html">数据引擎</a>
									<a href="toolchain.html">训测引擎</a>
								</div>
							</li>
							<li><a class="first" href="javascript:void()">平台生态</a>
								<div class="submenu">
									<a href="activity.html">活动比赛</a>
									<a href="developer.html">开发者社区</a>
									<a href="plan.html">光合计划</a>
								</div>
							</li>
							<li><a class="first haslink" href="aboutus.html">关于我们</a>

							</li>
						</ul>
						<div class="develop">
							<a href="https://github.com/InternRobotics" target="_blank">
								<img src="imgs/pic_59.svg">
							</a>
							<a href="https://huggingface.co/InternRobotics" target="_blank">
								<img src="imgs/pic_119.webp"></a>
						</div>
					</div>
				</div>
				<div class="m-wap m-wap-btn" @click="showWapMenu"><img class="lazyload" data-src="imgs/menu.svg"></div>
			</div>
			<!-- 菜单 -->
			<!-- wap显示 增加v-cloak,可以保持元素隐藏直到Vue实例编译结束,防止页面加载时页面先显示再隐藏,采用自定义动画的方式-->
			<transition name="custom-classes-transition" enter-active-class="animated slideInRight"
				leave-active-class="animated slideOutRight" v-cloak>
				<div class="m-wap m-wap-menu" v-if="isMenuVisible">
					<div class="u-closed" @click="closeMenu"><img class=" lazyload" data-src="imgs/close.svg">
					</div>
					<div class="display_flex flex-direction_column">
						<ul class="display_flex flex-direction_column">
							<li><a class="first" href="index.html">首页</a></li>
							<li><a class="first" href="viewpoint.html">NEWS</a></li>
							<li><a class="first" href="javascript:void()">科学研究</a></li>
							<li><a class="second" href="aigc.html">- 具身AIGC</a></li>
							<li><a class="second" href="largemodel.html">- 具身大模型</a></li>
							<li><a class="first" href="javascript:void()">全栈引擎</a></li>
							<li><a class="second" href="platform.html">- 仿真引擎</a></li>
							<li><a class="second" href="opendataset.html">- 数据引擎</a></li>
							<li><a class="second" href="toolchain.html">- 训测引擎</a></li>
							<li><a class="first" href="javascript:void()">平台生态</a></li>
							<li><a class="second" href="activity.html">- 活动比赛</a></li>
							<li><a class="second" href="developer.html">- 开发者社区</a></li>
							<li><a class="second" href="plan.html">- 光合计划</a></li>
							<li><a class="first" href="aboutus.html">关于我们</a></li>
						</ul>
					</div>
				</div>
			</transition>
		</div>
		<!-- swiper -->
		<div class="m-banner">
			<!-- banner处引导向下滚动的图标-->
			<div class="m-mousebox display_flex justify-content_flex-center">
				<div class="mousebox">
					<img src="imgs/mouse_01.png">
				</div>
			</div>
			<!-- Swiper -->
			<div class="swiper mySwiper1">
				<div class="swiper-wrapper">
					<div class="swiper-slide">
						<div class="slide-inner display_flex  align-items_center"
							style="background-image:url(imgs/banner/banner_01.webp)">
							<div class="introbox">
								<div class="intro">
									<h2 class="u-h2 u-h2-sy">『书生』具身全栈引擎</h2>
									<p class="u-p2">Intern Robotics</p>
									<p class="u-p3">连续多日登顶HuggingFace Robotics Trending榜</p>
									<!-- <p class="u-p4">Launch of Intern Robotics: Embodied AI Foundation Engine</p> -->
									<a class="u-more3" href="largemodel.html"><span>更多开源周成果详情</span></a>
								</div>
							</div>

						</div>
						<!-- 动画光束 -->
						<div class="m-shadow">dsafsdfsdfsdfsd</div>
					</div>
					<div class="swiper-slide">
						<div class="slide-inner display_flex align-items_center"
							style="background-image:url(imgs/banner/banner_02.webp)">
							<div class="introbox">
								<div class="intro">
									<h2 class="u-h2">仿真引擎</h2>
									<p class="u-p4">Simulation Engine</p>
									<p class="u-p">构建虚实交融的“工作空间”</p>
									<a class="u-more3 u-more3-1" href="platform.html"><span>了解更多</span></a>
								</div>
							</div>
						</div>
					</div>
					<div class="swiper-slide">
						<div class="slide-inner display_flex  align-items_center"
							style="background-image:url(imgs/banner/banner_03.webp)">


							<div class="introbox">
								<div class="intro">
									<h2 class="u-h2">数据引擎</h2>
									<p class="u-p4">Data Engine</p>
									<p class="u-p">打造高质量、低成本的“数据工厂”</p>
									<a class="u-more3 u-more3-1" href="opendataset.html"><span>了解更多</span></a>
								</div>
							</div>


						</div>
					</div>
					<div class="swiper-slide">
						<div class="slide-inner display_flex  align-items_center"
							style="background-image:url(imgs/banner/banner_04.webp)">
							<div class="introbox">
								<div class="intro">
									<h2 class="u-h2">具身 训测引擎</h2>
									<p class="u-p4">Training and Evaluation Engine</p>
									<p class="u-p">提供模块化、可扩展的模型“训练场”</p>
									<a class="u-more3 u-more3-1" href="toolchain.html"><span>了解更多</span></a>
								</div>
							</div>


						</div>
					</div>
				</div>
				<!-- Add Pagination -->
				<div class="swiper-pagination"></div>
				<!-- Navigation -->
				<div class="swiper-button-next"></div>
				<div class="swiper-button-prev"></div>
			</div>
		</div>
		<!-- 中部 -->
		<div id="main" class="g-bd">
			<!-- 研究方向 -->
			<section class="display_flex flex-direction_column align-items_center" data-aos="fade">


				<div class="m-title display_flex justify-content_flex-justify">
					<div>
						<div class="display_flex align-items_center flex-wrap">
							<h2>
								具身全栈引擎
							</h2>
							<img class="u-img" src="imgs/logo.webp">
						</div>
						<p>Intern Robotics</p>
					</div>
					<!-- <div>
						<div class="u-more"><a href="#">More</a></div>
					</div> -->
				</div>
				<div class="m-list1">
					<h2>书生具身智能全栈引擎作为面向具身智能的一体化基础设施平台，创新性地融合仿真引擎、通用基座模型、专用工具链与硬件接口，构建“感知-想象-执行”闭环，驱动“一脑多形”的高效协同作业，具有低成本、高效率、强泛化等特点
					</h2>
					<div class="itembox m-effect2">
						<a href="platform.html">
							<div class="item">
								<div class="imgbox">
									<img src="imgs/black/index_01.svg">
									<img style="opacity: 0;" src="imgs/black/index_01_1.svg">
									<img style="opacity: 0;" src="imgs/black/index_01_2.svg">
								</div>
								<h3>仿真引擎</h3>
								<!-- <p>Simulation Engine</p> -->
								<p>构建虚实交融的“工作空间”</p>
							</div>
						</a>
						<a href="opendataset.html">
							<div class="item">
								<div class="imgbox">
									<img class="lazyload" data-src="imgs/black/index_02.svg">
									<img style="opacity: 0;" src="imgs/black/index_02_1.svg">
									<img style="opacity: 0;" src="imgs/black/index_02_2.svg">
								</div>
								<h3>数据引擎</h3>
								<!-- <p>Data Engine</p> -->
								<p>打造高质量、低成本的“数据工厂”</p>
							</div>
						</a>
						<a href="toolchain.html">
							<div class="item">
								<div class="imgbox">
									<img class="lazyload" data-src="imgs/black/index_03.svg">
									<img style="opacity: 0;" src="imgs/black/index_03_1.svg">
									<img style="opacity: 0;" src="imgs/black/index_03_2.svg">
								</div>
								<h3>训测引擎</h3>
								<!-- <p>Training and Evaluation Engine</p> -->
								<p>提供模块化、可扩展的模型“训练场”</p>
							</div>
						</a>
					</div>

				</div>
			</section>
			<!-- 研究成果 -->
			<section class="display_flex flex-direction_column align-items_center" data-aos="fade">


				<div class="m-title display_flex justify-content_flex-justify">
					<div>
						<h2>
							最新研究成果
						</h2>
						<p>Latest Research</p>
					</div>
					<!-- <div>
						<div class="u-more"><a href="#">More</a></div>
					</div> -->
				</div>


				<div class="m-list3">
					<a href="largemodel.html">
						<div class="item">
							<div class="tips">
								<div>
									<img src="imgs/black/index_07.svg"><span>InternVLA-N1</span>
								</div>
							</div>
							<h2>导航大模型</h2>
							<div class="imgbox">
								<img class="u-img lazyload" data-src="imgs/black/1.webp" v-ratio-resize="0.5625">
								<!-- <img class="u-play" onclick="showVideoLayer(VIDEO_BASE_URL+'host.mp4')"
								src="imgs/black/index_06.png"> -->
								<div class="shadow"></div>

							</div>
							<p>低成本高效率训练空间智能大脑，实现国际领先的空间推理与导航能力</p>

						</div>
					</a><a href="largemodel.html">
						<div class="item">
							<div class="tips">
								<div>
									<img src="imgs/black/index_08.svg"><span>InternHumanoid</span>
								</div>
							</div>
							<h2>人形运动智能模型</h2>
							<div class="imgbox">
								<img class="u-img lazyload" data-src="imgs/black/2.webp" v-ratio-resize="0.5625">
								<div class="shadow"></div>

							</div>
							<p>实现从“基础运动”到“全身控制”再到“移动操作”的技能跃迁，显著增强机器人操控能力</p>

						</div>
					</a><a href="aigc.html">
						<div class="item">
							<div class="tips">
								<div>
									<img src="imgs/black/index_10.svg"><span>InternWorldModel</span>
								</div>
							</div>
							<h2>4D世界模型</h2>
							<div class="imgbox">
								<img class="u-img lazyload" data-src="imgs/black/4.webp" v-ratio-resize="0.5625">
								<div class="shadow"></div>
							</div>
							<p>首创“重建-预测-规划”一体化框架，支持目标导向视觉规划与动作条件视频生成</p>
						</div>
					</a>
					<a href="javecript:;">
						<div class="item">
							<div class="tips">
								<div>
									<img src="imgs/black/index_08.svg"><span>Coming Soon</span>
								</div>
							</div>
							<h2 style="opacity: 0;">Coming Soon</h2>
							<div class="imgbox">
								<img class="u-img lazyload" data-src="imgs/default1.webp" v-ratio-resize="0.5625">
								<div class="shadow"></div>

							</div>
							<p style="opacity: 0;">Coming Soon</p>

						</div>
					</a>
				</div>
			</section>
			<!-- 生态活动 -->
			<section class="display_flex flex-direction_column align-items_center" data-aos="fade">

				<div class="m-title display_flex justify-content_flex-justify">
					<div>
						<h2>
							最近新闻
						</h2>
						<p>Latest News</p>
					</div>
					<div>
						<div class="u-more"><a href="activity.html">More</a></div>
					</div>
				</div>

				<div class="m-list2">

					<a :href="item.link" v-for="(item, index) in activityList" :key="index">
						<div class="item">
							<div class="imgbox"><img class="u-img lazyload" :src="item.image" v-ratio-resize="0.7512">
								<span class="tips">{{ item.tip }}</span>
								<div class="intro">
									<p>{{ item.intro }}</p>
								</div>
							</div>
							<div class="txtbox">
								<h2>
									{{ item.title }}
								</h2>
								<div class="display_flex justify-content_flex-justify align-items_center">
									<p>{{ item.location }}</p>
									<p>{{ item.date }}</p>
								</div>

							</div>
						</div>
					</a>


				</div>



			</section>

		</div>
		<!-- 尾部 -->
		<div class="g-ft display_flex flex-direction_column align-items_center justify-content_flex-justify">
			<div class="m-ft">
				<img class="u-img1 lazyload" data-src="imgs/logo.webp">
				<div class="itembox">
					<!-- <div class="item">
						<h3>合作方：</h3>
						<p><span>合作方</span><span>合作方</span><span>合作方</span><span>合作方</span></p>
					</div> -->
					<div class="item">
						<h3>联系我们：</h3>
						<a href="mailto:embodiedai@pjlab.org.cn">embodiedai@pjlab.org.cn</a>
					</div>
					<div class="item">
						<h3>备案信息：</h3>
						<p>沪ICP备2021009351号-1</p>
					</div>
				</div>
			</div>

		</div>
	</div>
	<!-- 视频弹层 -->
	<div id="videoModal" class="m-modal">
		<!-- 关闭按钮 -->
		<span class="close" onclick="closeVideoLayer()">&times;</span>
		<div class="display_flex justify-content_flex-center align-items_center">

			<div class="modal-content" data-aos="zoom-in" data-aos-delay="300">

				<video id="videoPlayer" controls autoplay>
					<source src="" type="video/mp4">
					您的浏览器不支持视频播放。
				</video>
			</div>
		</div>

	</div>
	<!-- jquery -->
	<script src="plugins/jquery/jquery.min.js"></script>
	<!-- vue -->
	<script src="plugins/vue/vue.global.prod.js"></script>
	<!-- swiper -->
	<script src="plugins/swiper/swiper-bundle.min.js"></script>
	<!-- layui -->
	<script src="plugins/layui/layui.js"></script>
	<!-- aos -->
	<script src="plugins/aos/aos.js"></script>
	<script src="js/common.js?20250812"></script>
	<script>
		// 公共图片需要按照比例进行裁切时，需要vue代码，注册自定义指令在common.js中
		// 3、vue研究方向
		const mainApp = createApp({
			data() {
				return {
					activityList: [
						{
							image: "imgs/black/index_11.webp",
							tip: "研讨",
							intro: "汇聚机器人学习、计算机视觉与语言建模等领域的顶尖专家，共同探索多模态、交互式具身基础模型的前沿解决方案",
							title: "IROS 2025 物理世界中的多模态机器人学习研讨会",
							location: "中国·杭州",
							date: "2025.10.20",
							link: "https://internrobotics.shlab.org.cn/workshop/2025/"
						},
						{
							image: "imgs/black/index_12.webp",
							tip: "比赛",
							intro: "冀此次活动汇聚全球研究员与从业者，共同探多模态机器人学习前沿领域，为智能机器人未来的发展筑基",
							title: "IROS 2025 “桃源”与真实世界机器人学习挑战赛",
							location: "中国·杭州",
							date: "2025.10.20",
							link: "https://internrobotics.shlab.org.cn/challenge/2025/"
						},
						{
							image: "imgs/black/index_13.webp",
							tip: "生态",
							intro: "依托上海AI实验室，联动产学研用多方力量，共建开放共融的“物理智能”生态，推动智能体模型的迭代和落地",
							title: "光合计划启动",
							location: "中国·上海",
							date: "2025.7.27",
							link: "plan.html"
						},
						{
							image: "imgs/black/index_14.webp",
							tip: "大会",
							intro: "以“智能时代·同球共济”为主题，汇聚全球AI领袖思想与合作，重磅发布具身智能最新研究成果",
							title: "2025 WAIC 科学前沿大会",
							location: "中国·上海",
							date: "2025.7.27",
							link: "https://www.worldaic.com.cn/en/"
						},
					]

				};
			},
			watch: {

			},
			mounted() {

			},
			beforeUnmount() {

			},
			methods: {


			}
		})

		// 注册自定义指令
		mainApp.directive('ratio-resize', ratioResizeDirective);
		// 挂载应用
		mainApp.mount("#main");

		$(document).ready(function () {

			// 首页轮播图的创建光束动画
			gsap.to(".m-shadow", {
				x: "150vw",           // 水平移动到右侧
				scale: 3,
				duration: 3,
				repeat: - 1,           // 无限重复
				yoyo: false,           // 来回播放
				ease: "sine.inOut", // 缓动效果
			});

			$('.m-effect2 a').each(function () {
				const $a = $(this);
				const $imgBox = $a.find('.imgbox');
				const $images = $imgBox.find('img');
				let currentIndex = 0;
				let animation;

				function startImageAnimation() {
					// 清除旧动画
					if (animation) {
						animation.kill();
					}

					// 创建新的 GSAP Timeline
					animation = gsap.timeline({ repeat: -1 }); // 无限循环

					$images.each(function (index) {
						animation.to($images, {
							opacity: 0,
							visibility: 'hidden',
							duration: 0.1
						}, index * 0.1); // 每隔 0.2s 隐藏所有图

						animation.to($(this), {
							opacity: 1,
							visibility: 'visible',
							duration: 0.1
						}, index * 0.1); // 显示当前图
					});
				}

				function stopImageAnimation() {
					if (animation) {
						animation.kill();
						animation = null;
					}

					// 恢复只显示第一张图
					$images.css({ opacity: 0, visibility: 'hidden' });
					$images.eq(0).css({ opacity: 1, visibility: 'visible' });
				}

				$a.on('mouseenter', startImageAnimation);
				$a.on('mouseleave', stopImageAnimation);
			});
		});


	</script>
</body>

</html>