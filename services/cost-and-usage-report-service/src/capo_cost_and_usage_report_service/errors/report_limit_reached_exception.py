"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#ReportLimitReachedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cost_and_usage_report_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_cost_and_usage_report_service.types.error_message


class ReportLimitReachedException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_cost_and_usage_report_service.types.error_message.ErrorMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportLimitReachedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReportLimitReachedException_:
    out: ReportLimitReachedException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ReportLimitReachedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.costandusagereportservice#ReportLimitReachedException``."""

    code: str | None = "ReportLimitReachedException"

    def __init__(
        self,
        data: ReportLimitReachedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ReportLimitReachedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ReportLimitReachedException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
