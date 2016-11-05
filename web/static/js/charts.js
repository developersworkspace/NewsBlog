$(function () {

    var ctx = document.getElementById("myChart");

    $.get("/exchangerate/getdata", function (data) {
        var myLineChart = new Chart(ctx, {
            type: 'line',
            data: data,

        });
    });




});