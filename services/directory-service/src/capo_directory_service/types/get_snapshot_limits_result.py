"""Generated from Smithy shape ``com.amazonaws.directoryservice#GetSnapshotLimitsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.snapshot_limits


class GetSnapshotLimitsResult(TypedDict, closed=True):
    snapshot_limits: NotRequired[
        "capo_directory_service.types.snapshot_limits.SnapshotLimits"
    ]
    """<p>A <a>SnapshotLimits</a> object that contains the manual snapshot limits for the specified directory.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSnapshotLimitsResult) -> dict:
    out: dict = {}
    if "snapshot_limits" in value:
        import capo_directory_service.types.snapshot_limits

        out["SnapshotLimits"] = (
            capo_directory_service.types.snapshot_limits.serialize_aws_json_1_1(
                value["snapshot_limits"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSnapshotLimitsResult:
    out: GetSnapshotLimitsResult = {}  # type: ignore[typeddict-item]
    if data.get("SnapshotLimits") is not None:
        import capo_directory_service.types.snapshot_limits

        out["snapshot_limits"] = (
            capo_directory_service.types.snapshot_limits.deserialize_aws_json_1_1(
                data["SnapshotLimits"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetSnapshotLimitsResult) -> dict:
    out: dict = {}
    if "snapshot_limits" in value:
        import capo_directory_service.types.snapshot_limits

        out["SnapshotLimits"] = (
            capo_directory_service.types.snapshot_limits.serialize_cbor(
                value["snapshot_limits"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetSnapshotLimitsResult:
    out: GetSnapshotLimitsResult = {}  # type: ignore[typeddict-item]
    if data.get("SnapshotLimits") is not None:
        import capo_directory_service.types.snapshot_limits

        out["snapshot_limits"] = (
            capo_directory_service.types.snapshot_limits.deserialize_cbor(
                data["SnapshotLimits"]
            )
        )
    return out
