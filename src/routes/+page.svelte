<script>
    // @ts-nocheck
    import Validationbox from "$lib/Validationbox.svelte"
    //import { requirements } from "$lib/19-20_requirements.json"
    import { requirements as requirements_2425 } from "$lib/BS_2024-2025.json"
    import { requirements as requirements_2324 } from "$lib/BS_2023-2024.json"
    import { requirements as requirements_2223 } from "$lib/BS_2022-2023.json"
    import { requirements as requirements_2122 } from "$lib/BS_2021-2022.json"
    import { requirements as requirements_1920 } from "$lib/BS_2019-2020.json"
    import { semesters as semesters_1920 } from "$lib/BS_2019-2020.json"
    import { semesters as semesters_2425 } from "$lib/BS_2024-2025.json"
    import { semesters as semesters_2324 } from "$lib/BS_2023-2024.json"
    import { semesters as semesters_2223 } from "$lib/BS_2022-2023.json"
    import { semesters as semesters_2122 } from "$lib/BS_2021-2022.json"
    import _ from "lodash";
    import { ordering } from "$lib/pretty_slots.json" 
    import { Tabs, Tab, TabContent } from "carbon-components-svelte";
    import DegreeValidation from "$lib/DegreeValidation.svelte"
    import DegreeMapImport from "$lib/DegreeMapImport.svelte"
    import AddCourses from "$lib/AddCourses.svelte"
    import GenerateForms from "$lib/GenerateForms.svelte"
    import { generate_sheet} from "./curriculum-sheet/+page.svelte"
    import { ComboBox } from "carbon-components-svelte";

    function shouldFilterItem(item, value) {
    if (!value) return true;
    return item.text.toLowerCase().includes(value.toLowerCase());  
    }


    let all_requirements = {"B.S. 2024-2025": requirements_2425,
                            "B.S. 2023-2024": requirements_2324, 
                            "B.S. 2022-2023": requirements_2223,
                            "B.S. 2021-2022": requirements_2122,
                            "B.S. 2019-2020": requirements_1920}
    
    let all_semesters = {"B.S. 2024-2025": semesters_2425,
                         "B.S. 2023-2024": semesters_2324, 
                         "B.S. 2022-2023": semesters_2223,
                         "B.S. 2021-2022": semesters_2122,
                         "B.S. 2019-2020": semesters_1920}
    
    let requirements = requirements_2425;
    let formatted_reqs = requirements;
    console.log(formatted_reqs)
    formatted_reqs.sort((a, b) => a['courses'].length - b['courses'].length)
    formatted_reqs.sort((a, b) => ordering[a['req']] >  ordering[b['req']])
    // formatted_reqs.sort((a, b) => a['req'].split(/[a-zA-z_]+/) < b['req'].split(/[a-zA-z_]+/))
    // formatted_reqs.sort((a, b) => (a['req'].match(/[0-9]+/) < b['req'].match(/[0-9]+/) && b['req'].match(/[0-9]+/) != null))
    let reassign;
    let final_assignments;
    let swapped_assignments;
    let semester = semesters_2425;
    
    let cur_year = "B.S. 2024-2025"
    let current_semester = "spring2025";

    let reqs_filter = [];
    for (let req_year in all_requirements) {
        reqs_filter.push({'id': req_year, text: req_year})

    }

    console.log("formatted reqs", formatted_reqs)

    let header_emoji = "🧐 Degree Progress Validation Tool 🧐";
    let subtext = "";

    let assignment_arr = [{},{},[],[],semester];

    let course_semester = [];
    for (let req in formatted_reqs) {
        formatted_reqs[req]['courses'] = _.sortBy(formatted_reqs[req]['courses'], [(o) => o['id']])
    }
    
    function updateRequirements(event){
        cur_year = event.detail.selectedId
        formatted_reqs = all_requirements[event.detail.selectedId]
        semester= all_semesters[event.detail.selectedId]
    }

    function handle_import(event) {
        course_semester = event.detail;
        console.log("course data:", course_semester)
        assignment_arr = reassign(course_semester)
        console.log("ASSIGNMENT ARRAY",assignment_arr)
    }

    function update_working(event){
        let finished = event.detail;
        if (! finished){
            header_emoji = header_emoji = "🤔🤔 Validating...🤔🤔"
            subtext = "(This will take a brief moment...)"
        }
        else {
            header_emoji = "😌 Validation Complete! 😌"
            subtext = ""
            setTimeout(() => header_emoji = "🧐 Degree Progress Validation Tool 🧐", 2000)
        }
    }

    function add_courses(event) {
        let new_courses = event.detail
        
        for (let course of new_courses) {
            let dupe = false;
            for (let old_course of course_semester) {
                if (((old_course[0] == course[0]) && (old_course[1] == course[1]))) {
                    dupe = true;
                }
            }
            if (! dupe) {
            course_semester = course_semester.concat([course])
            }
        }
        if (course_semester.length == 0) {
            course_semester = new_courses
        }
        assignment_arr = reassign(course_semester);
        let final_assignments = assignment_arr[0];
        let swapped = assignment_arr[1];
        course_semester = assignment_arr[2];

    }

    // function add_selected_course(event) {
    //     // console.log(event)
    //     if ((event.detail[2] == "None") && (event.detail[1] != "None")) {
    //         // console.log(event)
    //         let slot = event.detail[0]
    //         let course = event.detail[1]
    //         let course_str = course+"#"+current_semester
    //         // console.log('adding', course, slot)

    //         //dedupe
    //         let dupe = false;
    //         for (let old_course of course_semester) {
    //             if (((old_course[0] == course[0]) && (old_course[1] == course[1]))) {
    //                 dupe = true;
    //             }
    //         }
    //         if (! dupe) {
    //         course_semester.push([course, current_semester, "--", "(3)"])
    //         console.log([course, current_semester, "--", "(3)"])
    //         console.log(course_semester)
    //         }
    //         assignment_arr[0][course_str] = slot;
    //         assignment_arr[1][slot] = course_str;
    //         assignment_arr[2] = course_semester;
    //     }

    // }

    // function clear_course(event) {
    //     let semester = event.detail[2].toLowerCase().replace(" ","")
    //     let slot = event.detail[0]
    //     let course_str = event.detail[1] + "#" + semester
    //     for (let j = 1; j < course_semester.length; j++){
            
    //         if (course_semester[j][0] == event.detail[1]) {
    //             // console.log(course_semester[j]);
    //             course_semester.splice(j,1);
    //             course_semester = course_semester;
    //             delete assignment_arr[0][course_str]
    //             delete assignment_arr[1][slot]
    //             assignment_arr[2] = course_semester
    //             console.log(course_semester)
    //         }   
    //     }

    // }

    function generate_form(event) {
        console.log('current assignments', assignment_arr);
        generate_sheet(assignment_arr, event.detail);
    }

    // function updateSemester(event){
    //     let course = event.detail[0]
    //     let new_semester = event.detail[1]["selectedId"].toLowerCase().replace(" ","")
    //     let slot = event.detail[2]['req']
    //     // console.log(event.detail[3])
    //     let old_semester;
    //     if (event.detail[3] != "None") {
    //         old_semester = event.detail[3].toLowerCase().replace(" ","")
    //     }
    //     else {
    //         old_semester = current_semester;
    //     }
    //     for (let j = 0; j < course_semester.length; j++) {
    //         if (course_semester[j][0] == course) {
    //             course_semester[j][1] = new_semester
    //         }
    //     }
    //     let course_str = course + "#" + new_semester
    //     let old_course_str = course + "#" + old_semester
    //     // console.log("removing", old_course_str)
    //     delete assignment_arr[0][old_course_str]
    //     if (event.detail[1]["selectedId"] != "None") {
    //         assignment_arr[0][course_str] = slot
    //         assignment_arr[1][slot] = course_str
    //         assignment_arr[2] = course_semester
    //         course_semester = course_semester;
    //     }
    // }

    // function updateGrade(event){
    //     let course = event.detail[0]
    //     let semester = event.detail[1].toLowerCase().replace(" ","")

        
    //     for (let j = 0; j < course_semester.length; j++) {
    //         if ((course_semester[j][0] == course) && (course_semester[j][1] = semester)){
    //             course_semester[j][2] = event.detail[2]['selectedId']
    //         }
    //     }
    //     assignment_arr[2] = course_semester
    // }

    // function updateCredits(event){
    //     let course = event.detail[0]
    //     let semester = event.detail[1].toLowerCase().replace(" ","")

        
    //     for (let j = 0; j < course_semester.length; j++) {
    //         if ((course_semester[j][0] == course) && (course_semester[j][1] = semester)){
    //             course_semester[j][3] = event.detail[2]['selectedId']
    //         }
    //     }
    //     assignment_arr[2] = course_semester
    // }

    function courseChanged(event){
        // console.log(event.detail)
        // {"req": req['req'], "course": selectedId,"semester": semester, "credits": credits, "grade": grade, "old_course": old_course, "old_semester": old_semester})
        let req = event.detail['req']
        let course = event.detail['course']
        let semester = event.detail['semester']
        let credits = event.detail['credits']
        let grade = event.detail['grade']
        let old_course = event.detail['old_course']
        let old_semester = event.detail['old_semester']
        let course_str = null;
        let old_course_str = null;
        let semester_str = null;
        let old_semester_str = null;

        if (semester !== null) {
            semester_str = semester.toLowerCase().replace(" ","")
            course_str = course + "#" + semester_str
        }
        if (old_semester !== null) {
            old_semester_str = old_semester.toLowerCase().replace(" ","")
            old_course_str = course + "#" + old_semester_str
        }
        // case: update course
        // only when all details filled in
        if ((course !== null) && (semester !== null) && (grade !== null) && (credits !== null)) {
            console.log("changing course!", course, semester_str);
            console.log("old:", old_course_str);
            assignment_arr[1][req] = course_str;
            let found = false;
            for (let i = 0; i < assignment_arr[2].length; i ++) {
                // update to existing
                if ((assignment_arr[2][i][0] == course) && (assignment_arr[2][i][1] == semester_str)) {
                    assignment_arr[2][i][2] = grade;
                    assignment_arr[2][i][3] = credits;
                    found = true;
                }
                // semester changed
                else if ((assignment_arr[2][i][0] == course) && (assignment_arr[2][i][1] == old_semester_str)) {
                    assignment_arr[2][i][1] = semester_str;
                    assignment_arr[2][i][2] = grade;
                    assignment_arr[2][i][3] = credits;
                    found = true;
                }
                // course changed
                else if ((assignment_arr[2][i][0] == old_course) && (assignment_arr[2][i][1] == semester_str)) {
                    assignment_arr[2][i][0] = course;
                    assignment_arr[2][i][2] = grade;
                    assignment_arr[2][i][3] = credits;
                    found = true;
                }
            }
            if (! found) {
                assignment_arr[2].push([course, semester_str, grade, credits])
            }
        }
        //removal case
        else {
            delete assignment_arr[1][req];
            for (let i = 0; i < assignment_arr[2].length; i ++) {
                // update to existing
                if ((assignment_arr[2][i][0] == course) && (assignment_arr[2][i][1] == semester_str)) {
                    assignment_arr[2].splice(i,1)
                }
                // semester changed
                else if ((assignment_arr[2][i][0] == course) && (assignment_arr[2][i][1] == old_semester_str)) {
                    assignment_arr[2].splice(i,1)
                }
                // course changed
                else if ((assignment_arr[2][i][0] == old_course) && (assignment_arr[2][i][1] == semester_str)) {
                    assignment_arr[2].splice(i,1)
                }
            }

        }

        let temp_swap = {}
        for (let k of Object.keys(assignment_arr[1])) {
            temp_swap[assignment_arr[1][k]] = k;
        }
        assignment_arr[0] = temp_swap;
        console.log("new assignments", assignment_arr)

    }

