"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListHarnessesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_summaries
    import capo_bedrock_agentcore_control.types.next_token


class ListHarnessesResponse(TypedDict, closed=True):
    harnesses: "capo_bedrock_agentcore_control.types.harness_summaries.HarnessSummaries"
    """<p>The list of harness summaries.</p>"""
    next_token: NotRequired["capo_bedrock_agentcore_control.types.next_token.NextToken"]
    """<p>The token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListHarnessesResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.harness_summaries

    out["harnesses"] = (
        capo_bedrock_agentcore_control.types.harness_summaries.serialize_json(
            value["harnesses"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListHarnessesResponse:
    out: ListHarnessesResponse = {}  # type: ignore[typeddict-item]
    if data.get("harnesses") is not None:
        import capo_bedrock_agentcore_control.types.harness_summaries

        out["harnesses"] = (
            capo_bedrock_agentcore_control.types.harness_summaries.deserialize_json(
                data["harnesses"]
            )
        )
    else:
        out["harnesses"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
