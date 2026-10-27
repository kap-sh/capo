"""Generated from Smithy shape ``com.amazonaws.connect#ResourceReplicationStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.aws_region
    import capo_connect.types.resource_replication_status_value


class ResourceReplicationStatus(TypedDict, closed=True):
    region: "capo_connect.types.aws_region.AwsRegion"
    """<p>The Amazon Web Services Region that the replication status applies to.</p>"""
    status: "capo_connect.types.resource_replication_status_value.ResourceReplicationStatusValue"
    """<p>The replication status of the resource type in the Region, such as <code>ENABLED</code>, <code>BLOCKED</code>, or <code>DISABLED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceReplicationStatus) -> dict:
    out: dict = {}
    out["Region"] = value["region"]
    out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> ResourceReplicationStatus:
    out: ResourceReplicationStatus = {}  # type: ignore[typeddict-item]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    else:
        out["region"] = ""
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        out["status"] = ""
    return out
