<script>
// @ts-nocheck

    import Typebox from "../lib/Typebox.svelte"
    let otis;
</script>

<h1>Welcome to SvelteKit</h1>
<br/>

<a href="/semester-planner">Semester Planner for {otis}</a>
<br/>
<Typebox bind:name={otis}/>

