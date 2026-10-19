"""Generated from Smithy shape ``com.amazonaws.inspector#PreviewAgentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.agent_preview_list
    import capo_inspector.types.pagination_token


class PreviewAgentsResponse(TypedDict, closed=True):
    agent_previews: "capo_inspector.types.agent_preview_list.AgentPreviewList"
    """<p>The resulting list of agents.</p>"""
    next_token: NotRequired["capo_inspector.types.pagination_token.PaginationToken"]
    """<p> When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the <b>nextToken</b> parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PreviewAgentsResponse) -> dict:
    out: dict = {}
    import capo_inspector.types.agent_preview_list

    out["agentPreviews"] = (
        capo_inspector.types.agent_preview_list.serialize_aws_json_1_1(
            value["agent_previews"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PreviewAgentsResponse:
    out: PreviewAgentsResponse = {}  # type: ignore[typeddict-item]
    if data.get("agentPreviews") is not None:
        import capo_inspector.types.agent_preview_list

        out["agent_previews"] = (
            capo_inspector.types.agent_preview_list.deserialize_aws_json_1_1(
                data["agentPreviews"]
            )
        )
    else:
        out["agent_previews"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
