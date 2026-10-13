"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#ListResourceRequestsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudcontrol.types.next_token
    import capo_cloudcontrol.types.resource_request_status_summaries


class ListResourceRequestsOutput(TypedDict, closed=True):
    resource_request_status_summaries: NotRequired[
        "capo_cloudcontrol.types.resource_request_status_summaries.ResourceRequestStatusSummaries"
    ]
    """<p>The requests that match the specified filter criteria.</p>"""
    next_token: NotRequired["capo_cloudcontrol.types.next_token.NextToken"]
    """<p>If the request doesn't return all of the remaining results, <code>NextToken</code> is set to a token. To retrieve the next set of results, call <code>ListResources</code> again and assign that token to the request object's <code>NextToken</code> parameter. If the request returns all results, <code>NextToken</code> is set to null.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListResourceRequestsOutput) -> dict:
    out: dict = {}
    if "resource_request_status_summaries" in value:
        import capo_cloudcontrol.types.resource_request_status_summaries

        out["ResourceRequestStatusSummaries"] = (
            capo_cloudcontrol.types.resource_request_status_summaries.serialize_aws_json_1_0(
                value["resource_request_status_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListResourceRequestsOutput:
    out: ListResourceRequestsOutput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceRequestStatusSummaries") is not None:
        import capo_cloudcontrol.types.resource_request_status_summaries

        out["resource_request_status_summaries"] = (
            capo_cloudcontrol.types.resource_request_status_summaries.deserialize_aws_json_1_0(
                data["ResourceRequestStatusSummaries"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListResourceRequestsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "resource_request_status_summaries" in value:
        import capo_cloudcontrol.types.resource_request_status_summaries

        out["resource_request_status_summaries"] = (
            capo_cloudcontrol.types.resource_request_status_summaries.redact_sensitive(
                value["resource_request_status_summaries"]
            )
        )
    return out
