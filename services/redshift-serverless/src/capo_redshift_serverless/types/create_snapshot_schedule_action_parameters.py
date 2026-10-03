"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#CreateSnapshotScheduleActionParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_redshift_serverless.types.namespace_name
    import capo_redshift_serverless.types.snapshot_name_prefix
    import capo_redshift_serverless.types.tag_list


class CreateSnapshotScheduleActionParameters(TypedDict, closed=True):
    namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName"
    """<p>The name of the namespace for which you want to configure a scheduled action to create a snapshot.</p>"""
    snapshot_name_prefix: (
        "capo_redshift_serverless.types.snapshot_name_prefix.SnapshotNamePrefix"
    )
    """<p>A string prefix that is attached to the name of the snapshot created by the scheduled action. The final name of the snapshot is the string prefix appended by the date and time of when the snapshot was created.</p>"""
    retention_period: NotRequired["int"]
    """<p>The retention period of the snapshot created by the scheduled action.</p>"""
    tags: NotRequired["capo_redshift_serverless.types.tag_list.TagList"]
    """<p>An array of <a href="https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_Tag.html">Tag objects</a> to associate with the snapshot.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSnapshotScheduleActionParameters) -> dict:
    out: dict = {}
    out["namespaceName"] = value["namespace_name"]
    out["snapshotNamePrefix"] = value["snapshot_name_prefix"]
    if "retention_period" in value:
        out["retentionPeriod"] = value["retention_period"]
    if "tags" in value:
        import capo_redshift_serverless.types.tag_list

        out["tags"] = capo_redshift_serverless.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSnapshotScheduleActionParameters:
    out: CreateSnapshotScheduleActionParameters = {}  # type: ignore[typeddict-item]
    if data.get("namespaceName") is not None:
        out["namespace_name"] = data["namespaceName"]
    else:
        raise DeserializationError(
            "CreateSnapshotScheduleActionParameters.namespace_name required"
        )
    if data.get("snapshotNamePrefix") is not None:
        out["snapshot_name_prefix"] = data["snapshotNamePrefix"]
    else:
        raise DeserializationError(
            "CreateSnapshotScheduleActionParameters.snapshot_name_prefix required"
        )
    if data.get("retentionPeriod") is not None:
        out["retention_period"] = data["retentionPeriod"]
    if data.get("tags") is not None:
        import capo_redshift_serverless.types.tag_list

        out["tags"] = capo_redshift_serverless.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
