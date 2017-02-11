var timeday;
var timesec;
var interval;
function changetimer(timeday,timesec){
  var timer=document.getElementById("timer");
  if(timeday>0){
    timer.innerHTML=timeday+" days " +Math.floor(timesec/3600) + " hrs " +Math.floor((timesec/60)%60) + " min "+Math.floor(timesec%60)+" secs";
  }
  else if(Math.floor(timesec/3600) > 0){
    timer.innerHTML=Math.floor(timesec/3600) + " hrs " +Math.floor((timesec/60)%60) + " min "+Math.floor(timesec%60)+" secs";
  }
  else if(Math.floor((timesec/60)%60) > 0){
    timer.innerHTML=Math.floor((timesec/60)%60) + " min "+Math.floor(timesec%60)+" secs";
  }
  else{
    timer.innerHTML=Math.floor(timesec%60)+" secs";
  }
}
function initializetimer(days,secs){
  timeday=days;
  timesec=secs;
  changetimer(timeday,timesec);
  interval=setInterval(updatetime,1000);
}
function updatetime(){
  timesec-=1;
  if(timesec<0){
    timeday-=1;
    if(timeday<0){
      clearInterval(interval);
      timeday=0;timesec=0;
    }
    else{
      timesec=24*3600-1;
    }
  }
  changetimer(timeday,timesec);
}
