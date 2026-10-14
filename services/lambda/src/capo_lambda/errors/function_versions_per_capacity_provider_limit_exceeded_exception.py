"""Generated from Smithy shape ``com.amazonaws.lambda#FunctionVersionsPerCapacityProviderLimitExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import ServiceError

if TYPE_CHECKING:
    import capo_lambda.types.string


class FunctionVersionsPerCapacityProviderLimitExceededException_(
    TypedDict, closed=True
):
    type: NotRequired["capo_lambda.types.string.String"]
    """<p>The exception type.</p>"""
    message: NotRequired["capo_lambda.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(
    value: FunctionVersionsPerCapacityProviderLimitExceededException_,
) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(
    data: dict,
) -> FunctionVersionsPerCapacityProviderLimitExceededException_:
    out: FunctionVersionsPerCapacityProviderLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class FunctionVersionsPerCapacityProviderLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#FunctionVersionsPerCapacityProviderLimitExceededException``."""

    code: str | None = "FunctionVersionsPerCapacityProviderLimitExceededException"

    def __init__(
        self,
        data: FunctionVersionsPerCapacityProviderLimitExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="FunctionVersionsPerCapacityProviderLimitExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "FunctionVersionsPerCapacityProviderLimitExceededException":
        return cls(deserialize_json(data), message, response=response)
