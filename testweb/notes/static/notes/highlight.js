
function getText(){
    var text = "";
    var textRange;
    text = (document.all) ? document.selection.createRange().text : window.getSelection().toString();

    text = text.trim();

    textRange = window.getSelection().getRangeAt(0);//where to put the styling


    var length = text.length;
    if(length > 0 && text !=""){
        console.log(text);
        highlight(textRange);
        //unHighlight(); //currently don't know how to implement this
        deselect();
    }
}

function highlight(range){
    var node = document.createElement("span");
    node.setAttribute("style","background-color:yellow; display: inline;");
    node.id = 'highlighted';
    range.surroundContents(node);
}

function unHighlight() {
    var tag = document.getElementById('highlighted');
    var content = document.getElementById('highlighted').textContent;
    var node = document.createTextNode(content);
    tag.parentNode.replaceChild(node,tag);
}

function deselect(){//deselects in browser to display the highlighting in yellow
     if ( document.selection ) {
        document.selection.empty();
    } else if ( window.getSelection ) {
        window.getSelection().removeAllRanges();
    }
}
document.onmouseup = getText;


