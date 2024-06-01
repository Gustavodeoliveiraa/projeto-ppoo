var input = document.getElementById('search')

var form = document.getElementById('search_input')

input.addEventListener("keypress", (event)=> {
    if (event.key === "Enter") {
        form.submit()
    }
})


// categorias

var form_categorie = document.querySelectorAll('.cate');

form_categorie.forEach(form => {
    form.addEventListener('click', function(event) {
        event.preventDefault();
        this.submit();
        this.scrollIntoView({ behavior: 'smooth', block: 'center' });
    });
});

