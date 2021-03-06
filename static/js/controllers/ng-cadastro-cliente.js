ngERPbrApp.controller('clientesListCtrl', ['$scope', '$http', '$filter', '$location', '$window', 'NgTableParams',
    function ($scope, $http, $filter, $location, $window, NgTableParams) {

        $scope.lista_loaded = false;

        $scope.getStatusSelect = function () {
            return [{id: "", title: "-----"}, {id: true, title: "Ativo"}, {id: false, title: "Inativo"}];
        };

        $scope.getLista = function () {
            return $http.get(DOMAIN + '/api/v1/clientes/').then(function (result) {
                return result.data;
            }, function (err) {
                console.error(err);
            });
        };

        $scope.carregaLista = function () {
            $scope.listTable = new NgTableParams({
                page: 1,
                count: 10
            }, {
                // total: $scope.lista.length,
                getData: function (params) {
                    $scope.getLista().then(
                        function (data) {
                            $scope.lista = data;
                            $scope.data = params.sorting() ? $filter('orderBy')($scope.lista, params.orderBy()) : $scope.lista;
                            $scope.data = params.filter() ? $filter('filter')($scope.data, params.filter()) : $scope.data;
                            $scope.data = $scope.data.slice((params.page() - 1) * params.count(), params.page() * params.count());
                            $scope.lista_loaded = true;
                            return $scope.data;
                        });
                }
            });

        };
        $scope.editaReg = function ($id) {
            $scope.lista_loaded = false;
            $window.location.href = (DOMAIN + '/cadastro/clientes/' + $id);
        };

        $scope.deleteReg = function ($id) {
            bootbox.confirm("Confirma a exclusão deste registro?", function (result) {
                if (result) {
                    console.log('Excluindo...');

                    $http.delete(DOMAIN + '/api/v1/clientes' + $id + '/').then(function (result) {
                        setMensagem('Registro Excluído com Sucesso', 'success');
                        $location.reload();
                    }, function (err) {
                        console.error(err);
                        setMensagem('Erro ao excluir o registro.', 'error');
                    });
                }
            });
        };

    }
]);

ngERPbrApp.controller('clientesFormCtrl', ['$scope', '$http', '$filter', '$location', '$window', 'NgTableParams',
    function ($scope, $http, $filter, $location, $window, NgTableParams) {

        $scope.form = {
            tipo_pessoa: 'PF'
        };

        $scope.getValores = function ($tp_pessoa) {
            $scope.form.tipo_pessoa = $tp_pessoa;
        }
    }
]);
