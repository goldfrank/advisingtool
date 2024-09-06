<script>
	// @ts-nocheck 
    import Validationbox from "../../lib/Validationbox.svelte"
    import { requirements } from "../../lib/bs19-21a.json"
   

    function all_reqs(requirements) {
        let formatted_reqs = [];
        let req_keys = Object.keys(requirements)
        
        for (let i = 0; i < req_keys.length; i++) {
            formatted_reqs.push({req: req_keys[i], satisfied_by: requirements[req_keys[i]]})
        }
        return formatted_reqs
    }

    function course_reformat(course_str) {
        let course_num = course_str.match(r_number)[0];
        let course_name = course_str.match(/#(.*)/)[1]
        let fulltext = course_num + " " + course_name
        let courseid = course_num.toLowerCase().replace(/\s/g, '')
        return {id: courseid, text:fulltext, num: course_num, desc: course_name}
    }
    
    function course_inventory(satisfied_arr) {
        let course_collection = [];
        for (let i = 0; i < satisfied_arr.length; i++) {
            let course = course_reformat(satisfied_arr[i])
            let duplicate = false;
            for (let j = 0; j < course_collection.length; j ++){
                if (course_collection[j]['id'] == course['id']) {
                    duplicate = true;
                }
            }
            if (! duplicate) {
            course_collection.push(course)
            }
        }
        return course_collection
    }

    
    let r_number = /[A-Z]{2,4} [0-9]{2,4}W?/;
    let formatted_reqs = all_reqs(requirements)
   
    let all_courses = []
    for (let i =0; i < formatted_reqs.length; i++) {
        let req = formatted_reqs[i]['req']
        let avail = course_inventory(formatted_reqs[i]['satisfied_by'])
        all_courses.push({req: req, courses: avail})
    }
    
    all_courses = {"requirements": all_courses}    
    
    let jsonData = JSON.stringify(all_courses)

</script>

Course Processor. Nothing to see here.


{jsonData}