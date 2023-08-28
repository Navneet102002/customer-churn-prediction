function onClickedEstimateChurn() {
  console.log("Estimate price button clicked");
  var age = document.getElementById("uiAge");
  var sub_months = document.getElementById("uiMonths");
  var bill = document.getElementById("uiBill");
  var gb_used = document.getElementById("uiUsedGB");
  var gender = document.getElementsByName("uiGender")[0].checked ? 1 : 0;
  var location = document.getElementById("uiLocations");
  var estChurn = document.getElementById("uiEstimatedChurn");
  
  // var url = "http://127.0.0.1:5000/predict_churn"; //Use this if you are NOT using nginx which is first 7 tutorials
  var url = "/predict_churn"; // Use this in ubuntu for ec2 deployment
  // var url = "/api/predict_churn"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  
  $.post(url, {
    age: age.value,
    sub_months: sub_months.value,
    bill: parseFloat(bill.value),
    gb_used: parseFloat(gb_used.value),
    gender: gender,
    location: location.value
  },function(data, status) {
    console.log(data.estimated_churn);
    estChurn.innerHTML = "<h2>" + data.estimated_churn.toString() + "</h2>";
    console.log(status);
  });
}
  
function onPageLoad() {
    console.log( "document loaded" );
    // var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
    var url = "/get_location_names"; // Use this for ubuntu for ec2 deployment
    // var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url,function(data, status) {
        console.log("got response for get_location_names request");
        if(data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
  }
  
  window.onload = onPageLoad;