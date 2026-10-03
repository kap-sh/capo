"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#CreateSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_redshift_serverless.types.tag_list


class CreateSnapshotRequest(TypedDict, closed=True):
    namespace_name: "str"
    """<p>The namespace to create a snapshot for.</p>"""
    snapshot_name: "str"
    """<p>The name of the snapshot.</p>"""
    retention_period: NotRequired["int"]
    """<p>How long to retain the created snapshot.</p>"""
    tags: NotRequired["capo_redshift_serverless.types.tag_list.TagList"]
    """<p>An array of <a href="https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_Tag.html">Tag objects</a> to associate with the snapshot.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSnapshotRequest) -> dict:
    out: dict = {}
    out["namespaceName"] = value["namespace_name"]
    out["snapshotName"] = value["snapshot_name"]
    if "retention_period" in value:
        out["retentionPeriod"] = value["retention_period"]
    if "tags" in value:
        import capo_redshift_serverless.types.tag_list

        out["tags"] = capo_redshift_serverless.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSnapshotRequest:
    out: CreateSnapshotRequest = {}  # type: ignore[typeddict-item]
    if data.get("namespaceName") is not None:
        out["namespace_name"] = data["namespaceName"]
    else:
        raise DeserializationError("CreateSnapshotRequest.namespace_name required")
    if data.get("snapshotName") is not None:
        out["snapshot_name"] = data["snapshotName"]
    else:
        raise DeserializationError("CreateSnapshotRequest.snapshot_name required")
    if data.get("retentionPeriod") is not None:
        out["retention_period"] = data["retentionPeriod"]
    if data.get("tags") is not None:
        import capo_redshift_serverless.types.tag_list

        out["tags"] = capo_redshift_serverless.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
