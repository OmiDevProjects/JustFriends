const alertBox = document.getElementById('alert-box');
const imgBox = document.getElementById('img-box');
const form = document.getElementById('p-form');

const image = document.getElementById('id_avatar');

const btnBox = document.getElementById('btn-box');
const btns = [...btnBox.children]

// *************************  Update Profile Info variables *************************

const alertProfileBox = document.getElementById('alert-profile-box');
const profileForm = document.getElementById('profile-form');
const csrf_token_profile = document.getElementsByName('csrfmiddlewaretoken');

const bio_ = document.getElementById('id_bio');
// const dob_ = document.getElementById('id_dob');
const profession_ = document.getElementById('id_profession');

const url_profile = '/profile/update_profile_info/';

// Handling Alert Boxes 
const handleAlerts_profile = (type, text) => {
    alertProfileBox.innerHTML = `
    <div class="ui ${type} message mt-2">${text}</div>
    `
}

// ************************* End of Profile info ******************** 

// Background Cover Image Changes Variable
const alertCoverBox = document.getElementById('alert-cover-box');
const imgCoverBox = document.getElementById('img-cover-box');
const formCover = document.getElementById('p-cover-form');

const imageCover = document.getElementById('id_background');
const csrf_cover = document.getElementsByName('csrfmiddlewaretoken');

const url_cover = '/profile/update_coverImage/';


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

// ************************************* End of Background  Cover ###############

var mediaURL = window.location.href + 'media/'

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
    form_data.append('avatar', image.files[0]);
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
            mediaURL = 'http://localhost:8000/media/';
            imgBox.innerHTML = `<img src="${mediaURL + data[0].fields.avatar}" width="100%">`

            handleAlerts('success', 'Your Avatar is Sucessfully Updated!!!');
        },
        error: function (error) {
            handleAlerts('danger', 'OOOPS, Got Something Wrong...');
        },
        cache: false,
        contentType: false,
        processData: false,
    })
})


let id_cover = null;
// Form Submiting to Server with POST Request ( AJAX )
formCover.addEventListener('submit', (e) => {
    e.preventDefault();

    const form_data_ = new FormData();
    form_data_.append('csrfmiddlewaretoken', csrf_cover[0].value);
    form_data_.append('cover', imageCover.files[0]);
    form_data_.append('id_cover', id_cover);

    $.ajax({
        type: 'POST',
        url: url_cover,
        enctype: 'multipart/form-data',
        data: form_data_,
        success: function (response) {
            const data = JSON.parse(response.cover);
            id_cover = data[0].pk;
            mediaURL = 'http://localhost:8000/media/';
            imgCoverBox.innerHTML = `<img src="${mediaURL + data[0].fields.background}" width="100%">`;

            handleAlerts_cover('success', 'Your Cover Image is Sucessfully Updated!!!');
        },
        error: function (error) {
            handleAlerts_cover('danger', 'OOOPS, Got Something Wrong...');
        },
        cache: false,
        contentType: false,
        processData: false,
    })
})

profileForm.addEventListener('submit', (e) => {
    e.preventDefault();
    
    const form_date_profile = new FormData();
    form_date_profile.append('csrfmiddlewaretoken', csrf_token_profile[0].value);
    form_date_profile.append('bio', bio_.value);
    // form_date_profile.append('dob', dob_);
    form_date_profile.append('profession', profession_.value);

    $.ajax({
        type: 'POST',
        url: url_profile,
        data: form_date_profile,
        success: function (response) {
            console.log(response);
            handleAlerts_profile('success', 'Your Profie info is Updated!!!');
        },
        error: function (error) {
            console.log(error);
            handleAlerts_profile('danger', 'OOOPS, Got Something Wrong...');
        },
        cache: false,
        contentType: false,
        processData: false,
    })
})