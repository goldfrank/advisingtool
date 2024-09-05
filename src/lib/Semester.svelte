<script>
    // @ts-nocheck
    
        import Classbox from "./Classbox.svelte";
        import { Button } from "carbon-components-svelte";
	    import { ContinuousDeployment } from "carbon-icons-svelte";
        import AddAlt from "carbon-icons-svelte/lib/AddAlt.svelte";
        import SubtractAlt from "carbon-icons-svelte/lib/SubtractAlt.svelte";
   
        export let courses = [];
        export let name = "Semester Name";
        export let available_courses = courses;
        available_courses.sort(compare_text)
        export let chosen = [];
        export let chosen_ids = [];
        export let num_courses = 4;
    
        for (let k = 0; k < num_courses; k++) {
            chosen.push("")
            chosen_ids.push("")
        }

        function compare_text(x, y){
            if (x.text < y.text) {
                return -1
            }
            if (x.text > y.text) {
                return 1
            }
            return 0
        }

        function update_available (courses, chosen, chosen_ids, i, remove=false, subtract=false) {
            if (remove && ! subtract) {
                console.log(chosen_ids[i])
                available_courses.push(courses.find((course) => course.id == chosen_ids[i]))
                available_courses.sort(compare_text)
                chosen_ids.pop()
                chosen.pop()
            }
            if (remove) {
                available_courses.sort(compare_text)
            }
            for (let course in courses) {
                if (chosen_ids.includes(courses[course].id)) {
                    available_courses = available_courses.filter(x => {
                    return x.id != courses[course].id;
                    })
                }
            }
            // chosen = chosen;
        };

        function add_course() {
            num_courses++
            chosen.length ++
            chosen_ids.length ++
        }

        function subtract_course(chosen_item, courses, chosen, chosen_ids) {
            console.log(chosen_item)
            if (num_courses > 0) {
                chosen.pop()
                chosen_ids.pop()
                num_courses--
                if (chosen_item) {
                    available_courses.push(courses.find((course) => course.id == chosen_item))
                    update_available(courses, chosen, chosen_ids, chosen.length-1, true, true)
                }
                
                // chosen.length = chosen.length - 1
                // chosen_ids.length = chosen_ids.length - 1
                console.table(chosen_ids)
                console.table(chosen)
                console.log(chosen.length)
                
            }
        }


        function selectable_courses(available_courses, selected_id, selected) {
            if (typeof selected_id != 'undefined') {
                if (selected_id[selected_id.length - 1] == 'w'){
                    console.log('otis')
                    return [{ id: selected_id, text: selected}]
                }
            }
            return available_courses
        }

    </script>

<h3>{name}</h3>
{#each {length: num_courses} as _, i}

<Classbox 
    bind:selected={chosen[i]}
    bind:selected_id={chosen_ids[i]}
    courses={selectable_courses(available_courses, chosen_ids[i], chosen[i])}
    on:message={update_available(courses, chosen, chosen_ids, i, false)}
    on:cleared={update_available(courses, chosen, chosen_ids, i, true)}
    on:message
    on:cleared
    /> 
{/each}
<br/>

<Button 
    icon={AddAlt} 
    kind = "ghost"
    on:click={add_course}
    >Add Course
</Button>

<Button 
    icon={SubtractAlt} 
    kind = "ghost"
    on:click={() => subtract_course(chosen_ids[chosen_ids.length - 1], courses, chosen, chosen_ids)}
    >
    Remove Course
</Button>