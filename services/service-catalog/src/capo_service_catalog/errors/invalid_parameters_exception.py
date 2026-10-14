"""Generated from Smithy shape ``com.amazonaws.servicecatalog#InvalidParametersException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_service_catalog.errors import ServiceError

if TYPE_CHECKING:
    import capo_service_catalog.types.error_message


class InvalidParametersException_(TypedDict, closed=True):
    message: NotRequired["capo_service_catalog.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidParametersException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidParametersException_:
    out: InvalidParametersException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InvalidParametersException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.servicecatalog#InvalidParametersException``."""

    code: str | None = "InvalidParametersException"

    def __init__(
        self,
        data: InvalidParametersException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidParametersException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidParametersException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
