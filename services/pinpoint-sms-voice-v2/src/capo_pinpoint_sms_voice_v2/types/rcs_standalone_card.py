"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RcsStandaloneCard``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.rcs_card_content


class RcsStandaloneCard(TypedDict, closed=True):
    card_orientation: "str"
    """<p>The orientation of the rich card. Valid values are HORIZONTAL and VERTICAL.</p>"""
    thumbnail_image_alignment: NotRequired["str"]
    """<p>The alignment of the thumbnail image in a horizontal card. Valid values are LEFT and RIGHT. Only applicable when CardOrientation is HORIZONTAL.</p>"""
    card_content: "capo_pinpoint_sms_voice_v2.types.rcs_card_content.RcsCardContent"
    """<p>The content of the rich card, including title, description, media, and card-level suggested actions.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RcsStandaloneCard) -> dict:
    out: dict = {}
    out["CardOrientation"] = value["card_orientation"]
    if "thumbnail_image_alignment" in value:
        out["ThumbnailImageAlignment"] = value["thumbnail_image_alignment"]
    import capo_pinpoint_sms_voice_v2.types.rcs_card_content

    out["CardContent"] = (
        capo_pinpoint_sms_voice_v2.types.rcs_card_content.serialize_aws_json_1_0(
            value["card_content"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RcsStandaloneCard:
    out: RcsStandaloneCard = {}  # type: ignore[typeddict-item]
    if data.get("CardOrientation") is not None:
        out["card_orientation"] = data["CardOrientation"]
    else:
        out["card_orientation"] = ""
    if data.get("ThumbnailImageAlignment") is not None:
        out["thumbnail_image_alignment"] = data["ThumbnailImageAlignment"]
    if data.get("CardContent") is not None:
        import capo_pinpoint_sms_voice_v2.types.rcs_card_content

        out["card_content"] = (
            capo_pinpoint_sms_voice_v2.types.rcs_card_content.deserialize_aws_json_1_0(
                data["CardContent"]
            )
        )
    else:
        raise DeserializationError("RcsStandaloneCard.card_content required")
    return out
