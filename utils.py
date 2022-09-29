import re
import json
import csv


def regex_unit_test(test_data_path, re_obj):
    """
    Test regex pattern on testcases then print notification
    @param test_data_path (str): testcase json file path
    @param reg_obj (re.Pattern): regex compiled object
    """
    with open(test_data_path) as file:
        print(f"{test_data_path} testing")
        data = json.load(file)
        testcases = data["testcases"]
        for type, cases in testcases.items(): 
            print(f"- {type}:")
            for case, truth in cases.items():
                match = re_obj.search(case)
                result = match.group(0) if match else None
                assert result == truth, f"Result: {result} and Truth: {truth}"
            print("\tPASS")
        print(f"{test_data_path} testing PASS")

def get_matched_list(text, re_obj):
    """
    Extract information from text using regex pattern object
    @param text (str): text to extract information
    @param reg_obj (re.Pattern): regex compiled object
    @return matched_list (list(tuple(int, int, str))): list of tuples 
                                                       (match start position, 
                                                       match len, match content) 
    """
    matched_list = list()
    for match in re_obj.finditer(text):
        matched_list.append((match.start(), len(match.group()), match.group()))
    return matched_list

def is_part_of_email(text, text_position, email, email_position):
    if (text_position > email_position and
        text_position + len(text) <= email_position + len(email)):
        if text in email:
            return True
    return False

def save_result(results, info_type, path):
    """Save results in a csv file
    @param results (list(tuple(str, str, str))): list of (start_position, len,
                                                 content) tuples
    @param info_type (str): type of result contents
    @param path (str): save path                                             
    """
    header = ["start_position", "len", "content", "info_type"]

    with open(path, "a", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=header)

        if output.tell() == 0:
            writer.writeheader()    
        
        for start_position, len, content in results:
            writer.writerow({"start_position": start_position, 
                             "len": len, 
                             "content": content, 
                             "info_type": info_type})
