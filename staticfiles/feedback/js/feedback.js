function switch_feedback() {
    // feedback form switching function

    switch_btn = document.getElementById("feedback-switch");
    switch_btn.classList.toggle("change");

    feedback_form = document.getElementById("feedback-form")
    feedback_form.classList.toggle("change");

    feedback_close = document.getElementById("feedback-close")
    feedback_close.classList.toggle("change");

}

function send_mail() {
    // function to send feedback to e-mail using drf

    send_feedback_url

    let form = document.forms['fb_form']
    let name = form.elements['feedback-form-name'].value
    let contact = form.elements['feedback-form-contact'].value
    let text = form.elements['feedback-form-text'].value
    let link = form.elements['feedback-form-link'].value
    let csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value

    form.elements['feedback-form-name'].value = ''
    form.elements['feedback-form-contact'].value = ''
    form.elements['feedback-form-text'].value = ''
    switch_feedback()

    response = fetch(send_feedback_url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf,
        },
        body: JSON.stringify({
            name: name,
            contact: contact,
            text: text,
            link: link
        })
    }).catch(error => alert('Ошибка отправки сообщения!'))

}
