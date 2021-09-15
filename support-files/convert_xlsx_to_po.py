from pathlib import Path
import po_excel_translate_edited as poet
import os

print("Begin\n")

locale_input = input("Enter locale info (bg_BG, si_SI etc.):\n")

input_file_path = input("Enter input file name in the user-files directory (bg-default.xlsx etc.):\n")
input_file_path = "../user-files/" + input_file_path

output_file_path = input("Enter output file name (output.po etc.):\n")  # Specify output file name
output_file_path = "../user-files/" + output_file_path

if not os.path.isfile(input_file_path):  # check if input file exists
	print("Error: Can't find input file: " + input_file_path)
else:  # execute xls2po conversion
	try:
		print("\nStarting the conversion...")
		poet.XLSXToPortableObjectFile(
			locale=locale_input,
			input_file_path=Path(input_file_path),
			output_file_path=Path(output_file_path)
		)
		print("Done. File " + output_file_path + " successfully generated.\n")
	except:
		print("Something went wrong during conversion.\n")
