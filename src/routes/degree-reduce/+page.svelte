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
    'hist2490', 'hist6801', 'hist6801', 'hist6801', 'csci4331', 'math2184', 'bisc1111',
    'csci3212', 'stat4157', 'csci4364', 'anth1003', 'anth1004', 'bisc1112', 'chem1112', 'csci1010', 'csci2312', 'csci2501', 'csci2541w', 'csci3313'];

    let course_semester = [];
    for (let c of courses_taken) {
        course_semester.push([c, 'fall23'])
    }
    course_semester[26][1] = "spring23";
    console.log(course_semester)
    
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

    function expand(assignments) {
        let test_assignment;
        for (let course_and_semester of course_semester){
            let course = course_and_semester[0]
            let semester = course_and_semester[1]
            if (! check_tuple(assignments, course, semester)) {
                for (let possible_assignment of possible_assignments(course)) {
                    if (! Object.keys(assignments).includes(possible_assignment)){
                        test_assignment = Object.assign({}, assignments);
                        test_assignment[possible_assignment] = [course, semester]
                        if (! check_reached(test_assignment)){
                            return test_assignment;
                        }
                    }
                }
            }
        }
        return false
    }

    let min_possible_score = Math.max(formatted_reqs.length-courses_taken.length, 0);  
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
            if (frontier.length == 0 || min_score == min_possible_score) {
                console.log(min_score, best_assignment)
                return best_assignment
            }
        }
    }

    let final_assignment = assign_courses();
    let flipped_assignment = {};
    for (let f of Object.keys(final_assignment)) {
        flipped_assignment[final_assignment[f]] = f
    }
    console.log("Done!")
    // check_reached(assignments)
    // console.log(Object.entries(otis).includes(assignments))

</script>
<h1>😌</h1>

<h3>Requirement Group</h3>

{#each formatted_reqs as req}
    <Validationbox
    requirementName = {req['req']}
    courses={req['courses']}
    semester={final_assignment[req['req']][1]}
    selectedId = {final_assignment[req['req']][0]}
    />
{/each}
<br/>
<br/>

<!-- courses={(course_inventory(req['satisfied_by']))} -->