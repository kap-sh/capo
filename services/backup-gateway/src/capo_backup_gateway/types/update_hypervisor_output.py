"""Generated from Smithy shape ``com.amazonaws.backupgateway#UpdateHypervisorOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup_gateway.types.server_arn


class UpdateHypervisorOutput(TypedDict, closed=True):
    hypervisor_arn: NotRequired["capo_backup_gateway.types.server_arn.ServerArn"]
    """<p>The Amazon Resource Name (ARN) of the hypervisor you updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateHypervisorOutput) -> dict:
    out: dict = {}
    if "hypervisor_arn" in value:
        out["HypervisorArn"] = value["hypervisor_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateHypervisorOutput:
    out: UpdateHypervisorOutput = {}  # type: ignore[typeddict-item]
    if data.get("HypervisorArn") is not None:
        out["hypervisor_arn"] = data["HypervisorArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateHypervisorOutput) -> dict:
    out: dict = {}
    if "hypervisor_arn" in value:
        out["HypervisorArn"] = value["hypervisor_arn"]
    return out


def deserialize_cbor(data: dict) -> UpdateHypervisorOutput:
    out: UpdateHypervisorOutput = {}  # type: ignore[typeddict-item]
    if data.get("HypervisorArn") is not None:
        out["hypervisor_arn"] = data["HypervisorArn"]
    return out
