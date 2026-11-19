"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ListSnapshotsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_name
    import capo_kinesis_analytics_v2.types.list_snapshots_limit
    import capo_kinesis_analytics_v2.types.next_token
    import capo_kinesis_analytics_v2.types.snapshot_initiator
    import capo_kinesis_analytics_v2.types.snapshot_initiator_operation
    import capo_kinesis_analytics_v2.types.snapshot_status


class ListSnapshotsRequest(TypedDict, closed=True):
    source_application_name: NotRequired[
        "capo_kinesis_analytics_v2.types.application_name.ApplicationName"
    ]
    snapshot_initiator: NotRequired[
        "capo_kinesis_analytics_v2.types.snapshot_initiator.SnapshotInitiator"
    ]
    """<p>Use this parameter to list only the snapshots with the specified initiator.</p>"""
    snapshot_initiator_operation: NotRequired[
        "capo_kinesis_analytics_v2.types.snapshot_initiator_operation.SnapshotInitiatorOperation"
    ]
    """<p>Use this parameter to list only the snapshots that were created by the specified operation.</p>"""
    snapshot_status: NotRequired[
        "capo_kinesis_analytics_v2.types.snapshot_status.SnapshotStatus"
    ]
    """<p>Use this parameter to list only the snapshots with the specified status.</p>"""
    limit: NotRequired[
        "capo_kinesis_analytics_v2.types.list_snapshots_limit.ListSnapshotsLimit"
    ]
    """<p>The maximum number of snapshots to list.</p>"""
    next_token: NotRequired["capo_kinesis_analytics_v2.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSnapshotsRequest) -> dict:
    out: dict = {}
    if "source_application_name" in value:
        out["SourceApplicationName"] = value["source_application_name"]
    if "snapshot_initiator" in value:
        import capo_kinesis_analytics_v2.types.snapshot_initiator

        out["SnapshotInitiator"] = (
            capo_kinesis_analytics_v2.types.snapshot_initiator.serialize_aws_json_1_1(
                value["snapshot_initiator"]
            )
        )
    if "snapshot_initiator_operation" in value:
        import capo_kinesis_analytics_v2.types.snapshot_initiator_operation

        out["SnapshotInitiatorOperation"] = (
            capo_kinesis_analytics_v2.types.snapshot_initiator_operation.serialize_aws_json_1_1(
                value["snapshot_initiator_operation"]
            )
        )
    if "snapshot_status" in value:
        import capo_kinesis_analytics_v2.types.snapshot_status

        out["SnapshotStatus"] = (
            capo_kinesis_analytics_v2.types.snapshot_status.serialize_aws_json_1_1(
                value["snapshot_status"]
            )
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSnapshotsRequest:
    out: ListSnapshotsRequest = {}  # type: ignore[typeddict-item]
    if data.get("SourceApplicationName") is not None:
        out["source_application_name"] = data["SourceApplicationName"]
    if data.get("SnapshotInitiator") is not None:
        import capo_kinesis_analytics_v2.types.snapshot_initiator

        out["snapshot_initiator"] = (
            capo_kinesis_analytics_v2.types.snapshot_initiator.deserialize_aws_json_1_1(
                data["SnapshotInitiator"]
            )
        )
    if data.get("SnapshotInitiatorOperation") is not None:
        import capo_kinesis_analytics_v2.types.snapshot_initiator_operation

        out["snapshot_initiator_operation"] = (
            capo_kinesis_analytics_v2.types.snapshot_initiator_operation.deserialize_aws_json_1_1(
                data["SnapshotInitiatorOperation"]
            )
        )
    if data.get("SnapshotStatus") is not None:
        import capo_kinesis_analytics_v2.types.snapshot_status

        out["snapshot_status"] = (
            capo_kinesis_analytics_v2.types.snapshot_status.deserialize_aws_json_1_1(
                data["SnapshotStatus"]
            )
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
