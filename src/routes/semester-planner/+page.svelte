<script>
// @ts-nocheck

    import Classbox from "../../lib/Classbox.svelte";
    import Semester from "../../lib/Semester.svelte";
    import { Button } from "carbon-components-svelte";
    import AddAlt from "carbon-icons-svelte/lib/AddAlt.svelte";
    import SubtractAlt from "carbon-icons-svelte/lib/SubtractAlt.svelte";

    let courses = [
    { id: "csci1111", text: "CSCI 1111"},
    { id: "csci1112", text: "CSCI 1112"},
    { id: "csci1311", text: "CSCI 1311"},
    { id: "csci2113", text: "CSCI 2113"},
    { id: "bask1001", text: "BASK 1001"},
    { id: "hist1235", text: "HIST 1235"}
    ];
    let available_courses = courses;
    
    let chosen_arr = [];
    let chosen_ids_arr = [];

    function logging (){
        chosen_arr = chosen_arr;
    }

    function generate_semesters(start_semester){
        let semesters = []
        let seasons = ["Spring", "Summer", "Fall"]
        let year = start_semester.match(/[0-9]{4}/)
        year = +year
        let season = start_semester.match(/[A-Z][a-z]+/)
        semesters.push(start_semester)
        for (let j = 0; j < 13; j++) {
            let i = seasons.indexOf(season)
            i = (i + 1) % 3
            season = seasons[i]
            if (i == 0) {
                year += 1
            }
            semesters.push(season + " " + year)
        }
        return semesters
    }

    let semesters = generate_semesters("Fall 2024")

    function add_semester(semesters) {
        let last_semester = semesters[semesters.length - 1]
        let seasons = ["Spring", "Summer", "Fall"]
        let year = last_semester.match(/[0-9]{4}/)
        year = +year
        let season = last_semester.match(/[A-Z][a-z]+/)
        let i = seasons.indexOf(season[0])
        i = (i + 1) % 3
        season = seasons[i]
        if (i == 0) {
            year += 1
        }
        semesters.push(season + " " + year)
        return semesters
    }

    function remove_semester(semesters){
        semesters.pop()
        return semesters
    }

    // add_semester(semesters)
</script>

{#each semesters as semester}
<Semester
    name = {semester}
    courses = {courses}
    num_courses = {(semester.includes("Summer")) ? 0 : 5}
    bind:chosen={chosen_arr[0]}
    bind:available_courses 
    on:cleared={logging}
    on:message={logging}
/>
{/each}
<br/>
<Button 
    icon={AddAlt} 
    on:click={() => semesters = add_semester(semesters)}
    >Add Semester
</Button>
<Button 
    icon={SubtractAlt} 
    on:click={() => semesters = remove_semester(semesters)}
    >Remove Semester
</Button>
    

<!-- <h3>Courses Chosen:</h3>
{#each chosen_arr as chosen}
    {#if chosen }
        {#each chosen as chosen_course}
            {#if chosen_course}
                {chosen_course} <br/>
            {/if}
        {/each}
    {/if}
{/each} -->