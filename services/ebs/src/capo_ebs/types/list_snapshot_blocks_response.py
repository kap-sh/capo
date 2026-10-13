"""Generated from Smithy shape ``com.amazonaws.ebs#ListSnapshotBlocksResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ebs.types.block_size
    import capo_ebs.types.blocks
    import capo_ebs.types.page_token
    import capo_ebs.types.time_stamp
    import capo_ebs.types.volume_size


class ListSnapshotBlocksResponse(TypedDict, closed=True):
    blocks: NotRequired["capo_ebs.types.blocks.Blocks"]
    """<p>An array of objects containing information about the blocks.</p>"""
    expiry_time: NotRequired["capo_ebs.types.time_stamp.TimeStamp"]
    """<p>The time when the <code>BlockToken</code> expires.</p>"""
    volume_size: NotRequired["capo_ebs.types.volume_size.VolumeSize"]
    """<p>The size of the volume in GB.</p>"""
    block_size: NotRequired["capo_ebs.types.block_size.BlockSize"]
    """<p>The size of the blocks in the snapshot, in bytes.</p>"""
    next_token: NotRequired["capo_ebs.types.page_token.PageToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSnapshotBlocksResponse) -> dict:
    out: dict = {}
    if "blocks" in value:
        import capo_ebs.types.blocks

        out["Blocks"] = capo_ebs.types.blocks.serialize_json(value["blocks"])
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


def deserialize_json(data: dict) -> ListSnapshotBlocksResponse:
    out: ListSnapshotBlocksResponse = {}  # type: ignore[typeddict-item]
    if data.get("Blocks") is not None:
        import capo_ebs.types.blocks

        out["blocks"] = capo_ebs.types.blocks.deserialize_json(data["Blocks"])
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


def redact_sensitive(value: ListSnapshotBlocksResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "blocks" in value:
        out["blocks"] = "*** Sensitive Data Redacted ***"
    return out
