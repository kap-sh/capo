"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListCapacityProvidersOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.capacity_provider_list
    import capo_bedrock_agentcore_control.types.next_token


class ListCapacityProvidersOutput(TypedDict, closed=True):
    capacity_providers: "capo_bedrock_agentcore_control.types.capacity_provider_list.CapacityProviderList"
    """<p>The list of capacity provider summaries.</p>"""
    next_token: NotRequired["capo_bedrock_agentcore_control.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCapacityProvidersOutput) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.capacity_provider_list

    out["capacityProviders"] = (
        capo_bedrock_agentcore_control.types.capacity_provider_list.serialize_json(
            value["capacity_providers"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCapacityProvidersOutput:
    out: ListCapacityProvidersOutput = {}  # type: ignore[typeddict-item]
    if data.get("capacityProviders") is not None:
        import capo_bedrock_agentcore_control.types.capacity_provider_list

        out["capacity_providers"] = (
            capo_bedrock_agentcore_control.types.capacity_provider_list.deserialize_json(
                data["capacityProviders"]
            )
        )
    else:
        out["capacity_providers"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
