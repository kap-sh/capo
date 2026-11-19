"""Generated from Smithy shape ``com.amazonaws.directoryservice#SnapshotLimits``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.limit
    import capo_directory_service.types.manual_snapshots_limit_reached


class SnapshotLimits(TypedDict, closed=True):
    manual_snapshots_limit: NotRequired["capo_directory_service.types.limit.Limit"]
    """<p>The maximum number of manual snapshots allowed.</p>"""
    manual_snapshots_current_count: NotRequired[
        "capo_directory_service.types.limit.Limit"
    ]
    """<p>The current number of manual snapshots of the directory.</p>"""
    manual_snapshots_limit_reached: "capo_directory_service.types.manual_snapshots_limit_reached.ManualSnapshotsLimitReached"
    """<p>Indicates if the manual snapshot limit has been reached.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotLimits) -> dict:
    out: dict = {}
    if "manual_snapshots_limit" in value:
        out["ManualSnapshotsLimit"] = value["manual_snapshots_limit"]
    if "manual_snapshots_current_count" in value:
        out["ManualSnapshotsCurrentCount"] = value["manual_snapshots_current_count"]
    out["ManualSnapshotsLimitReached"] = value.get(
        "manual_snapshots_limit_reached", False
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SnapshotLimits:
    out: SnapshotLimits = {}  # type: ignore[typeddict-item]
    if data.get("ManualSnapshotsLimit") is not None:
        out["manual_snapshots_limit"] = data["ManualSnapshotsLimit"]
    if data.get("ManualSnapshotsCurrentCount") is not None:
        out["manual_snapshots_current_count"] = data["ManualSnapshotsCurrentCount"]
    if data.get("ManualSnapshotsLimitReached") is not None:
        out["manual_snapshots_limit_reached"] = data["ManualSnapshotsLimitReached"]
    else:
        out["manual_snapshots_limit_reached"] = False
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SnapshotLimits) -> dict:
    out: dict = {}
    if "manual_snapshots_limit" in value:
        out["ManualSnapshotsLimit"] = value["manual_snapshots_limit"]
    if "manual_snapshots_current_count" in value:
        out["ManualSnapshotsCurrentCount"] = value["manual_snapshots_current_count"]
    out["ManualSnapshotsLimitReached"] = value.get(
        "manual_snapshots_limit_reached", False
    )
    return out


def deserialize_cbor(data: dict) -> SnapshotLimits:
    out: SnapshotLimits = {}  # type: ignore[typeddict-item]
    if data.get("ManualSnapshotsLimit") is not None:
        out["manual_snapshots_limit"] = data["ManualSnapshotsLimit"]
    if data.get("ManualSnapshotsCurrentCount") is not None:
        out["manual_snapshots_current_count"] = data["ManualSnapshotsCurrentCount"]
    if data.get("ManualSnapshotsLimitReached") is not None:
        out["manual_snapshots_limit_reached"] = data["ManualSnapshotsLimitReached"]
    else:
        out["manual_snapshots_limit_reached"] = False
    return out
