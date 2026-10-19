"""Generated from Smithy shape ``com.amazonaws.backupgateway#GetVirtualMachineInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_backup_gateway.types.resource_arn


class GetVirtualMachineInput(TypedDict, closed=True):
    resource_arn: "capo_backup_gateway.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the virtual machine.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetVirtualMachineInput) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetVirtualMachineInput:
    out: GetVirtualMachineInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    return out
