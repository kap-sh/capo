"""Generated from Smithy shape ``com.amazonaws.redshiftdata#ExecuteStatementException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_redshift_data.errors import ServiceError

if TYPE_CHECKING:
    import capo_redshift_data.types.string


class ExecuteStatementException_(TypedDict, closed=True):
    message: "capo_redshift_data.types.string.String"
    """<p>The exception message.</p>"""
    statement_id: "capo_redshift_data.types.string.String"
    """<p>Statement identifier of the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecuteStatementException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    out["StatementId"] = value["statement_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExecuteStatementException_:
    out: ExecuteStatementException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("StatementId") is not None:
        out["statement_id"] = data["StatementId"]
    else:
        out["statement_id"] = ""
    return out


class ExecuteStatementException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshiftdata#ExecuteStatementException``."""

    code: str | None = "ExecuteStatementException"

    def __init__(
        self,
        data: ExecuteStatementException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ExecuteStatementException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ExecuteStatementException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
