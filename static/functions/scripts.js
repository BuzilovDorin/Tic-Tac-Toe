$(document).click(function (e) {
    if ($(e.target).attr("id") == "head") {
        passCoinToss($(e.target).attr('value'))
        var soundbyte = document.createElement("audio")
        soundbyte.src = "/static/Assets/click1.mp3"
        soundbyte.play()
        remvCoinflip()
    }
    else if ($(e.target).attr("id") == "tails") {
        passCoinToss($(e.target).attr('value'))
        var soundbyte = document.createElement("audio")
        soundbyte.src = "/static/Assets/click2.mp3"
        soundbyte.play()
        remvCoinflip()
    }
    if ($(e.target).attr("id") == "reset") {
        AIturn()
        $("li").empty()
        $("li").removeClass()
        $("li").addClass('none')
        $('#cfResult').empty().removeClass()
        var soundbyte = document.createElement("audio")
        soundbyte.src = "/static/Assets/click2.mp3"
        soundbyte.play()
        if (!$("#coinflip").length) {
            addCoinflip()
        }
    }
    else if ($(e.target).attr("class") != "none") {
        return false
    }
    else {
        $(e.target).append('x')
        $(e.target).toggleClass("none x")
        var soundbyte = document.createElement("audio")
        soundbyte.src = "/static/Assets/click1.mp3"
        soundbyte.play()
    }
})

function passCoinToss(Value) {
    $.ajax({
        url: "/coinToss",
        type: "POST",
        async: false,
        contentType: "application/json",
        data: { picked: Value },
        success: function (response) {
            if (response == true) {
                $('#cfResult').addClass('win').append('You won the coin toss!')
            }
            else {
                $('#cfResult').addClass('lose').append('You lost the coin toss!')
            }
        }
    })
}

function AIturn() {
    var currGrid = []
    currGrid = $("#gridContainer").children('#Cell').map(function () {
        return $(this).attr("class");
    });
    arr = JSON.stringify(currGrid)
    console.log(arr)
    $.ajax({
        url: "/AITurn",
        type: "POST",
        async: false,
        contentType: "application/json",
        data: arr,
        success: function (response) {
            if (response == true) {
                console.log("########## YAAAAAYYY")
            }
        }
    })
}

function remvCoinflip() {
    $("#coinflip").remove()
}

function addCoinflip() {
    $('#centered').append('<div id="coinflip"><div id="chooseflip">Choose Head or Tails</div><div id="chooseflip_descript">~ Winner makes first move ~</div><div id="head" value="1">Head</div><div id="tails" value="0">Tails</div></div>')
}