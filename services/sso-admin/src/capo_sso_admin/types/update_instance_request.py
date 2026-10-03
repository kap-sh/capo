"""Generated from Smithy shape ``com.amazonaws.ssoadmin#UpdateInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sso_admin.types.encryption_configuration
    import capo_sso_admin.types.instance_arn
    import capo_sso_admin.types.name_type


class UpdateInstanceRequest(TypedDict, closed=True):
    name: NotRequired["capo_sso_admin.types.name_type.NameType"]
    """<p>Updates the instance name.</p>"""
    instance_arn: "capo_sso_admin.types.instance_arn.InstanceArn"
    """<p>The ARN of the instance of IAM Identity Center under which the operation will run. For more information about ARNs, see <a href="/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    encryption_configuration: NotRequired[
        "capo_sso_admin.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>Specifies the encryption configuration for your IAM Identity Center instance. You can use this to configure customer managed KMS keys or Amazon Web Services owned KMS keys for encrypting your instance data.</p>"""
    permission_sets_enabled: NotRequired["bool"]
    """<p>Enables permission sets for this Identity Center instance. The only accepted value is <code>true </code>. After permission sets are enabled, they cannot be disabled.</p> <note> <p>You can't set <code>EncryptionConfiguration</code> and <code>PermissionSetsEnabled</code> in the same request. To configure both, make two separate <code>UpdateInstance</code> calls. These calls can be made in parallel.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateInstanceRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    out["InstanceArn"] = value["instance_arn"]
    if "encryption_configuration" in value:
        import capo_sso_admin.types.encryption_configuration

        out["EncryptionConfiguration"] = (
            capo_sso_admin.types.encryption_configuration.serialize_aws_json_1_1(
                value["encryption_configuration"]
            )
        )
    if "permission_sets_enabled" in value:
        out["PermissionSetsEnabled"] = value["permission_sets_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateInstanceRequest:
    out: UpdateInstanceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("InstanceArn") is not None:
        out["instance_arn"] = data["InstanceArn"]
    else:
        raise DeserializationError("UpdateInstanceRequest.instance_arn required")
    if data.get("EncryptionConfiguration") is not None:
        import capo_sso_admin.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_sso_admin.types.encryption_configuration.deserialize_aws_json_1_1(
                data["EncryptionConfiguration"]
            )
        )
    if data.get("PermissionSetsEnabled") is not None:
        out["permission_sets_enabled"] = data["PermissionSetsEnabled"]
    return out
