"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ApiGatewayToolOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.rest_api_method


class ApiGatewayToolOverride(TypedDict, closed=True):
    name: "str"
    """<p>The name of tool. Identifies the tool in the Model Context Protocol.</p>"""
    description: NotRequired["str"]
    """<p>The description of the tool. Provides information about the purpose and usage of the tool. If not provided, uses the description from the API's OpenAPI specification.</p>"""
    path: "str"
    """<p>Resource path in the REST API (e.g., <code>/pets</code>). Must explicitly match an existing path in the REST API.</p>"""
    method: "capo_bedrock_agentcore_control.types.rest_api_method.RestApiMethod"
    """<p>The HTTP method to expose for the specified path.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApiGatewayToolOverride) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["path"] = value["path"]
    import capo_bedrock_agentcore_control.types.rest_api_method

    out["method"] = capo_bedrock_agentcore_control.types.rest_api_method.serialize_json(
        value["method"]
    )
    return out


def deserialize_json(data: dict) -> ApiGatewayToolOverride:
    out: ApiGatewayToolOverride = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("path") is not None:
        out["path"] = data["path"]
    else:
        out["path"] = ""
    if data.get("method") is not None:
        import capo_bedrock_agentcore_control.types.rest_api_method

        out["method"] = (
            capo_bedrock_agentcore_control.types.rest_api_method.deserialize_json(
                data["method"]
            )
        )
    else:
        import typing

        out["method"] = typing.cast(
            "capo_bedrock_agentcore_control.types.rest_api_method.RestApiMethod", ""
        )
    return out
