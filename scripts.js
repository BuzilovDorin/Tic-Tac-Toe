$(document).click(function (e) {
    if ($(e.target).attr("id") == "reset") {
        $("li").empty()
        $("li").removeClass()
        $("li").addClass('none')
        var soundbyte = document.createElement("audio")
        soundbyte.src = "/Assets/reset.mp3"
        soundbyte.play()
    }
    else if ($(e.target).attr("class") != "none") {
        return false
    }
    else {
        $(e.target).append('x')
        $(e.target).toggleClass("none x")
        var soundbyte = document.createElement("audio")
        soundbyte.src = "/Assets/click1.mp3"
        soundbyte.play()
    }
})