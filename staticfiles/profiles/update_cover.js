const alertCoverBox = document.getElementById('alert-cover-box');
const imgCoverBox = document.getElementById('img-cover-box');
const formCover = document.getElementById('p-cover-form');

const imageCover = document.getElementById('id_background');

var mediaURL = window.location.href + 'media/'

const csrf_cover = document.getElementsByName('csrfmiddlewaretoken');

const url_cover = '/profile/update_profile_view/';

// Handling Alert Boxes 
const handleAlerts_cover = (type, text) => {
    alertCoverBox.innerHTML = `
    <div class="ui ${type} message mt-2">${text}</div>
    `
}

// Showing Image Preview 
imageCover.addEventListener('change', () => {
    const image_data = imageCover.files[0];
    const img_url = URL.createObjectURL(image_data);

    imgCoverBox.innerHTML = `<img src=${img_url} width="100%">`

})


let id_cover = null;
// Form Submiting to Server with POST Request ( AJAX )
formCover.addEventListener('submit', (e) => {
    e.preventDefault();

    const form_data_ = new FormData();
    form_data_.append('csrfmiddlewaretoken', csrf_cover[0].value);
    form_data_.append('cover', image.files[0]);

    $.ajax({
        type: 'POST',
        url: url_cover,
        enctype: 'multipart/form-data',
        data: form_data_,
        success: function (response) {
            const data = JSON.parse(response.data);
            id_cover = data[0].pk;
            mediaURL = 'http://localhost:8000/media/';
            imgCoverBox.innerHTML = `<img src="${mediaURL + data[0].fields.avatar}" width="100%">`;

            handleAlerts_cover('success', 'Your Avatar is Sucessfully Updated!!!');
        },
        error: function (error) {
            handleAlerts_cover('danger', 'OOOPS, Got Something Wrong...');
        },
        cache: false,
        contentType: false,
        processData: false,
    })
})