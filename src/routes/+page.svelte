<script>
    // @ts-nocheck
    import Validationbox from "$lib/Validationbox.svelte"
    //import { requirements } from "$lib/19-20_requirements.json"
    import { requirements as requirements_2425 } from "$lib/BS_2024-2025.json"
    import { requirements as requirements_1920 } from "$lib/BS_2019-2020.json"
    import _ from "lodash";
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


    let all_requirements = {"B.S. 2024-2025": requirements_2425, "B.S. 2019-2020": requirements_1920}
    let requirements = requirements_2425;
    let formatted_reqs = requirements;
    let reassign;

    let reqs_filter = [];
    for (let req_year in all_requirements) {
        reqs_filter.push({'id': req_year, text: req_year})

    }

    console.log("formatted reqs", formatted_reqs)

    let header_emoji = "🧐 Degree Progress Validation Tool 🧐";
    let subtext = "";

    let assignment_arr = [[],[],[],[],[]];

    let course_semester = [];
    for (let req in formatted_reqs) {
        formatted_reqs[req]['courses'] = _.sortBy(formatted_reqs[req]['courses'], [(o) => o['id']])
    }
    
    function updateRequirements(event){
        console.log(event.detail.selectedId)
        formatted_reqs = all_requirements[event.detail.selectedId]
    }

    function handle_import(event) {
        course_semester = event.detail;
        console.log("course data:", course_semester)
        assignment_arr = reassign(course_semester)
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
        console.log('adding_courses')
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
        assignment_arr = reassign(course_semester)
        let final_assignments = assignment_arr[0]
        let swapped = assignment_arr[1]
        course_semester = assignment_arr[2]

    }

    function generate_form(event) {
        console.log('carl')
        console.log('current assignments', assignment_arr)
        generate_sheet(assignment_arr, event.detail)
    }

    console.log(course_semester)

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
<h3>Curriculum:</h3>

<div style="max-width: 55%">
    <ComboBox
  titleText="Contact"
  placeholder="Select contact method"
  items={reqs_filter}
  on:select={updateRequirements}
  {shouldFilterItem}
/>

</div>
<Tabs>
    <Tab label="Degree Validation" />
    <Tab label="Import Data" />
    <Tab label="Manually Add" />
    <Tab label="Generate Forms" />
    <svelte:fragment slot="content">
      <TabContent>
        <DegreeValidation
            course_details={course_semester}
            formatted_reqs={formatted_reqs}
            curriculum_year={"C.Y. 2021 B.S."}
            bind:reassign={reassign}
            on:working={update_working}
        />
      </TabContent>
      <TabContent>
        <DegreeMapImport
            on:data_import={handle_import}
        />
      </TabContent>
      <TabContent>
        <AddCourses 
            on:courses_added={add_courses}
        />
      </TabContent>
      <TabContent>
        <br/>
        <GenerateForms
            on:generate_form={generate_form}
        />
      </TabContent>
    </svelte:fragment>
  </Tabs>
</div>


<br/>
<br/>
