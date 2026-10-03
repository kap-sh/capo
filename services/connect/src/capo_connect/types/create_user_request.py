"""Generated from Smithy shape ``com.amazonaws.connect#CreateUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.after_contact_work_configs
    import capo_connect.types.agent_username
    import capo_connect.types.auto_accept_configs
    import capo_connect.types.directory_user_id
    import capo_connect.types.hierarchy_group_id
    import capo_connect.types.instance_id
    import capo_connect.types.password
    import capo_connect.types.persistent_connection_configs
    import capo_connect.types.phone_number_configs
    import capo_connect.types.routing_profile_id
    import capo_connect.types.security_profile_ids
    import capo_connect.types.tag_map
    import capo_connect.types.user_identity_info
    import capo_connect.types.user_phone_config
    import capo_connect.types.voice_enhancement_configs


class CreateUserRequest(TypedDict, closed=True):
    username: "capo_connect.types.agent_username.AgentUsername"
    r"""<p>The user name for the account. For instances not using SAML for identity management, the user name can include up to 20 characters. If you are using SAML for identity management, the user name can include up to 64 characters from [a-zA-Z0-9_-.\@]+.</p> <p>Username can include @ only if used in an email format. For example:</p> <ul> <li> <p>Correct: testuser</p> </li> <li> <p>Correct: testuser@example.com</p> </li> <li> <p>Incorrect: testuser@example</p> </li> </ul>"""
    password: NotRequired["capo_connect.types.password.Password"]
    """<p>The password for the user account. A password is required if you are using Connect Customer for identity management. Otherwise, it is an error to include a password.</p>"""
    identity_info: NotRequired["capo_connect.types.user_identity_info.UserIdentityInfo"]
    """<p>The information about the identity of the user.</p>"""
    phone_config: NotRequired["capo_connect.types.user_phone_config.UserPhoneConfig"]
    """<p>The phone settings for the user. This parameter is optional. If not provided, the user can be configured using channel-specific parameters such as <code>AutoAcceptConfigs</code>, <code>AfterContactWorkConfigs</code>, <code>PhoneNumberConfigs</code>, <code>PersistentConnectionConfigs</code>, and <code>VoiceEnhancementConfigs</code>.</p>"""
    directory_user_id: NotRequired[
        "capo_connect.types.directory_user_id.DirectoryUserId"
    ]
    """<p>The identifier of the user account in the directory used for identity management. If Connect Customer cannot access the directory, you can specify this identifier to authenticate users. If you include the identifier, we assume that Connect Customer cannot access the directory. Otherwise, the identity information is used to authenticate users from your directory.</p> <p>This parameter is required if you are using an existing directory for identity management in Connect Customer when Connect Customer cannot access your directory to authenticate users. If you are using SAML for identity management and include this parameter, an error is returned.</p>"""
    security_profile_ids: "capo_connect.types.security_profile_ids.SecurityProfileIds"
    """<p>The identifier of the security profile for the user.</p>"""
    routing_profile_id: "capo_connect.types.routing_profile_id.RoutingProfileId"
    """<p>The identifier of the routing profile for the user.</p>"""
    hierarchy_group_id: NotRequired[
        "capo_connect.types.hierarchy_group_id.HierarchyGroupId"
    ]
    """<p>The identifier of the hierarchy group for the user.</p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
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
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateUserRequest) -> dict:
    out: dict = {}
    out["Username"] = value["username"]
    if "password" in value:
        out["Password"] = value["password"]
    if "identity_info" in value:
        import capo_connect.types.user_identity_info

        out["IdentityInfo"] = capo_connect.types.user_identity_info.serialize_json(
            value["identity_info"]
        )
    if "phone_config" in value:
        import capo_connect.types.user_phone_config

        out["PhoneConfig"] = capo_connect.types.user_phone_config.serialize_json(
            value["phone_config"]
        )
    if "directory_user_id" in value:
        out["DirectoryUserId"] = value["directory_user_id"]
    import capo_connect.types.security_profile_ids

    out["SecurityProfileIds"] = capo_connect.types.security_profile_ids.serialize_json(
        value["security_profile_ids"]
    )
    out["RoutingProfileId"] = value["routing_profile_id"]
    if "hierarchy_group_id" in value:
        out["HierarchyGroupId"] = value["hierarchy_group_id"]
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
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateUserRequest:
    out: CreateUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    else:
        raise DeserializationError("CreateUserRequest.username required")
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    if data.get("IdentityInfo") is not None:
        import capo_connect.types.user_identity_info

        out["identity_info"] = capo_connect.types.user_identity_info.deserialize_json(
            data["IdentityInfo"]
        )
    if data.get("PhoneConfig") is not None:
        import capo_connect.types.user_phone_config

        out["phone_config"] = capo_connect.types.user_phone_config.deserialize_json(
            data["PhoneConfig"]
        )
    if data.get("DirectoryUserId") is not None:
        out["directory_user_id"] = data["DirectoryUserId"]
    if data.get("SecurityProfileIds") is not None:
        import capo_connect.types.security_profile_ids

        out["security_profile_ids"] = (
            capo_connect.types.security_profile_ids.deserialize_json(
                data["SecurityProfileIds"]
            )
        )
    else:
        raise DeserializationError("CreateUserRequest.security_profile_ids required")
    if data.get("RoutingProfileId") is not None:
        out["routing_profile_id"] = data["RoutingProfileId"]
    else:
        raise DeserializationError("CreateUserRequest.routing_profile_id required")
    if data.get("HierarchyGroupId") is not None:
        out["hierarchy_group_id"] = data["HierarchyGroupId"]
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
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
