"""Generated from Smithy shape ``com.amazonaws.route53resolver#UnknownResourceException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_route53resolver.errors import ServiceError

if TYPE_CHECKING:
    import capo_route53resolver.types.exception_message


class UnknownResourceException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_route53resolver.types.exception_message.ExceptionMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnknownResourceException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnknownResourceException_:
    out: UnknownResourceException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class UnknownResourceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53resolver#UnknownResourceException``."""

    code: str | None = "UnknownResourceException"

    def __init__(
        self,
        data: UnknownResourceException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnknownResourceException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "UnknownResourceException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
