"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateBrowserProfileRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.browser_profile_name
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.description
    import capo_bedrock_agentcore_control.types.tags_map


class CreateBrowserProfileRequest(TypedDict, closed=True):
    name: "capo_bedrock_agentcore_control.types.browser_profile_name.BrowserProfileName"
    """<p>The name of the browser profile. The name must be unique within your account and can contain alphanumeric characters and underscores.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>A description of the browser profile. Use this field to describe the purpose or contents of the profile.</p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request but does not return an error.</p>"""
    tags: NotRequired["capo_bedrock_agentcore_control.types.tags_map.TagsMap"]
    """<p>A map of tag keys and values to assign to the browser profile. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBrowserProfileRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_bedrock_agentcore_control.types.tags_map

        out["tags"] = capo_bedrock_agentcore_control.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateBrowserProfileRequest:
    out: CreateBrowserProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateBrowserProfileRequest.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_bedrock_agentcore_control.types.tags_map

        out["tags"] = capo_bedrock_agentcore_control.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out


def redact_sensitive(value: CreateBrowserProfileRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
