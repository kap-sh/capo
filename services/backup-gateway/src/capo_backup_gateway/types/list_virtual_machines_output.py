"""Generated from Smithy shape ``com.amazonaws.backupgateway#ListVirtualMachinesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup_gateway.types.next_token
    import capo_backup_gateway.types.virtual_machines


class ListVirtualMachinesOutput(TypedDict, closed=True):
    virtual_machines: NotRequired[
        "capo_backup_gateway.types.virtual_machines.VirtualMachines"
    ]
    """<p>A list of your <code>VirtualMachine</code> objects, ordered by their Amazon Resource Names (ARNs).</p>"""
    next_token: NotRequired["capo_backup_gateway.types.next_token.NextToken"]
    """<p>The next item following a partial list of returned resources. For example, if a request is made to return <code>maxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListVirtualMachinesOutput) -> dict:
    out: dict = {}
    if "virtual_machines" in value:
        import capo_backup_gateway.types.virtual_machines

        out["VirtualMachines"] = (
            capo_backup_gateway.types.virtual_machines.serialize_aws_json_1_0(
                value["virtual_machines"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListVirtualMachinesOutput:
    out: ListVirtualMachinesOutput = {}  # type: ignore[typeddict-item]
    if data.get("VirtualMachines") is not None:
        import capo_backup_gateway.types.virtual_machines

        out["virtual_machines"] = (
            capo_backup_gateway.types.virtual_machines.deserialize_aws_json_1_0(
                data["VirtualMachines"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListVirtualMachinesOutput) -> dict:
    out: dict = {}
    if "virtual_machines" in value:
        import capo_backup_gateway.types.virtual_machines

        out["VirtualMachines"] = (
            capo_backup_gateway.types.virtual_machines.serialize_cbor(
                value["virtual_machines"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListVirtualMachinesOutput:
    out: ListVirtualMachinesOutput = {}  # type: ignore[typeddict-item]
    if data.get("VirtualMachines") is not None:
        import capo_backup_gateway.types.virtual_machines

        out["virtual_machines"] = (
            capo_backup_gateway.types.virtual_machines.deserialize_cbor(
                data["VirtualMachines"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
