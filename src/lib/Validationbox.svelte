<script>
// @ts-nocheck
    import { ComboBox } from "carbon-components-svelte";
    import { createEventDispatcher } from 'svelte';
    import { Button } from "carbon-components-svelte";
    import { Tile } from "carbon-components-svelte";
    
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


    function shouldFilterItem(item, value) {
    if (!value) return true;
    return item.text.toLowerCase().includes(value.toLowerCase());  
    }

    export let courses;
    export let req;
    export let selectedId = '';
    export let requirementName = "Requirement";
    export let semester = "Winter 2019";
    export let credits;
    export let grade;

    // console.log(courses)


    const dispatch = createEventDispatcher();

	// function selected(event) {
	// 	dispatch('selected', event.detail);
	// }

    // function cleared(event) {
	// 	dispatch('cleared', event.detail);
    //     console.log("cleared", req);
	// }

    function selectCourse(event){
        selectedId = event.detail['selectedId']
        dispatch('selected', [req['req'], selectedId, semester]);
        // console.log('selected', [req['req'], selectedId]);
        
    }

    function clearCourse(event){
        dispatch('cleared', req['req']);
        // console.log("cleared", req['req']);
    }

    function changeSemester(event){
        dispatch("changeSemester",[selectedId, event.detail, req, semester]) //last item is *old* semester
    }

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
        items = {courses}
        selectedId = {selectedId}
        on:select={selectCourse}
        on:clear={clearCourse}
        {shouldFilterItem}
        />
    </div>

        <div class="semester-name">
            <ComboBox
            size=sm
            placeholder="Semester"
            items={possible_semesters}
            selectedId={semester}
            on:select={changeSemester}
            />
        </div>

        <div class="credits">
            <ComboBox
            size=sm
            placeholder="Credits"
            
            />
        </div>

</div>