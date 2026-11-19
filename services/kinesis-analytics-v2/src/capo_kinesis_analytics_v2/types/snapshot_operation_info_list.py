"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#SnapshotOperationInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.snapshot_operation_info

SnapshotOperationInfoList: TypeAlias = list[
    "capo_kinesis_analytics_v2.types.snapshot_operation_info.SnapshotOperationInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotOperationInfoList) -> list:
    import capo_kinesis_analytics_v2.types.snapshot_operation_info

    out: list = []
    for item in value:
        out.append(
            capo_kinesis_analytics_v2.types.snapshot_operation_info.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SnapshotOperationInfoList:
    import capo_kinesis_analytics_v2.types.snapshot_operation_info

    out: SnapshotOperationInfoList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_kinesis_analytics_v2.types.snapshot_operation_info.deserialize_aws_json_1_1(
                item
            )
        )
    return out
