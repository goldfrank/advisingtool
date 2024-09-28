<script context="module">
    //@ts-nocheck
    // import { semesters } from "$lib/19-20_cur_sheet.json"
    import { pretty_slots } from "$lib/pretty_slots.json"

    let assignments;
    let semesters;
    let swapped_assignments;
    let course_details;
    let formatted_reqs = [];
    let unused = [];
    let sheet_data = {};
    let student_name = "";
    let gwid = "";
    let admit_date = "";
    let advisor = "";
    let gpa = 0;
    let tech_gpa = 0;
    let grade_gpa = {"A": 4, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "C+": 2.3,
                 "C": 2, "C-": 1.7, "D+": 1.3, "D": 1.0, "D-": 0.7, "F": 0.0};
    let gpa_qp = 0;
    let gpa_denom = 0;
    let tech_gpa_qp = 0;
    let tech_gpa_denom = 0;
   

    export function generate_sheet(assignment_arr, extra){
        console.log("rx", assignment_arr)
        console.log("rx2", extra)
        assignments = assignment_arr[0]
        swapped_assignments = assignment_arr[1]
        course_details = assignment_arr[2]
        unused = assignment_arr[3]
        //[student_name, gwid, admit_date, advisor, gpa]
        student_name = extra[0]
        gwid = extra[1]
        admit_date = extra[2]
        advisor= extra[3]
        semesters = extra[4]
        formatted_reqs = assignment_arr[4]
        console.log("semesters", semesters)
        fill_sheet()
    }

    function course_detail(course_id, semester) {
        // console.log("Course details:", course_id, semester)
        // console.log(course_details)
        for (let course_detail of course_details) {
            if ((course_detail[0] == course_id) && (course_detail[1] == semester)){
                return [course_detail[2], course_detail[3]]
            }
        }
    }

    function fill_sheet() {
        sheet_data = {}
        for (let semester of semesters) {
            for (let slot of semester){
                if (slot in swapped_assignments) {
                    //course_id, semester, grade, credits
                    let course_id = swapped_assignments[slot].split("#")[0]
                    let course_desc;
                    for (let req of formatted_reqs) {
                        if (req['req'] == slot) {
                            for (let r_course of req['courses']) {
                                if (r_course['id'] == course_id) {
                                    course_desc = r_course['text']
                                }
                            }

                        }
                    }
                    let formatted_course_id = course_id.match(/[a-z]{2,4}/)[0].toUpperCase() + " " + course_id.match(/[0-9]{2,4}[wW]?/)
                    let semester = swapped_assignments[slot].split("#")[1]
                    let formatted_semester = semester.match(/[a-z]*/)[0][0].toUpperCase()+semester.match(/[a-z]*/)[0].slice(1)+semester.match(/[0-9]{4}/)
                    formatted_semester = formatted_semester.match(/[A-Za-z]*/) + " " + formatted_semester.match(/[0-9]+/)
                    let grade_credits = course_detail(course_id, semester)
                    let grade = grade_credits[0]
                    let credits = grade_credits[1]
                    if (grade in grade_gpa) {
                        gpa_qp += grade_gpa[grade]*+credits
                        gpa_denom += +credits
                        if (course_id.match(/[a-z]{2,4}/)[0].toUpperCase() == 'CSCI') {
                            tech_gpa_qp += grade_gpa[grade]*+credits
                            tech_gpa_denom += +credits
                        }
                    }
                    sheet_data[slot] = [credits, course_desc, grade, formatted_semester]
                }
            }
        }
        gpa = (gpa_qp/gpa_denom).toPrecision(3);
        tech_gpa = (tech_gpa_qp/tech_gpa_denom).toPrecision(3);
    }

    function format_unused(course_arr) {
        let course_id = course_arr[0]
        let formatted_course_id = course_id.match(/[a-z]{2,4}/)[0].toUpperCase() + " " + course_id.match(/[0-9]{2,4}[wW]?/)
        let semester = course_arr[1]
        let formatted_semester = semester.match(/[a-z]*/)[0][0].toUpperCase()+semester.match(/[a-z]*/)[0].slice(1)+semester.match(/[0-9]{4}/)
        return formatted_course_id + " " + formatted_semester
    }

    function slot_data(slot){
        if (slot in sheet_data) {
            return sheet_data[slot]
        }
        return ["", "", "", ""]
    }

    let ordinals = ['First', 'Second', 'Third', 'Fourth',
                    'Fifth', 'Sixth', 'Seventh', 'Eighth']

