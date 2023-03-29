let a_classes = document.getElementsByTagName('a')
for (let i = 0; i < a_classes.length; i++) {
    if (a_classes[i].className != 'non-click') {
        a_classes[i].onclick = loader_on
    }
}