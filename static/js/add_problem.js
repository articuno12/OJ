var c=1
document.getElementById('add_image').onclick=function(){ add_next() }  ;

function add_next()
{
    Object.prototype.insertAfter = function (newNode) { this.parentNode.insertBefore(newNode, this.nextSibling); }
        var d= c-1 ;
        var prev_element_id = "uploadimage" + d ;
        var prev_element = document.getElementById(prev_element_id) ;
        var next_input=document.createElement("input") ;
        next_input.type="file" ;
        next_input.name= "uploadimage" + c ;
        next_input.id= "uploadimage" + c ;
        next_input.class="my_upload_image"
        prev_element.insertAfter(next_input) ;
        c++ ;
}
