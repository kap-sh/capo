"""Generated from Smithy shape ``com.amazonaws.artifact#InquiryFileContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_artifact.types.file_section_list


class InquiryFileContent(TypedDict, closed=True):
    file_sections: NotRequired["capo_artifact.types.file_section_list.FileSectionList"]
    """<p>List of file sections/sheets to process.</p>"""
    content: "bytes"
    """<p>Binary content of the uploaded file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InquiryFileContent) -> dict:
    out: dict = {}
    if "file_sections" in value:
        import capo_artifact.types.file_section_list

        out["fileSections"] = capo_artifact.types.file_section_list.serialize_json(
            value["file_sections"]
        )
    import capo_artifact.types._prelude.blob

    out["content"] = capo_artifact.types._prelude.blob.serialize_json(value["content"])
    return out


def deserialize_json(data: dict) -> InquiryFileContent:
    out: InquiryFileContent = {}  # type: ignore[typeddict-item]
    if data.get("fileSections") is not None:
        import capo_artifact.types.file_section_list

        out["file_sections"] = capo_artifact.types.file_section_list.deserialize_json(
            data["fileSections"]
        )
    if data.get("content") is not None:
        import capo_artifact.types._prelude.blob

        out["content"] = capo_artifact.types._prelude.blob.deserialize_json(
            data["content"]
        )
    else:
        out["content"] = b""
    return out
