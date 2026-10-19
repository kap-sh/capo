"""Generated from Smithy shape ``com.amazonaws.kendra#DeleteThesaurusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.index_id
    import capo_kendra.types.thesaurus_id


class DeleteThesaurusRequest(TypedDict, closed=True):
    id: "capo_kendra.types.thesaurus_id.ThesaurusId"
    """<p>The identifier of the thesaurus you want to delete.</p>"""
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index for the thesaurus.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteThesaurusRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["IndexId"] = value["index_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteThesaurusRequest:
    out: DeleteThesaurusRequest = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("IndexId") is not None:
        out["index_id"] = data["IndexId"]
    else:
        out["index_id"] = ""
    return out
