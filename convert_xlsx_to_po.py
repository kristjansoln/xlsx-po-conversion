from pathlib import Path
import po_excel_translate_edited as poet
import os

print("Begin\n")

locale_input=input("Enter locale info (bg_BG, si_SI etc.):\n")
input_file_input=input("Enter input file name (bg-default.xlsx etc.):\n")

if not os.path.isfile(input_file_input):  # check if input file exists
	print("Can't find input file " + input_file_input)
else:
	# xls2po conversion
	try:
		poet.XLSXToPortableObjectFile(
			locale=locale_input,
			input_file_path=Path(input_file_input),
			output_file_path=Path("xlsx_output.po")
		)
		print("Successfully generated xlsx_output.po.\n")
	except:
		print("Something went wrong during conversion.\n")
