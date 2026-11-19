"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ListPlanExecutionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.abbreviated_executions_list


class ListPlanExecutionsResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_arc_region_switch.types.abbreviated_executions_list.AbbreviatedExecutionsList"
    ]
    """<p>The items in the plan execution to return.</p>"""
    next_token: NotRequired["str"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListPlanExecutionsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_arc_region_switch.types.abbreviated_executions_list

        out["items"] = (
            capo_arc_region_switch.types.abbreviated_executions_list.serialize_aws_json_1_0(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListPlanExecutionsResponse:
    out: ListPlanExecutionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_arc_region_switch.types.abbreviated_executions_list

        out["items"] = (
            capo_arc_region_switch.types.abbreviated_executions_list.deserialize_aws_json_1_0(
                data["items"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListPlanExecutionsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_arc_region_switch.types.abbreviated_executions_list

        out["items"] = (
            capo_arc_region_switch.types.abbreviated_executions_list.serialize_cbor(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListPlanExecutionsResponse:
    out: ListPlanExecutionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_arc_region_switch.types.abbreviated_executions_list

        out["items"] = (
            capo_arc_region_switch.types.abbreviated_executions_list.deserialize_cbor(
                data["items"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
