from pathlib import Path
import po_excel_translate_edited as poet

print("Begin\n")

input_file_path = input("Enter input file name in the user-files directory (default.po etc.):\n")
input_file_path = "../user-files/" + input_file_path

output_file_path = input("Enter output file name in the user-files directory (to-be-translated.xlsx etc.):\n")
output_file_path = "../user-files/" + output_file_path

print("\nStarting the conversion...")
# po2xls
po_files_to_convert = [
	poet.PortableObjectFile(input_file_path)
]

poet.PortableObjectFileToXLSX(
	po_files=po_files_to_convert,
	comment_types=[poet.CommentType.ALL],
	output_file_path=Path(output_file_path)
)

print("Done. File " + output_file_path + " successfully generated.\n")
