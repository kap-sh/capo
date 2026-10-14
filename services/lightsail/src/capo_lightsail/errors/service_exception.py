"""Generated from Smithy shape ``com.amazonaws.lightsail#ServiceException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_lightsail.errors import ServiceError

if TYPE_CHECKING:
    import capo_lightsail.types.string


class ServiceException_(TypedDict, closed=True):
    code: NotRequired["capo_lightsail.types.string.string"]
    docs: NotRequired["capo_lightsail.types.string.string"]
    message: NotRequired["capo_lightsail.types.string.string"]
    tip: NotRequired["capo_lightsail.types.string.string"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceException_) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "docs" in value:
        out["docs"] = value["docs"]
    if "message" in value:
        out["message"] = value["message"]
    if "tip" in value:
        out["tip"] = value["tip"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceException_:
    out: ServiceException_ = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("docs") is not None:
        out["docs"] = data["docs"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("tip") is not None:
        out["tip"] = data["tip"]
    return out


class ServiceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lightsail#ServiceException``."""

    code: str | None = "ServiceException"

    def __init__(
        self,
        data: ServiceException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ServiceException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
