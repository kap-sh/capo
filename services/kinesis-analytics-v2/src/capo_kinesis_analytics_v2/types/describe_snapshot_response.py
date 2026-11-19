"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#DescribeSnapshotResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.snapshot_info_details


class DescribeSnapshotResponse(TypedDict, closed=True):
    snapshot_info_details: (
        "capo_kinesis_analytics_v2.types.snapshot_info_details.SnapshotInfoDetails"
    )
    """<p>An object containing information about the enhanced snapshot.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSnapshotResponse) -> dict:
    out: dict = {}
    import capo_kinesis_analytics_v2.types.snapshot_info_details

    out["SnapshotInfoDetails"] = (
        capo_kinesis_analytics_v2.types.snapshot_info_details.serialize_aws_json_1_1(
            value["snapshot_info_details"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSnapshotResponse:
    out: DescribeSnapshotResponse = {}  # type: ignore[typeddict-item]
    if data.get("SnapshotInfoDetails") is not None:
        import capo_kinesis_analytics_v2.types.snapshot_info_details

        out["snapshot_info_details"] = (
            capo_kinesis_analytics_v2.types.snapshot_info_details.deserialize_aws_json_1_1(
                data["SnapshotInfoDetails"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeSnapshotResponse.snapshot_info_details required"
        )
    return out
