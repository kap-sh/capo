"""Generated from Smithy shape ``com.amazonaws.ec2#CreateDelegateMacVolumeOwnershipTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.instance_id
    import capo_ec2.types.sensitive_mac_credentials
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class CreateDelegateMacVolumeOwnershipTaskRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring Idempotency</a>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_id: NotRequired["capo_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the Amazon EC2 Mac instance.</p>"""
    mac_credentials: NotRequired[
        "capo_ec2.types.sensitive_mac_credentials.SensitiveMacCredentials"
    ]
    """<p>Specifies the following credentials:</p> <ul> <li> <p> <b>Internal disk administrative user</b> </p> <ul> <li> <p> <b>Username</b> - Only the default administrative user (<code>aws-managed-user</code>) is supported and it is used by default. You can't specify a different administrative user.</p> </li> <li> <p> <b>Password</b> - If you did not change the default password for <code>aws-managed-user</code>, specify the default password, which is <i>blank</i>. Otherwise, specify your password.</p> </li> </ul> </li> <li> <p> <b>Amazon EBS root volume administrative user</b> </p> <ul> <li> <p> <b>Username</b> - If you did not change the default administrative user, specify <code>ec2-user</code>. Otherwise, specify the username for your administrative user.</p> </li> <li> <p> <b>Password</b> - Specify the password for the administrative user.</p> </li> </ul> </li> </ul> <p>The credentials must be specified in the following JSON format:</p> <p> <code>{ "internalDiskPassword":"<i>internal-disk-admin_password</i>", "rootVolumeUsername":"<i>root-volume-admin_username</i>", "rootVolumepassword":"<i>root-volume-admin_password</i>" }</code> </p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to assign to the volume ownership delegation task.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateDelegateMacVolumeOwnershipTaskRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "mac_credentials" in value:
        pairs.append((f"{key_prefix}MacCredentials", str(value["mac_credentials"])))
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )


def deserialize_ec2_query(el: Element) -> CreateDelegateMacVolumeOwnershipTaskRequest:
    out: CreateDelegateMacVolumeOwnershipTaskRequest = {}  # type: ignore[typeddict-item]
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_mac_credentials = el.find("MacCredentials")
    if child_mac_credentials is not None:
        out["mac_credentials"] = str(child_mac_credentials.text or "")
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    return out
