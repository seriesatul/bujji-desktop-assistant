 var micbtn = document.querySelector(".btn-mic");
  var heading = document.querySelector(".heading");
  var siriWave = document.querySelector(".bujji-talking");

$(document).ready(function() {
    // Your code here

    function toTitleCase(str) {
        return str.toLowerCase().split(' ').map(function(word) {
            return word.charAt(0).toUpperCase() + word.slice(1);
        }).join(' ');
    }
    

    eel.expose(DisplayMessage)
    function DisplayMessage(message) {
        // Display the message in the chat window
      $(".message").text(toTitleCase(message));
      }

      eel.expose(showHeading)
      function showHeading(){
        heading.style.display = "block";
        siriWave.style.display = "none";
        }

       
    }
);
