"""Generated from Smithy shape ``com.amazonaws.ebs#ListChangedBlocksResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ebs.types.block_size
    import capo_ebs.types.changed_blocks
    import capo_ebs.types.page_token
    import capo_ebs.types.time_stamp
    import capo_ebs.types.volume_size


class ListChangedBlocksResponse(TypedDict, closed=True):
    changed_blocks: NotRequired["capo_ebs.types.changed_blocks.ChangedBlocks"]
    """<p>An array of objects containing information about the changed blocks.</p>"""
    expiry_time: NotRequired["capo_ebs.types.time_stamp.TimeStamp"]
    """<p>The time when the <code>BlockToken</code> expires.</p>"""
    volume_size: NotRequired["capo_ebs.types.volume_size.VolumeSize"]
    """<p>The size of the volume in GB.</p>"""
    block_size: NotRequired["capo_ebs.types.block_size.BlockSize"]
    """<p>The size of the blocks in the snapshot, in bytes.</p>"""
    next_token: NotRequired["capo_ebs.types.page_token.PageToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChangedBlocksResponse) -> dict:
    out: dict = {}
    if "changed_blocks" in value:
        import capo_ebs.types.changed_blocks

        out["ChangedBlocks"] = capo_ebs.types.changed_blocks.serialize_json(
            value["changed_blocks"]
        )
    if "expiry_time" in value:
        import capo_ebs.types.time_stamp

        out["ExpiryTime"] = capo_ebs.types.time_stamp.serialize_json(
            value["expiry_time"]
        )
    if "volume_size" in value:
        out["VolumeSize"] = value["volume_size"]
    if "block_size" in value:
        out["BlockSize"] = value["block_size"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListChangedBlocksResponse:
    out: ListChangedBlocksResponse = {}  # type: ignore[typeddict-item]
    if data.get("ChangedBlocks") is not None:
        import capo_ebs.types.changed_blocks

        out["changed_blocks"] = capo_ebs.types.changed_blocks.deserialize_json(
            data["ChangedBlocks"]
        )
    if data.get("ExpiryTime") is not None:
        import capo_ebs.types.time_stamp

        out["expiry_time"] = capo_ebs.types.time_stamp.deserialize_json(
            data["ExpiryTime"]
        )
    if data.get("VolumeSize") is not None:
        out["volume_size"] = data["VolumeSize"]
    if data.get("BlockSize") is not None:
        out["block_size"] = data["BlockSize"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListChangedBlocksResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "changed_blocks" in value:
        import capo_ebs.types.changed_blocks

        out["changed_blocks"] = capo_ebs.types.changed_blocks.redact_sensitive(
            value["changed_blocks"]
        )
    return out
