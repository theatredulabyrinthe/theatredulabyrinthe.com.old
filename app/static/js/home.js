const N = 5;

function loadHome() {
    if (!document.getElementById("home-carousel")) return;
    let cont = document.getElementById("home-carousel");

    while (cont.firstChild) {
        cont.removeChild(cont.firstChild);
    }

    let div = document.createElement('div');
    div.classList.add('carousel-inner');

    for (let i = 1; i < N + 1; i++) {
        let item = document.createElement('item');
        item.classList.add('carousel-item');

        if (i == 1) {
            item.classList.add('active');
        }

        let img = document.createElement('img');
        img.classList.add('d-block', 'w-100');
        img.src = `/static/resources/home/${i}.jpg`;

        let label_cont = document.createElement('div');
        label_cont.classList.add("carousel-caption", "d-none", "d-md-block");
        label_cont.style.color = 'rgb(48,194,87)';
        label_cont.style.backgroundColor = 'rgba(0, 0, 0, 100)';
        let label_p = document.createElement('p');
        label_p.textContent = 'Dernière Création';
        let label_H3 = document.createElement('h3');
        label_H3.textContent = 'ROUGE CERISE';

        label_cont.appendChild(label_p);
        label_cont.appendChild(label_H3);
        item.appendChild(img);
        item.appendChild(label_cont);
        div.appendChild(item);
    }
    cont.appendChild(div)

    let ol = document.createElement('ol');
    ol.classList.add("carousel-indicators");

    for (let i = 1; i < N + 1; i++) {
        let li = document.createElement('li');
        li.setAttribute('data-target', '#carouselExampleIndicators');
        li.setAttribute('data-slide-to', `${i}`);

        if (i == 1) {
            li.classList.add('active');
        }
        ol.appendChild(li);
    }
    cont.appendChild(ol);

    let a1 = document.createElement('a');
    a1.classList.add('carousel-control-prev');
    a1.href = '#carouselExampleIndicators';
    a1.setAttribute('role', 'button');
    a1.setAttribute('data-slide', 'prev');

    let span11 = document.createElement('span');
    span11.classList.add('carousel-control-prev-icon');
    span11.setAttribute('aria-hidden', 'true');

    let span12 = document.createElement('span');
    span12.classList.add('sr-only');
    span12.textContent = "Previous";

    a1.appendChild(span11);
    a1.appendChild(span12);

    //cont.appendChild(a1);

    let a2 = document.createElement('a');
    a2.classList.add('carousel-control-next');
    a2.href = '#carouselExampleIndicators';
    a2.setAttribute('role', 'button');
    a2.setAttribute('data-slide', 'next');

    let span21 = document.createElement('span');
    span21.classList.add('carousel-control-next-icon');
    span21.setAttribute('aria-hidden', 'true');

    let span22 = document.createElement('span');
    span22.classList.add('sr-only');
    span22.textContent = "Next";

    a2.appendChild(span21);
    a2.appendChild(span22);

    //cont.appendChild(a2);
}


window.onload = () => {
    loadHome();
    document.getElementById('bts-modal-btn').click();
}
