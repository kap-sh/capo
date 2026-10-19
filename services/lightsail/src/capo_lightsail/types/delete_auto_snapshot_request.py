"""Generated from Smithy shape ``com.amazonaws.lightsail#DeleteAutoSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.auto_snapshot_date
    import capo_lightsail.types.resource_name


class DeleteAutoSnapshotRequest(TypedDict, closed=True):
    resource_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the source instance or disk from which to delete the automatic snapshot.</p>"""
    date: "capo_lightsail.types.auto_snapshot_date.AutoSnapshotDate"
    """<p>The date of the automatic snapshot to delete in <code>YYYY-MM-DD</code> format. Use the <code>get auto snapshots</code> operation to get the available automatic snapshots for a resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAutoSnapshotRequest) -> dict:
    out: dict = {}
    out["resourceName"] = value["resource_name"]
    out["date"] = value["date"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAutoSnapshotRequest:
    out: DeleteAutoSnapshotRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceName") is not None:
        out["resource_name"] = data["resourceName"]
    else:
        out["resource_name"] = ""
    if data.get("date") is not None:
        out["date"] = data["date"]
    else:
        out["date"] = ""
    return out
