
from tqdm import tqdm
from pathlib import Path
from src.service.agent.article_information import get_reference_info
from src.service.document.load_document import load_json, parse_path_info, updata_document_metadata, save_json
from src.service.document.clean_markdown import chunk_identify_main_section, chunk_markdown_by_blank_lines, load_markdown

# 1. First identify main section-> clean_state = "identified_main_section"
def identify_title(file_data: dict, reidentify = False) -> str:
    """ 
    Identify title which academic paper section the markdown chunks belongs to.
    Args:
        file_data (dict): Metadata dictionary containing:
            - file_name
            - file_type
            - file_path
            - file_id
            - file_size
            - update_time
            - parsing_status
            - batch_id (optional)
            - DOI_state (optional)
            - doi (optional)
            - clean_state (optional)

    Returns: 
        file_data (dict): Updated file_data with DOI_state.
    """

    # ---- clean_state guard ----
    if reidentify == False:
        if file_data["DOI_state"] in {
                "Doi_Info_Getted",
                "Doi_Updated"
            }:
            print(f"{file_data['file_name']}: Already {file_data['DOI_state']}, skip title identify")
            return file_data

    # ---- load markdown ----
    content_markdown = load_markdown(file_data)
    chunks = chunk_markdown_by_blank_lines(content_markdown)

    # ---- load path info ----
    username, dataset_name = parse_path_info(file_data["file_path"])
    doi_path = Path(
        f"users/{username}/{dataset_name}/data_clean/{file_data['file_id']}/doi.json"
    )

    # ---- initial categories ----     
    BASE_CATEGORIES = {
        "title",
        "other",
    }
    CATEGORIES = set(BASE_CATEGORIES)

    with tqdm(
        total=len(chunks),
        desc=f"Identifying title [{file_data['file_name'][:5]}..]",
        unit="chunk",
        ncols=100,
        position=0,
        leave=False,
        bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} "
                "[{elapsed}<{remaining}, {rate_fmt}]"
    ) as pbar:
        for i, chunk in enumerate(chunks):
            label = chunk_identify_main_section(query=chunk, CATEGORIES=CATEGORIES)
            if label == "title":
                title_info = get_reference_info(chunk)
                # print(title_info)
                if title_info['doi']:
                    file_data["DOI_state"] = "Doi_Info_Getted"
                    file_data["doi"] = title_info['doi']
                    file_data["file_name"] = title_info['title']
                    updata_document_metadata(username, dataset_name, file_data, info=False)
                    save_json(title_info, doi_path)
                return file_data
            pbar.update(1)
