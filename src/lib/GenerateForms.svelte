<script>
    //@ts-nocheck
    import { ClickableTile } from "carbon-components-svelte";
    import { createEventDispatcher } from 'svelte';
    import { TextInput } from "carbon-components-svelte";

  const dispatch = createEventDispatcher();
  let student_name = "";
  let gwid = "";
  let admit_date ="";
  let advisor = "";
  let gpa = 0.0;

	function generate_form(event) {
        dispatch('generate_form', [student_name, gwid, admit_date, advisor, gpa]);
	}


</script>
  
<style>

</style>

<div style="width: 35rem">
  <TextInput labelText="Student Name" placeholder="Enter student name" 
    bind:value={student_name}
  />
  <br/>
  <TextInput labelText="GWID" placeholder="Enter GWID" 
    bind:value={gwid}
  />
  <br/>
  <TextInput labelText="Admit Date" placeholder="Enter Admit Date" 
    bind:value={admit_date}/>
  <br/>
  <TextInput labelText="Advisor" placeholder="Enter Advisor" 
    bind:value={advisor}/>
  <br/>
  <TextInput labelText="GPA" placeholder="Enter GPA" 
    bind:value={gpa}/>
  <br/>
  <ClickableTile href="/curriculum-sheet"
    on:click={(e) => generate_form(e)}
    >
    Generate Curriculum Sheet
  </ClickableTile>
</div>
  