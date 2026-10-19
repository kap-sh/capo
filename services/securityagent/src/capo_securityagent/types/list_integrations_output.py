"""Generated from Smithy shape ``com.amazonaws.securityagent#ListIntegrationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.integration_summary_list
    import capo_securityagent.types.next_token


class ListIntegrationsOutput(TypedDict, closed=True):
    integration_summaries: (
        "capo_securityagent.types.integration_summary_list.IntegrationSummaryList"
    )
    """<p>The list of integration summaries.</p>"""
    next_token: NotRequired["capo_securityagent.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIntegrationsOutput) -> dict:
    out: dict = {}
    import capo_securityagent.types.integration_summary_list

    out["integrationSummaries"] = (
        capo_securityagent.types.integration_summary_list.serialize_json(
            value["integration_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIntegrationsOutput:
    out: ListIntegrationsOutput = {}  # type: ignore[typeddict-item]
    if data.get("integrationSummaries") is not None:
        import capo_securityagent.types.integration_summary_list

        out["integration_summaries"] = (
            capo_securityagent.types.integration_summary_list.deserialize_json(
                data["integrationSummaries"]
            )
        )
    else:
        out["integration_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
