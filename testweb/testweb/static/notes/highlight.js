
function getText(){
    var text = "";

    text = (document.all) ? document.selection.createRange().text : window.getSelection().toString();
    text = text.trim();
    var length = text.length;
    if(length > 0 && text !=""){
        console.log(text);
    }

}

document.onmouseup = getText;

