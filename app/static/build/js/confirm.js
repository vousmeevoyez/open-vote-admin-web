var modalConfirm = function(callback){

  $("#yes-btn").on("click", function(){
    callback(true);
    $("#confirmBox").modal('hide');
  });
  
  $("#no-btn").on("click", function(){
    callback(false);
    $("#confirmBox").modal('hide');
  });
}