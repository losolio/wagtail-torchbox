$(document).ready(function(){tbx.heroImages(),tbx.mobileMenu(),tbx.loadMore(),tbx.clipThru(),tbx.scrollEvents(),tbx.map(),tbx.signUp()});var tbx={heroImages:function(){function e(){n.removeClass("initial-load")}function t(e){o.not(e).removeClass(i),a.removeClass(i)}function s(e){r=e.data("name"),e.addClass(i),l.find('[data-name="'+r+'"]').addClass(i)}var o=$(".featured-case-studies li"),n=$(".home-hero"),l=$(".feature-images"),a=$(".feature-image"),i="active",r=null;o.mouseenter(function(){e(),t($(this)),s($(this))})},mobileMenu:function(){function e(){o.removeClass(i),n.removeClass(l),setTimeout(function(){s.removeClass(a)},500)}function t(e){s.addClass(a),n.addClass(l),o.each(function(){e=$(this),e.addClass(i)})}var s=$(".bleed"),o=s.find("li"),n=$(".menu-button"),l="twist",a="visible out-animation",i="show";n.click(function(){n.hasClass(l)?e():t($(this))}),$(window).on("resize",function(){e()})},loadMore:function(){var e=$(".clients"),t=e.find("button"),s=$(".clients ul"),o="visible",n="Load more",l="Show less";t.click(function(){var e=$(this);s.hasClass(o)?(s.removeClass(o),setTimeout(function(){e.html(n)},900)):(s.addClass(o),setTimeout(function(){e.html(l)},1300))})},scrollEvents:function(){$(window).on("scroll",function(){var e=$(".about-text"),t=$(".hero-text"),s=$(window).scrollTop(),o="stop";!function(){s>=335?t.addClass(o):t.removeClass(o)}(),function(){s>=465?e.addClass(o):e.removeClass(o)}(),function(){var e=285,t=$(".text-content"),s=Math.abs($(document).scrollTop()+60),e=340;s<=e&&(paddingTop=s),t.css({paddingTop:paddingTop})}()})},clipThru:function(){$("#tester-unique").clipthru({autoUpdate:!0,autoUpdateInterval:30})},map:function(){function e(){var e={zoom:4,scrollwheel:!1,center:new google.maps.LatLng(45,(-30)),styles:[{featureType:"all",elementType:"labels.text.fill",stylers:[{saturation:36},{color:"#000000"},{lightness:40}]},{featureType:"all",elementType:"labels.text.stroke",stylers:[{visibility:"on"},{color:"#000000"},{lightness:16}]},{featureType:"all",elementType:"labels.icon",stylers:[{visibility:"off"}]},{featureType:"administrative",elementType:"geometry.fill",stylers:[{lightness:"69"}]},{featureType:"administrative",elementType:"geometry.stroke",stylers:[{color:"#000000"},{lightness:17},{weight:1.2}]},{featureType:"administrative.country",elementType:"geometry",stylers:[{lightness:"35"}]},{featureType:"administrative.country",elementType:"geometry.fill",stylers:[{lightness:"1"}]},{featureType:"administrative.province",elementType:"geometry.fill",stylers:[{weight:"3.94"},{lightness:"45"}]},{featureType:"landscape",elementType:"geometry",stylers:[{color:"#000000"},{lightness:20}]},{featureType:"poi",elementType:"geometry",stylers:[{color:"#000000"},{lightness:21}]},{featureType:"road.highway",elementType:"geometry.fill",stylers:[{color:"#000000"},{lightness:17}]},{featureType:"road.highway",elementType:"geometry.stroke",stylers:[{color:"#000000"},{lightness:29},{weight:.2}]},{featureType:"road.arterial",elementType:"geometry",stylers:[{color:"#000000"},{lightness:18}]},{featureType:"road.local",elementType:"geometry",stylers:[{color:"#000000"},{lightness:16}]},{featureType:"transit",elementType:"geometry",stylers:[{color:"#000000"},{lightness:19}]},{featureType:"water",elementType:"geometry",stylers:[{color:"#000000"},{lightness:17}]}]},t=document.getElementById("map"),s=new google.maps.Map(t,e);new google.maps.Marker({position:new google.maps.LatLng(51.858469,(-1.480863)),map:s,title:"Oxford",icon:"/static/torchbox/images/pin.png"}),new google.maps.Marker({position:new google.maps.LatLng(51.454814,(-2.597802)),map:s,title:"Bristol",icon:"/static/torchbox/images/pin.png"}),new google.maps.Marker({position:new google.maps.LatLng(39.950865,(-75.14559)),map:s,title:"PHILADELPHIA",icon:"/static/torchbox/images/pin.png"})}"#map".length&&google.maps.event.addDomListener(window,"load",e)},signUp:function(){}};