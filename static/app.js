function onClickMenu(){
	document.getElementById("menu").classList.toggle("change");
	document.getElementById("nav").classList.toggle("change");
	document.getElementById("social").classList.toggle("change");
	document.getElementById("menu-bg").classList.toggle("change-bg");
}


/*carousel*/
$(document).ready(function(){
	$(".slider").slick({
		infinite: true,
		arrows: false,
		dots: false,
		autoplay: false,
		speed: 800,
		slidesToShow: 1,
		slidesToScroll: 1,
		});
	
		//ticking machine
		var percentTime;
		var tick;
		var time = 1;
		var progressBarIndex = 0;
	
		$('.progressBarContainer .progressBar').each(function(index) {
			var progress = "<div class='inProgress inProgress" + index + "'></div>";
			$(this).html(progress);
		});
	
		function startProgressbar() {
			resetProgressbar();
			percentTime = 0;
			tick = setInterval(interval, 10);
		}
	
		function interval() {
			if (($('.slider .slick-track div[data-slick-index="' + progressBarIndex + '"]').attr("aria-hidden")) === "true") {
				progressBarIndex = $('.slider .slick-track div[aria-hidden="false"]').data("slickIndex");
				startProgressbar();
			} else {
				percentTime += 1 / (time + 5);
				$('.inProgress' + progressBarIndex).css({
					height: percentTime + "%"
				});
				if (percentTime >= 100) {
					$('.single-item').slick('slickNext');
					progressBarIndex++;
					if (progressBarIndex > 2) {
						progressBarIndex = 0;
					}
					startProgressbar();
				}
			}
		}
	
		function resetProgressbar() {
			$('.inProgress').css({
				height: 0 + '%'
			});
			clearInterval(tick);
		}
		startProgressbar();
		// End ticking machine
	
		$('.progressBarContainer div').click(function () {
			clearInterval(tick);
			var goToThisIndex = $(this).find("span").data("slickIndex");
			$('.single-item').slick('slickGoTo', goToThisIndex, false);
			startProgressbar();
		});
})
$(document).ready(function(){
	

	$(".sliderm").slick({
		infinite: true,
		arrows: false,
		dots: false,
		autoplay: false,
		speed: 800,
		slidesToShow: 1,
		slidesToScroll: 1,
		});
	
		//ticking machine
		var percentTime;
		var tick;
		var time = 1;
		var progressBarIndex = 0;

	//mobile view
	
		$('.progressBarmContainer .progressBar').each(function(index) {
			var progress = "<div class='minProgress minProgress" + index + "'></div>";
			$(this).html(progress);
		});
	
		function mstartProgressbar() {
			mresetProgressbar();
			percentTime = 0;
			tick = setInterval(minterval, 10);
		}
	
		function minterval() {
			if (($('.slider .slick-track div[data-slick-index="' + progressBarIndex + '"]').attr("aria-hidden")) === "true") {
				progressBarIndex = $('.slider .slick-track div[aria-hidden="false"]').data("slickIndex");
				mstartProgressbar();
			} else {
				percentTime += 1 / (time + 5);
				$('.minProgress' + progressBarIndex).css({
					width: percentTime + "%"
				});
				if (percentTime >= 100) {
					$('.single-item').slick('slickNext');
					progressBarIndex++;
					if (progressBarIndex > 2) {
						progressBarIndex = 0;
					}
					mstartProgressbar();
				}
			}
		}
	
		function mresetProgressbar() {
			$('.minProgress').css({
				width: 0 + '%'
			});
			clearInterval(tick);
		}
		mstartProgressbar();
		// End ticking machine
	
		$('.progressBarmContainer div').click(function () {
			clearInterval(tick);
			var goToThisIndex = $(this).find("span").data("slickIndex");
			$('.single-item').slick('slickGoTo', goToThisIndex, false);
			mstartProgressbar();
		});
	
		
});

//profile page

$(document).ready(function(){
	// When page loads...:
	$("div.content .profind").hide(); // Hide all content
  
	/* Check for hashtag in url */
	if (window.location.hash.length>0) {
		console.log(window.location.hash);
		/*find the menu item with this hashtag*/
		$( ".profnav li a" ).each(function() {
			if ( $( this ).attr("href") == window.location.hash )
				$( this ).parent().addClass("current").show(); // Activate page in menu
		});
		$(window.location.hash).fadeIn(); // Fade in the active page content
	}
	else { /* no hashtag: */
	  $(".profnav li:first").addClass("current").show(); // Activate first page
	  $("div.content div:first").show(); // Show first page content
	}

	// On Click Event (within list-element!)
	$(".profnav li").click(function() {
		$(".profnav li").removeClass("current"); // Remove any active class
		$(this).addClass("current"); // Add "current" class to selected page
		
		$("div.content .profind").hide(); // Hide all content

    // Find the href attribute value to identify the active page:
		var activePage = $(this).find("a").attr("href"); 
		$(activePage).fadeIn(); // Fade in the active page
	}); // end click method
	
}); // end $(document).ready method

