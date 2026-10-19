"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RcsFallbackConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.media_url_list
    import capo_pinpoint_sms_voice_v2.types.rcs_fallback_channel
    import capo_pinpoint_sms_voice_v2.types.rcs_fallback_message_body
    import capo_pinpoint_sms_voice_v2.types.rcs_fallback_origination_identity


class RcsFallbackConfiguration(TypedDict, closed=True):
    channel: "capo_pinpoint_sms_voice_v2.types.rcs_fallback_channel.RcsFallbackChannel"
    """<p>The fallback channel to use when RCS delivery fails. Valid values are SMS and MMS. SMS and MMS are mutually exclusive.</p>"""
    message_body: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.rcs_fallback_message_body.RcsFallbackMessageBody"
    ]
    """<p>The text body of the fallback message. Required for SMS fallback. For MMS fallback, at least one of MessageBody or MediaUrls must be provided.</p>"""
    media_urls: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.media_url_list.MediaUrlList"
    ]
    """<p>An array of S3 URIs to media files for MMS fallback. Only valid when Channel is MMS.</p>"""
    origination_identity: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.rcs_fallback_origination_identity.RcsFallbackOriginationIdentity"
    ]
    """<p>The origination identity to use for the fallback message. This can be a PhoneNumber, PhoneNumberId, PhoneNumberArn, SenderId, or SenderIdArn. Pool IDs and pool ARNs are not accepted. If not specified and the original message was sent via a pool, the service selects a suitable number from the pool.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RcsFallbackConfiguration) -> dict:
    out: dict = {}
    out["Channel"] = value["channel"]
    if "message_body" in value:
        out["MessageBody"] = value["message_body"]
    if "media_urls" in value:
        import capo_pinpoint_sms_voice_v2.types.media_url_list

        out["MediaUrls"] = (
            capo_pinpoint_sms_voice_v2.types.media_url_list.serialize_aws_json_1_0(
                value["media_urls"]
            )
        )
    if "origination_identity" in value:
        out["OriginationIdentity"] = value["origination_identity"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RcsFallbackConfiguration:
    out: RcsFallbackConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Channel") is not None:
        out["channel"] = data["Channel"]
    else:
        out["channel"] = ""
    if data.get("MessageBody") is not None:
        out["message_body"] = data["MessageBody"]
    if data.get("MediaUrls") is not None:
        import capo_pinpoint_sms_voice_v2.types.media_url_list

        out["media_urls"] = (
            capo_pinpoint_sms_voice_v2.types.media_url_list.deserialize_aws_json_1_0(
                data["MediaUrls"]
            )
        )
    if data.get("OriginationIdentity") is not None:
        out["origination_identity"] = data["OriginationIdentity"]
    return out
