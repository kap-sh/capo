"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#GetPlanInRegionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.plan


class GetPlanInRegionResponse(TypedDict, closed=True):
    plan: NotRequired["capo_arc_region_switch.types.plan.Plan"]
    """<p>The details of the Region switch plan.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetPlanInRegionResponse) -> dict:
    out: dict = {}
    if "plan" in value:
        import capo_arc_region_switch.types.plan

        out["plan"] = capo_arc_region_switch.types.plan.serialize_aws_json_1_0(
            value["plan"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetPlanInRegionResponse:
    out: GetPlanInRegionResponse = {}  # type: ignore[typeddict-item]
    if data.get("plan") is not None:
        import capo_arc_region_switch.types.plan

        out["plan"] = capo_arc_region_switch.types.plan.deserialize_aws_json_1_0(
            data["plan"]
        )
    return out
