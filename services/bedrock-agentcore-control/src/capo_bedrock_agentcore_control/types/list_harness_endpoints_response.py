"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListHarnessEndpointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_endpoints
    import capo_bedrock_agentcore_control.types.next_token


class ListHarnessEndpointsResponse(TypedDict, closed=True):
    endpoints: "capo_bedrock_agentcore_control.types.harness_endpoints.HarnessEndpoints"
    """<p>The list of harness endpoints.</p>"""
    next_token: NotRequired["capo_bedrock_agentcore_control.types.next_token.NextToken"]
    """<p>The token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListHarnessEndpointsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.harness_endpoints

    out["endpoints"] = (
        capo_bedrock_agentcore_control.types.harness_endpoints.serialize_json(
            value["endpoints"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListHarnessEndpointsResponse:
    out: ListHarnessEndpointsResponse = {}  # type: ignore[typeddict-item]
    if data.get("endpoints") is not None:
        import capo_bedrock_agentcore_control.types.harness_endpoints

        out["endpoints"] = (
            capo_bedrock_agentcore_control.types.harness_endpoints.deserialize_json(
                data["endpoints"]
            )
        )
    else:
        out["endpoints"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
