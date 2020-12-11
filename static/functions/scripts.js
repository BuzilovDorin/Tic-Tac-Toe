$(document).click(function (e) {
    if ($(e.target).attr("id") == "head") {
        var tossVal = $(e.target).attr('value')
        passCoinToss(tossVal)

        var soundbyte = document.createElement("audio")
        soundbyte.src = "/static/Assets/click1.mp3"
        soundbyte.play()
        remvCoinflip()
    }
    else if ($(e.target).attr("id") == "tails") {
        var soundbyte = document.createElement("audio")
        soundbyte.src = "/static/Assets/click2.mp3"
        soundbyte.play()
        remvCoinflip()
    }
    if ($(e.target).attr("id") == "reset") {
        $("li").empty()
        $("li").removeClass()
        $("li").addClass('none')
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
        url: "/test",
        type: "POST",
        async: false,
        contentType: "application/json",
        data: { picked: Value },
        success: function (response) {
            if (response == true) {
                alert(response)
            }
            else {
                alert("Not true")
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