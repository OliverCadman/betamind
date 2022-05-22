/* 
    Displays messages provided by Django or from AJAX success callbacks.
    Takes two arguments:
    1. msg - The message being passed.
    2. representativeColor - A color to represent that nature of the message.
    Utilises the Toastify.js library
    https://apvarun.github.io/toastify-js/
    */

function displayToast(message, representativeColor) {
  Toastify({
    text: message,
    duration: 5000,
    close: true,
    gravity: "top",
    position: "center",
    style: {
      background: "#fefefe",
      fontFamily: "'Montserrat', sans-serif",
      color: representativeColor,
      fontSize: "18px",
    },
  }).showToast();
}
