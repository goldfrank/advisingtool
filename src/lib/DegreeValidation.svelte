<script>
    //@ts-nocheck
    import Validationbox from "./Validationbox.svelte";
    import _ from "lodash";
    
    export let formatted_reqs = [];
    export let course_details = [];
    export let curriculum_year = "21";
    
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

    function check_collection(assignments, collection) {
        let was_reached = false;
        for (let prior_assignments of collection) {
            if (_.isEqual(prior_assignments, assignments)) {
                was_reached = true;
            }
        }
        return was_reached
    }

    function sort_and_prune(course_details) {
        let new_course_details = []
        for (let c in course_details) {
            if (course_details[c].length < 5) {
                course_details[c][4] = possible_assignments(course_details[c][0]).length
            }
            if (course_details[c][4] > 0) {
                new_course_details.push(course_details[c])
            }
            else{
                console.log("Pruning", course_details[c])
            }
            
        }
        return _.sortBy(new_course_details, [(o) => o[4]]).reverse()
    }

    function cy_checks(assignments, course, possible_slot, cy) {
        if (cy == "C.Y. 2021 B.S.") {
            // check 1-credit general electives
            if ((possible_slot.includes("elective_") && +course[4] < 3)) {
                console.log("too few credits", course)    
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
        }
        return true
    }

    function expand(assignments) {
        // generate all successor assignments
        let candidate_assignments = Object.assign({}, assignments);
        for (let course of course_details) {
            let course_str = course[0]+ "#" + course[1]
            if (! Object.keys(candidate_assignments).includes(course_str)) {
                for (let possible_slot of possible_assignments(course[0])) {
                    if (! Object.values(candidate_assignments).includes(possible_slot)) {
                        candidate_assignments[course_str] = possible_slot;
                        if (! check_collection(candidate_assignments, reached) && ! check_collection(candidate_assignments, frontier) ) {
                            if (cy_checks(assignment, course, possible_slot, curriculum_year)) {
                            frontier.push(candidate_assignments)
                            candidate_assignments = Object.assign({}, assignments);
                            }
                        }
                    }
                }
            }
        }
    }

    let min_possible_score = Math.max(formatted_reqs.length-course_details.length, 0);  
    let frontier = []; 
    let reached = [];
    let unused = [];

    
    function assign_courses() {
        min_possible_score = Math.max(formatted_reqs.length-course_details.length, 0);
        console.log("best possible score:", min_possible_score);
        let min_score = formatted_reqs.length;
        let score = formatted_reqs.length;
        let assignments = {}; // course#semester: slot
        let best_assignments = {}
        expand(assignments);
        let k = 0;
        while (true && min_score > min_possible_score && k < 5000) {
            assignments = frontier.pop();
            reached.push(assignments)
            score = formatted_reqs.length-Object.keys(assignments).length;
            expand(assignments);
            if (score <= min_score) {
                min_score = score;
                best_assignments = Object.assign({}, assignments);
                console.log(score, best_assignments);
            }
            if (k % 100 == 0){
                console.log(k)
            }
            k++;
        }
        return(best_assignments)
    }


    let swapped_assignments = {}
    let final_assignments = {};
    
    export function reassign(course_details_update) {
        course_details = course_details_update;
        course_details = sort_and_prune(course_details)
        console.log("sorted course list", course_details)
        final_assignments = assign_courses();
        for (let k of Object.keys(final_assignments)) {
            swapped_assignments[final_assignments[k]] =k;
        }
        console.log("Swapped", swapped_assignments)
        unused = find_unused(course_details, final_assignments);
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
                return x[k].split("#")[1]
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

    console.log("Done!")




</script>

<h3>{curriculum_year} Curriculum</h3>
{#each formatted_reqs as req}
    <Validationbox
    requirementName = {req['req']}
    courses={req['courses']}
    semester={semester_if_exists(swapped_assignments, req)}
    selectedId = {course_if_exists(swapped_assignments, req)}
    />
{/each}
<br/><br/>
<h3>Not Used</h3>
{#each unused as unused_course}
    {unused_course[0]}
    {unused_course[1]} 
    <br/>
{/each}
