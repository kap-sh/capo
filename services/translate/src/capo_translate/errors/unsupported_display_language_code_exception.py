"""Generated from Smithy shape ``com.amazonaws.translate#UnsupportedDisplayLanguageCodeException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_translate.errors import ServiceError

if TYPE_CHECKING:
    import capo_translate.types.language_code_string
    import capo_translate.types.string


class UnsupportedDisplayLanguageCodeException_(TypedDict, closed=True):
    message: NotRequired["capo_translate.types.string.String"]
    display_language_code: NotRequired[
        "capo_translate.types.language_code_string.LanguageCodeString"
    ]
    """<p>Language code passed in with the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsupportedDisplayLanguageCodeException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "display_language_code" in value:
        out["DisplayLanguageCode"] = value["display_language_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnsupportedDisplayLanguageCodeException_:
    out: UnsupportedDisplayLanguageCodeException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("DisplayLanguageCode") is not None:
        out["display_language_code"] = data["DisplayLanguageCode"]
    return out


class UnsupportedDisplayLanguageCodeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.translate#UnsupportedDisplayLanguageCodeException``."""

    code: str | None = "UnsupportedDisplayLanguageCodeException"

    def __init__(
        self,
        data: UnsupportedDisplayLanguageCodeException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedDisplayLanguageCodeException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "UnsupportedDisplayLanguageCodeException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
