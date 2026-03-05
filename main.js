let pyodide;

async function init(){

    pyodide = await loadPyodide();

    const code = await (await fetch("generator.py")).text();

    await pyodide.runPythonAsync(code);

    await pyodide.runPythonAsync("await init()");
}

init();

function setAvatar(name){

    document.getElementById("avatar").src="images/"+name;

}

async function askBot(){

    setAvatar("think.png")

    document.getElementById("sentence").innerText="Thinking..."

    await new Promise(r=>setTimeout(r,3000+Math.random()*1000))

    const sentence = pyodide.runPython("generate_sentence()")

    document.getElementById("sentence").innerText=sentence

    setAvatar("answer.png")

}

function feedback(ok){

    if(ok){
        setAvatar("good.png")
    }else{
        setAvatar("bad.png")
    }

}