</script>

<style>

    
    .header {
        max-width: 90%;
        margin: auto;
        text-align: center;
    }

    .section {
        /* max-width: 90%; */
        margin-top: 1rem;
        padding: 0.25rem 0.25rem 0.25rem 0.25rem;
        border: 0.15rem solid darkslategrey;
        display: flex;
        flex-wrap: wrap;
        font-size:90%;
        }

    .item {
        padding: 0.4rem 0.4rem 0.4rem 0.4rem;
        margin: 0.2rem auto 0.2rem auto;
        border: 0.15rem solid darkslategrey;
        flex-basis: 49%;
        box-sizing: border-box;
        }

    .semesters {
        display: grid;
        grid-template-columns: 1fr 1fr;
        border: none;
        gap: 2rem;
    }

    .semester {
        box-sizing: border-box;
        width: auto;
    }

    .semester-head {
        padding: 0.4rem 0.4rem 0.4rem 0.4rem;
        box-sizing: border-box;
        flex-basis: 100%;
    }

    .semester-body {
        display: grid;
        grid-template-columns: 1fr 5fr 8fr 2fr 5fr;
        gap: 2px;
    }

    .semester-item {
        box-sizing: border-box;
        padding: 0.4rem 0.4rem 0.4rem 0.4rem;
        border: 0.15rem solid darkslategrey;
        width:auto;
    }

    .hr {
        grid-column: 1;
    }

    .course {
        grid-column: 2;
    }

    .descr {
        grid-column: 3;
    }

    .grade {
        grid-column: 4;
    }

    .date {
        grid-column: 5;
    }


</style>

<div class="header">
    Dept. of Computer Science<br/>
    2021-2022<br/>
    BS Computer Science<br/>
</div>

<div class="section">
    <div class='item'>
        Student Name: {student_name}
    </div>
    <div class='item'>
        GWID: {gwid}
    </div>
    <div class='item'>
        Admit Date: {admit_date}
    </div>
    <div class='item'>
        Advisor: {advisor}
    </div>
    <div class='item'>
        GPA: {gpa}
    </div>
    <div class='item'>
        Technical GPA: {tech_gpa}
    </div>
</div>

<div class="section semesters">

    {#each semesters as semester, i}
    <div class="semester">
        <div class='semester-head'>
        {#if i % 2 == 0}
        Fall <br/>
        {:else}
        Spring <br/>
        {/if}
        {ordinals[i]} Semester
        </div>
        <div class='semester-body'>
            <div class="semester-item hr">Hr.</div>
            <div class="semester-item course">Course</div>
            <div class="semester-item descr">Description</div>
            <div class="semester-item grade">Grade</div>
            <div class="semester-item date">Date</div>
        {#each semester as slot}
            <div class="semester-item hr">{slot_data(slot)[0]}</div>
            <div class="semester-item course">{pretty_slots[slot]}</div>
            <div class="semester-item descr">{slot_data(slot)[1]}</div>
            <div class="semester-item grade">{slot_data(slot)[2]}</div>
            <div class="semester-item date">{slot_data(slot)[3]}</div>
        {/each}
        </div>
    </div>
    {/each}
</div>

<div class="section semesters" style="margin-bottom: 2rem;">
    <div class="semester">
        Fall-Through Classes <br/>
        {#each unused as extra_course}
            {format_unused(extra_course)} <br/>
        {/each}
    </div>
</div>