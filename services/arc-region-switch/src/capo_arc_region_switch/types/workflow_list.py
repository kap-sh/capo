"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#WorkflowList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_region_switch.types.workflow

WorkflowList: TypeAlias = list["capo_arc_region_switch.types.workflow.Workflow"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowList) -> list:
    import capo_arc_region_switch.types.workflow

    out: list = []
    for item in value:
        out.append(capo_arc_region_switch.types.workflow.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> WorkflowList:
    import capo_arc_region_switch.types.workflow

    out: WorkflowList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_arc_region_switch.types.workflow.deserialize_aws_json_1_0(item))
    return out
