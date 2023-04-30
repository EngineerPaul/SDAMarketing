// COMMON FUNCTIONS

// function to get request parameters
let get_query_params = function() {
    let query_string = window.location.search;
    let params = new Object();
    let param_list = query_string.substring(1).split("&");
    if (param_list) {
        for (let i = 0; i < param_list.length; i++) {
            key = param_list[i].split("=")[0]
            value = param_list[i].split("=")[1]
            if (key in params) {
                params[key].push(value)
            } else {
                params[key] = [value];
            }
        }
    }
    if (params[""]) {params=false}
    return params;
};

// function that create string of query parameters without url
function get_query_str(param_dict) {
    let query_str = ''
    for (let param_name in param_dict) {
        for (let i=0; i<param_dict[param_name].length; i++) {
            query_str = query_str + param_name + '=' + param_dict[param_name][i] + '&'
        }
    }
    query_str = query_str.slice(0, -1)
    return query_str
}


// CHECKBOX

// function that activates the checkbox
let activate_checkboxes = function() {
    let all_parameters = get_query_params()
    for (let key in all_parameters) {
        for (let i=0; i<all_parameters[key].length; i++) {
            any_checkbox = document.getElementById(key+'_id_'+all_parameters[key][i])
            if (any_checkbox) {
                any_checkbox.checked = true
            }
        }
    }

    // all_industries element check
    if (!(all_parameters['industry'])) {
        all_industries_element = document.getElementById('all_industies_id')
        all_industries_element.checked = true
    }
}

activate_checkboxes()


// function that adds and removes the checkbox id in href
function swith_query_param(param_name, id) {
    let all_parameters = get_query_params()
    if (!(all_parameters)) {
        all_parameters = {}
    }
    if (!(all_parameters[param_name])) {
        all_parameters[param_name] = []
    }
    if (all_parameters[param_name].includes(id)) {
        let index = all_parameters[param_name].indexOf(id)
        all_parameters[param_name].splice(index, 1)
    } else {
        if (only_single_filter) {
            all_parameters[param_name] = [id, ]
        } else {
            all_parameters[param_name].push(id)
        }
    }
    let link = window.location.pathname
    query_str = get_query_str(all_parameters)
    if (query_str) {
        link = link + '?' + get_query_str(all_parameters)
    } else {
        link = link
    }
    window.location.href = link
}


// function to clear the address bar
function clear_industries_param() {
    let industries = get_query_params()['industry']
    if (industries) {
        let all_parameters = get_query_params()
        delete all_parameters['industry']

        let link = window.location.pathname
        query_str = get_query_str(all_parameters)
        if (query_str) {
            link = link + '?' + get_query_str(all_parameters)
        } else {
            link = link
        }
        window.location.href = link
    }

    // all_industries element check
    let all_parameters = get_query_params()
    if (!(all_parameters['industry'])) {
        all_industries_element = document.getElementById('all_industies_id')
        all_industries_element.checked = true
    }
}


// function that opens filters (checkboxes) when the window width is greater than 768px
let open_filters = function() {
    if (window.innerWidth > 768) {
        let accord_btns = document.getElementsByClassName('accordion-button')
        let accord = document.getElementsByClassName('accordion-collapse collapse')
        
        for (let i=0; i<accord_btns.length; i++) {
            accord_btns[i].classList.toggle('collapsed')
        }

        for (let i=0; i<accord.length; i++) {
            accord[i].classList.toggle('show')
        }
    }
}

open_filters()


// COMMON VARIABLES AND FUNCTIONS FOR UPLOADING CONTENT

let count = 0  // count of all upload projects, getting from page one (first request)
let counter = 0  // count of uploaded projects
let page = 1  // loading page number
let is_perfoming = false // variable that slows down the call to the next request

let block_id = 'projects_content'  // id of the div block where content will be generated
let block = document.getElementById(block_id);
const only_single_filter = true  // only one filter (query parameter) of the same type can be applied

let check_status = function(response) {
    if (response.status !== 200) {
        return Promise.reject(new Error(response.statusText))
    }
    return Promise.resolve(response)
}

let to_json = function(response) {
    return response.json()
}

let display_blocks = function(data) {
    for (i=0; i<data['results'].length; i++) {
        block.innerHTML = block.innerHTML + 
        `<div class="project">
            <div class="content-direction">
                ${data['results'][i]['direction']}
            </div>
            <div class="content-title">
                <a href='${data['results'][i]['get_absolute_url']}' onclick="loader_on()">
                    <p>${data['results'][i]['title']}</p>
                </a>
            </div>
        </div>`
        counter++
    }
    page++
    loader_off()
    setTimeout(() => is_perfoming = false, 500)
}

let raise_error = function (error) {
    console.log('error', error)
    loader_off()
}

let get_url = function(url, param_dict) {
    url = url+'?'
    for (let param_name in param_dict) {
        for (let i=0; i<param_dict[param_name].length; i++) {
            url = url + param_name + '=' + param_dict[param_name][i] + '&'
        }
    }
    url = url.slice(0, -1)
    return url
}

function get_href(pathname, param_dict) {
    pathname = pathname + '?'
    for (let param_name in param_dict) {
        for (let i=0; i<param_dict[param_name].length; i++) {
            pathname = pathname + param_name + '=' + param_dict[param_name][i] + '&'
        }
    }
    pathname = pathname.slice(0, -1)
    return pathname
}


// GETTING THE FIRST PAGE

let query_params = Object.assign({'page': [page]}, get_query_params())
url = get_url(projects_api_url, query_params)

loader_on()
fetch(url)
.then(check_status)
.then (to_json)
.then( (data) => {
    count = data['count']
    display_blocks(data)
})
.catch(raise_error)


// GETTING ANOTHER PAGES

window.addEventListener("scroll", function() {

    let contentHeight = block.offsetHeight;
    let yOffset       = window.pageYOffset;
    let window_height = window.innerHeight;
    let y             = yOffset + 2*window_height;

    // if the user has reached the of the page
    if (y >= contentHeight) {

        if (!(is_perfoming)) {
            is_perfoming = true

            if (counter<count) {
                let query_params = Object.assign({'page': [page]}, get_query_params())
                url = get_url(projects_api_url, query_params)

                fetch(url)
                .then(check_status)
                .then (to_json)
                .then(display_blocks)
                .catch(raise_error)

            }

        }
    }
});
