"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentLabel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.float
    import capo_comprehend.types.integer
    import capo_comprehend.types.string


class DocumentLabel(TypedDict, closed=True):
    name: NotRequired["capo_comprehend.types.string.String"]
    """<p>The name of the label.</p>"""
    score: NotRequired["capo_comprehend.types.float.Float"]
    """<p>The confidence score that Amazon Comprehend has this label correctly attributed.</p>"""
    page: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>Page number where the label occurs. This field is present in the response only if your request includes the <code>Byte</code> parameter. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentLabel) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "score" in value:
        out["Score"] = (
            "NaN"
            if value["score"] != value["score"]
            else "Infinity"
            if value["score"] == float("inf")
            else "-Infinity"
            if value["score"] == float("-inf")
            else value["score"]
        )
    if "page" in value:
        out["Page"] = value["page"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentLabel:
    out: DocumentLabel = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    if data.get("Page") is not None:
        out["page"] = data["Page"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DocumentLabel) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "score" in value:
        out["Score"] = value["score"]
    if "page" in value:
        out["Page"] = value["page"]
    return out


def deserialize_cbor(data: dict) -> DocumentLabel:
    out: DocumentLabel = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    if data.get("Page") is not None:
        out["page"] = data["Page"]
    return out
