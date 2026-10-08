from pdf2image import convert_from_path

output_folder = r"C:/Users/niza/OneDrive - Danish Agriculture & Food Council/Dokumenter/Hjemmeside"

pages = convert_from_path("Guide_nysmittet_besætning.pdf", dpi=300)

for i, page in enumerate(pages, start=1):
    page.save(f"{output_folder}\\{i}.png", "PNG")