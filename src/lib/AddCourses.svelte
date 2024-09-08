<script>
    //@ts-nocheck
    import { TextArea } from "carbon-components-svelte";
    import { Button } from "carbon-components-svelte";
    import { createEventDispatcher } from 'svelte';
    import { Select, SelectItem } from "carbon-components-svelte";

    let text_input;
    let instructions_text = " "
    let semester="Spring 2025";
    let new_courses = [];

    const dispatch = createEventDispatcher();

	function courses_added(new_courses) {
        console.log("dispatching", new_courses)
        dispatch('courses_added', new_courses);
	}

    function click_handle(){
        new_courses = []
        instructions_text = "Ensure input is one course per line!"
        let lines = text_input.split("\n")
        for (let line of lines) {
            let course_id = line.match(/[a-zA-Z]*/)[0].toLowerCase() + line.match(/[0-9]{2,4}[wW]?/)[0].toLowerCase()
            let grade = "--"
            let credits = "3"
            if (line.includes("(")) {
                credits = line.match(/\([0-9]\)/)[0][1]
            }
            new_courses.push([course_id, semester.toLowerCase().replace(/\s/g, ''), grade, credits])
        }
        instructions_text = "Courses added!"
        console.log("New courses:", new_courses)
        courses_added(new_courses)
    }
</script>

<div style="width: 55rem">
        <Select
    labelText="Semester"
    bind:value={semester}
    on:change={(e) => semester = e.target.value}
    >
        <SelectItem value="Spring 2025" />
        <SelectItem value="Summer 2025" />
        <SelectItem value="Fall 2025" />
        <SelectItem value="Spring 2026" />
        <SelectItem value="Summer 2026" />
    </Select>
    Type in candidate courses, once per line.<br/>
    If course is not 3 credits, indicate credits in parentheses. <br/>
    <br/>
    Examples:<br/> 
    CSCI 2113<br/>
    CSCI 1010 (1)<br/>
    CSCI 3907 (2)<br/>
    <TextArea 
        labelText="" 
        placeholder="Courses to add..." 
        bind:value={text_input}
    />
</div>
<br/>
<Button     
    on:click={click_handle}
    >Add Courses
</Button>
<br/>
{instructions_text}