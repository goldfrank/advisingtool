<script>
// @ts-nocheck
    import { ComboBox } from "carbon-components-svelte";
    import { createEventDispatcher } from 'svelte';
    import { Button } from "carbon-components-svelte";
    import NonCertified from "carbon-icons-svelte/lib/NonCertified.svelte";

    function shouldFilterItem(item, value) {
    if (!value) return true;
    return item.text.toLowerCase().includes(value.toLowerCase());  
    }

    export let courses;
    export let selected;
    export let selected_id;
    export let withdrawn = false;

    const dispatch = createEventDispatcher();

	function forward(event) {
		dispatch('message', event.detail);
	}

    function cleared(event) {
		dispatch('cleared', event.detail);
	}

    function withdraw(event){
        withdrawn = true;
        dispatch('withdraw', event.detail);
    }
</script>

<style>
    .semester-box {
        max-width: 45%;
        margin-top: 0.5rem;
    }
    
</style>

<div class="semester-box">
    <ComboBox
      bind:value={selected}
      bind:selectedId={selected_id}
      placeholder="Select Course"
      items = {courses}
      on:select={forward}
      on:clear={cleared}
      {shouldFilterItem}
    />
    <span style="display: inline-block;">
        <Button 
        iconDescription="Withdrawn" 
        icon={NonCertified} 
        kind="ghost"
        on:click={withdraw}> </Button>
    </span>
</div>