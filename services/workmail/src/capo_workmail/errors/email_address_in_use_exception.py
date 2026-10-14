"""Generated from Smithy shape ``com.amazonaws.workmail#EmailAddressInUseException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_workmail.errors import ServiceError

if TYPE_CHECKING:
    import capo_workmail.types.string


class EmailAddressInUseException_(TypedDict, closed=True):
    message: NotRequired["capo_workmail.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EmailAddressInUseException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EmailAddressInUseException_:
    out: EmailAddressInUseException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class EmailAddressInUseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workmail#EmailAddressInUseException``."""

    code: str | None = "EmailAddressInUseException"

    def __init__(
        self,
        data: EmailAddressInUseException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EmailAddressInUseException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "EmailAddressInUseException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
