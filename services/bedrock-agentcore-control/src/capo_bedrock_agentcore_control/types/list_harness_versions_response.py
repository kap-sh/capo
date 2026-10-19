"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListHarnessVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_version_summaries
    import capo_bedrock_agentcore_control.types.next_token


class ListHarnessVersionsResponse(TypedDict, closed=True):
    harness_versions: "capo_bedrock_agentcore_control.types.harness_version_summaries.HarnessVersionSummaries"
    """<p>The list of harness version summaries.</p>"""
    next_token: NotRequired["capo_bedrock_agentcore_control.types.next_token.NextToken"]
    """<p>The token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListHarnessVersionsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.harness_version_summaries

    out["harnessVersions"] = (
        capo_bedrock_agentcore_control.types.harness_version_summaries.serialize_json(
            value["harness_versions"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListHarnessVersionsResponse:
    out: ListHarnessVersionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("harnessVersions") is not None:
        import capo_bedrock_agentcore_control.types.harness_version_summaries

        out["harness_versions"] = (
            capo_bedrock_agentcore_control.types.harness_version_summaries.deserialize_json(
                data["harnessVersions"]
            )
        )
    else:
        out["harness_versions"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
