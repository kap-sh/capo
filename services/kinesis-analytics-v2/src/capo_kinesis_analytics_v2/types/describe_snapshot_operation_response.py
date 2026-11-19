"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#DescribeSnapshotOperationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.snapshot_operation_info_details


class DescribeSnapshotOperationResponse(TypedDict, closed=True):
    snapshot_operation_info_details: "capo_kinesis_analytics_v2.types.snapshot_operation_info_details.SnapshotOperationInfoDetails"
    """<p>An object containing information about the snapshot operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSnapshotOperationResponse) -> dict:
    out: dict = {}
    import capo_kinesis_analytics_v2.types.snapshot_operation_info_details

    out["SnapshotOperationInfoDetails"] = (
        capo_kinesis_analytics_v2.types.snapshot_operation_info_details.serialize_aws_json_1_1(
            value["snapshot_operation_info_details"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSnapshotOperationResponse:
    out: DescribeSnapshotOperationResponse = {}  # type: ignore[typeddict-item]
    if data.get("SnapshotOperationInfoDetails") is not None:
        import capo_kinesis_analytics_v2.types.snapshot_operation_info_details

        out["snapshot_operation_info_details"] = (
            capo_kinesis_analytics_v2.types.snapshot_operation_info_details.deserialize_aws_json_1_1(
                data["SnapshotOperationInfoDetails"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeSnapshotOperationResponse.snapshot_operation_info_details required"
        )
    return out
