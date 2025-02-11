// a slidiing window function to find the longest subarray sum
function slidingWindow(arr,k) {
    let left_pointer = 0;
    let curr = 0;
    length_of_array = arr.length;

    
    let answer = 0;

    for (let right_pointer = 1; right_pointer < length_of_array - 1; right_pointer++){
        curr += nums[right_pointer]

        while (curr > k){
            curr -= nums[left_pointer]
            left_pointer += 1
        }
        answer = Math.max(answer, right_pointer - left_pointer + 1)
    }

    return answer;
    
}