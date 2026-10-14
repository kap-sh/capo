"""Generated from Smithy shape ``com.amazonaws.route53recoverycluster#ThrottlingException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_route53_recovery_cluster.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_route53_recovery_cluster.types.retry_after_seconds
    import capo_route53_recovery_cluster.types.string


class ThrottlingException_(TypedDict, closed=True):
    message: "capo_route53_recovery_cluster.types.string.String"
    retry_after_seconds: (
        "capo_route53_recovery_cluster.types.retry_after_seconds.RetryAfterSeconds"
    )


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["retryAfterSeconds"] = value.get("retry_after_seconds", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ThrottlingException_.message required")
    if data.get("retryAfterSeconds") is not None:
        out["retry_after_seconds"] = data["retryAfterSeconds"]
    else:
        out["retry_after_seconds"] = 0
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53recoverycluster#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(
        self,
        data: ThrottlingException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottlingException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ThrottlingException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
