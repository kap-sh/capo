"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_sso_admin.errors import ServiceError

if TYPE_CHECKING:
    import capo_sso_admin.types.resource_not_found_exception_reason
    import capo_sso_admin.types.resource_not_found_message


class ResourceNotFoundException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_sso_admin.types.resource_not_found_message.ResourceNotFoundMessage"
    ]
    reason: NotRequired[
        "capo_sso_admin.types.resource_not_found_exception_reason.ResourceNotFoundExceptionReason"
    ]
    """<p>The reason for the resource not found exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        import capo_sso_admin.types.resource_not_found_exception_reason

        out["Reason"] = (
            capo_sso_admin.types.resource_not_found_exception_reason.serialize_aws_json_1_1(
                value["reason"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Reason") is not None:
        import capo_sso_admin.types.resource_not_found_exception_reason

        out["reason"] = (
            capo_sso_admin.types.resource_not_found_exception_reason.deserialize_aws_json_1_1(
                data["Reason"]
            )
        )
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssoadmin#ResourceNotFoundException``."""

    code: str | None = "ResourceNotFoundException"

    def __init__(
        self,
        data: ResourceNotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceNotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceNotFoundException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
