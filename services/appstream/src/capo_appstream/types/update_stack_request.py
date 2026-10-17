"""Generated from Smithy shape ``com.amazonaws.appstream#UpdateStackRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.access_endpoint_list
    import capo_appstream.types.agent_access_config_for_update
    import capo_appstream.types.application_settings
    import capo_appstream.types.boolean
    import capo_appstream.types.content_redirection
    import capo_appstream.types.description
    import capo_appstream.types.display_name
    import capo_appstream.types.embed_host_domains
    import capo_appstream.types.feedback_url
    import capo_appstream.types.redirect_url
    import capo_appstream.types.stack_attributes
    import capo_appstream.types.storage_connector_list
    import capo_appstream.types.streaming_experience_settings
    import capo_appstream.types.string
    import capo_appstream.types.user_setting_list


class UpdateStackRequest(TypedDict, closed=True):
    display_name: NotRequired["capo_appstream.types.display_name.DisplayName"]
    """<p>The stack name to display.</p>"""
    description: NotRequired["capo_appstream.types.description.Description"]
    """<p>The description to display.</p>"""
    name: NotRequired["capo_appstream.types.string.String"]
    """<p>The name of the stack.</p>"""
    storage_connectors: NotRequired[
        "capo_appstream.types.storage_connector_list.StorageConnectorList"
    ]
    """<p>The storage connectors to enable.</p>"""
    delete_storage_connectors: NotRequired["capo_appstream.types.boolean.Boolean"]
    """<p>Deletes the storage connectors currently enabled for the stack.</p>"""
    redirect_url: NotRequired["capo_appstream.types.redirect_url.RedirectURL"]
    """<p>The URL that users are redirected to after their streaming session ends.</p>"""
    feedback_url: NotRequired["capo_appstream.types.feedback_url.FeedbackURL"]
    """<p>The URL that users are redirected to after they choose the Send Feedback link. If no URL is specified, no Send Feedback link is displayed.</p>"""
    attributes_to_delete: NotRequired[
        "capo_appstream.types.stack_attributes.StackAttributes"
    ]
    """<p>The stack attributes to delete.</p>"""
    user_settings: NotRequired["capo_appstream.types.user_setting_list.UserSettingList"]
    """<p>The actions that are enabled or disabled for users during their streaming sessions. By default, these actions are enabled.</p>"""
    application_settings: NotRequired[
        "capo_appstream.types.application_settings.ApplicationSettings"
    ]
    """<p>The persistent application settings for users of a stack. When these settings are enabled, changes that users make to applications and Windows settings are automatically saved after each session and applied to the next session.</p>"""
    access_endpoints: NotRequired[
        "capo_appstream.types.access_endpoint_list.AccessEndpointList"
    ]
    """<p>The list of interface VPC endpoint (interface endpoint) objects. Users of the stack can connect to WorkSpaces Applications only through the specified endpoints.</p>"""
    embed_host_domains: NotRequired[
        "capo_appstream.types.embed_host_domains.EmbedHostDomains"
    ]
    """<p>The domains where WorkSpaces Applications streaming sessions can be embedded in an iframe. You must approve the domains that you want to host embedded WorkSpaces Applications streaming sessions. </p>"""
    streaming_experience_settings: NotRequired[
        "capo_appstream.types.streaming_experience_settings.StreamingExperienceSettings"
    ]
    """<p>The streaming protocol you want your stack to prefer. This can be UDP or TCP. Currently, UDP is only supported in the Windows native client.</p>"""
    content_redirection: NotRequired[
        "capo_appstream.types.content_redirection.ContentRedirection"
    ]
    agent_access_config: NotRequired[
        "capo_appstream.types.agent_access_config_for_update.AgentAccessConfigForUpdate"
    ]
    """<p>The configuration for agent access on the stack. Specify this to update agent access settings. To remove agent access, use AttributesToDelete with the AGENT_ACCESS_CONFIG value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateStackRequest) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "name" in value:
        out["Name"] = value["name"]
    if "storage_connectors" in value:
        import capo_appstream.types.storage_connector_list

        out["StorageConnectors"] = (
            capo_appstream.types.storage_connector_list.serialize_aws_json_1_1(
                value["storage_connectors"]
            )
        )
    if "delete_storage_connectors" in value:
        out["DeleteStorageConnectors"] = value["delete_storage_connectors"]
    if "redirect_url" in value:
        out["RedirectURL"] = value["redirect_url"]
    if "feedback_url" in value:
        out["FeedbackURL"] = value["feedback_url"]
    if "attributes_to_delete" in value:
        import capo_appstream.types.stack_attributes

        out["AttributesToDelete"] = (
            capo_appstream.types.stack_attributes.serialize_aws_json_1_1(
                value["attributes_to_delete"]
            )
        )
    if "user_settings" in value:
        import capo_appstream.types.user_setting_list

        out["UserSettings"] = (
            capo_appstream.types.user_setting_list.serialize_aws_json_1_1(
                value["user_settings"]
            )
        )
    if "application_settings" in value:
        import capo_appstream.types.application_settings

        out["ApplicationSettings"] = (
            capo_appstream.types.application_settings.serialize_aws_json_1_1(
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
        import capo_appstream.types.agent_access_config_for_update

        out["AgentAccessConfig"] = (
            capo_appstream.types.agent_access_config_for_update.serialize_aws_json_1_1(
                value["agent_access_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateStackRequest:
    out: UpdateStackRequest = {}  # type: ignore[typeddict-item]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("StorageConnectors") is not None:
        import capo_appstream.types.storage_connector_list

        out["storage_connectors"] = (
            capo_appstream.types.storage_connector_list.deserialize_aws_json_1_1(
                data["StorageConnectors"]
            )
        )
    if data.get("DeleteStorageConnectors") is not None:
        out["delete_storage_connectors"] = data["DeleteStorageConnectors"]
    if data.get("RedirectURL") is not None:
        out["redirect_url"] = data["RedirectURL"]
    if data.get("FeedbackURL") is not None:
        out["feedback_url"] = data["FeedbackURL"]
    if data.get("AttributesToDelete") is not None:
        import capo_appstream.types.stack_attributes

        out["attributes_to_delete"] = (
            capo_appstream.types.stack_attributes.deserialize_aws_json_1_1(
                data["AttributesToDelete"]
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
        import capo_appstream.types.application_settings

        out["application_settings"] = (
            capo_appstream.types.application_settings.deserialize_aws_json_1_1(
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
        import capo_appstream.types.agent_access_config_for_update

        out["agent_access_config"] = (
            capo_appstream.types.agent_access_config_for_update.deserialize_aws_json_1_1(
                data["AgentAccessConfig"]
            )
        )
    return out
