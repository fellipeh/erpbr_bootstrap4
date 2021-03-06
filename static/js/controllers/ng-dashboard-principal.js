ngERPbrApp.controller('dashboardPrincipalCtrl', ['$scope', '$http', '$filter', 'NgTableParams', '$window',
    function ($scope, $http, $filter, NgTableParams, $window) {

        $scope.lista_loaded = false;


        $scope.getLista = function () {
            return $http.get(APIURL + '/get/dashboard/').then(function (result) {
                return result.data;
            }, function (err) {
                console.error(err);
            });
        };

        $scope.carregaLista = function () {
            console.log("Carregando dashboard...");
            $scope.lista_loaded = false;
            $scope.getLista().then(
                function (data) {
                    $scope.data = data;
                    $scope.lista_loaded = true;
                    console.log($scope.data);
                    return $scope.data;
                });

        };


    }
]);
