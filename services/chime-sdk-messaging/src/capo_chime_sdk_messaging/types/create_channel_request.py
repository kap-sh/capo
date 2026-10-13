"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#CreateChannelRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_messaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_id
    import capo_chime_sdk_messaging.types.channel_member_arns
    import capo_chime_sdk_messaging.types.channel_mode
    import capo_chime_sdk_messaging.types.channel_moderator_arns
    import capo_chime_sdk_messaging.types.channel_privacy
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.client_request_token
    import capo_chime_sdk_messaging.types.elastic_channel_configuration
    import capo_chime_sdk_messaging.types.expiration_settings
    import capo_chime_sdk_messaging.types.metadata
    import capo_chime_sdk_messaging.types.non_empty_resource_name
    import capo_chime_sdk_messaging.types.tag_list


class CreateChannelRequest(TypedDict, closed=True):
    app_instance_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel request.</p>"""
    name: "capo_chime_sdk_messaging.types.non_empty_resource_name.NonEmptyResourceName"
    """<p>The name of the channel.</p>"""
    mode: NotRequired["capo_chime_sdk_messaging.types.channel_mode.ChannelMode"]
    """<p>The channel mode: <code>UNRESTRICTED</code> or <code>RESTRICTED</code>. Administrators, moderators, and channel members can add themselves and other members to unrestricted channels. Only administrators and moderators can add members to restricted channels.</p>"""
    privacy: NotRequired[
        "capo_chime_sdk_messaging.types.channel_privacy.ChannelPrivacy"
    ]
    """<p>The channel's privacy level: <code>PUBLIC</code> or <code>PRIVATE</code>. Private channels aren't discoverable by users outside the channel. Public channels are discoverable by anyone in the <code>AppInstance</code>.</p>"""
    metadata: NotRequired["capo_chime_sdk_messaging.types.metadata.Metadata"]
    """<p>The metadata of the creation request. Limited to 1KB and UTF-8.</p>"""
    client_request_token: (
        "capo_chime_sdk_messaging.types.client_request_token.ClientRequestToken"
    )
    """<p>The client token for the request. An <code>Idempotency</code> token.</p>"""
    tags: NotRequired["capo_chime_sdk_messaging.types.tag_list.TagList"]
    """<p>The tags for the creation request.</p>"""
    chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>"""
    channel_id: NotRequired["capo_chime_sdk_messaging.types.channel_id.ChannelId"]
    """<p>An ID for the channel being created. If you do not specify an ID, a UUID will be created for the channel.</p>"""
    member_arns: NotRequired[
        "capo_chime_sdk_messaging.types.channel_member_arns.ChannelMemberArns"
    ]
    """<p>The ARNs of the channel members in the request.</p>"""
    moderator_arns: NotRequired[
        "capo_chime_sdk_messaging.types.channel_moderator_arns.ChannelModeratorArns"
    ]
    """<p>The ARNs of the channel moderators in the request.</p>"""
    elastic_channel_configuration: NotRequired[
        "capo_chime_sdk_messaging.types.elastic_channel_configuration.ElasticChannelConfiguration"
    ]
    """<p>The attributes required to configure and create an elastic channel. An elastic channel can support a maximum of 1-million users, excluding moderators.</p>"""
    expiration_settings: NotRequired[
        "capo_chime_sdk_messaging.types.expiration_settings.ExpirationSettings"
    ]
    """<p>Settings that control the interval after which the channel is automatically deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChannelRequest) -> dict:
    out: dict = {}
    out["AppInstanceArn"] = value["app_instance_arn"]
    out["Name"] = value["name"]
    if "mode" in value:
        import capo_chime_sdk_messaging.types.channel_mode

        out["Mode"] = capo_chime_sdk_messaging.types.channel_mode.serialize_json(
            value["mode"]
        )
    if "privacy" in value:
        import capo_chime_sdk_messaging.types.channel_privacy

        out["Privacy"] = capo_chime_sdk_messaging.types.channel_privacy.serialize_json(
            value["privacy"]
        )
    if "metadata" in value:
        out["Metadata"] = value["metadata"]
    out["ClientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import capo_chime_sdk_messaging.types.tag_list

        out["Tags"] = capo_chime_sdk_messaging.types.tag_list.serialize_json(
            value["tags"]
        )
    if "channel_id" in value:
        out["ChannelId"] = value["channel_id"]
    if "member_arns" in value:
        import capo_chime_sdk_messaging.types.channel_member_arns

        out["MemberArns"] = (
            capo_chime_sdk_messaging.types.channel_member_arns.serialize_json(
                value["member_arns"]
            )
        )
    if "moderator_arns" in value:
        import capo_chime_sdk_messaging.types.channel_moderator_arns

        out["ModeratorArns"] = (
            capo_chime_sdk_messaging.types.channel_moderator_arns.serialize_json(
                value["moderator_arns"]
            )
        )
    if "elastic_channel_configuration" in value:
        import capo_chime_sdk_messaging.types.elastic_channel_configuration

        out["ElasticChannelConfiguration"] = (
            capo_chime_sdk_messaging.types.elastic_channel_configuration.serialize_json(
                value["elastic_channel_configuration"]
            )
        )
    if "expiration_settings" in value:
        import capo_chime_sdk_messaging.types.expiration_settings

        out["ExpirationSettings"] = (
            capo_chime_sdk_messaging.types.expiration_settings.serialize_json(
                value["expiration_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateChannelRequest:
    out: CreateChannelRequest = {}  # type: ignore[typeddict-item]
    if data.get("AppInstanceArn") is not None:
        out["app_instance_arn"] = data["AppInstanceArn"]
    else:
        raise DeserializationError("CreateChannelRequest.app_instance_arn required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateChannelRequest.name required")
    if data.get("Mode") is not None:
        import capo_chime_sdk_messaging.types.channel_mode

        out["mode"] = capo_chime_sdk_messaging.types.channel_mode.deserialize_json(
            data["Mode"]
        )
    if data.get("Privacy") is not None:
        import capo_chime_sdk_messaging.types.channel_privacy

        out["privacy"] = (
            capo_chime_sdk_messaging.types.channel_privacy.deserialize_json(
                data["Privacy"]
            )
        )
    if data.get("Metadata") is not None:
        out["metadata"] = data["Metadata"]
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    else:
        raise DeserializationError("CreateChannelRequest.client_request_token required")
    if data.get("Tags") is not None:
        import capo_chime_sdk_messaging.types.tag_list

        out["tags"] = capo_chime_sdk_messaging.types.tag_list.deserialize_json(
            data["Tags"]
        )
    if data.get("ChannelId") is not None:
        out["channel_id"] = data["ChannelId"]
    if data.get("MemberArns") is not None:
        import capo_chime_sdk_messaging.types.channel_member_arns

        out["member_arns"] = (
            capo_chime_sdk_messaging.types.channel_member_arns.deserialize_json(
                data["MemberArns"]
            )
        )
    if data.get("ModeratorArns") is not None:
        import capo_chime_sdk_messaging.types.channel_moderator_arns

        out["moderator_arns"] = (
            capo_chime_sdk_messaging.types.channel_moderator_arns.deserialize_json(
                data["ModeratorArns"]
            )
        )
    if data.get("ElasticChannelConfiguration") is not None:
        import capo_chime_sdk_messaging.types.elastic_channel_configuration

        out["elastic_channel_configuration"] = (
            capo_chime_sdk_messaging.types.elastic_channel_configuration.deserialize_json(
                data["ElasticChannelConfiguration"]
            )
        )
    if data.get("ExpirationSettings") is not None:
        import capo_chime_sdk_messaging.types.expiration_settings

        out["expiration_settings"] = (
            capo_chime_sdk_messaging.types.expiration_settings.deserialize_json(
                data["ExpirationSettings"]
            )
        )
    return out


def redact_sensitive(value: CreateChannelRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "metadata" in value:
        out["metadata"] = "*** Sensitive Data Redacted ***"
    if "client_request_token" in value:
        out["client_request_token"] = "*** Sensitive Data Redacted ***"
    if "tags" in value:
        import capo_chime_sdk_messaging.types.tag_list

        out["tags"] = capo_chime_sdk_messaging.types.tag_list.redact_sensitive(
            value["tags"]
        )
    if "channel_id" in value:
        out["channel_id"] = "*** Sensitive Data Redacted ***"
    return out
