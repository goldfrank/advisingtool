<script>
// @ts-nocheck
    import { ComboBox } from "carbon-components-svelte";
    import { createEventDispatcher } from 'svelte';
    import { Button } from "carbon-components-svelte";
    import { Tile } from "carbon-components-svelte";
    import { Toggle } from "carbon-components-svelte";

    
    let possible_semesters = [{ id:"Fall 2021", text: "Fall 2021"},
    { id:"Spring 2022", text: "Spring 2022"},
    { id:"Summer 2022", text: "Summer 2022"},
    { id:"Fall 2022", text: "Fall 2022"},
    { id:"Spring 2023", text: "Spring 2023"},
    { id:"Summer 2023", text: "Summer 2023"},
    { id:"Fall 2023", text: "Fall 2023"},
    { id:"Spring 2024", text: "Spring 2024"},
    { id:"Summer 2024", text: "Summer 2024"},
    { id:"Fall 2024", text: "Fall 2024"},
    { id:"Spring 2025", text: "Spring 2025"}
    ]

    let grade_gpa = {"--": null, "A": 4, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "C+": 2.3,
                 "C": 2, "C-": 1.7, "D+": 1.3, "D": 1.0, "D-": 0.7, "F": 0.0, "TR": null};

    let grade_index = []

    for (let [g, val] of Object.entries(grade_gpa)) {
        grade_index.push({id: g, text: g})
    }

    let credit_index = [{id: "1", text: 1}, {id: "2", text: 2}, {id: "3", text: 3}, {id: "4", text: 4}, {id: "5", text: 5}, {id: "(1)", text: "(1)"}, {id: "(2)", text: "(2)"}, {id: "(3)", text: "(3)"}, {id: "(4)", text: "(4)"}, {id: "(5)", text: "(5)"}] 

    function shouldFilterItem(item, value) {
    if (!value) return true;
    return item.text.toLowerCase().includes(value.toLowerCase());  
    }

    export let courses;
    export let req;
    export let selectedId = '';
    export let requirementName = "Requirement";
    export let semester;
    export let credits;
    export let grade;
    export let all_courses;
    let old_course = null;
    let old_semester = null;
    let toggled;


    const dispatch = createEventDispatcher();

    function selectCourse(event){
        dispatch('selected', [req['req'], selectedId, semester]);  
    }

    function changeCourse(type, event){
        if (type == "selectCourse") {
            old_course = selectedId;
            selectedId = event.detail['selectedId']
        }
        if (type == "clearCourse") {
            old_course = selectedId;
            selectedId = null;
            old_semester = semester;
            semester = null;
            credits = null;
            grade = null;
        }
        if (type == "selectSemester") {
            old_semester = semester;
            old_course = null;
            semester = event.detail['selectedId']
        }
        if (type == "clearSemester") {
            old_semester = semester;
            old_course = null;
            semester = null;
        }
        if (type == "selectCredits") {
            old_semester = null;
            old_course = null;
            credits = event.detail['selectedId']
        }
        if (type == "clearCredits") {
            old_semester = null;
            old_course = null;
            credits = null;
        }
        if (type == "selectGrade") {
            old_semester = null;
            old_course = null;
            grade = event.detail['selectedId']
        }
        if (type == "clearGrade") {
            old_semester = null;
            old_course = null;
            grade = null
        }
        if (type == "clearCourse" || selectedId) {
            dispatch('changeCourse', {"req": req['req'], "course": selectedId,"semester": semester, "credits": credits, "grade": grade, "old_course": old_course, "old_semester": old_semester});
        }
    }

    console.log(req)
console.log(all_courses)

</script>

<style>
    .validation-box {
        margin-top: 0.5rem;
        width: 25rem;
        display: inline-block;
        margin-left: 1rem;
    }
    .course-box {
		/* background-color */
		-webkit-text-fill-color: rgb(0, 50, 77);
		color: rgb(0, 50, 77);
        margin-top: 0.15rem;
	}
    .req-name {
        display: inline-block; 
        position:relative; 
        top: 0.6em; 
        min-width: 11rem;
        padding-left: 1rem;
    }
    .semester-name {
        display: inline-block; 
        position:relative; 
        /* top: 0.6em;  */
        min-width: 6rem;
        /* margin-left: 0.5rem; */
        text-align: center;
        width: 12rem;
    }
    .credits {
        display: inline-block; 
        position:relative; 
        /* top: 0.6em;  */
        min-width: 6rem;
        /* margin-left: 0.5rem; */
        text-align: center;
        width: 8rem;
    }
    .toggle {
        display: inline-block; 
        position: relative; 
        top: -1.5rem; 
        min-width: 6rem;
        margin-left: 0.5rem;
        text-align: center;
        width: 12rem;
        height: 1rem;
    }
    .req-wrap {
        border: 1px;
        border-style:solid;
        border-color:darkslategrey;
        display: inline-block;
        height: 2rem;
    }

</style>



<div class="course-box">
    <div class="req-wrap">
        <div class="req-name">
            {requirementName} 
        </div>
    </div>
    <div class="validation-box">
        <ComboBox 
        size=sm
        placeholder="Find Course"
        items = {!toggled ? courses : all_courses}
        selectedId = {selectedId}
        on:select={(e) => changeCourse('selectCourse', e)}
        on:clear={(e) => changeCourse('clearCourse', e)}
        {shouldFilterItem}
        />
    </div>

        <div class="semester-name">
            <ComboBox
            size=sm
            placeholder="Semester"
            items={possible_semesters}
            selectedId={semester}
            on:select={(e) => changeCourse('selectSemester', e)}
            on:clear={(e) => changeCourse('clearSemester', e)}
            />
        </div>

        <div class="credits">
            <ComboBox
            size=sm
            placeholder="Credits"
            items={credit_index}
            selectedId={credits}
            on:select={(e) => changeCourse('selectCredits', e)}
            on:clear={(e) => changeCourse('clearCredits', e)}
            />
        </div>

        <div class="credits">
            <ComboBox
            size=sm
            placeholder="Grade"
            items={grade_index}
            selectedId={grade}
            on:select={(e) => changeCourse('selectGrade', e)}
            on:clear={(e) => changeCourse('clearGrade', e)}
            />
        </div>

        <div class="toggle">
            
            <Toggle 
            bind:toggled
            labelA="Override?" 
            labelB="Overriden."
            />
            
        </div>

</div>