function get_feedback_link(feedback_id, feedback_link) {
    let hostname = window.location.hostname
    let block = document.getElementById('feedback_link_'+feedback_id)
    block.innerHTML = hostname + feedback_link
    block.href = feedback_link
}

function switch_feedback() {

    switch_btn = document.getElementById("feedback-switch");
    switch_btn.classList.toggle("change");

    feedback_form = document.getElementById("feedback-form")
    feedback_form.classList.toggle("change");

    feedback_close = document.getElementById("feedback-close")
    feedback_close.classList.toggle("change");
    
}