"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#SnapshotInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.snapshot_info

SnapshotInfoList: TypeAlias = list[
    "capo_kinesis_analytics_v2.types.snapshot_info.SnapshotInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotInfoList) -> list:
    import capo_kinesis_analytics_v2.types.snapshot_info

    out: list = []
    for item in value:
        out.append(
            capo_kinesis_analytics_v2.types.snapshot_info.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SnapshotInfoList:
    import capo_kinesis_analytics_v2.types.snapshot_info

    out: SnapshotInfoList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_kinesis_analytics_v2.types.snapshot_info.deserialize_aws_json_1_1(item)
        )
    return out
