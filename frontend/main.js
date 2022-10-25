console.log("Hello there");

let projectsUrl = "http://localhost:8000/api/projects/";
let propjectsWrapper = document.getElementById("projects-wrapper");

let getProjects = async () => {
    try {
        let response = await fetch(projectsUrl);
        let data = await response.json();
        console.log(data);
        buildProjects(data);
    } catch (err) {
        console.log(err);
    }
};

getProjects();

let buildProjects = (data) => {
    data.forEach((d) => {
        const html = `<div><h1>${d.title}</h1></div>`;

        propjectsWrapper.insertAdjacentHTML("beforeend", html);
    });
};
