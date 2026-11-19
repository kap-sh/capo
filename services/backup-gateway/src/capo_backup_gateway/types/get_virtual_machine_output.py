"""Generated from Smithy shape ``com.amazonaws.backupgateway#GetVirtualMachineOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup_gateway.types.virtual_machine_details


class GetVirtualMachineOutput(TypedDict, closed=True):
    virtual_machine: NotRequired[
        "capo_backup_gateway.types.virtual_machine_details.VirtualMachineDetails"
    ]
    """<p>This object contains the basic attributes of <code>VirtualMachine</code> contained by the output of <code>GetVirtualMachine</code> </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetVirtualMachineOutput) -> dict:
    out: dict = {}
    if "virtual_machine" in value:
        import capo_backup_gateway.types.virtual_machine_details

        out["VirtualMachine"] = (
            capo_backup_gateway.types.virtual_machine_details.serialize_aws_json_1_0(
                value["virtual_machine"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetVirtualMachineOutput:
    out: GetVirtualMachineOutput = {}  # type: ignore[typeddict-item]
    if data.get("VirtualMachine") is not None:
        import capo_backup_gateway.types.virtual_machine_details

        out["virtual_machine"] = (
            capo_backup_gateway.types.virtual_machine_details.deserialize_aws_json_1_0(
                data["VirtualMachine"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetVirtualMachineOutput) -> dict:
    out: dict = {}
    if "virtual_machine" in value:
        import capo_backup_gateway.types.virtual_machine_details

        out["VirtualMachine"] = (
            capo_backup_gateway.types.virtual_machine_details.serialize_cbor(
                value["virtual_machine"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetVirtualMachineOutput:
    out: GetVirtualMachineOutput = {}  # type: ignore[typeddict-item]
    if data.get("VirtualMachine") is not None:
        import capo_backup_gateway.types.virtual_machine_details

        out["virtual_machine"] = (
            capo_backup_gateway.types.virtual_machine_details.deserialize_cbor(
                data["VirtualMachine"]
            )
        )
    return out
