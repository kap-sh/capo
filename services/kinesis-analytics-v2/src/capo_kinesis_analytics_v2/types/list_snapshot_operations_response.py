"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ListSnapshotOperationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.next_token
    import capo_kinesis_analytics_v2.types.snapshot_operation_info_list


class ListSnapshotOperationsResponse(TypedDict, closed=True):
    snapshot_operation_info_list: "capo_kinesis_analytics_v2.types.snapshot_operation_info_list.SnapshotOperationInfoList"
    """<p>A list of <code>SnapshotOperationInfo</code> objects.</p>"""
    next_token: NotRequired["capo_kinesis_analytics_v2.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSnapshotOperationsResponse) -> dict:
    out: dict = {}
    import capo_kinesis_analytics_v2.types.snapshot_operation_info_list

    out["SnapshotOperationInfoList"] = (
        capo_kinesis_analytics_v2.types.snapshot_operation_info_list.serialize_aws_json_1_1(
            value["snapshot_operation_info_list"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSnapshotOperationsResponse:
    out: ListSnapshotOperationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("SnapshotOperationInfoList") is not None:
        import capo_kinesis_analytics_v2.types.snapshot_operation_info_list

        out["snapshot_operation_info_list"] = (
            capo_kinesis_analytics_v2.types.snapshot_operation_info_list.deserialize_aws_json_1_1(
                data["SnapshotOperationInfoList"]
            )
        )
    else:
        out["snapshot_operation_info_list"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
