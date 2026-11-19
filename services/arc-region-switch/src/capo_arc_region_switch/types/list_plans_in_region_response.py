"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ListPlansInRegionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.next_token
    import capo_arc_region_switch.types.plan_list


class ListPlansInRegionResponse(TypedDict, closed=True):
    plans: NotRequired["capo_arc_region_switch.types.plan_list.PlanList"]
    """<p>The plans that were requested.</p>"""
    next_token: NotRequired["capo_arc_region_switch.types.next_token.NextToken"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListPlansInRegionResponse) -> dict:
    out: dict = {}
    if "plans" in value:
        import capo_arc_region_switch.types.plan_list

        out["plans"] = capo_arc_region_switch.types.plan_list.serialize_aws_json_1_0(
            value["plans"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListPlansInRegionResponse:
    out: ListPlansInRegionResponse = {}  # type: ignore[typeddict-item]
    if data.get("plans") is not None:
        import capo_arc_region_switch.types.plan_list

        out["plans"] = capo_arc_region_switch.types.plan_list.deserialize_aws_json_1_0(
            data["plans"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListPlansInRegionResponse) -> dict:
    out: dict = {}
    if "plans" in value:
        import capo_arc_region_switch.types.plan_list

        out["plans"] = capo_arc_region_switch.types.plan_list.serialize_cbor(
            value["plans"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListPlansInRegionResponse:
    out: ListPlansInRegionResponse = {}  # type: ignore[typeddict-item]
    if data.get("plans") is not None:
        import capo_arc_region_switch.types.plan_list

        out["plans"] = capo_arc_region_switch.types.plan_list.deserialize_cbor(
            data["plans"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
