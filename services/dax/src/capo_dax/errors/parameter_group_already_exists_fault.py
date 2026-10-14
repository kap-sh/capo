"""Generated from Smithy shape ``com.amazonaws.dax#ParameterGroupAlreadyExistsFault``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_dax.errors import ServiceError

if TYPE_CHECKING:
    import capo_dax.types.exception_message


class ParameterGroupAlreadyExistsFault_(TypedDict, closed=True):
    message: NotRequired["capo_dax.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterGroupAlreadyExistsFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ParameterGroupAlreadyExistsFault_:
    out: ParameterGroupAlreadyExistsFault_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ParameterGroupAlreadyExistsFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dax#ParameterGroupAlreadyExistsFault``."""

    code: str | None = "ParameterGroupAlreadyExistsFault"

    def __init__(
        self,
        data: ParameterGroupAlreadyExistsFault_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ParameterGroupAlreadyExistsFault",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ParameterGroupAlreadyExistsFault":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
