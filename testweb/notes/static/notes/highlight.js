
function getText(){
    var text = "";

    text = (document.all) ? document.selection.createRange().text : window.getSelection().toString();
    text = text.trim();

    var length = text.length;
    if(length > 0 && text !=""){
        console.log(text);
        unHighlight();
    }
}

function unHighlight() {
    if ( document.selection ) {
        document.selection.empty();
    } else if ( window.getSelection ) {
        window.getSelection().removeAllRanges();
    }
}
document.onmouseup = getText;


