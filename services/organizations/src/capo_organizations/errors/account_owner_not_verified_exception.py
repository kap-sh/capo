"""Generated from Smithy shape ``com.amazonaws.organizations#AccountOwnerNotVerifiedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_organizations.errors import ServiceError

if TYPE_CHECKING:
    import capo_organizations.types.exception_message


class AccountOwnerNotVerifiedException_(TypedDict, closed=True):
    message: NotRequired["capo_organizations.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountOwnerNotVerifiedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AccountOwnerNotVerifiedException_:
    out: AccountOwnerNotVerifiedException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class AccountOwnerNotVerifiedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.organizations#AccountOwnerNotVerifiedException``."""

    code: str | None = "AccountOwnerNotVerifiedException"

    def __init__(
        self,
        data: AccountOwnerNotVerifiedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccountOwnerNotVerifiedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "AccountOwnerNotVerifiedException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
