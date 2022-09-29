import argparse

from phone_number_regex import re_obj as phone_number_re_obj
from email_regex import re_obj as email_re_obj
from url_regex import re_obj as url_re_obj
from utils import get_matched_list, is_part_of_email, save_result


def main(input_path, output_path, print_result=False):
    """
    Get email, url, phone number from file in input_path, then write results in
    output_path, print result if needing
    @param input_path (str)
    @param output_path (str)
    @param print_result (bool)
    """
    phone_numbers = list()
    emails = list()
    urls = list()

    with open(input_path) as file:
        for line in file:
            phone_numbers += get_matched_list(line, phone_number_re_obj)
            matched_emails = get_matched_list(line, email_re_obj)
            matched_urls = get_matched_list(line, url_re_obj)
            # only choose matched URL which is not a part of matched emails
            if matched_emails:
                for email_position, __, email in matched_emails:
                    for url_position, url_len, url in matched_urls:
                        if not is_part_of_email(url, url_position, email, email_position):
                            urls.append([url_position, url_len, url])
                emails += matched_emails
            else:
                urls += matched_urls

    if print_result:
        print(f"Phone numbers: \n{phone_numbers}")
        print(f"Emails: \n{emails}")
        print(f"URLs: \n{urls}")

    save_result(phone_numbers, "phone", output_path)
    save_result(emails, "email", output_path)
    save_result(urls, "url", output_path)
            

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Get email, phone number, url from file txt using regex"
    )

    parser.add_argument("--ipath",
                        action="store",
                        default="data/test_story.txt",
                        help="txt input file path",
                        dest="input_path")

    parser.add_argument("--opath",
                        action="store",
                        default="result.csv",
                        help="csv output file path",
                        dest="output_path")

    parser.add_argument("--print",
                        action="store_true",
                        default=False,
                        help="result printing flag",
                        dest="print_result")

    args = parser.parse_args()

    main(**vars(args))