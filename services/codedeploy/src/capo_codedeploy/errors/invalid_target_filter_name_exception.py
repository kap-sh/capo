"""Generated from Smithy shape ``com.amazonaws.codedeploy#InvalidTargetFilterNameException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_codedeploy.errors import ServiceError

if TYPE_CHECKING:
    import capo_codedeploy.types.message


class InvalidTargetFilterNameException_(TypedDict, closed=True):
    message: NotRequired["capo_codedeploy.types.message.Message"]
    """<p>The message that corresponds to the exception thrown by CodeDeploy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidTargetFilterNameException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidTargetFilterNameException_:
    out: InvalidTargetFilterNameException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidTargetFilterNameException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codedeploy#InvalidTargetFilterNameException``."""

    code: str | None = "InvalidTargetFilterNameException"

    def __init__(
        self,
        data: InvalidTargetFilterNameException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidTargetFilterNameException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidTargetFilterNameException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
