"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateSegmentSnapshotResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.uuid


class CreateSegmentSnapshotResponse(TypedDict, closed=True):
    snapshot_id: "capo_customer_profiles.types.uuid.uuid"
    """<p>The unique identifier of the segment snapshot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSegmentSnapshotResponse) -> dict:
    out: dict = {}
    out["SnapshotId"] = value["snapshot_id"]
    return out


def deserialize_json(data: dict) -> CreateSegmentSnapshotResponse:
    out: CreateSegmentSnapshotResponse = {}  # type: ignore[typeddict-item]
    if data.get("SnapshotId") is not None:
        out["snapshot_id"] = data["SnapshotId"]
    else:
        out["snapshot_id"] = ""
    return out
