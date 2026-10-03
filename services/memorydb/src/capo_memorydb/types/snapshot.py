"""Generated from Smithy shape ``com.amazonaws.memorydb#Snapshot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.cluster_configuration
    import capo_memorydb.types.data_tiering_status
    import capo_memorydb.types.string


class Snapshot(TypedDict, closed=True):
    name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the snapshot</p>"""
    status: NotRequired["capo_memorydb.types.string.String"]
    """<p>The status of the snapshot. Valid values: creating | available | restoring | copying | deleting.</p>"""
    source: NotRequired["capo_memorydb.types.string.String"]
    """<p>Indicates whether the snapshot is from an automatic backup (automated) or was created manually (manual).</p>"""
    kms_key_id: NotRequired["capo_memorydb.types.string.String"]
    """<p>The ID of the KMS key used to encrypt the snapshot.</p>"""
    arn: NotRequired["capo_memorydb.types.string.String"]
    """<p>The ARN (Amazon Resource Name) of the snapshot.</p>"""
    cluster_configuration: NotRequired[
        "capo_memorydb.types.cluster_configuration.ClusterConfiguration"
    ]
    """<p>The configuration of the cluster from which the snapshot was taken</p>"""
    data_tiering: NotRequired[
        "capo_memorydb.types.data_tiering_status.DataTieringStatus"
    ]
    """<p>Enables data tiering. Data tiering is only supported for clusters using the r6gd node type. This parameter must be set when using r6gd nodes. For more information, see <a href="https://docs.aws.amazon.com/memorydb/latest/devguide/data-tiering.html">Data tiering</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Snapshot) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        out["Status"] = value["status"]
    if "source" in value:
        out["Source"] = value["source"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "arn" in value:
        out["ARN"] = value["arn"]
    if "cluster_configuration" in value:
        import capo_memorydb.types.cluster_configuration

        out["ClusterConfiguration"] = (
            capo_memorydb.types.cluster_configuration.serialize_aws_json_1_1(
                value["cluster_configuration"]
            )
        )
    if "data_tiering" in value:
        import capo_memorydb.types.data_tiering_status

        out["DataTiering"] = (
            capo_memorydb.types.data_tiering_status.serialize_aws_json_1_1(
                value["data_tiering"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Snapshot:
    out: Snapshot = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("Source") is not None:
        out["source"] = data["Source"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    if data.get("ClusterConfiguration") is not None:
        import capo_memorydb.types.cluster_configuration

        out["cluster_configuration"] = (
            capo_memorydb.types.cluster_configuration.deserialize_aws_json_1_1(
                data["ClusterConfiguration"]
            )
        )
    if data.get("DataTiering") is not None:
        import capo_memorydb.types.data_tiering_status

        out["data_tiering"] = (
            capo_memorydb.types.data_tiering_status.deserialize_aws_json_1_1(
                data["DataTiering"]
            )
        )
    return out
