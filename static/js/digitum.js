function share_fb($titulo, $link) {
    FB.ui(
        {
            method: 'feed',
            name: 'SoOfertas - O melhor site de ofertas da sua cidade!',
            caption: $titulo,
            description: 'Plataforma de produtos em ofertas, das melhores empresas da sua cidade, tudo em um único lugar!',
            link: $link,
            picture: 'https://www.soofertas.net.br/static/images/logo.png'
        },
        function (response) {
            console.log(response);
        }
    );
}

// tipo: success, error, warning, info, successPopup, errorPopup, warningPopup, infoPopup
function setCookieMensagem(mensagem, tipo) {
    if (mensagem == null)
        mensagem = "Foi identificado um erro.";
    jQuery.cookie("Flash." + jQuery.ucfirst(tipo), mensagem, {path: '/'});
}

// tipo: success, notice, warning, error
function setMensagem(mensagem, tipo) {
    if (mensagem == null)
        mensagem = "Foi identificado um erro.";

    toastr.options = {
        "closeButton": true,
        "debug": false,
        "positionClass": "toast-top-right",
        "onclick": null,
        "showDuration": "1000",
        "hideDuration": "1000",
        "timeOut": "5000",
        "extendedTimeOut": "1000",
        "showEasing": "swing",
        "hideEasing": "linear",
        "showMethod": "fadeIn",
        "hideMethod": "fadeOut"
    };

    if (tipo === 'info') {
        toastr.info(mensagem, "Aviso");
    }
    if (tipo === 'error') {
        toastr.error(mensagem, "Aviso");
    }
    if (tipo === 'notice') {
        toastr.warning(mensagem, "Aviso");
    }
    if (tipo === 'success') {
        toastr.success(mensagem, "Aviso");
    }

    //jQuery().toastmessage('showToast', {
    //    text: mensagem,
    //    closeText: "&times;",
    //    sticky: false,
    //    stayTime: 10000,
    //    position: 'middle-center',
    //    type: tipo
    //});
}
