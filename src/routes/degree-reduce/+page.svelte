<script>
    // @ts-nocheck
    import Validationbox from "../../lib/Validationbox.svelte"
    import { requirements } from "../../lib/19-20_requirements.json"
    import _ from "lodash";

    let formatted_reqs = requirements;

    let courses_taken = ['csci1111','csci1112','csci1311', 'csci2113', 
    'seas1001', 'csci1012', 'csci4511', 'csci3410', 'csci4531', 'csci4243',
    'csci4244', 'csci3410', 'csci3411', 'math1231', 'math1232', 'csci3401', 'uw1020',
    'uw1099', 'geol2151', 'amst1200', 'anth3701', 'geog2141', 'cmus1701', 'fina6224',
    'hist2490', 'amst3950', 'hist6801', 'amst1160', 'csci4331', 'math2184'];
    
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

    
       

    function expand(assignments) {
        let test_assignment;
        for (let course of courses_taken){
            if (! Object.keys(assignments).includes(course)) {
                for (let possible_assignment of possible_assignments(course)) {
                    if (! Object.values(assignments).includes(possible_assignment)){
                        test_assignment = Object.assign({}, assignments);
                        test_assignment[course] = possible_assignment
                        if (! check_reached(test_assignment)){
                            return test_assignment;
                        }
                    }
                }
            }
        }
        console.log("xok")
        return false
    }



    let min_possible_score = Math.max(formatted_reqs.length-courses_taken.length, 0);
    // console.log(min_possible_score)
    

    let frontier = []; 
    let reached = [];
    
    function assign_courses() {
        let min_score = formatted_reqs.length
        let assignments = {};
        frontier.push(assignments)
        let i = 0;
        console.log("best possible score", min_possible_score)
        let best_assignment;
        while(true){
            assignments = frontier.pop()
            let expanded = expand(assignments)
            if (expanded) {
                reached.push(expanded)
                frontier.push(expanded)
            }
            let score = formatted_reqs.length - Object.values(assignments).length
            if (score < min_score) {
                min_score = score;
                // console.log(score, assignments)
                best_assignment = assignments;
            }
            if (frontier.length == 0) {
                console.log(min_score, best_assignment)
                return best_assignment
            }
            i ++
        }
        console.log(Object.values(assignments).length, assignments)
        if (formatted_reqs.length - Object.values(assignments).length == min_possible_score){
            console.log("Optimal Assignment Found")
            return assignments
        }
    }

    assign_courses()

    // check_reached(assignments)
    // console.log(Object.entries(otis).includes(assignments))

</script>
<h1>😌</h1>

<h3>Requirement Group</h3>

{#each formatted_reqs as req}
    <Validationbox
    requirementName = {req['req']}
    courses={req['courses']}
    semester='xok'
    />
{/each}
<br/>
<br/>

<!-- courses={(course_inventory(req['satisfied_by']))} -->