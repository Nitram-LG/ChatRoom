let overlay = document.querySelector('#overlay')

window.addEventListener('DOMContentLoaded', function () {

    setTimeout(function () {

        overlay.style.opacity = "0";

    }, 500)

    setTimeout(function () {

        overlay.style.width = "0";
        overlay.style.height = "0";

    }, 1000)

})

function enlargeItem(element) {

    element.style.width = "140px"

}

function reduceItem(element) {

    element.style.width = "35px"

}

function changeTo(new_page) {

    overlay.style.width = "100%";
    overlay.style.height = "100%";

    overlay.style.opacity = "1";

    setTimeout(function () {

        location.href = new_page;

    }, 500)

}

function openUserMenu() {

    document.querySelector('.drop').setAttribute('onClick', 'javascript: closeUserMenu();');
    document.querySelector('.drop').setAttribute('class', 'far fa-user icon drop');

    document.querySelector('.drop-content').style['transform'] = "translateX(0px)";

}

function closeUserMenu() {

    document.querySelector('.drop').setAttribute('onClick', 'javascript: openUserMenu();');
    document.querySelector('.drop').setAttribute('class', 'fas fa-user icon drop');

    document.querySelector('.drop-content').style['transform'] = "translateX(280px)";
}

function togglePasswordVisibility() {

    let passwordInput = document.querySelector('#password-input');

    if (passwordInput.type === "password") {

        passwordInput.type = "text";

    } else {

        passwordInput.type = "password";

    }

}

function toggleUserSelect(element) {

    let submit = document.querySelector("#user-submit");

    if (element.textContent === "REGISTER") {
        
        submit.innerHTML = 'REGISTER <i class="fas fa-user-plus"></i>';

    } else {
        
        submit.innerHTML = 'LOGIN <i class="fas fa-sign-in-alt"></i>';
        
    }

}

function permformUserAction() {

    xhttp = new XMLHttpRequest();

    let form = new FormData(document.querySelector('#user-form'));
    let action = document.querySelector('#user-submit').textContent;
    let status = document.querySelector('#status-message');
    
    let out = ""
    
    out += form.get('username');
    out += "|";
    out += form.get('password');

    if (action.includes('REGISTER')) {

        xhttp.open("POST", "/register", true);

    } else {

        xhttp.open("POST", "/login", true);

    }

    xhttp.send(out);

    xhttp.onreadystatechange = function() {

        if (xhttp.readyState === 4) {

            switch (xhttp.response) {
                
                case '0':
                    status.innerHTML = 'Account created successfully';
                    break;
            
                case '1':
                    status.innerHTML = 'Error : username not available';
                    break;

                case '2':
                    status.innerHTML = 'Successfully connected'
                    location.reload(); 
                    break;

                case '3':
                    status.innerHTML = 'Error : wrong credentials';
                    break;

                default:
                    status.innerHTML = 'Something unexpected happend';
                    break;

            }

            setTimeout(() => {

                status.innerHTML = '';

            }, 3000);

        }
    }

    document.querySelector('#user-form').reset();

}
