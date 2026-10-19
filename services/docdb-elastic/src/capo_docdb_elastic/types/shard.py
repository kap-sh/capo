"""Generated from Smithy shape ``com.amazonaws.docdbelastic#Shard``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_docdb_elastic.types.status


class Shard(TypedDict, closed=True):
    shard_id: "str"
    """<p>The ID of the shard.</p>"""
    create_time: "str"
    """<p>The time when the shard was created in Universal Coordinated Time (UTC).</p>"""
    status: "capo_docdb_elastic.types.status.Status"
    """<p>The current status of the shard.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Shard) -> dict:
    out: dict = {}
    out["shardId"] = value["shard_id"]
    out["createTime"] = value["create_time"]
    out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> Shard:
    out: Shard = {}  # type: ignore[typeddict-item]
    if data.get("shardId") is not None:
        out["shard_id"] = data["shardId"]
    else:
        out["shard_id"] = ""
    if data.get("createTime") is not None:
        out["create_time"] = data["createTime"]
    else:
        out["create_time"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    return out
