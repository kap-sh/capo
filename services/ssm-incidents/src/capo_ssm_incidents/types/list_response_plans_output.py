"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ListResponsePlansOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_incidents.types.next_token
    import capo_ssm_incidents.types.response_plan_summary_list


class ListResponsePlansOutput(TypedDict, closed=True):
    response_plan_summaries: (
        "capo_ssm_incidents.types.response_plan_summary_list.ResponsePlanSummaryList"
    )
    """<p>Details of each response plan.</p>"""
    next_token: NotRequired["capo_ssm_incidents.types.next_token.NextToken"]
    """<p>The pagination token to use when requesting the next set of items. If there are no additional items to return, the string is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResponsePlansOutput) -> dict:
    out: dict = {}
    import capo_ssm_incidents.types.response_plan_summary_list

    out["responsePlanSummaries"] = (
        capo_ssm_incidents.types.response_plan_summary_list.serialize_json(
            value["response_plan_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResponsePlansOutput:
    out: ListResponsePlansOutput = {}  # type: ignore[typeddict-item]
    if data.get("responsePlanSummaries") is not None:
        import capo_ssm_incidents.types.response_plan_summary_list

        out["response_plan_summaries"] = (
            capo_ssm_incidents.types.response_plan_summary_list.deserialize_json(
                data["responsePlanSummaries"]
            )
        )
    else:
        out["response_plan_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
