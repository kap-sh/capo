"""Generated from Smithy shape ``com.amazonaws.securityagent#ListIntegratedResourcesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.integrated_resource_summary_list
    import capo_securityagent.types.next_token


class ListIntegratedResourcesOutput(TypedDict, closed=True):
    integrated_resource_summaries: "capo_securityagent.types.integrated_resource_summary_list.IntegratedResourceSummaryList"
    """<p>The list of integrated resource summaries.</p>"""
    next_token: NotRequired["capo_securityagent.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIntegratedResourcesOutput) -> dict:
    out: dict = {}
    import capo_securityagent.types.integrated_resource_summary_list

    out["integratedResourceSummaries"] = (
        capo_securityagent.types.integrated_resource_summary_list.serialize_json(
            value["integrated_resource_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIntegratedResourcesOutput:
    out: ListIntegratedResourcesOutput = {}  # type: ignore[typeddict-item]
    if data.get("integratedResourceSummaries") is not None:
        import capo_securityagent.types.integrated_resource_summary_list

        out["integrated_resource_summaries"] = (
            capo_securityagent.types.integrated_resource_summary_list.deserialize_json(
                data["integratedResourceSummaries"]
            )
        )
    else:
        out["integrated_resource_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
