
function getText(){
    var text = "";

    text = (document.all) ? document.selection.createRange().text : window.getSelection().toString();
    text = text.trim();
    var length = text.length;
    console.log(text);
    if(length > 0 && text !=""){
        alert(text);
    }

}

document.onmouseup = getText;

