"""Generated from Smithy shape ``com.amazonaws.backupgateway#Hypervisor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup_gateway.types.host
    import capo_backup_gateway.types.hypervisor_state
    import capo_backup_gateway.types.kms_key_arn
    import capo_backup_gateway.types.name
    import capo_backup_gateway.types.server_arn


class Hypervisor(TypedDict, closed=True):
    host: NotRequired["capo_backup_gateway.types.host.Host"]
    """<p>The server host of the hypervisor. This can be either an IP address or a fully-qualified domain name (FQDN).</p>"""
    hypervisor_arn: NotRequired["capo_backup_gateway.types.server_arn.ServerArn"]
    """<p>The Amazon Resource Name (ARN) of the hypervisor.</p>"""
    kms_key_arn: NotRequired["capo_backup_gateway.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the Key Management Service used to encrypt the hypervisor.</p>"""
    name: NotRequired["capo_backup_gateway.types.name.Name"]
    """<p>The name of the hypervisor.</p>"""
    state: NotRequired["capo_backup_gateway.types.hypervisor_state.HypervisorState"]
    """<p>The state of the hypervisor.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Hypervisor) -> dict:
    out: dict = {}
    if "host" in value:
        out["Host"] = value["host"]
    if "hypervisor_arn" in value:
        out["HypervisorArn"] = value["hypervisor_arn"]
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "state" in value:
        out["State"] = value["state"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Hypervisor:
    out: Hypervisor = {}  # type: ignore[typeddict-item]
    if data.get("Host") is not None:
        out["host"] = data["Host"]
    if data.get("HypervisorArn") is not None:
        out["hypervisor_arn"] = data["HypervisorArn"]
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("State") is not None:
        out["state"] = data["State"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Hypervisor) -> dict:
    out: dict = {}
    if "host" in value:
        out["Host"] = value["host"]
    if "hypervisor_arn" in value:
        out["HypervisorArn"] = value["hypervisor_arn"]
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "state" in value:
        out["State"] = value["state"]
    return out


def deserialize_cbor(data: dict) -> Hypervisor:
    out: Hypervisor = {}  # type: ignore[typeddict-item]
    if data.get("Host") is not None:
        out["host"] = data["Host"]
    if data.get("HypervisorArn") is not None:
        out["hypervisor_arn"] = data["HypervisorArn"]
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("State") is not None:
        out["state"] = data["State"]
    return out
