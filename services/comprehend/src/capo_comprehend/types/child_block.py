"""Generated from Smithy shape ``com.amazonaws.comprehend#ChildBlock``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.integer
    import capo_comprehend.types.string


class ChildBlock(TypedDict, closed=True):
    child_block_id: NotRequired["capo_comprehend.types.string.String"]
    """<p>Unique identifier for the child block.</p>"""
    begin_offset: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>Offset of the start of the child block within its parent block.</p>"""
    end_offset: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>Offset of the end of the child block within its parent block.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChildBlock) -> dict:
    out: dict = {}
    if "child_block_id" in value:
        out["ChildBlockId"] = value["child_block_id"]
    if "begin_offset" in value:
        out["BeginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["EndOffset"] = value["end_offset"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ChildBlock:
    out: ChildBlock = {}  # type: ignore[typeddict-item]
    if data.get("ChildBlockId") is not None:
        out["child_block_id"] = data["ChildBlockId"]
    if data.get("BeginOffset") is not None:
        out["begin_offset"] = data["BeginOffset"]
    if data.get("EndOffset") is not None:
        out["end_offset"] = data["EndOffset"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ChildBlock) -> dict:
    out: dict = {}
    if "child_block_id" in value:
        out["ChildBlockId"] = value["child_block_id"]
    if "begin_offset" in value:
        out["BeginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["EndOffset"] = value["end_offset"]
    return out


def deserialize_cbor(data: dict) -> ChildBlock:
    out: ChildBlock = {}  # type: ignore[typeddict-item]
    if data.get("ChildBlockId") is not None:
        out["child_block_id"] = data["ChildBlockId"]
    if data.get("BeginOffset") is not None:
        out["begin_offset"] = data["BeginOffset"]
    if data.get("EndOffset") is not None:
        out["end_offset"] = data["EndOffset"]
    return out
