
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
    textRange = sel.cloneRange();//where to put the styling
    parentNode = textRange.startContainer.parentNode.id;

    if(length > 0 && text !="" && parentNode =="content"){//only highlights body of note
        /*prevents offsets from referencing spans instead of the parent node*/
        textRange.selectNodeContents(textRange.startContainer.parentNode);
        textRange.setEnd(sel.startContainer, sel.startOffset);
        startRange = textRange.toString().length;
        endRange = startRange + sel.toString().length;

        document.designMode = "on";//highlights stuff
        document.execCommand("BackColor", false,"#FFFF00");
        document.designMode = "off";

        deselect();
        console.log(startRange);
        console.log(endRange);

    }else{
        console.log(startRange);
        console.log(endRange);
        deselect();
    }
}

function highlight(){
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

function deselect(){//deselects in browser to display the highlighting in yellow
     if ( document.selection ) {
        document.selection.empty();
    } else if ( window.getSelection ) {
        window.getSelection().removeAllRanges();
    }
}


document.onmouseup = highlight;


