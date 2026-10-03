"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ConvertRecoveryPointToSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_redshift_serverless.types.tag_list


class ConvertRecoveryPointToSnapshotRequest(TypedDict, closed=True):
    recovery_point_id: "str"
    """<p>The unique identifier of the recovery point.</p>"""
    snapshot_name: "str"
    """<p>The name of the snapshot.</p>"""
    retention_period: NotRequired["int"]
    """<p>How long to retain the snapshot.</p>"""
    tags: NotRequired["capo_redshift_serverless.types.tag_list.TagList"]
    """<p>An array of <a href="https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_Tag.html">Tag objects</a> to associate with the created snapshot.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConvertRecoveryPointToSnapshotRequest) -> dict:
    out: dict = {}
    out["recoveryPointId"] = value["recovery_point_id"]
    out["snapshotName"] = value["snapshot_name"]
    if "retention_period" in value:
        out["retentionPeriod"] = value["retention_period"]
    if "tags" in value:
        import capo_redshift_serverless.types.tag_list

        out["tags"] = capo_redshift_serverless.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConvertRecoveryPointToSnapshotRequest:
    out: ConvertRecoveryPointToSnapshotRequest = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPointId") is not None:
        out["recovery_point_id"] = data["recoveryPointId"]
    else:
        raise DeserializationError(
            "ConvertRecoveryPointToSnapshotRequest.recovery_point_id required"
        )
    if data.get("snapshotName") is not None:
        out["snapshot_name"] = data["snapshotName"]
    else:
        raise DeserializationError(
            "ConvertRecoveryPointToSnapshotRequest.snapshot_name required"
        )
    if data.get("retentionPeriod") is not None:
        out["retention_period"] = data["retentionPeriod"]
    if data.get("tags") is not None:
        import capo_redshift_serverless.types.tag_list

        out["tags"] = capo_redshift_serverless.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
