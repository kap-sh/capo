"""Generated from Smithy shape ``com.amazonaws.route53domains#InvalidInput``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_route_53_domains.errors import ServiceError

if TYPE_CHECKING:
    import capo_route_53_domains.types.error_message


class InvalidInput_(TypedDict, closed=True):
    message: NotRequired["capo_route_53_domains.types.error_message.ErrorMessage"]
    """<p>The requested item is not acceptable. For example, for an OperationId it might refer to the ID of an operation that is already completed. For a domain name, it might not be a valid domain name or belong to the requester account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidInput_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidInput_:
    out: InvalidInput_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidInput(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53domains#InvalidInput``."""

    code: str | None = "InvalidInput"

    def __init__(
        self,
        data: InvalidInput_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidInput",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidInput":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
