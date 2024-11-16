let courseCount = 0;

document.getElementById("add-course").addEventListener("click", () => {
    courseCount++;
    const container = document.getElementById("courses-container");
    const courseDiv = document.createElement("div");
    courseDiv.classList.add("form-group");
    courseDiv.innerHTML = `
        <label>Course ${courseCount}</label>
        <!--<input type="text" class="grade" placeholder="Enter grade (A, B+, etc.)">-->
        <select class="grade">
            <option value="">Select grade</option>
            <option value="A+">A+</option>
            <option value="A">A</option>
            <option value="A-">A-</option>
            <option value="B+">B+</option>
            <option value="B">B</option>
            <option value="B-">B-</option>
            <option value="C+">C+</option>
            <option value="C">C</option>
            <option value="C-">C-</option>
            <option value="D+">D+</option>
            <option value="D">D</option>
            <option value="F">F</option>
        </select>
        <input type="number" class="credit" placeholder="Enter credit hours">
    `;
    container.appendChild(courseDiv);
});

document.getElementById("calculate-gpa").addEventListener("click", () => {
    const grades = document.querySelectorAll(".grade");
    const credits = document.querySelectorAll(".credit");
    let totalPoints = 0;
    let totalCreditHours = 0;

    for (let i = 0; i < grades.length; i++) {
        const grade = grades[i].value.toUpperCase();
        const creditHours = parseInt(credits[i].value);

        let points = 0;
        if (grade === "A+" ||grade === "A" ) points = 4.0 * creditHours;
        else if (grade === "A-") points = 3.67 * creditHours;
        else if (grade === "B+") points = 3.33 * creditHours;
        else if (grade === "B") points = 3.0 * creditHours;
        else if (grade === "B-") points = 2.67 * creditHours;
        else if (grade === "C+") points = 2.33 * creditHours;
        else if (grade === "C") points = 2.0 * creditHours;
        else if (grade === "C-") points = 1.67 * creditHours;
        else if (grade === "D+") points = 1.33 * creditHours;
        else if (grade === "D") points = 1.0 * creditHours;
        else if (grade === "F") points = 0 * creditHours;
        else {
            alert(`Invalid grade for Course ${i + 1}.`);
            return;
        }

        totalPoints += points;
        totalCreditHours += creditHours;
    }

    const gpa = totalCreditHours > 0 ? (totalPoints / totalCreditHours).toFixed(2) : 0;
    document.getElementById("gpa-result").textContent = `Your GPA is ${gpa}`;
});
