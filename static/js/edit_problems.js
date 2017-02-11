function delete_image(image,bt,box)
{
    var delete_image=document.getElementById(image) ;
    var delete_button=document.getElementById(bt) ;
    var delete_box= document.getElementById(box) ;
    delete_box.value="1" ;
    delete_image.style.display="None" ;
    delete_button.style.display="None" ;
}

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
