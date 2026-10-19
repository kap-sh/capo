"""Generated from Smithy shape ``com.amazonaws.route53recoverycluster#EndpointTemporarilyUnavailableException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_route53_recovery_cluster.errors import ServiceError

if TYPE_CHECKING:
    import capo_route53_recovery_cluster.types.string


class EndpointTemporarilyUnavailableException_(TypedDict, closed=True):
    message: "capo_route53_recovery_cluster.types.string.String"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EndpointTemporarilyUnavailableException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EndpointTemporarilyUnavailableException_:
    out: EndpointTemporarilyUnavailableException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


class EndpointTemporarilyUnavailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53recoverycluster#EndpointTemporarilyUnavailableException``."""

    code: str | None = "EndpointTemporarilyUnavailableException"

    def __init__(
        self,
        data: EndpointTemporarilyUnavailableException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="EndpointTemporarilyUnavailableException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "EndpointTemporarilyUnavailableException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
