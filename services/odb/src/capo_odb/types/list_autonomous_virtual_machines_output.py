"""Generated from Smithy shape ``com.amazonaws.odb#ListAutonomousVirtualMachinesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.autonomous_virtual_machine_list


class ListAutonomousVirtualMachinesOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The pagination token from which to continue listing.</p>"""
    autonomous_virtual_machines: (
        "capo_odb.types.autonomous_virtual_machine_list.AutonomousVirtualMachineList"
    )
    """<p>The list of Autonomous VMs in the specified Autonomous VM cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutonomousVirtualMachinesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_odb.types.autonomous_virtual_machine_list

    out["autonomousVirtualMachines"] = (
        capo_odb.types.autonomous_virtual_machine_list.serialize_aws_json_1_0(
            value["autonomous_virtual_machines"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutonomousVirtualMachinesOutput:
    out: ListAutonomousVirtualMachinesOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("autonomousVirtualMachines") is not None:
        import capo_odb.types.autonomous_virtual_machine_list

        out["autonomous_virtual_machines"] = (
            capo_odb.types.autonomous_virtual_machine_list.deserialize_aws_json_1_0(
                data["autonomousVirtualMachines"]
            )
        )
    else:
        out["autonomous_virtual_machines"] = []
    return out
