def convert_base(in_number, out_base):

    out_number = []



    # divide integer until quotient equals zero
    while in_number != 0:

        step = int(in_number % out_base)  # modulo; obtain remainder
        out_number.append(step)

        in_number //= out_base  # floor division; obtain quotient

    return out_number[::-1]


input_number = 500000
output_base = 12

check = str(input_number)
if "." in check:
    input_number = check.split(".")


output_number = convert_base(input_number, output_base)

print(output_number)

'''TODO
    * in base conversion, check if input is a list
        * if a list: 
            - convert index 0 to integer
            - check for leading zeroes in index 1
            - save leading zeroes
            - process index 0 and 1
                * convert values above conversion_base-1 to letters
                    * add list of English letters
                    * check for values above base-1
                    * assign letters, A–Z, to respective values
            - combine lists to respective strings
            - add leading zeroes to beginning of index 1
            - combine index 0 and 1 with "." between
            - return output

'''
