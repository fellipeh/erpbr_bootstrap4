angular.module("app.filters", []).filter("currency", function () {
    return function (number, currencyCode) {
        var currency = {
                USD: "$",
                RUB: ""
            },
            thousand, decimal, format;
        if ($.inArray(currencyCode, ["USD", "RUB"]) >= 0) {
            thousand = " ";
            decimal = ".";
            format = "%s%v";
        }
        else {
            thousand = ".";
            decimal = ",";
            format = "%s%v";
        }

        return accounting.formatMoney(number, "", 2, thousand, decimal, format);
    };
});

// modulo principal
var ngERPbrApp = angular.module("erpbrapp", ['ngResource', 'ui.router', 'ngCookies', 'app.filters',
    'ngTable'])
    .value('$anchorScroll', angular.noop)
    .filter('email', function () {
        return function (input) {
            return input;
        };
    })
    .config(function ($httpProvider, $interpolateProvider) {
        $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
    });

// desativando cache ajax
ngERPbrApp.run(['$rootScope', '$http', '$templateCache', '$state', '$stateParams', '$window', '$cookies',
    function ($rootScope, $http, $templateCache, $state, $stateParams, $window, $cookies) {
        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
        $rootScope.$on('$viewContentLoaded', function () {
            $templateCache.removeAll();
            var state = $state.$current;
            if (state.scrollTo === undefined) {
                $window.scrollTo(0, 0);
            } else {
                var to = 0;
                if (state.scrollTo.id != undefined)
                    to = jQuery(state.scrollTo.id).offset().top;
                if (jQuery($window).scrollTop() == to)
                    return;
                if (state.scrollTo.animated)
                    jQuery(document.body).animate({scrollTop: to});
                else
                    $window.scrollTo(0, to);
            }
        });
    }]);

