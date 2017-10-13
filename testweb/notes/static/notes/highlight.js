
function getText(){
    var text = "";
    var textRange,sel;
    var startRange = 0;
    var endRange = 0;
    var parentNode;
    text = (document.all) ? document.selection.createRange().text : window.getSelection().toString();

    text = text.trim();
    var length = text.length;
    sel = window.getSelection().getRangeAt(0);
    textRange = window.getSelection().getRangeAt(0);//where to put the styling
    parentNode = textRange.startContainer.parentNode.id;




    if(length > 0 && text !="" && parentNode =="content"){
        startRange = textRange.startOffset;
        endRange = textRange.endOffset;
        if(sel.rangeCount && sel.getRangeAt){
            textRange = sel.getRangeAt(0);
        }

        document.designMode = "on";



        document.execCommand("BackColor", false,"#FFFF00");


        document.designMode = "off";


        //unHighlight(); //currently don't know how to implement this
        deselect();
        console.log(startRange);
        console.log(endRange);


    }else{
        console.log(startRange);
        console.log(endRange);
        deselect();
    }
}

function newHighlight(){
    var range, sel;

    if(window.getSelection){
        try{
            if(!document.execCommand("BackColor", false, "#FFFF00")){
                getText();
            }
        } catch(ex){
            getText();
        }
    }else if(document.selection && document.selection.createRange){
        range = document.selection.createRange();
        range.execCommand("BackColor", false, "#FFFF00");
    }

}

function highlight(range){
    var node = document.createElement("span");
    node.setAttribute("style","background-color:yellow; display: inline;");
    node.id = 'highlighted';
    range.surroundContents(node);
}



/*function removeAllRanges(range){
    if(range.rangeCount > 1){
        for(var i = 1; i<range.rangeCount; i++){
            range.removeRance(range.getRangeAt(i));
        }
    }
}*/

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


document.onmouseup = newHighlight;


