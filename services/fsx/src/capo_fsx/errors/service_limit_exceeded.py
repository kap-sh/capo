"""Generated from Smithy shape ``com.amazonaws.fsx#ServiceLimitExceeded``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_fsx.errors import ServiceError

if TYPE_CHECKING:
    import capo_fsx.types.error_message
    import capo_fsx.types.service_limit


class ServiceLimitExceeded_(TypedDict, closed=True):
    limit: NotRequired["capo_fsx.types.service_limit.ServiceLimit"]
    """<p>Enumeration of the service limit that was exceeded. </p>"""
    message: NotRequired["capo_fsx.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceLimitExceeded_) -> dict:
    out: dict = {}
    if "limit" in value:
        import capo_fsx.types.service_limit

        out["Limit"] = capo_fsx.types.service_limit.serialize_aws_json_1_1(
            value["limit"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceLimitExceeded_:
    out: ServiceLimitExceeded_ = {}  # type: ignore[typeddict-item]
    if data.get("Limit") is not None:
        import capo_fsx.types.service_limit

        out["limit"] = capo_fsx.types.service_limit.deserialize_aws_json_1_1(
            data["Limit"]
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ServiceLimitExceeded(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#ServiceLimitExceeded``."""

    code: str | None = "ServiceLimitExceeded"

    def __init__(
        self,
        data: ServiceLimitExceeded_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceLimitExceeded",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ServiceLimitExceeded":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
