"""Generated from Smithy shape ``com.amazonaws.redshiftdata#DatabaseConnectionException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_redshift_data.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_redshift_data.types.string


class DatabaseConnectionException_(TypedDict, closed=True):
    message: "capo_redshift_data.types.string.String"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatabaseConnectionException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DatabaseConnectionException_:
    out: DatabaseConnectionException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("DatabaseConnectionException_.message required")
    return out


class DatabaseConnectionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshiftdata#DatabaseConnectionException``."""

    code: str | None = "DatabaseConnectionException"

    def __init__(
        self,
        data: DatabaseConnectionException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="DatabaseConnectionException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DatabaseConnectionException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
