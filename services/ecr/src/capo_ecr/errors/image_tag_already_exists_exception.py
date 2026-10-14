"""Generated from Smithy shape ``com.amazonaws.ecr#ImageTagAlreadyExistsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ecr.errors import ServiceError

if TYPE_CHECKING:
    import capo_ecr.types.exception_message


class ImageTagAlreadyExistsException_(TypedDict, closed=True):
    message: NotRequired["capo_ecr.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageTagAlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImageTagAlreadyExistsException_:
    out: ImageTagAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ImageTagAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecr#ImageTagAlreadyExistsException``."""

    code: str | None = "ImageTagAlreadyExistsException"

    def __init__(
        self,
        data: ImageTagAlreadyExistsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ImageTagAlreadyExistsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ImageTagAlreadyExistsException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
