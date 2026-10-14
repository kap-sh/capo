"""Generated from Smithy shape ``com.amazonaws.iotjobsdataplane#ThrottlingException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_iot_jobs_data_plane.errors import ServiceError

if TYPE_CHECKING:
    import capo_iot_jobs_data_plane.types.binary_blob
    import capo_iot_jobs_data_plane.types.error_message


class ThrottlingException_(TypedDict, closed=True):
    message: NotRequired["capo_iot_jobs_data_plane.types.error_message.errorMessage"]
    """<p>The message associated with the exception.</p>"""
    payload: NotRequired["capo_iot_jobs_data_plane.types.binary_blob.BinaryBlob"]
    """<p>The payload associated with the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "payload" in value:
        import capo_iot_jobs_data_plane.types.binary_blob

        out["payload"] = capo_iot_jobs_data_plane.types.binary_blob.serialize_json(
            value["payload"]
        )
    return out


def deserialize_json(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("payload") is not None:
        import capo_iot_jobs_data_plane.types.binary_blob

        out["payload"] = capo_iot_jobs_data_plane.types.binary_blob.deserialize_json(
            data["payload"]
        )
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotjobsdataplane#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(
        self,
        data: ThrottlingException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottlingException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ThrottlingException":
        return cls(deserialize_json(data), message, response=response)
