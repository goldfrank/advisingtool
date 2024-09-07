<script>
    // @ts-nocheck
    import Validationbox from "../../lib/Validationbox.svelte"
    import { requirements } from "../../lib/19-20_requirements.json"
    import _ from "lodash";
    import { Tabs, Tab, TabContent } from "carbon-components-svelte";
    import DegreeValidation from "../../lib/DegreeValidation.svelte"
    import DegreeMapImport from "../../lib/DegreeMapImport.svelte"
    import UAF from "../../lib/UAF.svelte"

    let formatted_reqs = requirements;
    let reassign;

    let header_emoji = "🧐 Degree Progress Validation Tool";
    let subtext = "";

    let course_semester = [];
    for (let req in formatted_reqs) {
        formatted_reqs[req]['courses'] = _.sortBy(formatted_reqs[req]['courses'], [(o) => o['id']])
    }
    
    
    function handle_import(event) {
        course_semester = event.detail;
        console.log("course data:", course_semester)
        reassign(course_semester);
    }

    function update_working(event){
        let finished = event.detail;
        if (! finished){
            header_emoji = header_emoji = "🤔🤔 Validating..."
            subtext = "(This will take a brief moment...)"
        }
        else {
            header_emoji = "😌 Validation Complete!"
            subtext = ""
        }
    }

    function add_courses(event) {
        let new_courses = event.detail
        console.log('adding_courses')
        course_semester = course_semester.concat(new_courses)
        // DEDUPE
        reassign(course_semester)
    }

</script>
<h1>{header_emoji}</h1>
{subtext}
<br/>
<Tabs>
    <Tab label="Degree Validation" />
    <Tab label="Import Data" />
    <Tab label="Add Courses" />
    <svelte:fragment slot="content">
      <TabContent>
        <DegreeValidation
            course_semester={course_semester}
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
        <UAF 
        on:courses_added={add_courses}
        />
      </TabContent>
    </svelte:fragment>
  </Tabs>
  


<br/>
<br/>
