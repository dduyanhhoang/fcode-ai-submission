const SampleScript = (element: HTMLDivElement) => {
    const h1 = document.createElement('h1');
    h1.textContent = 'Hello from lesson 1!';
    element.appendChild(h1);
    console.log("Lesson 1 Logs")
};

const AddNumbers = (element: HTMLDivElement, a: number, b: number): number => {
    console.log(a + b);
    const div = document.createElement('div');
    div.textContent = "a + b =" + String(a + b);
    element.appendChild(div);
    return a + b;
}

export { SampleScript, AddNumbers };
