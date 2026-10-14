"""Generated from Smithy shape ``com.amazonaws.lambda#ProvisionedConcurrencyConfigNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import ServiceError

if TYPE_CHECKING:
    import capo_lambda.types.string


class ProvisionedConcurrencyConfigNotFoundException_(TypedDict, closed=True):
    type: NotRequired["capo_lambda.types.string.String"]
    message: NotRequired["capo_lambda.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ProvisionedConcurrencyConfigNotFoundException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ProvisionedConcurrencyConfigNotFoundException_:
    out: ProvisionedConcurrencyConfigNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ProvisionedConcurrencyConfigNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#ProvisionedConcurrencyConfigNotFoundException``."""

    code: str | None = "ProvisionedConcurrencyConfigNotFoundException"

    def __init__(
        self,
        data: ProvisionedConcurrencyConfigNotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ProvisionedConcurrencyConfigNotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ProvisionedConcurrencyConfigNotFoundException":
        return cls(deserialize_json(data), message, response=response)
