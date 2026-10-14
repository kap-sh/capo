"""Generated from Smithy shape ``com.amazonaws.dax#ServiceLinkedRoleNotFoundFault``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_dax.errors import ServiceError

if TYPE_CHECKING:
    import capo_dax.types.exception_message


class ServiceLinkedRoleNotFoundFault_(TypedDict, closed=True):
    message: NotRequired["capo_dax.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceLinkedRoleNotFoundFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceLinkedRoleNotFoundFault_:
    out: ServiceLinkedRoleNotFoundFault_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ServiceLinkedRoleNotFoundFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dax#ServiceLinkedRoleNotFoundFault``."""

    code: str | None = "ServiceLinkedRoleNotFoundFault"

    def __init__(
        self,
        data: ServiceLinkedRoleNotFoundFault_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceLinkedRoleNotFoundFault",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ServiceLinkedRoleNotFoundFault":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
