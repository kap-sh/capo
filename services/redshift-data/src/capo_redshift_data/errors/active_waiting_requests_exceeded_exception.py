"""Generated from Smithy shape ``com.amazonaws.redshiftdata#ActiveWaitingRequestsExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_redshift_data.errors import ServiceError

if TYPE_CHECKING:
    import capo_redshift_data.types.string


class ActiveWaitingRequestsExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_redshift_data.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActiveWaitingRequestsExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ActiveWaitingRequestsExceededException_:
    out: ActiveWaitingRequestsExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ActiveWaitingRequestsExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshiftdata#ActiveWaitingRequestsExceededException``."""

    code: str | None = "ActiveWaitingRequestsExceededException"

    def __init__(
        self,
        data: ActiveWaitingRequestsExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ActiveWaitingRequestsExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ActiveWaitingRequestsExceededException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
