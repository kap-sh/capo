"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#ListAutomationRulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.filter_list
    import capo_compute_optimizer_automation.types.next_token


class ListAutomationRulesRequest(TypedDict, closed=True):
    filters: NotRequired[
        "capo_compute_optimizer_automation.types.filter_list.FilterList"
    ]
    """<p> The filters to apply to the list of automation rules. </p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of automation rules to return in a single response. Valid range is 1-1000.</p>"""
    next_token: NotRequired[
        "capo_compute_optimizer_automation.types.next_token.NextToken"
    ]
    """<p>A token used for pagination to retrieve the next set of results when the response is truncated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutomationRulesRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_compute_optimizer_automation.types.filter_list

        out["filters"] = (
            capo_compute_optimizer_automation.types.filter_list.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutomationRulesRequest:
    out: ListAutomationRulesRequest = {}  # type: ignore[typeddict-item]
    if data.get("filters") is not None:
        import capo_compute_optimizer_automation.types.filter_list

        out["filters"] = (
            capo_compute_optimizer_automation.types.filter_list.deserialize_aws_json_1_0(
                data["filters"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListAutomationRulesRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_compute_optimizer_automation.types.filter_list

        out["filters"] = (
            capo_compute_optimizer_automation.types.filter_list.serialize_cbor(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListAutomationRulesRequest:
    out: ListAutomationRulesRequest = {}  # type: ignore[typeddict-item]
    if data.get("filters") is not None:
        import capo_compute_optimizer_automation.types.filter_list

        out["filters"] = (
            capo_compute_optimizer_automation.types.filter_list.deserialize_cbor(
                data["filters"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
