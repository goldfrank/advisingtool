<script>
    //@ts-nocheck
    import Validationbox from "./Validationbox.svelte";
    import _ from "lodash";
    
    export let formatted_reqs;
    export let course_semester;
    export let curriculum_year;
    
    function possible_assignments(target_course) {
        let reqs = [];
        for (let req in formatted_reqs){
            for (let course in formatted_reqs[req]['courses']) {
                if (formatted_reqs[req]['courses'][course]['id'] == target_course) {
                    reqs.push(formatted_reqs[req]['req']);
                }
            }
            
        }
        return reqs
    }

    function check_reached(assignments) {
        let was_reached = false;
        for (let prior_assignments of reached) {
            if (_.isEqual(prior_assignments, assignments)) {
                was_reached = true;
            }
        }
        return was_reached
    }

    function check_tuple(assignments, course, semester){
        let found = false;
        for (let v of Object.values(assignments)) {
            if (v[0] == course && v[1] == semester) {
                found = true
            }
        }
        return found
    }


    function sort_and_prune(course_semester) {
        let new_course_semester = []
        for (let c in course_semester) {
            if (course_semester[c].length < 5) {
                course_semester[c][4] = possible_assignments(course_semester[c][0]).length
            }
            if (course_semester[c][4] > 0) {
                new_course_semester.push(course_semester[c])
            }
            else{
                console.log("Pruning", course_semester[c])
            }
            
        }
        return _.sortBy(new_course_semester, [(o) => o[4]])
    }

    function expand(assignments) {
        // console.log("======Expanding=====")
        let test_assignment;
        let to_return = [];
        for (let course_and_semester of course_semester){
            let course = course_and_semester[0]
            let semester = course_and_semester[1]
            if (! check_tuple(assignments, course, semester)) {
                for (let possible_assignment of possible_assignments(course)) {
                    if (! Object.keys(assignments).includes(possible_assignment)){
                        test_assignment = Object.assign({}, assignments);
                        test_assignment[possible_assignment] = [course, semester]
                        if (! check_reached(test_assignment)){
                            to_return.push(test_assignment);
                        }
                    }
                }
            }
        }
        if (to_return.length > 0) {
            return to_return
        }
        return false
    }

    let min_possible_score = Math.max(formatted_reqs.length-course_semester.length, 0);  
    let frontier = []; 
    let reached = [];
    let unused = [];

    export function reassign(course_semester_update) {
        course_semester = course_semester_update;
        course_semester = sort_and_prune(course_semester)
        console.log("sorted course list", course_semester)
        final_assignment = assign_courses();
        console.log("final assignment:",final_assignment);
        unused = find_unused(course_semester, final_assignment);
    }
    
    function assign_courses() {
        min_possible_score = Math.max(formatted_reqs.length-course_semester.length, 0)
        console.log("best possible score:", min_possible_score)
        let min_score = formatted_reqs.length
        let assignments = {};
        frontier.push(assignments)
        let i = 0;
        let best_assignment = Object.assign({}, assignments);
        while(true){
            i ++
            assignments = frontier.pop()
            let all_expanded = expand(assignments)
            if (all_expanded) {
                for (let expanded of all_expanded) {
                    reached.push(expanded)
                    frontier.push(expanded)
                } 
            }
            let score = formatted_reqs.length - Object.values(assignments).length
            // console.log(score)
            if (score < min_score) {
                min_score = score;
                best_assignment = assignments;
                console.log(min_score, assignments)
            }
            if (frontier.length == 0 || min_score == min_possible_score || i > 250) {
                console.log("assigning with score", min_score, best_assignment)
                return best_assignment
            }
        }
    }

    function find_unused(course_semester, assignments) {
        let unused = [];
        for (let course of course_semester) {
            let used = false;
            for (let assignment of Object.values(assignments)) {
                if (course[0] == assignment[0]){
                    used = true;
                }
            }
            if (! used) {
                unused.push(course)
            }
        }
        return unused;
    }

    let final_assignment = assign_courses();
    
    console.log("Done!")

    function semester_assignment(final_assignment, req) {
        if (Object.values(final_assignment).length > 0) {
            if (Object.keys(final_assignment).includes(req['req'])) {
                return final_assignment[req['req']][1];
            }
        }
        return "None";
    }
    
    function selectedId_assignment(final_assignment, req) {
        if (Object.values(final_assignment).length > 0) {
            if (Object.keys(final_assignment).includes(req['req'])) {
                return final_assignment[req['req']][0];
            }
        }
        return
    }
</script>

<h3>{curriculum_year} Curriculum</h3>
{#each formatted_reqs as req}
    <Validationbox
    requirementName = {req['req']}
    courses={req['courses']}
    semester={semester_assignment(final_assignment, req)}
    selectedId = {selectedId_assignment(final_assignment, req)}
    />
{/each}
<br/><br/>
<h3>Not Used</h3>
{#each unused as unused_course}
    {unused_course[0]}
    {unused_course[1]} 
    <br/>
{/each}
