"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#MinimalWorkflow``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.execution_action


class MinimalWorkflow(TypedDict, closed=True):
    action: NotRequired["capo_arc_region_switch.types.execution_action.ExecutionAction"]
    """<p>The action for a minimal workflow, which can be Activate or Deactivate.</p>"""
    name: NotRequired["str"]
    """<p>The name for a minimal workflow</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MinimalWorkflow) -> dict:
    out: dict = {}
    if "action" in value:
        import capo_arc_region_switch.types.execution_action

        out["action"] = (
            capo_arc_region_switch.types.execution_action.serialize_aws_json_1_0(
                value["action"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MinimalWorkflow:
    out: MinimalWorkflow = {}  # type: ignore[typeddict-item]
    if data.get("action") is not None:
        import capo_arc_region_switch.types.execution_action

        out["action"] = (
            capo_arc_region_switch.types.execution_action.deserialize_aws_json_1_0(
                data["action"]
            )
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MinimalWorkflow) -> dict:
    out: dict = {}
    if "action" in value:
        import capo_arc_region_switch.types.execution_action

        out["action"] = capo_arc_region_switch.types.execution_action.serialize_cbor(
            value["action"]
        )
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_cbor(data: dict) -> MinimalWorkflow:
    out: MinimalWorkflow = {}  # type: ignore[typeddict-item]
    if data.get("action") is not None:
        import capo_arc_region_switch.types.execution_action

        out["action"] = capo_arc_region_switch.types.execution_action.deserialize_cbor(
            data["action"]
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out
