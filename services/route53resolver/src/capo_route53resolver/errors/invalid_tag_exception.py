"""Generated from Smithy shape ``com.amazonaws.route53resolver#InvalidTagException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_route53resolver.errors import ServiceError

if TYPE_CHECKING:
    import capo_route53resolver.types.exception_message


class InvalidTagException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_route53resolver.types.exception_message.ExceptionMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidTagException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidTagException_:
    out: InvalidTagException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InvalidTagException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53resolver#InvalidTagException``."""

    code: str | None = "InvalidTagException"

    def __init__(
        self,
        data: InvalidTagException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidTagException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidTagException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
