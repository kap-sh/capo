"""Generated from Smithy shape ``com.amazonaws.costexplorer#AnalysisNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cost_explorer.errors import ServiceError

if TYPE_CHECKING:
    import capo_cost_explorer.types.error_message


class AnalysisNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_cost_explorer.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnalysisNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AnalysisNotFoundException_:
    out: AnalysisNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class AnalysisNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.costexplorer#AnalysisNotFoundException``."""

    code: str | None = "AnalysisNotFoundException"

    def __init__(
        self,
        data: AnalysisNotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AnalysisNotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "AnalysisNotFoundException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