</script>

<style>
    .main {
        margin-left: 15rem;
        margin-top: 3rem;
    }
    
    
</style>

<div class="main">
<h1>{header_emoji}</h1>
{subtext}
<br/>
<b>Public Alpha</b> -- 
<a href="https://github.com/goldfrank/advisingtool">Bug reports and pull requests welcome!</a><br/>
<div style="max-width: 60%"><em>This is an advising tool and is not a contract. It is intended for program progress tracking and is not considered an academic transcript, nor should it be used for official certification of academic records. It is the responsibility of each student to be aware of and understand the requirements of the selected degree or certificate program as posted in the University Bulletin. Students should contact their academic advisor for assistance in interpreting or verifying the accuracy of any information contained within this report. </em></div>
<h3>Curriculum:</h3>

<div style="max-width: 55%">
    <ComboBox
  placeholder="Select curriculum"
  items={reqs_filter}
  on:select={updateRequirements}
  {shouldFilterItem}
/>

</div>
<Tabs>
    <Tab label="Degree Validation" />
    <Tab label="Import Data" />
    <!-- <Tab label="Manually Add" /> -->
    <Tab label="Generate Forms" />
    <svelte:fragment slot="content">
      <TabContent>
        <DegreeValidation
            course_details={course_semester}
            formatted_reqs={formatted_reqs}
            curriculum_year={cur_year}
            bind:reassign={reassign}
            bind:final_assignments={final_assignments}
            bind:swapped_assignments={swapped_assignments}
            on:working={update_working}
            on:changeCourse={courseChanged}

        />
      </TabContent>
      <TabContent>
        <DegreeMapImport
            on:data_import={handle_import}
        />
      </TabContent>
      <!-- <TabContent>
        <AddCourses 
            on:courses_added={add_courses}
        />
      </TabContent> -->
      <TabContent>
        <br/>
        <GenerateForms
            on:generate_form={generate_form}
            semester={semester}
        />
      </TabContent>
    </svelte:fragment>
  </Tabs>
</div>


<br/>
<br/>
