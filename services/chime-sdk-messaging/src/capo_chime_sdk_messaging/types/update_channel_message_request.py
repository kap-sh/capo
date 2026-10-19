"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#UpdateChannelMessageRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.content_type
    import capo_chime_sdk_messaging.types.message_id
    import capo_chime_sdk_messaging.types.metadata
    import capo_chime_sdk_messaging.types.non_empty_content
    import capo_chime_sdk_messaging.types.sub_channel_id


class UpdateChannelMessageRequest(TypedDict, closed=True):
    channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel.</p>"""
    message_id: "capo_chime_sdk_messaging.types.message_id.MessageId"
    """<p>The ID string of the message being updated.</p>"""
    content: "capo_chime_sdk_messaging.types.non_empty_content.NonEmptyContent"
    """<p>The content of the channel message. </p>"""
    metadata: NotRequired["capo_chime_sdk_messaging.types.metadata.Metadata"]
    """<p>The metadata of the message being updated.</p>"""
    chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>"""
    sub_channel_id: NotRequired[
        "capo_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
    ]
    """<p>The ID of the SubChannel in the request.</p> <note> <p>Only required when updating messages in a SubChannel that the user belongs to.</p> </note>"""
    content_type: NotRequired["capo_chime_sdk_messaging.types.content_type.ContentType"]
    """<p>The content type of the channel message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChannelMessageRequest) -> dict:
    out: dict = {}
    out["Content"] = value["content"]
    if "metadata" in value:
        out["Metadata"] = value["metadata"]
    if "sub_channel_id" in value:
        out["SubChannelId"] = value["sub_channel_id"]
    if "content_type" in value:
        out["ContentType"] = value["content_type"]
    return out


def deserialize_json(data: dict) -> UpdateChannelMessageRequest:
    out: UpdateChannelMessageRequest = {}  # type: ignore[typeddict-item]
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    else:
        out["content"] = ""
    if data.get("Metadata") is not None:
        out["metadata"] = data["Metadata"]
    if data.get("SubChannelId") is not None:
        out["sub_channel_id"] = data["SubChannelId"]
    if data.get("ContentType") is not None:
        out["content_type"] = data["ContentType"]
    return out


def redact_sensitive(value: UpdateChannelMessageRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        out["content"] = "*** Sensitive Data Redacted ***"
    if "metadata" in value:
        out["metadata"] = "*** Sensitive Data Redacted ***"
    if "content_type" in value:
        out["content_type"] = "*** Sensitive Data Redacted ***"
    return out
