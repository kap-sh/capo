"""Generated from Smithy shape ``com.amazonaws.translate#DetectedLanguageLowConfidenceException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_translate.errors import ServiceError

if TYPE_CHECKING:
    import capo_translate.types.language_code_string
    import capo_translate.types.string


class DetectedLanguageLowConfidenceException_(TypedDict, closed=True):
    message: NotRequired["capo_translate.types.string.String"]
    detected_language_code: NotRequired[
        "capo_translate.types.language_code_string.LanguageCodeString"
    ]
    """<p>The language code of the auto-detected language from Amazon Comprehend.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectedLanguageLowConfidenceException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "detected_language_code" in value:
        out["DetectedLanguageCode"] = value["detected_language_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectedLanguageLowConfidenceException_:
    out: DetectedLanguageLowConfidenceException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("DetectedLanguageCode") is not None:
        out["detected_language_code"] = data["DetectedLanguageCode"]
    return out


class DetectedLanguageLowConfidenceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.translate#DetectedLanguageLowConfidenceException``."""

    code: str | None = "DetectedLanguageLowConfidenceException"

    def __init__(
        self,
        data: DetectedLanguageLowConfidenceException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DetectedLanguageLowConfidenceException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DetectedLanguageLowConfidenceException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
