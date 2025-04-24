import './style.css'
import typescriptLogo from './typescript.svg'
import viteLogo from '/vite.svg'
import { setupCounter } from './counter.ts'
import { SampleScript, AddNumbers } from './1-introduction/SampleScripts.ts'
import { Lesson2SampleScript } from './2-variable/Variable.ts'

document.querySelector<HTMLDivElement>('#app')!.innerHTML = `
  <div>
    <a href="https://vite.dev" target="_blank">
      <img src="${viteLogo}" class="logo" alt="Vite logo" />
    </a>
    <a href="https://www.typescriptlang.org/" target="_blank">
      <img src="${typescriptLogo}" class="logo vanilla" alt="TypeScript logo" />
    </a>
    <h1>Vite + TypeScript</h1>
    <div class="card">
      <button id="counter" type="button"></button>
    </div>
    <div id="lesson-1">
    </div>
    <div id="lesson-2">
    </div>
    <p class="read-the-docs">
      Click on the Vite and TypeScript logos to learn more
    </p>
  </div>
`

// const appBody = document.querySelector<HTMLDivElement>('#app')!;

// const h1 = document.createElement('h1');
// appBody.appendChild(h1);

setupCounter(document.querySelector<HTMLButtonElement>('#counter')!);
SampleScript(document.querySelector("#lesson-1")!);
AddNumbers(document.querySelector("#lesson-1")!, 2, 3);

Lesson2SampleScript(document.querySelector("#lesson-2")!);