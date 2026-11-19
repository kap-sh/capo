"""Generated from Smithy shape ``com.amazonaws.comprehend#BlockReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.integer
    import capo_comprehend.types.list_of_child_blocks
    import capo_comprehend.types.string


class BlockReference(TypedDict, closed=True):
    block_id: NotRequired["capo_comprehend.types.string.String"]
    """<p>Unique identifier for the block.</p>"""
    begin_offset: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>Offset of the start of the block within its parent block.</p>"""
    end_offset: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>Offset of the end of the block within its parent block.</p>"""
    child_blocks: NotRequired[
        "capo_comprehend.types.list_of_child_blocks.ListOfChildBlocks"
    ]
    """<p>List of child blocks within this block.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BlockReference) -> dict:
    out: dict = {}
    if "block_id" in value:
        out["BlockId"] = value["block_id"]
    if "begin_offset" in value:
        out["BeginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["EndOffset"] = value["end_offset"]
    if "child_blocks" in value:
        import capo_comprehend.types.list_of_child_blocks

        out["ChildBlocks"] = (
            capo_comprehend.types.list_of_child_blocks.serialize_aws_json_1_1(
                value["child_blocks"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BlockReference:
    out: BlockReference = {}  # type: ignore[typeddict-item]
    if data.get("BlockId") is not None:
        out["block_id"] = data["BlockId"]
    if data.get("BeginOffset") is not None:
        out["begin_offset"] = data["BeginOffset"]
    if data.get("EndOffset") is not None:
        out["end_offset"] = data["EndOffset"]
    if data.get("ChildBlocks") is not None:
        import capo_comprehend.types.list_of_child_blocks

        out["child_blocks"] = (
            capo_comprehend.types.list_of_child_blocks.deserialize_aws_json_1_1(
                data["ChildBlocks"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BlockReference) -> dict:
    out: dict = {}
    if "block_id" in value:
        out["BlockId"] = value["block_id"]
    if "begin_offset" in value:
        out["BeginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["EndOffset"] = value["end_offset"]
    if "child_blocks" in value:
        import capo_comprehend.types.list_of_child_blocks

        out["ChildBlocks"] = capo_comprehend.types.list_of_child_blocks.serialize_cbor(
            value["child_blocks"]
        )
    return out


def deserialize_cbor(data: dict) -> BlockReference:
    out: BlockReference = {}  # type: ignore[typeddict-item]
    if data.get("BlockId") is not None:
        out["block_id"] = data["BlockId"]
    if data.get("BeginOffset") is not None:
        out["begin_offset"] = data["BeginOffset"]
    if data.get("EndOffset") is not None:
        out["end_offset"] = data["EndOffset"]
    if data.get("ChildBlocks") is not None:
        import capo_comprehend.types.list_of_child_blocks

        out["child_blocks"] = (
            capo_comprehend.types.list_of_child_blocks.deserialize_cbor(
                data["ChildBlocks"]
            )
        )
    return out
