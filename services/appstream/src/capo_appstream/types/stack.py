"""Generated from Smithy shape ``com.amazonaws.appstream#Stack``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.access_endpoint_list
    import capo_appstream.types.agent_access_config
    import capo_appstream.types.application_settings_response
    import capo_appstream.types.arn
    import capo_appstream.types.content_redirection
    import capo_appstream.types.embed_host_domains
    import capo_appstream.types.feedback_url
    import capo_appstream.types.redirect_url
    import capo_appstream.types.stack_errors
    import capo_appstream.types.storage_connector_list
    import capo_appstream.types.streaming_experience_settings
    import capo_appstream.types.string
    import capo_appstream.types.timestamp
    import capo_appstream.types.user_setting_list


class Stack(TypedDict, closed=True):
    arn: NotRequired["capo_appstream.types.arn.Arn"]
    """<p>The ARN of the stack.</p>"""
    name: NotRequired["capo_appstream.types.string.String"]
    """<p>The name of the stack.</p>"""
    description: NotRequired["capo_appstream.types.string.String"]
    """<p>The description to display.</p>"""
    display_name: NotRequired["capo_appstream.types.string.String"]
    """<p>The stack name to display.</p>"""
    created_time: NotRequired["capo_appstream.types.timestamp.Timestamp"]
    """<p>The time the stack was created.</p>"""
    storage_connectors: NotRequired[
        "capo_appstream.types.storage_connector_list.StorageConnectorList"
    ]
    """<p>The storage connectors to enable.</p>"""
    redirect_url: NotRequired["capo_appstream.types.redirect_url.RedirectURL"]
    """<p>The URL that users are redirected to after their streaming session ends.</p>"""
    feedback_url: NotRequired["capo_appstream.types.feedback_url.FeedbackURL"]
    """<p>The URL that users are redirected to after they click the Send Feedback link. If no URL is specified, no Send Feedback link is displayed.</p>"""
    stack_errors: NotRequired["capo_appstream.types.stack_errors.StackErrors"]
    """<p>The errors for the stack.</p>"""
    user_settings: NotRequired["capo_appstream.types.user_setting_list.UserSettingList"]
    """<p>The actions that are enabled or disabled for users during their streaming sessions. By default these actions are enabled.</p>"""
    application_settings: NotRequired[
        "capo_appstream.types.application_settings_response.ApplicationSettingsResponse"
    ]
    """<p>The persistent application settings for users of the stack.</p>"""
    access_endpoints: NotRequired[
        "capo_appstream.types.access_endpoint_list.AccessEndpointList"
    ]
    """<p>The list of virtual private cloud (VPC) interface endpoint objects. Users of the stack can connect to WorkSpaces Applications only through the specified endpoints. </p>"""
    embed_host_domains: NotRequired[
        "capo_appstream.types.embed_host_domains.EmbedHostDomains"
    ]
    """<p>The domains where WorkSpaces Applications streaming sessions can be embedded in an iframe. You must approve the domains that you want to host embedded WorkSpaces Applications streaming sessions.</p>"""
    streaming_experience_settings: NotRequired[
        "capo_appstream.types.streaming_experience_settings.StreamingExperienceSettings"
    ]
    """<p>The streaming protocol you want your stack to prefer. This can be UDP or TCP. Currently, UDP is only supported in the Windows native client.</p>"""
    content_redirection: NotRequired[
        "capo_appstream.types.content_redirection.ContentRedirection"
    ]
    """<p>Configuration for bidirectional URL redirection between the streaming session and the local client. Use HostToClient to redirect URLs from the remote desktop to the local browser.</p>"""
    agent_access_config: NotRequired[
        "capo_appstream.types.agent_access_config.AgentAccessConfig"
    ]
    """<p>The agent access configuration of the stack, if agent access is enabled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Stack) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "created_time" in value:
        import capo_appstream.types.timestamp

        out["CreatedTime"] = capo_appstream.types.timestamp.serialize_aws_json_1_1(
            value["created_time"]
        )
    if "storage_connectors" in value:
        import capo_appstream.types.storage_connector_list

        out["StorageConnectors"] = (
            capo_appstream.types.storage_connector_list.serialize_aws_json_1_1(
                value["storage_connectors"]
            )
        )
    if "redirect_url" in value:
        out["RedirectURL"] = value["redirect_url"]
    if "feedback_url" in value:
        out["FeedbackURL"] = value["feedback_url"]
    if "stack_errors" in value:
        import capo_appstream.types.stack_errors

        out["StackErrors"] = capo_appstream.types.stack_errors.serialize_aws_json_1_1(
            value["stack_errors"]
        )
    if "user_settings" in value:
        import capo_appstream.types.user_setting_list

        out["UserSettings"] = (
            capo_appstream.types.user_setting_list.serialize_aws_json_1_1(
                value["user_settings"]
            )
        )
    if "application_settings" in value:
        import capo_appstream.types.application_settings_response

        out["ApplicationSettings"] = (
            capo_appstream.types.application_settings_response.serialize_aws_json_1_1(
                value["application_settings"]
            )
        )
    if "access_endpoints" in value:
        import capo_appstream.types.access_endpoint_list

        out["AccessEndpoints"] = (
            capo_appstream.types.access_endpoint_list.serialize_aws_json_1_1(
                value["access_endpoints"]
            )
        )
    if "embed_host_domains" in value:
        import capo_appstream.types.embed_host_domains

        out["EmbedHostDomains"] = (
            capo_appstream.types.embed_host_domains.serialize_aws_json_1_1(
                value["embed_host_domains"]
            )
        )
    if "streaming_experience_settings" in value:
        import capo_appstream.types.streaming_experience_settings

        out["StreamingExperienceSettings"] = (
            capo_appstream.types.streaming_experience_settings.serialize_aws_json_1_1(
                value["streaming_experience_settings"]
            )
        )
    if "content_redirection" in value:
        import capo_appstream.types.content_redirection

        out["ContentRedirection"] = (
            capo_appstream.types.content_redirection.serialize_aws_json_1_1(
                value["content_redirection"]
            )
        )
    if "agent_access_config" in value:
        import capo_appstream.types.agent_access_config

        out["AgentAccessConfig"] = (
            capo_appstream.types.agent_access_config.serialize_aws_json_1_1(
                value["agent_access_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Stack:
    out: Stack = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("CreatedTime") is not None:
        import capo_appstream.types.timestamp

        out["created_time"] = capo_appstream.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedTime"]
        )
    if data.get("StorageConnectors") is not None:
        import capo_appstream.types.storage_connector_list

        out["storage_connectors"] = (
            capo_appstream.types.storage_connector_list.deserialize_aws_json_1_1(
                data["StorageConnectors"]
            )
        )
    if data.get("RedirectURL") is not None:
        out["redirect_url"] = data["RedirectURL"]
    if data.get("FeedbackURL") is not None:
        out["feedback_url"] = data["FeedbackURL"]
    if data.get("StackErrors") is not None:
        import capo_appstream.types.stack_errors

        out["stack_errors"] = (
            capo_appstream.types.stack_errors.deserialize_aws_json_1_1(
                data["StackErrors"]
            )
        )
    if data.get("UserSettings") is not None:
        import capo_appstream.types.user_setting_list

        out["user_settings"] = (
            capo_appstream.types.user_setting_list.deserialize_aws_json_1_1(
                data["UserSettings"]
            )
        )
    if data.get("ApplicationSettings") is not None:
        import capo_appstream.types.application_settings_response

        out["application_settings"] = (
            capo_appstream.types.application_settings_response.deserialize_aws_json_1_1(
                data["ApplicationSettings"]
            )
        )
    if data.get("AccessEndpoints") is not None:
        import capo_appstream.types.access_endpoint_list

        out["access_endpoints"] = (
            capo_appstream.types.access_endpoint_list.deserialize_aws_json_1_1(
                data["AccessEndpoints"]
            )
        )
    if data.get("EmbedHostDomains") is not None:
        import capo_appstream.types.embed_host_domains

        out["embed_host_domains"] = (
            capo_appstream.types.embed_host_domains.deserialize_aws_json_1_1(
                data["EmbedHostDomains"]
            )
        )
    if data.get("StreamingExperienceSettings") is not None:
        import capo_appstream.types.streaming_experience_settings

        out["streaming_experience_settings"] = (
            capo_appstream.types.streaming_experience_settings.deserialize_aws_json_1_1(
                data["StreamingExperienceSettings"]
            )
        )
    if data.get("ContentRedirection") is not None:
        import capo_appstream.types.content_redirection

        out["content_redirection"] = (
            capo_appstream.types.content_redirection.deserialize_aws_json_1_1(
                data["ContentRedirection"]
            )
        )
    if data.get("AgentAccessConfig") is not None:
        import capo_appstream.types.agent_access_config

        out["agent_access_config"] = (
            capo_appstream.types.agent_access_config.deserialize_aws_json_1_1(
                data["AgentAccessConfig"]
            )
        )
    return out
