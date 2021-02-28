const alertBox = document.getElementById('alert-box');
const imgBox = document.getElementById('img-box');
const form = document.getElementById('p-form');

const image = document.getElementById('id_post_document');

const btnBox = document.getElementById('btn-box');
const btns = [...btnBox.children]

const mediaURL = window.location.href + 'media/'

const csrf = document.getElementsByName('csrfmiddlewaretoken');

const url = '/profile/update_profile_view/';

// Handling Alert Boxes 
const handleAlerts = (type, text) => {
    alertBox.innerHTML = `
    <div class="ui ${type} message mt-2">${text}</div>
    `
}

// Showing Image Preview 
image.addEventListener('change', () => {
    const image_data = image.files[0];
    const img_url = URL.createObjectURL(image_data);
    console.log(img_url)

    imgBox.innerHTML = `<img src=${img_url} width="100%">`

    btnBox.classList.remove('not-visible');
})

// Select Filter Options function 
let filter = null;
btns.forEach(btn => btn.addEventListener('click', () => {
    filter = btn.getAttribute('data-filter');
}))

let id = null;
// Form Submiting to Server with POST Request ( AJAX )
form.addEventListener('submit', (e) => {
    e.preventDefault();

    const form_data = new FormData();
    form_data.append('csrfmiddlewaretoken', csrf[0].value);
    form_data.append('post_document', image.files[0]);
    console.log(image.files[0]);
    form_data.append('action', filter);
    form_data.append('id', id)

    $.ajax({
        type: 'POST',
        url: url,
        enctype: 'multipart/form-data',
        data: form_data,
        success: function (response) {
            const data = JSON.parse(response.data);
            id = data[0].pk;
            imgBox.innerHTML = `<img src="${mediaURL + data[0].fields.post_document}" width="100%">`

            handleAlerts('success', 'Your Image is Sucessfully Saved!!!');
        },
        error: function (error) {
            handleAlerts('danger', 'OOOPS, Got Something Wrong...');
        },
        cache: false,
        contentType: false,
        processData: false,
    })
})