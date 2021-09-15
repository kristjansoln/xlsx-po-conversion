from pathlib import Path
import po_excel_translate_edited as poet
import os

print("Begin\n")

input_file_path = input("Enter input file name in the user-files directory (default.po etc.):\n")
input_file_path = "../user-files/" + input_file_path

output_file_path = input("Enter output file name in the user-files directory (to-be-translated.xlsx etc.):\n")
output_file_path = "../user-files/" + output_file_path


if not os.path.isfile(input_file_path):  # check if input file exists
	print("Error: Can't find input file: " + input_file_path)
else:  # execute po2xls conversion
	try:
		print("\nStarting the conversion...")
		po_files_to_convert = [
			poet.PortableObjectFile(input_file_path)
		]

		poet.PortableObjectFileToXLSX(
			po_files=po_files_to_convert,
			comment_types=[poet.CommentType.ALL],
			output_file_path=Path(output_file_path)
		)

		print("Done. File " + output_file_path + " successfully generated.\n")
	except:
		print("Something went wrong during conversion.\n")
