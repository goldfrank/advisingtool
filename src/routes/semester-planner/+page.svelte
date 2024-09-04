<script>
// @ts-nocheck

    import Classbox from "../../lib/Classbox.svelte";
    import Semester from "../../lib/Semester.svelte";

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

    function update_available (courses, chosen, i, remove) {
        available_courses = courses;
        if (remove) { 
            console.log(chosen_ids[i]);
            chosen_ids[i] = ""
            chosen[i] = ""
        }
        for (let course in courses) {
            if (chosen_ids.includes(courses[course].id)) {
                available_courses = available_courses.filter(x => {
                return x.id != courses[course].id;
                })
            }
        }
        console.log(chosen);
    };

    function otis (){
        console.log("otis")
    }
    function carl (){
        console.log("carl")
    }
</script>


<Semester bind:chosen={chosen_arr[1]} 
    on:cleared={otis}
    on:forward={carl}
    on:otis
       
/>



<!-- <h2> <strong>Semester Planner </strong></h2>
{#each {length: num_courses} as _, i}
<Classbox 
    courses={available_courses} 
    bind:selected={chosen[i]}
    bind:selected_id={chosen_ids[i]}
    on:message={update_available(courses, chosen, i, false)}
    on:cleared={update_available(courses, chosen, i, true)}
    />
{/each} -->

<h3>Courses Chosen:</h3>
{#if chosen_arr[1] }
    {#each chosen_arr[1] as chosen_course}
        {#if chosen_course}
            {chosen_course} <br/>
        {/if}
    {/each}
{/if}