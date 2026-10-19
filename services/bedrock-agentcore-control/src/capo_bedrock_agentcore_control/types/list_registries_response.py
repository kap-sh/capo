"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListRegistriesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.next_token
    import capo_bedrock_agentcore_control.types.registry_summary_list


class ListRegistriesResponse(TypedDict, closed=True):
    registries: (
        "capo_bedrock_agentcore_control.types.registry_summary_list.RegistrySummaryList"
    )
    """<p>The list of registry summaries. For details about the fields in each summary, see the <code>RegistrySummary</code> data type.</p>"""
    next_token: NotRequired["capo_bedrock_agentcore_control.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRegistriesResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.registry_summary_list

    out["registries"] = (
        capo_bedrock_agentcore_control.types.registry_summary_list.serialize_json(
            value["registries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRegistriesResponse:
    out: ListRegistriesResponse = {}  # type: ignore[typeddict-item]
    if data.get("registries") is not None:
        import capo_bedrock_agentcore_control.types.registry_summary_list

        out["registries"] = (
            capo_bedrock_agentcore_control.types.registry_summary_list.deserialize_json(
                data["registries"]
            )
        )
    else:
        out["registries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListRegistriesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "registries" in value:
        import capo_bedrock_agentcore_control.types.registry_summary_list

        out["registries"] = (
            capo_bedrock_agentcore_control.types.registry_summary_list.redact_sensitive(
                value["registries"]
            )
        )
    return out
