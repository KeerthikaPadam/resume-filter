// script.js
document.addEventListener("DOMContentLoaded", function () {
    const skillFilter = document.getElementById("skill-filter");
    const experienceFilter = document.getElementById("experience-filter");
    const experiences = document.querySelectorAll(".experience");

    // Function to filter the experiences based on selected filters
    function filterContent() {
        const selectedSkill = skillFilter.value;
        const selectedExperience = experienceFilter.value;

        experiences.forEach((exp) => {
            const expSkill = exp.getAttribute("data-skill");
            const expLevel = exp.getAttribute("data-level");

            // Show experience if it matches the selected filters
            if (
                (selectedSkill === "all" || expSkill === selectedSkill) &&
                (selectedExperience === "all" || expLevel === selectedExperience)
            ) {
                exp.style.display = "block";
            } else {
                exp.style.display = "none";
            }
        });
    }

    // Event listeners for the filters
    skillFilter.addEventListener("change", filterContent);
    experienceFilter.addEventListener("change", filterContent);

    // Initial call to filter content
    filterContent();
});
