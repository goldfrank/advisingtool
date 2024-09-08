<script>
    //@ts-nocheck
    
    import Validationbox from "$lib/Validationbox.svelte";
    import _ from "lodash";
    import { createEventDispatcher } from 'svelte';
    import { pretty_slots } from "$lib/pretty_slots.json"
    

    
    export let formatted_reqs = [];
    export let course_details = [];
    export let curriculum_year = "21";

    // Prettify Display (eventually JSON/config per CY?)
    
    
    // Handle dispatch
    const dispatch = createEventDispatcher();

	function working(finished) {
        dispatch('working', finished);
	}
    

    
    // What slot assignments are possible for each course?
    function possible_assignments(target_course) {
        let reqs = [];
        for (let req in formatted_reqs){
            for (let course in formatted_reqs[req]['courses']) {
                if (formatted_reqs[req]['courses'][course]['id'] == target_course) {
                    reqs.push(formatted_reqs[req]['req']);
                }
            }        
        }
        return reqs.reverse()
    }

    // Pregenerate table of possible assignments per course
    function generate_assign_table(){
        let possible_assign_table = {};
        console.log("populating table")
            for (let course of course_details) {
                let target_course = course[0];
                // console.log(target_course)
                let reqs = [];
                for (let req in formatted_reqs){
                    for (let course in formatted_reqs[req]['courses']) {
                        if (formatted_reqs[req]['courses'][course]['id'] == target_course) {
                            reqs.push(formatted_reqs[req]['req']);
                        }
                    }        
                }
                possible_assign_table[target_course] = reqs.reverse()
            } 
        return possible_assign_table
    }

    // Prune courses that can't go in any slot
    // Sort courses by number of slots they can occupy
    function sort_and_prune(course_details) {
        let new_course_details = []
        for (let c in course_details) {
            //count
            if (course_details[c].length < 5) {
                course_details[c][4] = possible_assignments(course_details[c][0]).length
            }
            //prune
            if (course_details[c][4] > 0) {
                new_course_details.push(course_details[c])
            }
            else{
            }
            
        }
        //sort and return
        return _.sortBy(new_course_details, [(o) => o[4]]).reverse()
    }

    // Special checks for each curriculum year
    function cy_checks(assignments, candidate_assignments, course, possible_slot, cy) {
        if (cy == "C.Y. 2021 B.S.") {
            // check 1-credit general electives
            if ((possible_slot.includes("elect") && (course[3].includes('1') || course[3].includes('2')) )) {
                return false
            }
            // check for two-couse science sequence
            if (possible_slot.includes("sci_2")) {
                let to_break = false
                for (let assignment of Object.keys(candidate_assignments)) {
                    if (assignment.slice(0,4) == course[0].match(/[A-Z]{4}/)) {
                        to_break = true;
                    }
                }
                if (to_break) { 
                    return false 
                }
            }
            // check for 6534 repeats
            if (course[0].includes("csci6534")) {
                if (JSON.stringify(candidate_assignments).match(/csci6534/g).length > 1) {
                    return false
                }
            }
        }
        return true
    }

    // expand current assignments (node)
    function expand(assignments, table) {
        // generate all successor assignments
        let candidate_assignments = Object.assign({}, assignments);
        for (let course of course_details) {
            let course_str = course[0]+ "#" + course[1]
            if (! Object.keys(candidate_assignments).includes(course_str)) {
                for (let possible_slot of table[course[0]]) {
                    if (! Object.values(candidate_assignments).includes(possible_slot)) {
                        candidate_assignments[course_str] = possible_slot;
                        if (!( (JSON.stringify(candidate_assignments) in frontier_dict) && (JSON.stringify(candidate_assignments) in reached_dict) )) {
                            if (cy_checks(assignments, candidate_assignments, course, possible_slot, curriculum_year)) {
                                frontier.push(candidate_assignments)
                                frontier_dict[JSON.stringify(candidate_assignments)] = true;
                                reached_dict[JSON.stringify(candidate_assignments).replace(/\_[0-9]\"/g,"\"")] = true;
                            }                            
                            candidate_assignments = Object.assign({}, assignments);                
                        }
                    }
                }
            }
        }
    }

    let min_possible_score = Math.max(formatted_reqs.length-course_details.length, 0);  
    let frontier = [];
    let frontier_dict = {}
    let reached_dict = {};
    let unused = [];

    
    function assign_courses(table) {
        min_possible_score = Math.max(formatted_reqs.length-course_details.length, 0);
        console.log("best possible score:", min_possible_score);
        let min_score = formatted_reqs.length;
        let score = formatted_reqs.length;
        let assignments = {}; // course#semester: slot
        let best_assignments = {}
        expand(assignments, table);
        let k = 0
        while (true && min_score > min_possible_score && k < 100 && frontier.length > 0) {
            assignments = frontier.pop();
            delete frontier_dict[JSON.stringify(assignments)]
            // reached.push(assignments)
            score = formatted_reqs.length-Object.keys(assignments).length;
            expand(assignments, table);
            // prevent cycling amongst equivalent solns
            if (score == min_score)  {
                k++
            }
            if (score < min_score) {
                k = 0
                min_score = score;
                best_assignments = Object.assign({}, assignments);
            }
            
        }
        working(true)
        return(best_assignments)
    }


    let swapped_assignments = {}
    let final_assignments = {};
    
    export function reassign(course_details_update) {
        working(false)
        course_details = Object.assign({}, course_details_update);
        course_details = sort_and_prune(course_details)
        let assign_table = generate_assign_table();
        final_assignments = assign_courses(assign_table);
        for (let k of Object.keys(final_assignments)) {
            swapped_assignments[final_assignments[k]] =k;
        }
        unused = find_unused(course_details_update, final_assignments);
        console.log("Unused Courses", unused)
        return [final_assignments, swapped_assignments, course_details, unused]

    }

    function find_unused(course_details, assignments) {
        let unused = [];
        for (let course of course_details) {
            let used = false;
            for (let assignment of Object.keys(assignments)) {
                if (course[0] + "#" + course[1] == assignment){
                    used = true;
                }
            }
            if (! used) {
                unused.push(course)
            }
        }
        return unused;
    }

    
    function semester_if_exists(x, req){
        let k = req['req']
        if (Object.keys(x).length > 0){
            if (Object.keys(x).includes(k)) {
                let sem = x[k].split("#")[1];
                let season = sem.split(/[0-9]{4}/)[0]
                let year = sem.split(/.*(?=[0-9]{4})/)[1]
                return season.charAt(0).toUpperCase() + season.slice(1) + " " + year
            }
        }
        return "None"
    }

    function course_if_exists(x, req){
        let k = req['req']
        if (Object.keys(x).length > 0){
            if (Object.keys(x).includes(k)) {
                return x[k].split("#")[0]
            }
        }
        return "None"
    }

    console.log("course details", course_details)


</script>

<h3>{curriculum_year} Curriculum</h3>
{#each formatted_reqs as req}
    <Validationbox
    requirementName = {pretty_slots[req['req']]}
    courses={req['courses']}
    semester={semester_if_exists(swapped_assignments, req)}
    selectedId = {course_if_exists(swapped_assignments, req)}
    />
{/each}
<br/><br/>
<h3>Not Used</h3>
{#each unused as unused_course}
    {unused_course[0].match(/[a-z]*/)[0].toUpperCase()}
    {unused_course[0].match(/[0-9]{2,4}[wW]?/)[0].toUpperCase()}
    {unused_course[1].match(/[a-z]*/)[0][0].toUpperCase() + unused_course[1].match(/[a-z]*/)[0].slice(1)}
    {unused_course[1].match(/[0-9]{2,4}/)}
    <br/>
{/each}
