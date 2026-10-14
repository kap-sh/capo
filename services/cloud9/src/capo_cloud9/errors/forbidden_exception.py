"""Generated from Smithy shape ``com.amazonaws.cloud9#ForbiddenException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloud9.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloud9.types.integer
    import capo_cloud9.types.string


class ForbiddenException_(TypedDict, closed=True):
    message: NotRequired["capo_cloud9.types.string.String"]
    class_name: NotRequired["capo_cloud9.types.string.String"]
    code: "capo_cloud9.types.integer.Integer"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ForbiddenException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "class_name" in value:
        out["className"] = value["class_name"]
    out["code"] = value.get("code", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> ForbiddenException_:
    out: ForbiddenException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("className") is not None:
        out["class_name"] = data["className"]
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        out["code"] = 0
    return out


class ForbiddenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloud9#ForbiddenException``."""

    code: str | None = "ForbiddenException"

    def __init__(
        self,
        data: ForbiddenException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ForbiddenException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ForbiddenException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
