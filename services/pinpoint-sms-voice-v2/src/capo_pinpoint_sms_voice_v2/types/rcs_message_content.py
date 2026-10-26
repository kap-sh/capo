"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RcsMessageContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.rcs_content
    import capo_pinpoint_sms_voice_v2.types.rcs_suggested_action_list


class RcsMessageContent(TypedDict, closed=True):
    content: "capo_pinpoint_sms_voice_v2.types.rcs_content.RcsContent"
    """<p>The content of the RCS message. Exactly one content type must be specified: TextMessage, FileMessage, RichCard, or Carousel.</p>"""
    suggestions: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.rcs_suggested_action_list.RcsSuggestedActionList"
    ]
    """<p>Message-level suggested actions displayed to the recipient. Maximum 11 suggestions per message.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RcsMessageContent) -> dict:
    out: dict = {}
    import capo_pinpoint_sms_voice_v2.types.rcs_content

    out["Content"] = (
        capo_pinpoint_sms_voice_v2.types.rcs_content.serialize_aws_json_1_0(
            value["content"]
        )
    )
    if "suggestions" in value:
        import capo_pinpoint_sms_voice_v2.types.rcs_suggested_action_list

        out["Suggestions"] = (
            capo_pinpoint_sms_voice_v2.types.rcs_suggested_action_list.serialize_aws_json_1_0(
                value["suggestions"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RcsMessageContent:
    out: RcsMessageContent = {}  # type: ignore[typeddict-item]
    if data.get("Content") is not None:
        import capo_pinpoint_sms_voice_v2.types.rcs_content

        out["content"] = (
            capo_pinpoint_sms_voice_v2.types.rcs_content.deserialize_aws_json_1_0(
                data["Content"]
            )
        )
    else:
        out["content"] = {"$unknown": {"name": ""}}
    if data.get("Suggestions") is not None:
        import capo_pinpoint_sms_voice_v2.types.rcs_suggested_action_list

        out["suggestions"] = (
            capo_pinpoint_sms_voice_v2.types.rcs_suggested_action_list.deserialize_aws_json_1_0(
                data["Suggestions"]
            )
        )
    return out
