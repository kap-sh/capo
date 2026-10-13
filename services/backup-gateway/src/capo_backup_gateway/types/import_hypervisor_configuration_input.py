"""Generated from Smithy shape ``com.amazonaws.backupgateway#ImportHypervisorConfigurationInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_backup_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backup_gateway.types.host
    import capo_backup_gateway.types.kms_key_arn
    import capo_backup_gateway.types.name
    import capo_backup_gateway.types.password
    import capo_backup_gateway.types.tags
    import capo_backup_gateway.types.username


class ImportHypervisorConfigurationInput(TypedDict, closed=True):
    name: "capo_backup_gateway.types.name.Name"
    """<p>The name of the hypervisor.</p>"""
    host: "capo_backup_gateway.types.host.Host"
    """<p>The server host of the hypervisor. This can be either an IP address or a fully-qualified domain name (FQDN).</p>"""
    username: NotRequired["capo_backup_gateway.types.username.Username"]
    """<p>The username for the hypervisor.</p>"""
    password: NotRequired["capo_backup_gateway.types.password.Password"]
    """<p>The password for the hypervisor.</p>"""
    kms_key_arn: NotRequired["capo_backup_gateway.types.kms_key_arn.KmsKeyArn"]
    """<p>The Key Management Service for the hypervisor.</p>"""
    tags: NotRequired["capo_backup_gateway.types.tags.Tags"]
    """<p>The tags of the hypervisor configuration to import.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportHypervisorConfigurationInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Host"] = value["host"]
    if "username" in value:
        out["Username"] = value["username"]
    if "password" in value:
        out["Password"] = value["password"]
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    if "tags" in value:
        import capo_backup_gateway.types.tags

        out["Tags"] = capo_backup_gateway.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ImportHypervisorConfigurationInput:
    out: ImportHypervisorConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ImportHypervisorConfigurationInput.name required")
    if data.get("Host") is not None:
        out["host"] = data["Host"]
    else:
        raise DeserializationError("ImportHypervisorConfigurationInput.host required")
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if data.get("Tags") is not None:
        import capo_backup_gateway.types.tags

        out["tags"] = capo_backup_gateway.types.tags.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out


def redact_sensitive(value: ImportHypervisorConfigurationInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "username" in value:
        out["username"] = "*** Sensitive Data Redacted ***"
    if "password" in value:
        out["password"] = "*** Sensitive Data Redacted ***"
    return out
