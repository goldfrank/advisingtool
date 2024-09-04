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

    function logging (){
        chosen_arr = chosen_arr;
    }
</script>


<Semester
    name = "F24"
    courses = {courses}
    bind:chosen={chosen_arr[0]}
    bind:available_courses 
    on:cleared={logging}
    on:message={logging}
/>


<Semester 
    name = "S25"
    courses = {courses}
    bind:chosen={chosen_arr[1]}
    bind:available_courses
    on:cleared={logging}
    on:message={logging}
/>


<h3>Courses Chosen:</h3>
{#each chosen_arr as chosen}
    {#if chosen }
        {#each chosen as chosen_course}
            {#if chosen_course}
                {chosen_course} <br/>
            {/if}
        {/each}
    {/if}
{/each}