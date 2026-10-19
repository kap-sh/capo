"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RcsContent``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError, SerializationError
from capo_pinpoint_sms_voice_v2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.rcs_carousel
    import capo_pinpoint_sms_voice_v2.types.rcs_file_message
    import capo_pinpoint_sms_voice_v2.types.rcs_standalone_card
    import capo_pinpoint_sms_voice_v2.types.rcs_text_message


class _RcsContent_TextMessage(TypedDict, closed=True):
    TextMessage: "capo_pinpoint_sms_voice_v2.types.rcs_text_message.RcsTextMessage"


class _RcsContent_FileMessage(TypedDict, closed=True):
    FileMessage: "capo_pinpoint_sms_voice_v2.types.rcs_file_message.RcsFileMessage"


class _RcsContent_RichCard(TypedDict, closed=True):
    RichCard: "capo_pinpoint_sms_voice_v2.types.rcs_standalone_card.RcsStandaloneCard"


class _RcsContent_Carousel(TypedDict, closed=True):
    Carousel: "capo_pinpoint_sms_voice_v2.types.rcs_carousel.RcsCarousel"


RcsContent: TypeAlias = (
    _RcsContent_TextMessage
    | _RcsContent_FileMessage
    | _RcsContent_RichCard
    | _RcsContent_Carousel
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RcsContent) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"RcsContent: cannot serialize unknown variant {value.name!r}"
        )
    elif "TextMessage" in value:
        import capo_pinpoint_sms_voice_v2.types.rcs_text_message

        return {
            "TextMessage": capo_pinpoint_sms_voice_v2.types.rcs_text_message.serialize_aws_json_1_0(
                value["TextMessage"]
            )
        }
    elif "FileMessage" in value:
        import capo_pinpoint_sms_voice_v2.types.rcs_file_message

        return {
            "FileMessage": capo_pinpoint_sms_voice_v2.types.rcs_file_message.serialize_aws_json_1_0(
                value["FileMessage"]
            )
        }
    elif "RichCard" in value:
        import capo_pinpoint_sms_voice_v2.types.rcs_standalone_card

        return {
            "RichCard": capo_pinpoint_sms_voice_v2.types.rcs_standalone_card.serialize_aws_json_1_0(
                value["RichCard"]
            )
        }
    elif "Carousel" in value:
        import capo_pinpoint_sms_voice_v2.types.rcs_carousel

        return {
            "Carousel": capo_pinpoint_sms_voice_v2.types.rcs_carousel.serialize_aws_json_1_0(
                value["Carousel"]
            )
        }
    else:
        raise SerializationError("RcsContent: no variant present")


def deserialize_aws_json_1_0(data: dict) -> RcsContent:
    if data.get("TextMessage") is not None:
        import capo_pinpoint_sms_voice_v2.types.rcs_text_message

        return {
            "TextMessage": capo_pinpoint_sms_voice_v2.types.rcs_text_message.deserialize_aws_json_1_0(
                data["TextMessage"]
            )
        }
    elif data.get("FileMessage") is not None:
        import capo_pinpoint_sms_voice_v2.types.rcs_file_message

        return {
            "FileMessage": capo_pinpoint_sms_voice_v2.types.rcs_file_message.deserialize_aws_json_1_0(
                data["FileMessage"]
            )
        }
    elif data.get("RichCard") is not None:
        import capo_pinpoint_sms_voice_v2.types.rcs_standalone_card

        return {
            "RichCard": capo_pinpoint_sms_voice_v2.types.rcs_standalone_card.deserialize_aws_json_1_0(
                data["RichCard"]
            )
        }
    elif data.get("Carousel") is not None:
        import capo_pinpoint_sms_voice_v2.types.rcs_carousel

        return {
            "Carousel": capo_pinpoint_sms_voice_v2.types.rcs_carousel.deserialize_aws_json_1_0(
                data["Carousel"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("RcsContent: no recognized variant key")
