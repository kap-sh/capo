"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RcsCarousel``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.rcs_carousel_card_content_list


class RcsCarousel(TypedDict, closed=True):
    card_width: "str"
    """<p>The width of cards in the carousel. Valid values are SMALL and MEDIUM.</p>"""
    card_contents: "capo_pinpoint_sms_voice_v2.types.rcs_carousel_card_content_list.RcsCarouselCardContentList"
    """<p>The list of cards in the carousel. Minimum 2, maximum 10 cards.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RcsCarousel) -> dict:
    out: dict = {}
    out["CardWidth"] = value["card_width"]
    import capo_pinpoint_sms_voice_v2.types.rcs_carousel_card_content_list

    out["CardContents"] = (
        capo_pinpoint_sms_voice_v2.types.rcs_carousel_card_content_list.serialize_aws_json_1_0(
            value["card_contents"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RcsCarousel:
    out: RcsCarousel = {}  # type: ignore[typeddict-item]
    if data.get("CardWidth") is not None:
        out["card_width"] = data["CardWidth"]
    else:
        out["card_width"] = ""
    if data.get("CardContents") is not None:
        import capo_pinpoint_sms_voice_v2.types.rcs_carousel_card_content_list

        out["card_contents"] = (
            capo_pinpoint_sms_voice_v2.types.rcs_carousel_card_content_list.deserialize_aws_json_1_0(
                data["CardContents"]
            )
        )
    else:
        out["card_contents"] = []
    return out
