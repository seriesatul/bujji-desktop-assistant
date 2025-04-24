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

function smile() {
    document.querySelector('.mouth').style.borderRadius = "0 0 70% 70%";
    document.querySelector('.mouth').style.height = "50px";
    
}

function sadFace() {
    document.querySelector('.mouth').style.borderRadius = "70% 70% 0 0";
}

recognition.start();

function partyMode() {
    const head = document.querySelector('.head-section');
    head.classList.add('dance');
    setTimeout(() => {
        head.classList.remove('dance');
    }, 5000); // Party for 5 seconds
}


function speak(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    const mouth = document.querySelector('.mouth');

    // Set pitch, rate, and volume (feel free to tweak)
    utterance.pitch = 1.2;  // Slightly more lively
    utterance.rate = 1;     
    utterance.volume = 1;

    // Load voices and pick a female one
    const voices = speechSynthesis.getVoices();
    const femaleVoice = voices.find(voice => 
        voice.name.toLowerCase().includes('female') ||
        voice.name.toLowerCase().includes('woman') ||
        voice.name.toLowerCase().includes('google us english') || // This one is clean and feminine
        voice.name.toLowerCase().includes('zira') // Zira is default MS female voice
    );

    if (femaleVoice) {
        utterance.voice = femaleVoice;
    } else {
        console.log("No female voice found, using default.");
    }

    // Handle mouth animation
    utterance.onstart = () => mouth.classList.add('talking');
    utterance.onend = () => mouth.classList.remove('talking');

    // Speak!
    speechSynthesis.speak(utterance);
}


let bujjiVoice = null;

window.speechSynthesis.onvoiceschanged = () => {
    const voices = window.speechSynthesis.getVoices();

    // Try to find a nice female voice
    bujjiVoice = voices.find(voice => 
        voice.name.toLowerCase().includes('female') ||
        voice.name.toLowerCase().includes('zira') ||
        voice.name.toLowerCase().includes('google uk english female') ||
        voice.name.toLowerCase().includes('samantha')
    );

    console.log("Available Voices:", voices);
    console.log("BUJJI Voice Selected:", bujjiVoice ? bujjiVoice.name : "None");
};

window.onload = () => {
    // Set a default voice if none is selected
    if (!bujjiVoice) {
        const voices = window.speechSynthesis.getVoices();
        bujjiVoice = voices[0]; // Fallback to the first available voice
    }
    speechSynthesis.cancel(); // Stop any ongoing speech
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
        eel.takeCommand()();

    })






