const background = document.getElementById("backgroundLines");

function createPulsingLines() {
  for (let i = 0; i < 20; i++) {
    const line = document.createElement("div");
    line.id = `line${i}`;
    line.classList.add("line");
    background.appendChild(line);
  }
}

createPulsingLines();
