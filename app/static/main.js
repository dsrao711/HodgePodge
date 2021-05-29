const socket = io();
socket.on("message", (data) => {
    console.log(data);
});

function chatapp(name) {
    var ele = document.getElementById("chat-header");
    ele.innerHTML = name;

    localStorage.setItem("currChat", name);
}

function joinRoom() {
    socket.emit('join', {"room": localStorage.getItem("currUsername") || "user1" });
}

function onMessageSend() {
    var msg = document.getElementById("message").value;

    var data = {
        to: localStorage.getItem("currChat"),
        from: localStorage.getItem("currUsername") || "user1",
        msg: msg
    }
    console.log(data);

    var ele = document.getElementById("messages")
    if (ele.innerHTML == "") {
        ele.innerHTML = `<div class="flex justify-end">
            ${data.msg}
        </div>`
    } else {
        ele.innerHTML = `${ele.innerHTML}<div class="flex justify-end">
            ${data.msg}
        </div>`
    }
    socket.emit("message", data)
}