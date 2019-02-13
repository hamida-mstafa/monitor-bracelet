
function getTemp(){
    $.get("/get_latest_temp", function(data, status){
        update(data)
      });
}
function update(d){
    $("#tempValue").text(d.temperature)
    $("#timeStamp").text(d.timestamp)
}

setInterval(getTemp,1000)
