document.addEventListener('DOMContentLoaded', function() {
    fetch('https://3245-raaaaaaaad-amazonflask-jmvinb0im4v.ws-eu111.gitpod.io/data')
    .then(response => response.json())
    .then(data => {
        console.log(data);
        // Fai qualcosa con i dati, ad esempio visualizzali nella pagina
    })
    .catch(error => {
        console.error('Si è verificato un errore durante la richiesta:', error);
    });
});