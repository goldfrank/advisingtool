<script>
    //@ts-nocheck
    import Validationbox from "./Validationbox.svelte";
    import _ from "lodash";
    import { createEventDispatcher } from 'svelte';
    
    export let formatted_reqs = [];
    export let course_details = [];
    export let curriculum_year = "21";

    const dispatch = createEventDispatcher();

    const pretty_slots = {
        "seas1001": "SEAS 1001",
        "cs1010": "CSCI 1010",
        "cs1111": "CSCI 1111",
        "cs1112": "CSCI 1112",
        "cs2113": "CSCI 2113",
        "cs_architecture": "Architecture",
        "cs1311": "CSCI 1311",
        "calc_1": "Calculus I",
        "calc_2": "Calculus II",
        "uw1020": "UW 1020",
        "cs2312": "CSCI 2312",
        "cs2501": "CSCI 2501",
        "cs2541W": "CSCI 2541W",
        "cs3212": "CSCI 3212",
        "cs3313": "CSCI 3313",
        "cs3410": "CSCI 3410",
        "cs3411": "CSCI 3411",
        "cs4243W": "Capstone I",
        "cs4244": "Capstone II",
        "cs_tech_track_2113_1": "Tech Track I",
        "cs_tech_track_2113_2": "Tech Track II",
        "cs_tech_track_core_1": "Tech Track (Core) I",
        "cs_tech_track_core_2": "Tech Track (Core) II",
        "stats": "Statistics",
        "linear_alg": "Linear Algebra",
        "gened_ss_1": "GenEd (SS) I",
        "gened_ss_2": "GenEd (SS) II",
        "gened_hum": "GenEd (Hum)",
        "sci_seq_1": "Science I",
        "sci_seq_2": "Science II",
        "sci_2": "Science III",
        "seas_hss_1": "SEAS HSS I",
        "seas_hss_2": "SEAS HSS II",
        "seas_hss_3": "SEAS HSS III",
        "ntt_1": "Non-Tech Track I",
        "ntt_2": "Non-Tech Track II",
        "ntt_3": "Non-Tech Track III",
        "elective_1": "Elective I",
        "elective_2": "Elective II",
        "elective_3": "Elective III",
        "elective_4": "Elective IV"
    }

	function working(finished) {
        console.log('dispatch')
        dispatch('working', finished);
	}
    
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

    function cy_checks(assignments, candidate_assignments, course, possible_slot, cy) {
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
                            if (cy_checks(assignments, candidate_assignments, course, possible_slot, curriculum_year)) {
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
        while (true && min_score > min_possible_score) {
            assignments = frontier.pop();
            reached.push(assignments)
            score = formatted_reqs.length-Object.keys(assignments).length;
            expand(assignments);
            if (score <= min_score) {
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
            setTimeout(function() {
            course_details = Object.assign({}, course_details_update);
            course_details = sort_and_prune(course_details)
            console.log("sorted course list", course_details)
            final_assignments = assign_courses();
            for (let k of Object.keys(final_assignments)) {
                swapped_assignments[final_assignments[k]] =k;
            }
            console.log("Swapped", swapped_assignments)
            unused = find_unused(course_details_update, final_assignments);
            console.log(unused)
        },50)
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

    console.log("Done!")


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
    {unused_course[0].match(/[0-9]{4}/)}
    {unused_course[1].match(/[a-z]*/)[0][0].toUpperCase() + unused_course[1].match(/[a-z]*/)[0].slice(1)}
    {unused_course[1].match(/[0-9]{2,4}/)}
    <br/>
{/each}
