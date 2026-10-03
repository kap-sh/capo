"""Generated from Smithy shape ``com.amazonaws.ec2#ImportSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.client_data
    import capo_ec2.types.kms_key_id
    import capo_ec2.types.snapshot_disk_container
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class ImportSnapshotRequest(TypedDict, closed=True):
    client_data: NotRequired["capo_ec2.types.client_data.ClientData"]
    """<p>The client-specific data.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Token to enable idempotency for VM import requests.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description string for the import snapshot task.</p>"""
    disk_container: NotRequired[
        "capo_ec2.types.snapshot_disk_container.SnapshotDiskContainer"
    ]
    """<p>Information about the disk container.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    encrypted: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Specifies whether the destination snapshot of the imported image should be encrypted. The default KMS key for EBS is used unless you specify a non-default KMS key using <code>KmsKeyId</code>. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html">Amazon EBS Encryption</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>.</p>"""
    kms_key_id: NotRequired["capo_ec2.types.kms_key_id.KmsKeyId"]
    """<p>An identifier for the symmetric KMS key to use when creating the encrypted snapshot. This parameter is only required if you want to use a non-default KMS key; if this parameter is not specified, the default KMS key for EBS is used. If a <code>KmsKeyId</code> is specified, the <code>Encrypted</code> flag must also be set. </p> <p>The KMS key identifier may be provided in any of the following formats: </p> <ul> <li> <p>Key ID</p> </li> <li> <p>Key alias</p> </li> <li> <p>ARN using key ID. The ID ARN contains the <code>arn:aws:kms</code> namespace, followed by the Region of the key, the Amazon Web Services account ID of the key owner, the <code>key</code> namespace, and then the key ID. For example, arn:aws:kms:<i>us-east-1</i>:<i>012345678910</i>:key/<i>abcd1234-a123-456a-a12b-a123b4cd56ef</i>.</p> </li> <li> <p>ARN using key alias. The alias ARN contains the <code>arn:aws:kms</code> namespace, followed by the Region of the key, the Amazon Web Services account ID of the key owner, the <code>alias</code> namespace, and then the key alias. For example, arn:aws:kms:<i>us-east-1</i>:<i>012345678910</i>:alias/<i>ExampleAlias</i>. </p> </li> </ul> <p>Amazon Web Services parses <code>KmsKeyId</code> asynchronously, meaning that the action you call may appear to complete even though you provided an invalid identifier. This action will eventually report failure. </p> <p>The specified KMS key must exist in the Region that the snapshot is being copied to.</p> <p>Amazon EBS does not support asymmetric KMS keys.</p>"""
    role_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the role to use when not using the default role, 'vmimport'.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the import snapshot task during creation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImportSnapshotRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "client_data" in value:
        import capo_ec2.types.client_data

        capo_ec2.types.client_data.serialize_ec2_query(
            value["client_data"], pairs, f"{key_prefix}ClientData"
        )
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "disk_container" in value:
        import capo_ec2.types.snapshot_disk_container

        capo_ec2.types.snapshot_disk_container.serialize_ec2_query(
            value["disk_container"], pairs, f"{key_prefix}DiskContainer"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "encrypted" in value:
        pairs.append(
            (f"{key_prefix}Encrypted", "true" if value["encrypted"] else "false")
        )
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "role_name" in value:
        pairs.append((f"{key_prefix}RoleName", str(value["role_name"])))
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )


def deserialize_ec2_query(el: Element) -> ImportSnapshotRequest:
    out: ImportSnapshotRequest = {}  # type: ignore[typeddict-item]
    child_client_data = el.find("ClientData")
    if child_client_data is not None:
        import capo_ec2.types.client_data

        out["client_data"] = capo_ec2.types.client_data.deserialize_ec2_query(
            child_client_data
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_disk_container = el.find("DiskContainer")
    if child_disk_container is not None:
        import capo_ec2.types.snapshot_disk_container

        out["disk_container"] = (
            capo_ec2.types.snapshot_disk_container.deserialize_ec2_query(
                child_disk_container
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_encrypted = el.find("Encrypted")
    if child_encrypted is not None:
        out["encrypted"] = (child_encrypted.text or "").lower() == "true"
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_role_name = el.find("RoleName")
    if child_role_name is not None:
        out["role_name"] = str(child_role_name.text or "")
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    return out
