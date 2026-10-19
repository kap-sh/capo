"""Generated from Smithy shape ``com.amazonaws.ssmsap#ListSubCheckRuleResultsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_sap.types.max_results
    import capo_ssm_sap.types.next_token
    import capo_ssm_sap.types.sub_check_result_id


class ListSubCheckRuleResultsInput(TypedDict, closed=True):
    sub_check_result_id: "capo_ssm_sap.types.sub_check_result_id.SubCheckResultId"
    """<p>The ID of the sub check result.</p>"""
    max_results: NotRequired["capo_ssm_sap.types.max_results.MaxResults"]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.</p>"""
    next_token: NotRequired["capo_ssm_sap.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSubCheckRuleResultsInput) -> dict:
    out: dict = {}
    out["SubCheckResultId"] = value["sub_check_result_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSubCheckRuleResultsInput:
    out: ListSubCheckRuleResultsInput = {}  # type: ignore[typeddict-item]
    if data.get("SubCheckResultId") is not None:
        out["sub_check_result_id"] = data["SubCheckResultId"]
    else:
        out["sub_check_result_id"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
