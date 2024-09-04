<script>
    // @ts-nocheck
    
        import Classbox from "./Classbox.svelte";
    
        export let courses = [];
        
        export let available_courses = courses;
        export let chosen = [];
        export let chosen_ids = [];
        let num_courses = 4;
    
        function update_available (courses, chosen, i, remove) {
            available_courses = courses;
            if (remove) { 
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
            chosen = chosen;
            console.log(chosen);
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