"""Generated from Smithy shape ``com.amazonaws.costexplorer#GenerationExistsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cost_explorer.errors import ServiceError

if TYPE_CHECKING:
    import capo_cost_explorer.types.error_message


class GenerationExistsException_(TypedDict, closed=True):
    message: NotRequired["capo_cost_explorer.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GenerationExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GenerationExistsException_:
    out: GenerationExistsException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class GenerationExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.costexplorer#GenerationExistsException``."""

    code: str | None = "GenerationExistsException"

    def __init__(
        self,
        data: GenerationExistsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="GenerationExistsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "GenerationExistsException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
