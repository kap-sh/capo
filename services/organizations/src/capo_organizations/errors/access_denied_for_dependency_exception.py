"""Generated from Smithy shape ``com.amazonaws.organizations#AccessDeniedForDependencyException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_organizations.errors import ServiceError

if TYPE_CHECKING:
    import capo_organizations.types.access_denied_for_dependency_exception_reason
    import capo_organizations.types.exception_message


class AccessDeniedForDependencyException_(TypedDict, closed=True):
    message: NotRequired["capo_organizations.types.exception_message.ExceptionMessage"]
    reason: NotRequired[
        "capo_organizations.types.access_denied_for_dependency_exception_reason.AccessDeniedForDependencyExceptionReason"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessDeniedForDependencyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        import capo_organizations.types.access_denied_for_dependency_exception_reason

        out["Reason"] = (
            capo_organizations.types.access_denied_for_dependency_exception_reason.serialize_aws_json_1_1(
                value["reason"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AccessDeniedForDependencyException_:
    out: AccessDeniedForDependencyException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Reason") is not None:
        import capo_organizations.types.access_denied_for_dependency_exception_reason

        out["reason"] = (
            capo_organizations.types.access_denied_for_dependency_exception_reason.deserialize_aws_json_1_1(
                data["Reason"]
            )
        )
    return out


class AccessDeniedForDependencyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.organizations#AccessDeniedForDependencyException``."""

    code: str | None = "AccessDeniedForDependencyException"

    def __init__(
        self,
        data: AccessDeniedForDependencyException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccessDeniedForDependencyException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "AccessDeniedForDependencyException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
