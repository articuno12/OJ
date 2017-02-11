function show_submission_status(url,sid){
  $.ajax({
    type:"POST",
    url:url,
    data:"sid="+String(sid),
    dataType:"json",
    success: function(result){
      var html;
      if(result.status=="DONE"){
        clearInterval(ajaxinterval);
        switch(result.result)
        {
          case "Accepted":
            html="<div class='row' style='position:relative;'><div class='col-md-5'><img src='/oj/static/images/accepted.png' class='icon'></div><div class='col-md-7 vcenter'><span class='status'>ACCEPTED</span></div></div><div class='row' ><div class='col-md-9 col-md-offset-2 subdetails'>Execution Time: "+result.time +" sec<br>Memory: "+result.memory+" MB</div></div>"
            $("#display-result").addClass("result-accepted");
            break;
          case "Wrong Answer":
            html="<div class='row' style='position:relative;'><div class='col-md-5'><img src='/oj/static/images/wrong.png' class='icon'></div><div class='col-md-7 vcenter'><span class='status'>WRONG ANSWER</span></div></div><div class='row' ><div class='col-md-9 col-md-offset-2 subdetails'>Execution Time: "+result.time +" sec<br>Memory: "+result.memory+" MB</div></div>"
            $("#display-result").addClass("result-wrong");
            break;
          case "Time limit exceeded":
            html="<div class='row' style='position:relative;'><div class='col-md-5'><img src='/oj/static/images/clock.png' class='icon'></div><div class='col-md-7 vcenter'><span class='status'>TIMIT LIMIT EXCEEDED</span></div></div><div class='row' >"
            $("#display-result").addClass("result-tle");
            break;
          default:
            html="<div class='row' style='position:relative;'><div class='col-md-5'><img src='/oj/static/images/error.png' class='icon'></div><div class='col-md-7 vcenter'><span class='status'>"+result.result+"</span></div></div>"
            break;
        }
        $("#display-result").html(html);
      }
    }
  });
}
