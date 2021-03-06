ngERPbrApp.controller('lancamentoListCtrl', ['$scope', '$http', '$filter', 'NgTableParams', '$window',
    function ($scope, $http, $filter, NgTableParams, $window) {

        $scope.lista_loaded = false;

        $scope.getResumo = function () {
            return $http.get(DOMAIN + '/api/v1/exec/lancamentos/resumo/').then(function (result) {
                $scope.resumo = result.data;
            }, function (err) {
                console.error(err);
            });
        };

        $scope.getLista = function () {
            return $http.get(DOMAIN + '/api/v1/lancamentos/').then(function (result) {
                return result.data;
            }, function (err) {
                console.error(err);
            });
        };

        $scope.carregaLista = function () {
            $scope.lista_loaded = false;
            $scope.listTable = new NgTableParams({
                page: 1,
                count: 10
            }, {
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

        $scope.editaReg = function ($id, $deb_cred) {
            $scope.lista_loaded = false;

            console.log($id, $deb_cred);

            if ($deb_cred === -1) {
                $window.location.href = (DOMAIN + '/financeiro/lancamento/despesa/' + $id);
                $scope.lista_loaded = true;
            } else {
                $window.location.href = (DOMAIN + '/financeiro/lancamento/receita/' + $id);
                $scope.lista_loaded = true;
            }
        };

        $scope.deleteReg = function ($id) {
            bootbox.confirm("Confirma a exclusão deste registro?", function (result) {
                if (result) {
                    $http.delete(DOMAIN + '/api/v1/lancamentos/' + $id + '/').then(function (result) {
                        setMensagem('Registro Excluído com Sucesso', 'success');
                        $window.location.reload();
                    }, function (result) {
                        setMensagem(result.data.message, 'error');
                    });
                }
            });
        };

        $scope.cancelarReg = function ($id) {
            bootbox.prompt("Digite o motivo do cancelamento, e clique Cancelar para confirmar.", function (result) {
                if (result) {
                    var parameter = JSON.stringify({"lanc_id": $id, motivo: result});
                    $http.post(DOMAIN + '/api/v1/exec/lancamentos/cancelar/', parameter).then(function (result) {
                        setMensagem('Registro Cancelado com Sucesso', 'success');
                        $window.location.reload();
                    }, function (result) {
                        setMensagem(result.data.message, 'error');
                    });
                }
            });
        };

        $scope.fecharReg = function ($id) {
            bootbox.confirm("Confirma o fechamento deste registro?", function (result) {
                if (result) {
                    var parameter = JSON.stringify({"lanc_id": $id});
                    $http.post(DOMAIN + '/api/v1/exec/lancamentos/fechar/', parameter).then(function (result) {
                        setMensagem('Registro Fechado com Sucesso', 'success');
                        $window.location.reload();
                    }, function (result) {
                        setMensagem(result.data.message, 'error');
                    });
                }
            });
        };

        $scope.regVencido = function ($data) {
            var q = new Date();
            var m = q.getMonth() + 1;
            var d = q.getDay();
            var y = q.getFullYear();
            var date = new Date(y, m, d);
            mydate = new Date($data);
            return (date > mydate);
        };

    }
]);


ngERPbrApp.controller('receberFormCtrl', ['$scope', '$http', '$window', function ($scope, $http, $window) {
    $scope.form = {
        vlr_bruto: 0.00,
        vlr_juros: 0.00,
        vlr_desc: 0.00,
        vlr_liq: 0.00,
        parcelado: false
    };

    $scope.exibirParcelamento = false;

    $scope.$watch("form.vlr_bruto", function (newValue, oldValue) {
        if (newValue !== oldValue) {
            if (typeof(newValue) !== "string") {
                $scope.form.vlr_bruto = 0;
            }
            $scope.form.vlr_liq = parseFloat($scope.form.vlr_bruto.replace(/,/g, '')) + parseFloat($scope.form.vlr_juros.replace(/,/g, '')) - parseFloat($scope.form.vlr_desc.replace(/,/g, ''));
        }
    });
    $scope.$watch("form.vlr_juros", function (newValue, oldValue) {
        if (newValue !== oldValue) {
            if (typeof(newValue) !== "string") {
                $scope.form.vlr_juros = 0;
            }
            $scope.form.vlr_liq = parseFloat($scope.form.vlr_bruto.replace(/,/g, '')) + parseFloat($scope.form.vlr_juros.replace(/,/g, '')) - parseFloat($scope.form.vlr_desc.replace(/,/g, ''));
        }
    });
    $scope.$watch("form.vlr_desc", function (newValue, oldValue) {
        if (newValue !== oldValue) {
            if (typeof(newValue) !== "string") {
                $scope.form.vlr_desc = 0;
            }
            $scope.form.vlr_liq = parseFloat($scope.form.vlr_bruto.replace(/,/g, '')) + parseFloat($scope.form.vlr_juros.replace(/,/g, '')) - parseFloat($scope.form.vlr_desc.replace(/,/g, ''));
        }
    });

    $scope.init = function (p_vlr_bruto, p_vlr_juros, p_vlr_desc, p_vlr_liq, p_parcelado) {
        $scope.form.vlr_bruto = p_vlr_bruto;
        $scope.form.vlr_juros = p_vlr_juros;
        $scope.form.vlr_desc = p_vlr_desc;
        $scope.form.vlr_liq = p_vlr_liq;
        $scope.form.parcelado = p_parcelado === "True";
    };
}]);