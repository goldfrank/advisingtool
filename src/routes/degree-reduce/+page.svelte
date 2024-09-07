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

    let courses_taken = ['csci1111','csci1112','csci1311', 'csci2113', 
    'seas1001', 'csci1012', 'csci4511', 'csci3410', 'csci4531', 'csci4243',
    'csci4244', 'csci3410', 'csci3411', 'math1231', 'math1232', 'csci3401', 'uw1020',
    'uw1099', 'geol2151', 'amst1200', 'anth3701', 'geog2141', 'cmus1701', 'fina6224',
    'hist2490', 'hist6801', 'hist6801', 'hist6801', 'csci4331', 'math2184', 'bisc1111',
    'csci3212', 'stat4157', 'csci4364', 'anth1003', 'anth1004', 'bisc1112', 'chem1112', 'csci1010', 'csci2312', 'csci2501', 'csci2541w', 'csci3313'];

    let course_semester = [];
    // for (let c of courses_taken) {
    //     course_semester.push([c, 'fall23'])
    // }
    // course_semester[26][1] = "spring23";
    
    
    function handle_import(event) {
        course_semester = event.detail;
        console.log("course data:", course_semester)
        reassign(course_semester);
    }

</script>
<h1>😌</h1>
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
