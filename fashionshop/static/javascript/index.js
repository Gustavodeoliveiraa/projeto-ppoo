document.addEventListener('DOMContentLoaded', function() {

    var input = document.getElementById('search')

    var form = document.getElementById('search_input')
    if (input != null){

        input.addEventListener("keypress", (event)=> {
            if (event.key === "Enter") {
                form.submit()
            }
        })
    }

    // categorias

    var form_categorie = document.querySelectorAll('.cate');

    form_categorie.forEach(form => {
        form.addEventListener('click', function(event) {
            event.preventDefault();
            this.submit();
            this.scrollIntoView({ behavior: 'smooth', block: 'center' });
        });
    });


    // enviando form de registro
    var form_register_btn = document.getElementById('btn-register')
    var register_form = document.getElementById('register-form')

    form_register_btn.addEventListener('click', function(event) {
        register_form.submit()
        console.log('aaaaaaaaaaaaaaaaaaaaaaa')
        
    })


})