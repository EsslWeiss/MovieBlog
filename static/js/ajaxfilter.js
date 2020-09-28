function ajaxSend(url, params) {
    // Отправляем запрос
    fetch(`${url}?${params}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
        .then(response => response.json())
        .then(json => render(json))
        .catch(error => console.error(error))
}

const forms = document.querySelector('form[name=filter]');

forms.addEventListener('submit', function (e) {
    // Получаем данные из формы
    e.preventDefault();
    let url = this.action;
    let params = new URLSearchParams(new FormData(this)).toString();
    ajaxSend(url, params);
});

function render(data) {
    // Рендер шаблона
    let template = Hogan.compile(html);
    let output = template.render(data);

    const div = document.querySelector('.filmsfilter');
    div.innerHTML = output;
}

let html = '\
{{#films}}\
    <div id="filmscontent">\
            <div style="margin-left: 100px;" class="card">\
              <a href="#">\
                <div class="img1"><img src="/media/{{ image }}">{{ title }}</div>\
                <div class="img2"></div>\
                <div class="title">\
                <a style="color: #DAF7A6;" href="/{{ url }}/">{{ title }}</a>\
                </div>\
                <a href="/{{ url }}/"><div class="catagory">{{ category }}\
                <i class="fas fa-film"></i>\
                </div>\
                </a>\
                <a href="#">\
                <div class="views">20211  <i class="far fa-eye"></i> </div>\
                </a>\
              </a>\
            </div>\
        </div>\
{{/films}}'
