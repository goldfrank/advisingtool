<script>
// @ts-nocheck
    import { ComboBox } from "carbon-components-svelte";
    import { createEventDispatcher } from 'svelte';
    import { Button } from "carbon-components-svelte";
    import { Tile } from "carbon-components-svelte";


    function shouldFilterItem(item, value) {
    if (!value) return true;
    return item.text.toLowerCase().includes(value.toLowerCase());  
    }

    export let courses;
    export let selectedId;
    export let requirementName = "Requirement";
    export let semester;


    const dispatch = createEventDispatcher();

	function selected(event) {
		dispatch('selected', event.detail);
	}

    function cleared(event) {
		dispatch('cleared', event.detail);
	}

</script>

<style>
    .validation-box {
        margin-top: 0.5rem;
        width: 25rem;
        display: inline-block;
        margin-left: 1rem;
    }
    .course-box {
		/* background-color */
		-webkit-text-fill-color: rgb(0, 50, 77);
		color: rgb(0, 50, 77);
        margin-top: 0.15rem;
	}
    .req-name {
        display: inline-block; 
        position:relative; 
        top: 0.6em; 
        min-width: 11rem;
        padding-left: 1rem;
    }
    .semester-name {
        display: inline-block; 
        position:relative; 
        top: 0.6em; 
        min-width: 5rem;
        margin-left: 0.5rem;
    }
    .req-wrap {
        border: 1px;
        border-style:solid;
        border-color:darkslategrey;
        display: inline-block;
        height: 2rem;
    }

</style>


<div class="course-box">
    <div class="req-wrap">
        <div class="req-name">
            {requirementName} 
        </div>
    </div>
    <div class="validation-box">
        <ComboBox 
        size=sm
        placeholder="Select Course"
        items = {courses}
        selectedId = {selectedId}
        {shouldFilterItem}
        />
    </div>
    <div class="req-wrap">
        <div class="semester-name">
            SEMESTER
        </div>
    </div>
</div>

<!-- notes for styling
.bx--text-input:disabled {}
background-color
-webkit-text-fill-color
color
cursor: not-allowed;
-->