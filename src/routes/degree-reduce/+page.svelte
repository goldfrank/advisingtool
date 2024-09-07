<script>
    // @ts-nocheck
    import Validationbox from "../../lib/Validationbox.svelte"
    import { requirements } from "../../lib/19-20_requirements.json"
    import _ from "lodash";
    import { Tabs, Tab, TabContent } from "carbon-components-svelte";
    import DegreeValidation from "../../lib/DegreeValidation.svelte"
    import DegreeMapImport from "../../lib/DegreeMapImport.svelte"

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
            subtext = "(This might take a minute or two, please be patient.)"
        }
        else {
            header_emoji = "😌 Validation Complete!"
            subtext = ""
        }
    }

</script>
<h1>{header_emoji}</h1>
{subtext}
<br/>
<Tabs>
    <Tab label="Degree Validation" />
    <Tab label="Import Data" />
    <Tab label="xok" />
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
      <TabContent>xok</TabContent>
    </svelte:fragment>
  </Tabs>
  


<br/>
<br/>
