function setMood(happy) {
    const mouth = document.querySelector('.mouth');
    if (happy) {
        mouth.style.borderRadius = '0 0 70% 70%';
    } else {
        mouth.style.borderRadius = '70% 70% 0 0';
    }
}
setMood(true);

function tiltHead() {
    const head = document.querySelector('.head-section');
    head.classList.add('tilt');
    setTimeout(() => {
        head.classList.remove('tilt');
    }, 1000);
}
tiltHead();

const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();

recognition.onstart = () => {
    console.log("Listening...");
    tiltHead(); // Tilt when listening starts
};

recognition.onresult = (event) => {
    const transcript = event.results[0][0].transcript.toLowerCase();
    console.log("Heard:", transcript);

    if (transcript.includes("party mode")) {
        partyMode();
    } else if (transcript.includes("hello") || transcript.includes("hi")) {
        smile();
    } else if (transcript.includes("sad")) {
        sadFace();
    }
};


eel.expose(smile);
function smile() {
    document.querySelector('.mouth').style.borderRadius = "0 0 70% 70%";
    document.querySelector('.mouth').style.height = "50px";
    
}


eel.expose(sadFace);
function sadFace() {
    document.querySelector('.mouth').style.borderRadius = "70% 70% 0 0";
}

recognition.start();

eel.expose(partyMode);
function partyMode() {
    const head = document.querySelector('.head-section');
    head.classList.add('dance');
    setTimeout(() => {
        head.classList.remove('dance');
    }, 5000); // Party for 5 seconds
}






var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 340,
    height: 100,
    speed:0.10
  });

  var micbtn = document.querySelector(".btn-mic");
  var heading = document.querySelector(".heading");
  var siriWave = document.querySelector(".bujji-talking");

    micbtn.addEventListener("click", function() {
        heading.style.display = "none";
        siriWave.style.display = "block";
        eel.allCommand()();

    })

    function docKeyUP(e){

        if(e.key === "j" && e.metaKey){
            heading.style.display = "none";
            siriWave.style.display = "block";
            eel.allCommand()();
        }

    }

    document.addEventListener("keyup", docKeyUP,false);








eel.expose(startMouthAnimation);
function startMouthAnimation() {
    document.querySelector('.mouth').classList.add('talking');
}

eel.expose(stopMouthAnimation);
function stopMouthAnimation() {
    document.querySelector('.mouth').classList.remove('talking');
}

function nodHead() {
    const head = document.querySelector(".head");
    head.classList.add("nod");
    setTimeout(() => head.classList.remove("nod"), 500);
  }
  eel.expose(nodHead);
  

  // Chat panel functionality - Fixed version


  








