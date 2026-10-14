"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#DuplicateReportNameException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cost_and_usage_report_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_cost_and_usage_report_service.types.error_message


class DuplicateReportNameException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_cost_and_usage_report_service.types.error_message.ErrorMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DuplicateReportNameException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DuplicateReportNameException_:
    out: DuplicateReportNameException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class DuplicateReportNameException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.costandusagereportservice#DuplicateReportNameException``."""

    code: str | None = "DuplicateReportNameException"

    def __init__(
        self,
        data: DuplicateReportNameException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DuplicateReportNameException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DuplicateReportNameException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
