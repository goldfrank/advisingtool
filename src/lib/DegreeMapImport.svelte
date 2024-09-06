<script>
    //@ts-nocheck
    import { TextArea } from "carbon-components-svelte";
    import { Button } from "carbon-components-svelte";
    import { createEventDispatcher } from 'svelte';

    let text_input = "";
    let split_string=[];
    export let course_semester = []
    export let uncounted_courses = []

    let r_course_block = /[A-Z]{2,4}\s[0-9]{2,4}W?\s*.*\s*[A-Z\-][A-Z\-\+]?\s*\(?[0-9]\)?\s*[A-Z][a-z]*\s[0-9]{4}/g;
    
    function click_handle(){
        if (text_input) {
            course_semester = []
            split_string = text_input.match(r_course_block)
            let course_strings = []
            for (let substring of split_string){
                course_strings.push(substring.replace(/(\r\n|\n|\r)/gm, ""));
            }
            for (let course_string of course_strings) {
                let split_course = course_string.split("\t");
                let course_id = split_course[0].toLowerCase().replace(" ","");
                let grade= split_course[2];
                let credits = split_course[3];
                let semester= split_course[4].toLowerCase().replace(" ","")
                //handle duplicates
                let duplicate = false;
                for (let existing_course of course_semester) {
                    if ((existing_course[0] == course_id && existing_course[1] == semester)) {
                        duplicate = true;
                    }
                }
                if (! duplicate) {
                    course_semester.push([course_id, semester, grade, credits])
                }
            }
            // course_semester = course_semester
            let cleaned_courses = clean_courses(course_semester)
            course_semester = cleaned_courses[0]
            data_import(course_semester)
        }
    }

    function clean_courses(course_semester) {course_semester
        let counted_courses = []
        let uncounted_courses = []
        for (let course of course_semester) {
            if  (course[2] == "F" || course[2] == "W") {
                uncounted_courses.push(course)
            }
            else {
                counted_courses.push(course)
            }
        }
        console.log("uncounted", uncounted_courses)
        return [counted_courses, uncounted_courses]
    }

    const dispatch = createEventDispatcher();

	function data_import(course_semester) {
        dispatch('data_import', course_semester);
	}



</script>

<div style="width: 55rem">
    <TextArea 
        labelText="" 
        placeholder="Copy and Paste from Degree Map Here" 
        bind:value={text_input}
    />
</div>
<br/>
<Button     
    on:click={click_handle}
    >Import Data
</Button>
<br/>
{#each split_string as s}
{s} <br/>
{/each}