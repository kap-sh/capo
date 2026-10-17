"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#Step``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_arc_region_switch.types.execution_block_configuration
    import capo_arc_region_switch.types.execution_block_type
    import capo_arc_region_switch.types.step_name


class Step(TypedDict, closed=True):
    name: "capo_arc_region_switch.types.step_name.StepName"
    """<p>The name of a step in a workflow.</p>"""
    description: NotRequired["str"]
    """<p>The description of a step in a workflow.</p>"""
    execution_block_configuration: "capo_arc_region_switch.types.execution_block_configuration.ExecutionBlockConfiguration"
    """<p>The configuration for an execution block in a workflow.</p>"""
    execution_block_type: (
        "capo_arc_region_switch.types.execution_block_type.ExecutionBlockType"
    )
    """<p>The type of an execution block in a workflow.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Step) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_arc_region_switch.types.execution_block_configuration

    out["executionBlockConfiguration"] = (
        capo_arc_region_switch.types.execution_block_configuration.serialize_aws_json_1_0(
            value["execution_block_configuration"]
        )
    )
    import capo_arc_region_switch.types.execution_block_type

    out["executionBlockType"] = (
        capo_arc_region_switch.types.execution_block_type.serialize_aws_json_1_0(
            value["execution_block_type"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> Step:
    out: Step = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Step.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("executionBlockConfiguration") is not None:
        import capo_arc_region_switch.types.execution_block_configuration

        out["execution_block_configuration"] = (
            capo_arc_region_switch.types.execution_block_configuration.deserialize_aws_json_1_0(
                data["executionBlockConfiguration"]
            )
        )
    else:
        raise DeserializationError("Step.execution_block_configuration required")
    if data.get("executionBlockType") is not None:
        import capo_arc_region_switch.types.execution_block_type

        out["execution_block_type"] = (
            capo_arc_region_switch.types.execution_block_type.deserialize_aws_json_1_0(
                data["executionBlockType"]
            )
        )
    else:
        raise DeserializationError("Step.execution_block_type required")
    return out
