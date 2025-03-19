import os

from markitdown import MarkItDown


def convert_pdf_to_md(pdf_path, output_dir):
    base_name = os.path.basename(pdf_path)
    base_name_without_ext = os.path.splitext(base_name)[0]
    md_path = os.path.join(output_dir, f"{base_name_without_ext}.md")

    print(f"Converting: {pdf_path} -> {md_path}")

    try:
        markitdown = MarkItDown()
        result = markitdown.convert(pdf_path)

        # https://github.com/microsoft/markitdown/issues/285
        with open(md_path, "w", encoding="utf-8", errors="replace") as f:
            f.write(result.text_content)

        return True
    except Exception as e:
        print(f"Error converting {pdf_path}: {str(e)}")
        return False


output_dir = os.path.join("markdown", "raw")
os.makedirs(output_dir, exist_ok=True)

successful = 0
failed = 0


pdf_files = [
    f for f in os.listdir() if f.lower().endswith(".pdf") and os.path.isfile(f)
]

for pdf_file in pdf_files:
    if convert_pdf_to_md(pdf_file, output_dir):
        successful += 1
    else:
        failed += 1

print(
    f"\nConversion complete! Successfully converted {successful} files, {failed} failed."
)
