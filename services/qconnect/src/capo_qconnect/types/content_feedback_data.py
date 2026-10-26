"""Generated from Smithy shape ``com.amazonaws.qconnect#ContentFeedbackData``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError
from capo_qconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qconnect.types.generative_content_feedback_data


class _ContentFeedbackData_generativeContentFeedbackData(TypedDict, closed=True):
    generativeContentFeedbackData: "capo_qconnect.types.generative_content_feedback_data.GenerativeContentFeedbackData"


ContentFeedbackData: TypeAlias = (
    _ContentFeedbackData_generativeContentFeedbackData | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ContentFeedbackData) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ContentFeedbackData: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "generativeContentFeedbackData" in value:
        import capo_qconnect.types.generative_content_feedback_data

        return {
            "generativeContentFeedbackData": capo_qconnect.types.generative_content_feedback_data.serialize_json(
                value["generativeContentFeedbackData"]
            )
        }
    else:
        raise SerializationError("ContentFeedbackData: no variant present")


def deserialize_json(data: dict) -> ContentFeedbackData:
    if data.get("generativeContentFeedbackData") is not None:
        import capo_qconnect.types.generative_content_feedback_data

        return {
            "generativeContentFeedbackData": capo_qconnect.types.generative_content_feedback_data.deserialize_json(
                data["generativeContentFeedbackData"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ContentFeedbackData: no recognized variant key")
