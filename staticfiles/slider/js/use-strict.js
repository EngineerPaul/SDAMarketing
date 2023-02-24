(function ($) {
    "use strict";

    $(function () {
        var masterslider_a304 = new MasterSlider();

        // slider controls
        masterslider_a304.control('arrows', { autohide: false, overVideo: true });
        // slider setup
        masterslider_a304.setup("MS63f870388a304", {
            width: 1650,
            height: 165,
            minHeight: 0,
            space: 0,
            start: 1,
            grabCursor: true,
            swipe: true,
            mouse: true,
            layout: "boxed",
            wheel: false,
            autoplay: false,
            instantStartLayers: false,
            loop: false,
            shuffle: false,
            preload: 0,
            heightLimit: true,
            autoHeight: false,
            smoothHeight: true,
            endPause: false,
            overPause: true,
            fillMode: "fill",
            centerControls: true,
            startOnAppear: false,
            layersMode: "center",
            hideLayers: false,
            fullscreenMargin: 0,
            speed: 20,
            dir: "h",
            parallaxMode: 'swipe',
            view: "basic"
        });


        window.masterslider_instances = window.masterslider_instances || [];
        window.masterslider_instances.push(masterslider_a304);
    });

})(jQuery);