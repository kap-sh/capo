"""Generated from Smithy shape ``com.amazonaws.comprehend#ExtractedCharactersListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.integer


class ExtractedCharactersListItem(TypedDict, closed=True):
    page: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>Page number.</p>"""
    count: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>Number of characters extracted from each page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExtractedCharactersListItem) -> dict:
    out: dict = {}
    if "page" in value:
        out["Page"] = value["page"]
    if "count" in value:
        out["Count"] = value["count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExtractedCharactersListItem:
    out: ExtractedCharactersListItem = {}  # type: ignore[typeddict-item]
    if data.get("Page") is not None:
        out["page"] = data["Page"]
    if data.get("Count") is not None:
        out["count"] = data["Count"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExtractedCharactersListItem) -> dict:
    out: dict = {}
    if "page" in value:
        out["Page"] = value["page"]
    if "count" in value:
        out["Count"] = value["count"]
    return out


def deserialize_cbor(data: dict) -> ExtractedCharactersListItem:
    out: ExtractedCharactersListItem = {}  # type: ignore[typeddict-item]
    if data.get("Page") is not None:
        out["page"] = data["Page"]
    if data.get("Count") is not None:
        out["count"] = data["Count"]
    return out
