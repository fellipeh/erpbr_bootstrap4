ngERPbrApp.controller('fornecedorFormCtrl', ['$scope', '$http', '$filter', '$location', '$window', 'NgTableParams',
    function ($scope, $http, $filter, $location, $window, NgTableParams) {

        $scope.form = {
            tipo_pessoa: 'PF'
        };

        $scope.getValores = function ($tp_pessoa) {
            $scope.form.tipo_pessoa = $tp_pessoa;
        }
    }
]);
