"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreateChatResponseConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.display_name
    import capo_qbusiness.types.response_configurations
    import capo_qbusiness.types.string
    import capo_qbusiness.types.tags


class CreateChatResponseConfigurationRequest(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The unique identifier of the Amazon Q Business application for which to create the new chat response configuration.</p>"""
    display_name: "capo_qbusiness.types.display_name.DisplayName"
    """<p>A human-readable name for the new chat response configuration, making it easier to identify and manage among multiple configurations.</p>"""
    client_token: NotRequired["capo_qbusiness.types.string.String"]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request. This helps prevent the same configuration from being created multiple times if retries occur.</p>"""
    response_configurations: (
        "capo_qbusiness.types.response_configurations.ResponseConfigurations"
    )
    """<p>A collection of response configuration settings that define how Amazon Q Business will generate and format responses to user queries in chat interactions.</p>"""
    tags: NotRequired["capo_qbusiness.types.tags.Tags"]
    """<p>A list of key-value pairs to apply as tags to the new chat response configuration, enabling categorization and management of resources across Amazon Web Services services.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChatResponseConfigurationRequest) -> dict:
    out: dict = {}
    out["displayName"] = value["display_name"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import capo_qbusiness.types.response_configurations

    out["responseConfigurations"] = (
        capo_qbusiness.types.response_configurations.serialize_json(
            value["response_configurations"]
        )
    )
    if "tags" in value:
        import capo_qbusiness.types.tags

        out["tags"] = capo_qbusiness.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateChatResponseConfigurationRequest:
    out: CreateChatResponseConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("responseConfigurations") is not None:
        import capo_qbusiness.types.response_configurations

        out["response_configurations"] = (
            capo_qbusiness.types.response_configurations.deserialize_json(
                data["responseConfigurations"]
            )
        )
    else:
        out["response_configurations"] = {}
    if data.get("tags") is not None:
        import capo_qbusiness.types.tags

        out["tags"] = capo_qbusiness.types.tags.deserialize_json(data["tags"])
    return out
