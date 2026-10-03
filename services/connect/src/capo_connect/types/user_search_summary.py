"""Generated from Smithy shape ``com.amazonaws.connect#UserSearchSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.after_contact_work_configs
    import capo_connect.types.agent_username
    import capo_connect.types.arn
    import capo_connect.types.auto_accept_configs
    import capo_connect.types.directory_user_id
    import capo_connect.types.hierarchy_group_id
    import capo_connect.types.persistent_connection_configs
    import capo_connect.types.phone_number_configs
    import capo_connect.types.routing_profile_id
    import capo_connect.types.security_profile_ids
    import capo_connect.types.tag_map
    import capo_connect.types.user_id
    import capo_connect.types.user_identity_info_lite
    import capo_connect.types.user_phone_config
    import capo_connect.types.voice_enhancement_configs


class UserSearchSummary(TypedDict, closed=True):
    arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the user.</p>"""
    directory_user_id: NotRequired[
        "capo_connect.types.directory_user_id.DirectoryUserId"
    ]
    """<p>The directory identifier of the user.</p>"""
    hierarchy_group_id: NotRequired[
        "capo_connect.types.hierarchy_group_id.HierarchyGroupId"
    ]
    """<p>The identifier of the user's hierarchy group.</p>"""
    id: NotRequired["capo_connect.types.user_id.UserId"]
    """<p>The identifier of the user's summary.</p>"""
    identity_info: NotRequired[
        "capo_connect.types.user_identity_info_lite.UserIdentityInfoLite"
    ]
    """<p>The user's first name and last name.</p>"""
    phone_config: NotRequired["capo_connect.types.user_phone_config.UserPhoneConfig"]
    routing_profile_id: NotRequired[
        "capo_connect.types.routing_profile_id.RoutingProfileId"
    ]
    """<p>The identifier of the user's routing profile.</p>"""
    security_profile_ids: NotRequired[
        "capo_connect.types.security_profile_ids.SecurityProfileIds"
    ]
    """<p>The identifiers of the user's security profiles.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p>"""
    username: NotRequired["capo_connect.types.agent_username.AgentUsername"]
    """<p>The name of the user.</p>"""
    auto_accept_configs: NotRequired[
        "capo_connect.types.auto_accept_configs.AutoAcceptConfigs"
    ]
    """<p>The list of auto-accept configuration settings for each channel.</p>"""
    after_contact_work_configs: NotRequired[
        "capo_connect.types.after_contact_work_configs.AfterContactWorkConfigs"
    ]
    """<p>The list of after contact work (ACW) timeout configuration settings for each channel.</p>"""
    phone_number_configs: NotRequired[
        "capo_connect.types.phone_number_configs.PhoneNumberConfigs"
    ]
    """<p>The list of phone number configuration settings for each channel.</p>"""
    persistent_connection_configs: NotRequired[
        "capo_connect.types.persistent_connection_configs.PersistentConnectionConfigs"
    ]
    """<p>The list of persistent connection configuration settings for each channel.</p>"""
    voice_enhancement_configs: NotRequired[
        "capo_connect.types.voice_enhancement_configs.VoiceEnhancementConfigs"
    ]
    """<p>The list of voice enhancement configuration settings for each channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserSearchSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "directory_user_id" in value:
        out["DirectoryUserId"] = value["directory_user_id"]
    if "hierarchy_group_id" in value:
        out["HierarchyGroupId"] = value["hierarchy_group_id"]
    if "id" in value:
        out["Id"] = value["id"]
    if "identity_info" in value:
        import capo_connect.types.user_identity_info_lite

        out["IdentityInfo"] = capo_connect.types.user_identity_info_lite.serialize_json(
            value["identity_info"]
        )
    if "phone_config" in value:
        import capo_connect.types.user_phone_config

        out["PhoneConfig"] = capo_connect.types.user_phone_config.serialize_json(
            value["phone_config"]
        )
    if "routing_profile_id" in value:
        out["RoutingProfileId"] = value["routing_profile_id"]
    if "security_profile_ids" in value:
        import capo_connect.types.security_profile_ids

        out["SecurityProfileIds"] = (
            capo_connect.types.security_profile_ids.serialize_json(
                value["security_profile_ids"]
            )
        )
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    if "username" in value:
        out["Username"] = value["username"]
    if "auto_accept_configs" in value:
        import capo_connect.types.auto_accept_configs

        out["AutoAcceptConfigs"] = (
            capo_connect.types.auto_accept_configs.serialize_json(
                value["auto_accept_configs"]
            )
        )
    if "after_contact_work_configs" in value:
        import capo_connect.types.after_contact_work_configs

        out["AfterContactWorkConfigs"] = (
            capo_connect.types.after_contact_work_configs.serialize_json(
                value["after_contact_work_configs"]
            )
        )
    if "phone_number_configs" in value:
        import capo_connect.types.phone_number_configs

        out["PhoneNumberConfigs"] = (
            capo_connect.types.phone_number_configs.serialize_json(
                value["phone_number_configs"]
            )
        )
    if "persistent_connection_configs" in value:
        import capo_connect.types.persistent_connection_configs

        out["PersistentConnectionConfigs"] = (
            capo_connect.types.persistent_connection_configs.serialize_json(
                value["persistent_connection_configs"]
            )
        )
    if "voice_enhancement_configs" in value:
        import capo_connect.types.voice_enhancement_configs

        out["VoiceEnhancementConfigs"] = (
            capo_connect.types.voice_enhancement_configs.serialize_json(
                value["voice_enhancement_configs"]
            )
        )
    return out


def deserialize_json(data: dict) -> UserSearchSummary:
    out: UserSearchSummary = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("DirectoryUserId") is not None:
        out["directory_user_id"] = data["DirectoryUserId"]
    if data.get("HierarchyGroupId") is not None:
        out["hierarchy_group_id"] = data["HierarchyGroupId"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("IdentityInfo") is not None:
        import capo_connect.types.user_identity_info_lite

        out["identity_info"] = (
            capo_connect.types.user_identity_info_lite.deserialize_json(
                data["IdentityInfo"]
            )
        )
    if data.get("PhoneConfig") is not None:
        import capo_connect.types.user_phone_config

        out["phone_config"] = capo_connect.types.user_phone_config.deserialize_json(
            data["PhoneConfig"]
        )
    if data.get("RoutingProfileId") is not None:
        out["routing_profile_id"] = data["RoutingProfileId"]
    if data.get("SecurityProfileIds") is not None:
        import capo_connect.types.security_profile_ids

        out["security_profile_ids"] = (
            capo_connect.types.security_profile_ids.deserialize_json(
                data["SecurityProfileIds"]
            )
        )
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    if data.get("AutoAcceptConfigs") is not None:
        import capo_connect.types.auto_accept_configs

        out["auto_accept_configs"] = (
            capo_connect.types.auto_accept_configs.deserialize_json(
                data["AutoAcceptConfigs"]
            )
        )
    if data.get("AfterContactWorkConfigs") is not None:
        import capo_connect.types.after_contact_work_configs

        out["after_contact_work_configs"] = (
            capo_connect.types.after_contact_work_configs.deserialize_json(
                data["AfterContactWorkConfigs"]
            )
        )
    if data.get("PhoneNumberConfigs") is not None:
        import capo_connect.types.phone_number_configs

        out["phone_number_configs"] = (
            capo_connect.types.phone_number_configs.deserialize_json(
                data["PhoneNumberConfigs"]
            )
        )
    if data.get("PersistentConnectionConfigs") is not None:
        import capo_connect.types.persistent_connection_configs

        out["persistent_connection_configs"] = (
            capo_connect.types.persistent_connection_configs.deserialize_json(
                data["PersistentConnectionConfigs"]
            )
        )
    if data.get("VoiceEnhancementConfigs") is not None:
        import capo_connect.types.voice_enhancement_configs

        out["voice_enhancement_configs"] = (
            capo_connect.types.voice_enhancement_configs.deserialize_json(
                data["VoiceEnhancementConfigs"]
            )
        )
    return out
