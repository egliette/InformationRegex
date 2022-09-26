import re
import json
import csv
import os

def regex_unit_test(test_data_path, regex):
    """
    Test regex string on testcases then print notification
    @param test_data_path (str): testcase json file path
    @regex (str) regex string
    """
    with open(test_data_path) as file:
        print(f"{test_data_path} testing")
        data = json.load(file)
        testcases = data["testcases"]
        for type, cases in testcases.items(): 
            print(f"- {type}:")
            for phone, truth in cases.items():
                match = re.search(regex, phone, re.VERBOSE)
                result = match.group(0) if match else None
                assert result == truth, f"Result: {result} and Truth: {truth}"
            print("\tPASS")
        print(f"{test_data_path} testing PASS")

def get_matched_list(text, regex):
    """
    Extract information from text using regex string
    @param text (str): text to extract information
    @param regex (str): regex of information
    @return matched_list (list(tuple(int, int, str))): list of tuples 
                                                       (match start position, 
                                                       match len, match content) 
    """
    matched_list = list()
    for match in re.finditer(regex, text, re.VERBOSE):
        matched_list.append((match.start(), len(match.group()), match.group()))
    return matched_list

def is_part_of_email(text, text_position, email, email_position):
    if (text_position > email_position and
        text_position + len(text) <= email_position + len(email)):
        if text in email:
            return True
    return False

def save_result(results, info_type, path):
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
