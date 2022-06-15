var target = document.getElementById("chat-container");
var eventSource = new EventSource("/stream");

eventSource.onmessage = function(e) {

    target.innerHTML = '';

    let data = e.data;
    data = data.substring(1, data.length - 1);
    data = (new Function('return [' + data + '];')());

    data.forEach(function (item) {
        let p = document.createElement('p');
        p.classList.add('msg'); 
        target.appendChild(p);

        p.innerHTML += item;
    });

};

function sendToServer() {

    xhttp = new XMLHttpRequest();

    let msg = new FormData(document.querySelector('#chat-input'));

    document.querySelector("#chatbox").value = "";

    xhttp.open("POST", "/send", true);
    xhttp.send(msg.get('content'));

};

let textarea = document.getElementById("chat-input");

textarea.addEventListener('keypress', (e) => {

    if (e.key === 'Enter' && !e.shiftKey) {

        e.preventDefault();
        sendToServer();
        
    }

})

function adjustText(element) {

    if (element.value.length > 74) {

        textarea.style.gridTemplateRows = "70px";

    } else {

        textarea.style.gridTemplateRows = "50px";

    }

};

let new_icon = document.createElement('i');
new_icon.setAttribute('class', 'fad fa-comments-alt icon');
document.querySelector('.chat').childNodes[1].replaceWith(new_icon);