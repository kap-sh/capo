"""Generated from Smithy shape ``com.amazonaws.machinelearning#InternalServerException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_machine_learning.errors import ServiceError

if TYPE_CHECKING:
    import capo_machine_learning.types.error_code
    import capo_machine_learning.types.error_message


class InternalServerException_(TypedDict, closed=True):
    message: NotRequired["capo_machine_learning.types.error_message.ErrorMessage"]
    code: "capo_machine_learning.types.error_code.ErrorCode"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InternalServerException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    out["code"] = value.get("code", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        out["code"] = 0
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.machinelearning#InternalServerException``."""

    code: str | None = "InternalServerException"

    def __init__(
        self,
        data: InternalServerException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalServerException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
