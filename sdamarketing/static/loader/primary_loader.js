loader_on = function() {
    let loader = document.getElementById('loader-id')
    loader.className = 'loader'
    setTimeout(loader_off, 1000*10)
}

loader_off = function() {
    let loader = document.getElementById('loader-id')
    loader.className = 'loader-none'
}