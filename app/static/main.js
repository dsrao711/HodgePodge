//Scroll


var scrolled = false;

function updateScroll() {
    if (!scrolled) {
        var element = document.getElementById("msg");
        element.scrollTop = element.scrollHeight;
    }
}

$("#msg").on('scroll', function() {
    scrolled = true;
});


//socket 


const socket = io();

socket.on("message", (data) => {
    console.log(data);

    if (data.msg) {
        var ele = document.getElementById("msg")

        ele.innerHTML = `${ele.innerHTML}
        <div class="flex-row d-flex">
            <div class="alert alert-success"  style="max-width: 40% ; height : 7vh ">
                <p>${data.msg}</p>
            </div>
        </div>`
    }
    
});

function chatapp(name) {
    var chatName = document.getElementById("chat-header");
    chatName.innerHTML = name;

    var ele = document.getElementById("msg");
    var messages = JSON.parse(localStorage.getItem("messages"));
    console.log(messages);

    if (messages) {
        var prevName = localStorage.getItem("currChat");
        messages[prevName] = ele.innerHTML;

        if (messages[name]) {
            ele.innerHTML = messages[name];
        } else {
            ele.innerHTML = "";
        }
        localStorage.setItem("messages", JSON.stringify(messages));
    } else {
        var prevName = localStorage.getItem("currChat")
        if (prevName) {
            var messages = {};
            messages[prevName] = ele.innerHTML;
        }
        console.log(messages)
        ele.innerHTML = ""
        localStorage.setItem("messages", JSON.stringify(messages));
    }

    localStorage.setItem("currChat", name);
}

function joinRoom() {
    socket.emit('join', { "room": localStorage.getItem("currUsername") || "user1" });
}

function onMessageSend() {

    var ele = document.getElementById("message");
    var msg = ele.value;
    ele.value = ""

    var data = {
        to: localStorage.getItem("currChat"),
        from: localStorage.getItem("currUsername") || "user1",
        msg: msg
    }
    console.log(data);

    var ele = document.getElementById("msg")

    ele.innerHTML = `${ele.innerHTML}
    <div class="flex-row-reverse d-flex">
        <div class="alert alert-info"  style="max-width: 40% ; height : 7vh ">
            <p>${data.msg}</p>
        </div>
    </div>`


    socket.emit("message", data)
}