"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ApiGatewayToolFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.rest_api_methods


class ApiGatewayToolFilter(TypedDict, closed=True):
    filter_path: "str"
    """<p>Resource path to match in the REST API. Supports exact paths (for example, <code>/pets</code>) or wildcard paths (for example, <code>/pets/*</code> to match all paths under <code>/pets</code>). Must match existing paths in the REST API.</p>"""
    methods: "capo_bedrock_agentcore_control.types.rest_api_methods.RestApiMethods"
    """<p>The methods to filter for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApiGatewayToolFilter) -> dict:
    out: dict = {}
    out["filterPath"] = value["filter_path"]
    import capo_bedrock_agentcore_control.types.rest_api_methods

    out["methods"] = (
        capo_bedrock_agentcore_control.types.rest_api_methods.serialize_json(
            value["methods"]
        )
    )
    return out


def deserialize_json(data: dict) -> ApiGatewayToolFilter:
    out: ApiGatewayToolFilter = {}  # type: ignore[typeddict-item]
    if data.get("filterPath") is not None:
        out["filter_path"] = data["filterPath"]
    else:
        out["filter_path"] = ""
    if data.get("methods") is not None:
        import capo_bedrock_agentcore_control.types.rest_api_methods

        out["methods"] = (
            capo_bedrock_agentcore_control.types.rest_api_methods.deserialize_json(
                data["methods"]
            )
        )
    else:
        out["methods"] = []
    return out
