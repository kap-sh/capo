"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ServiceUnavailableException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_media_pipelines.errors import ServiceError

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.error_code
    import capo_chime_sdk_media_pipelines.types.string


class ServiceUnavailableException_(TypedDict, closed=True):
    code: NotRequired["capo_chime_sdk_media_pipelines.types.error_code.ErrorCode"]
    message: NotRequired["capo_chime_sdk_media_pipelines.types.string.String"]
    request_id: NotRequired["capo_chime_sdk_media_pipelines.types.string.String"]
    """<p>The request ID associated with the call responsible for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceUnavailableException_) -> dict:
    out: dict = {}
    if "code" in value:
        import capo_chime_sdk_media_pipelines.types.error_code

        out["Code"] = capo_chime_sdk_media_pipelines.types.error_code.serialize_json(
            value["code"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ServiceUnavailableException_:
    out: ServiceUnavailableException_ = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        import capo_chime_sdk_media_pipelines.types.error_code

        out["code"] = capo_chime_sdk_media_pipelines.types.error_code.deserialize_json(
            data["Code"]
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out


class ServiceUnavailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chimesdkmediapipelines#ServiceUnavailableException``."""

    code: str | None = "ServiceUnavailableException"

    def __init__(
        self,
        data: ServiceUnavailableException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceUnavailableException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ServiceUnavailableException":
        return cls(deserialize_json(data), message, response=response)
