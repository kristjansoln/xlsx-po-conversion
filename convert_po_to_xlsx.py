from pathlib import Path
import po_excel_translate_edited as poet

print("Begin\n")

# po2xls
po_files_to_convert = [
	poet.PortableObjectFile("default.po")
]

poet.PortableObjectFileToXLSX(
	po_files=po_files_to_convert,
	comment_types=[poet.CommentType.ALL],
	output_file_path=Path("output.xlsx")
)

print("Generated output.xlsx file.\n")
