let pyodide;
let thinking = false;



async function init(){

    pyodide = await loadPyodide();

    const code = await (await fetch("generator.py")).text();

    document.getElementById("codeBlock").textContent = code;

    await pyodide.runPythonAsync(code);

    await pyodide.runPythonAsync("await init()");

    askBot();
}

init();



function setAvatar(name){

    document.getElementById("avatar").src="images/"+name;

}



function setButtons(enabled){

    document.querySelectorAll(".feedback button")
        .forEach(b=>b.disabled=!enabled);

}



function addChatMessage(text){

    const log = document.getElementById("chatLog");

    const bubble = document.createElement("div");

    bubble.className="bubble bot";

    bubble.innerText=text;

    log.appendChild(bubble);

    log.scrollTop = log.scrollHeight;
}



async function typingAnimation(text){

    const log = document.getElementById("chatLog");

    const bubble = document.createElement("div");

    bubble.className="bubble bot";

    log.appendChild(bubble);

    let i=0;

    return new Promise(resolve=>{

        const interval=setInterval(()=>{

            bubble.textContent += text[i];

            i++;

            log.scrollTop = log.scrollHeight;

            if(i>=text.length){

                clearInterval(interval);

                resolve();

            }

        },30);

    });
}



async function askBot(){

    if(thinking) return;

    thinking=true;

    setButtons(false);

    setAvatar("think.png");

    document.getElementById("typing").innerText="Thinking...";

    const delay = 3000 + Math.random()*1000;

    await new Promise(r=>setTimeout(r,delay));

    const sentence = pyodide.runPython("generate_sentence()");

    setAvatar("answer.png");

    document.getElementById("typing").innerText="";

    await typingAnimation(sentence);

    setButtons(true);

    thinking=false;
}



function feedback(ok){

    if(thinking) return;

    if(ok){

        setAvatar("good.png");

    }else{

        setAvatar("bad.png");

    }

    setButtons(false);

    setTimeout(()=>{

        askBot();

    },1500);

}



function toggleCode(){

    const code=document.getElementById("codeBlock");

    code.style.display =
        code.style.display==="none" ? "block" : "none";
}