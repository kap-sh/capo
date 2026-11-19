"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ListSnapshotOperationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.list_snapshot_operations_limit
    import capo_kinesis_analytics_v2.types.next_token
    import capo_kinesis_analytics_v2.types.snapshot_operation
    import capo_kinesis_analytics_v2.types.snapshot_operation_status
    import capo_kinesis_analytics_v2.types.snapshot_v2_name


class ListSnapshotOperationsRequest(TypedDict, closed=True):
    snapshot_name: "capo_kinesis_analytics_v2.types.snapshot_v2_name.SnapshotV2Name"
    """<p>The name of the enhanced snapshot.</p>"""
    snapshot_operation: NotRequired[
        "capo_kinesis_analytics_v2.types.snapshot_operation.SnapshotOperation"
    ]
    """<p>Use this parameter to list only the operations of the specified type.</p>"""
    snapshot_operation_status: NotRequired[
        "capo_kinesis_analytics_v2.types.snapshot_operation_status.SnapshotOperationStatus"
    ]
    """<p>Use this parameter to list only the operations with the specified status.</p>"""
    limit: NotRequired[
        "capo_kinesis_analytics_v2.types.list_snapshot_operations_limit.ListSnapshotOperationsLimit"
    ]
    """<p>The maximum number of snapshot operations to list.</p>"""
    next_token: NotRequired["capo_kinesis_analytics_v2.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSnapshotOperationsRequest) -> dict:
    out: dict = {}
    out["SnapshotName"] = value["snapshot_name"]
    if "snapshot_operation" in value:
        import capo_kinesis_analytics_v2.types.snapshot_operation

        out["SnapshotOperation"] = (
            capo_kinesis_analytics_v2.types.snapshot_operation.serialize_aws_json_1_1(
                value["snapshot_operation"]
            )
        )
    if "snapshot_operation_status" in value:
        import capo_kinesis_analytics_v2.types.snapshot_operation_status

        out["SnapshotOperationStatus"] = (
            capo_kinesis_analytics_v2.types.snapshot_operation_status.serialize_aws_json_1_1(
                value["snapshot_operation_status"]
            )
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSnapshotOperationsRequest:
    out: ListSnapshotOperationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("SnapshotName") is not None:
        out["snapshot_name"] = data["SnapshotName"]
    else:
        out["snapshot_name"] = ""
    if data.get("SnapshotOperation") is not None:
        import capo_kinesis_analytics_v2.types.snapshot_operation

        out["snapshot_operation"] = (
            capo_kinesis_analytics_v2.types.snapshot_operation.deserialize_aws_json_1_1(
                data["SnapshotOperation"]
            )
        )
    if data.get("SnapshotOperationStatus") is not None:
        import capo_kinesis_analytics_v2.types.snapshot_operation_status

        out["snapshot_operation_status"] = (
            capo_kinesis_analytics_v2.types.snapshot_operation_status.deserialize_aws_json_1_1(
                data["SnapshotOperationStatus"]
            )
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
