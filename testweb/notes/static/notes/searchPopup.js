

window.onload = function(){
    var popup = document.getElementById('popup');
    var button = document.getElementById('searchBtn');
    var span = document.getElementById('close');

    button.onclick = function(){
        popup.style.display = "block";
    }

    span.onclick = function(){
        popup.style.display = "none";
    }
}


