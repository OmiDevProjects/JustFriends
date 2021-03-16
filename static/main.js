$(document).ready(function () {
    $(".ui.toggle.button").click(function () {
        $(".mobile.only.grid .ui.vertical.menu").toggle(100);
    });

    $(".ui.dropdown").dropdown();
    $('.message .close')
        .on('click', function () {
            $(this)
                .closest('.message')
                .transition('fade');
        });

    $('.ui.accordion')
        .accordion();

    $('.profile_1')
        .transition('pulse')
      ;
      
    $('.add-posts')
      .transition('pulse')
    ;

    $('.suggesstions')
      .transition('tada')
    ;

    $('.friends_online_list')
      .transition('tada')
    ;

    $('.post-image')
    .transition('flash')
    ;

    $('.following')
        .transition('tada')
        ;

    $('.followers')
    .transition('tada')
    ;

    $('.friends')
    .transition('tada')
    ;

    $('.total_post')
    .transition('tada')
    ;
    // $('.message')
    //     .transition('fly right', {
    //         duration: '20s',
    //     });

});

$('[data-modal-target]')
    .popup({
        inline: true,
        position: 'right center',
        target: '[data-modal]',
        // title: 'My favorite dog',
        // content: 'My favorite dog would like other dogs as much as themselves'
    });

$('[data-modal-target]').on('click', function () {
    var target = $(this).data('modal-target');
    $('[data-modal="' + target + '"]').modal('show');
})

const startit = () => {
    setTimeout(function () {
        console.log("start");
        confetti.start();
    }, 500);
};

const stopit = () => {
    setTimeout(function () {
        console.log("stop");
        confetti.stop();
    }, 1200);
};

startit();
stopit();

function startheart() {
    const startit = () => {
        setTimeout(function () {
            console.log("start");
            confetti.start();
        }, 500);
    };

    const stopit = () => {
        setTimeout(function () {
            console.log("stop");
            confetti.stop();
        }, 500);
    };

    const id = document.getElementById('post');

    $('.autumn.leaf').transition('tada');
    startit();
    stopit();
}

$(function () {
    $('textarea').emoji({
        button: '&#x1F642;',
        place: 'after',
        listCSS: {
            position: 'relative',
            padding: '20px',
            border: 'none',
            display: 'none',
        },
        emojis: ['&#x1F642;', '&#x1F641;', '&#x1f600;', '&#x1f601;', '&#x1f602;', '&#x1f603;',
            '&#x1f604;', '&#x1f605;', '&#x1f606;', '&#x1f607;', '&#x1f608;', '&#x1f609;',
            '&#x1f60a;', '&#x1f60b;', '&#x1f60c;', '&#x1f60d;', '&#x1f60e;', '&#x1f60f;',
            '&#x1f610;', '&#x1f611;', '&#x1f612;', '&#x1f613;', '&#x1f614;', '&#x1f615;',
            '&#x1f616;', '&#x1f617;', '&#x1f618;', '&#x1f619;', '&#x1f61a;', '&#x1f61b;',
            '&#x1f61c;', '&#x1f61d;', '&#x1f61e;', '&#x1f61f;', '&#x1f620;', '&#x1f621;',
            '&#x1f622;', '&#x1f623;', '&#x1f624;', '&#x1f625;', '&#x1f626;', '&#x1f627;',
            '&#x1f628;', '&#x1f629;', '&#x1f62a;', '&#x1f62b;', '&#x1f62c;', '&#x1f62d;',
            '&#x1f62e;', '&#x1f62f;', '&#x1f630;', '&#x1f631;', '&#x1f632;', '&#x1f633;',
            '&#x1f634;', '&#x1f635;', '&#x1f636;', '&#x1f637;', '&#x1f638;', '&#x1f639;',
            '&#x1f63a;', '&#x1f63b;', '&#x1f63c;', '&#x1f63d;', '&#x1f63e;', '&#x1f63f;',
            '&#x1f640;', '&#x1f643;', '&#x1f4a9;', '&#x1f644;', '&#x2620;', '&#x1F44C;',
            '&#x1F44D;', '&#x1F44E;', '&#x1F648;', '&#x1F649;', '&#x1F64A;', '&#x1f64b;',
            '&#x1F911;', '&#x1F921;', '&#x1F922;', '&#x1F915;', '&#x1F912;', '&#x1F47B;',
            '&#x1F467;', '&#x1F466;', '&#x1F575;', '&#x1F482;', '&#x1F473;', '&#x1F385;',
            '&#x1F934;', '&#x1F470;', '&#x1F935;', '&#x1F930;', '&#x1F483;', '&#x1F57A;',
            '&#x1F46F;', '&#x1F46C;', '&#x1F46B;', '&#x1F48F;', '&#x1F46A;', '&#x1F4AA;',
            '&#x1F448;', '&#x1F449;', '&#x261D;', '&#x1F595;', '&#x270C;', '&#x1F91E;',
            '&#x1F918;',
            '&#x1F590;', '&#x270B;', '&#x1F44C;', '&#x1F44D;', '&#x1F44E;', '&#x1F44A;',
            '&#x1F44B;',
            '&#x1F44F;', '&#x270D;', '&#x1F64C;', '&#x1F91D;', '&#x1F442;', '&#x1F444;',
            '&#x1F48B;',
            '&#x1F498;', '&#x1F493;', '&#x1F495;', '&#x1F5A4;', '&#x1F48C;', '&#x1F455;',
            '&#x1F456;',
            '&#x1F457;', '&#x1F454;', '&#x1F453;', '&#x1F45C;', '&#x1F451;', '&#x1F452;',
            '&#x1F45E;',
            '&#x1F393;', '&#x1F48D;', '&#x1F405;', '&#x1F418;', '&#x1F413;', '&#x1F40D;',
            '&#x1F98E;',
            '&#x1F40A;', '&#x1F419;', '&#x1F980;', '&#x1F98B;', '&#x1F339;', '&#x1F332;',
            '&#x1F34C;',
            '&#x1F349;', '&#x1F347;', '&#x1F340;', '&#x1F34E;', '&#x1F351;', '&#x1F352;',
            '&#x1F353;',
            '&#x1F368;', '&#x1F382;', '&#x1F36B;', '&#x1F36C;', '&#x1F37E;', '&#x1F377;',
            '&#x1F37A;',
            '&#x1F942;', '&#x1F30F;', '&#x1F30B;', '&#x1F3E1;', '&#x1F3E5;', '&#x1F3E6;',
            '	&#x1F3E8;',
            '&#x1F69A;', '&#x1F697;'
        ]
    });
})