//profiles nav
$(document).ready(function(){
	$(".al").removeClass('invisible');
	$(".core").addClass('invisible');
	$(".ci").addClass('invisible');
	$(".design").addClass('invisible');
	$(".fin").addClass('invisible');
	$(".it").addClass('invisible');
	$(".manc").addClass('invisible');
	$(".man").addClass('invisible');
	$(".re").addClass('invisible');
	$(".strat").addClass('invisible');
	$(".other").addClass('invisible');
});
$("#al").click(function(){
	$(".al").removeClass('invisible');
	$(".core").addClass('invisible');
	$(".ci").addClass('invisible');
	$(".design").addClass('invisible');
	$(".fin").addClass('invisible');
	$(".it").addClass('invisible');
	$(".manc").addClass('invisible');
	$(".man").addClass('invisible');
	$(".re").addClass('invisible');
	$(".strat").addClass('invisible');
	$(".other").addClass('invisible');
})
$("#core").click(function(){
	$(".al").addClass('invisible');
	$(".core").removeClass('invisible');
	$(".ci").addClass('invisible');
	$(".design").addClass('invisible');
	$(".fin").addClass('invisible');
	$(".it").addClass('invisible');
	$(".manc").addClass('invisible');
	$(".man").addClass('invisible');
	$(".re").addClass('invisible');
	$(".strat").addClass('invisible');
	$(".other").addClass('invisible');
})
$("#ci").click(function(){
	$(".al").addClass('invisible');
	$(".core").addClass('invisible');
	$(".ci").removeClass('invisible');
	$(".design").addClass('invisible');
	$(".fin").addClass('invisible');
	$(".it").addClass('invisible');
	$(".manc").addClass('invisible');
	$(".man").addClass('invisible');
	$(".re").addClass('invisible');
	$(".strat").addClass('invisible');
	$(".other").addClass('invisible');
})
$("#design").click(function(){
	$(".al").addClass('invisible');
	$(".core").addClass('invisible');
	$(".ci").addClass('invisible');
	$(".design").removeClass('invisible');
	$(".fin").addClass('invisible');
	$(".it").addClass('invisible');
	$(".manc").addClass('invisible');
	$(".man").addClass('invisible');
	$(".re").addClass('invisible');
	$(".strat").addClass('invisible');
	$(".other").addClass('invisible');
})
$("#fin").click(function(){
	$(".al").addClass('invisible');
	$(".core").addClass('invisible');
	$(".ci").addClass('invisible');
	$(".design").addClass('invisible');
	$(".fin").removeClass('invisible');
	$(".it").addClass('invisible');
	$(".manc").addClass('invisible');
	$(".man").addClass('invisible');
	$(".re").addClass('invisible');
	$(".strat").addClass('invisible');
	$(".other").addClass('invisible');
})
$("#it").click(function(){
	$(".al").addClass('invisible');
	$(".core").addClass('invisible');
	$(".ci").addClass('invisible');
	$(".design").addClass('invisible');
	$(".fin").addClass('invisible');
	$(".it").removeClass('invisible');
	$(".manc").addClass('invisible');
	$(".man").addClass('invisible');
	$(".re").addClass('invisible');
	$(".strat").addClass('invisible');
	$(".other").addClass('invisible');
})
$("#manc").click(function(){
	$(".al").addClass('invisible');
	$(".core").addClass('invisible');
	$(".ci").addClass('invisible');
	$(".design").addClass('invisible');
	$(".fin").addClass('invisible');
	$(".it").addClass('invisible');
	$(".manc").removeClass('invisible');
	$(".man").addClass('invisible');
	$(".re").addClass('invisible');
	$(".strat").addClass('invisible');
	$(".other").addClass('invisible');
})
$("#man").click(function(){
	$(".al").addClass('invisible');
	$(".core").addClass('invisible');
	$(".ci").addClass('invisible');
	$(".design").addClass('invisible');
	$(".fin").addClass('invisible');
	$(".it").addClass('invisible');
	$(".manc").addClass('invisible');
	$(".man").removeClass('invisible');
	$(".re").addClass('invisible');
	$(".strat").addClass('invisible');
	$(".other").addClass('invisible');
})
$("#re").click(function(){
	$(".al").addClass('invisible');
	$(".core").addClass('invisible');
	$(".ci").addClass('invisible');
	$(".design").addClass('invisible');
	$(".fin").addClass('invisible');
	$(".it").addClass('invisible');
	$(".manc").addClass('invisible');
	$(".man").addClass('invisible');
	$(".re").removeClass('invisible');
	$(".strat").addClass('invisible');
	$(".other").addClass('invisible');
})
$("#strat").click(function(){
	$(".al").addClass('invisible');
	$(".core").addClass('invisible');
	$(".ci").addClass('invisible');
	$(".design").addClass('invisible');
	$(".fin").addClass('invisible');
	$(".it").addClass('invisible');
	$(".manc").addClass('invisible');
	$(".man").addClass('invisible');
	$(".re").addClass('invisible');
	$(".strat").removeClass('invisible');
	$(".other").addClass('invisible');
})
$("#other").click(function(){
	$(".al").addClass('invisible');
	$(".core").addClass('invisible');
	$(".ci").addClass('invisible');
	$(".design").addClass('invisible');
	$(".fin").addClass('invisible');
	$(".it").addClass('invisible');
	$(".manc").addClass('invisible');
	$(".man").addClass('invisible');
	$(".re").addClass('invisible');
	$(".strat").addClass('invisible');
	$(".other").removeClass('invisible');
})
	