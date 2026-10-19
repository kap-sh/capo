"""Generated from Smithy shape ``com.amazonaws.docdbelastic#CopyClusterSnapshotInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_docdb_elastic.types.tag_map


class CopyClusterSnapshotInput(TypedDict, closed=True):
    snapshot_arn: "str"
    """<p>The Amazon Resource Name (ARN) identifier of the elastic cluster snapshot.</p>"""
    target_snapshot_name: "str"
    """<p>The identifier of the new elastic cluster snapshot to create from the source cluster snapshot. This parameter is not case sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <p>Example: <code>elastic-cluster-snapshot-5</code> </p>"""
    kms_key_id: NotRequired["str"]
    """<p>The Amazon Web Services KMS key ID for an encrypted elastic cluster snapshot. The Amazon Web Services KMS key ID is the Amazon Resource Name (ARN), Amazon Web Services KMS key identifier, or the Amazon Web Services KMS key alias for the Amazon Web Services KMS encryption key.</p> <p>If you copy an encrypted elastic cluster snapshot from your Amazon Web Services account, you can specify a value for <code>KmsKeyId</code> to encrypt the copy with a new Amazon Web ServicesS KMS encryption key. If you don't specify a value for <code>KmsKeyId</code>, then the copy of the elastic cluster snapshot is encrypted with the same <code>AWS</code> KMS key as the source elastic cluster snapshot.</p> <p>To copy an encrypted elastic cluster snapshot to another Amazon Web Services region, set <code>KmsKeyId</code> to the Amazon Web Services KMS key ID that you want to use to encrypt the copy of the elastic cluster snapshot in the destination region. Amazon Web Services KMS encryption keys are specific to the Amazon Web Services region that they are created in, and you can't use encryption keys from one Amazon Web Services region in another Amazon Web Services region.</p> <p>If you copy an unencrypted elastic cluster snapshot and specify a value for the <code>KmsKeyId</code> parameter, an error is returned.</p>"""
    copy_tags: NotRequired["bool"]
    """<p>Set to <code>true</code> to copy all tags from the source cluster snapshot to the target elastic cluster snapshot. The default is <code>false</code>.</p>"""
    tags: NotRequired["capo_docdb_elastic.types.tag_map.TagMap"]
    """<p>The tags to be assigned to the elastic cluster snapshot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CopyClusterSnapshotInput) -> dict:
    out: dict = {}
    out["targetSnapshotName"] = value["target_snapshot_name"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "copy_tags" in value:
        out["copyTags"] = value["copy_tags"]
    if "tags" in value:
        import capo_docdb_elastic.types.tag_map

        out["tags"] = capo_docdb_elastic.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CopyClusterSnapshotInput:
    out: CopyClusterSnapshotInput = {}  # type: ignore[typeddict-item]
    if data.get("targetSnapshotName") is not None:
        out["target_snapshot_name"] = data["targetSnapshotName"]
    else:
        out["target_snapshot_name"] = ""
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("copyTags") is not None:
        out["copy_tags"] = data["copyTags"]
    if data.get("tags") is not None:
        import capo_docdb_elastic.types.tag_map

        out["tags"] = capo_docdb_elastic.types.tag_map.deserialize_json(data["tags"])
    return out
