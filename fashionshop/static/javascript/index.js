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

    if (form_register_btn != null){
        form_register_btn.addEventListener('click', function(event) {
            register_form.submit()
            
        })
    }


    var logado = document.getElementById("iflog");

    logado.addEventListener('click', (event) => {
        if (logado.classList.contains('True') || logado.classList.contains('true')) {
            event.preventDefault();
            console.log('O usuário está logado.');
        } else {
            console.log('O usuário não está logado.');
        }
    });
    
    // fechando model
    document.getElementById('close').addEventListener('click', function() {
        // Oculta o modal
        document.querySelector('.modal').style.display = 'none';
    });
    

    document.getElementById('iflog').addEventListener('click', function() {
        document.querySelector('.modal').style.display = 'flex'
    })
})
