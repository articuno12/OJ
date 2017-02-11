function changemenustate(header,newstate){
  if(header.data('state')!=newstate){
    header.data('state',newstate);
    console.log(newstate);
    if(newstate==1){
      $("nav",header).addClass('navbar-fixed-top');
      // $(document).scrollTop($(document).scrollTop()-100);
    }
    else if(newstate==0){
      $("nav",header).removeClass('navbar-fixed-top');
    }
  }

}

$(document).scroll(function(){
  var header=$("div[role='header']");
  var scroll=$(document).scrollTop()
  if(scroll>70 && header.data('state')==0){
    changemenustate(header,1);
  }
  else if(scroll<50 && header.data('state'==1)){
    changemenustate(header,0);
  }
});
