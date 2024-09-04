<script>
    // @ts-nocheck
    
        import Classbox from "./Classbox.svelte";
    
        export let courses = [
        { id: "csci1111", text: "CSCI 1111"},
        { id: "csci1112", text: "CSCI 1112"},
        { id: "csci1311", text: "CSCI 1311"},
        { id: "csci2113", text: "CSCI 2113"},
        { id: "bask1001", text: "BASK 1001"},
        { id: "hist1235", text: "HIST 1235"}
        ];
        
        export let available_courses = courses;
        export let chosen = [];
        export let chosen_ids = [];
        let num_courses = 4;
    
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
        };
    </script>


{#each {length: num_courses} as _, i}
<Classbox 
    courses={available_courses} 
    bind:selected={chosen[i]}
    bind:selected_id={chosen_ids[i]}
    on:message={update_available(courses, chosen, i, false)}
    on:cleared={update_available(courses, chosen, i, true)}
    on:message
    on:cleared
    />
{/each}