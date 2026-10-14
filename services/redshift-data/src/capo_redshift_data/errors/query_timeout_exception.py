"""Generated from Smithy shape ``com.amazonaws.redshiftdata#QueryTimeoutException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_redshift_data.errors import ServiceError

if TYPE_CHECKING:
    import capo_redshift_data.types.string


class QueryTimeoutException_(TypedDict, closed=True):
    message: NotRequired["capo_redshift_data.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryTimeoutException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryTimeoutException_:
    out: QueryTimeoutException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class QueryTimeoutException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshiftdata#QueryTimeoutException``."""

    code: str | None = "QueryTimeoutException"

    def __init__(
        self,
        data: QueryTimeoutException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="QueryTimeoutException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "QueryTimeoutException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
