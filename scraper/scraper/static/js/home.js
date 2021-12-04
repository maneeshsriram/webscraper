$(document).ready(function () {
    $(window).scroll(function () {
        var scroll = $(window).scrollTop();
        if (scroll < 500) {
            $(".navs").css("background", "white");
            $(".nav-links").css("color", "black");
        }
        else if (scroll > 500 && scroll < 1000) {
            $(".navs").css("background", "black");
            $(".nav-links").css("color", "white");

        }
        else if (scroll > 1000 && scroll < 1450) {
            $(".navs").css("background", "#f1c40f");
        }
        else if (scroll > 1450 && scroll < 1900) {
            $(".navs").css("background", "#16a085");
        }
        else {
            $(".navs").css("background", "white");
        }
    })
})