"""Generated from Smithy shape ``com.amazonaws.inspector#InvalidCrossAccountRoleException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_inspector.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_inspector.types.bool
    import capo_inspector.types.error_message
    import capo_inspector.types.invalid_cross_account_role_error_code


class InvalidCrossAccountRoleException_(TypedDict, closed=True):
    message: "capo_inspector.types.error_message.ErrorMessage"
    """<p>Details of the exception error.</p>"""
    error_code: "capo_inspector.types.invalid_cross_account_role_error_code.InvalidCrossAccountRoleErrorCode"
    """<p>Code that indicates the type of error that is generated.</p>"""
    can_retry: "capo_inspector.types.bool.Bool"
    """<p>You can immediately retry your request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidCrossAccountRoleException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    import capo_inspector.types.invalid_cross_account_role_error_code

    out["errorCode"] = (
        capo_inspector.types.invalid_cross_account_role_error_code.serialize_aws_json_1_1(
            value["error_code"]
        )
    )
    out["canRetry"] = value["can_retry"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidCrossAccountRoleException_:
    out: InvalidCrossAccountRoleException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InvalidCrossAccountRoleException_.message required")
    if data.get("errorCode") is not None:
        import capo_inspector.types.invalid_cross_account_role_error_code

        out["error_code"] = (
            capo_inspector.types.invalid_cross_account_role_error_code.deserialize_aws_json_1_1(
                data["errorCode"]
            )
        )
    else:
        raise DeserializationError(
            "InvalidCrossAccountRoleException_.error_code required"
        )
    if data.get("canRetry") is not None:
        out["can_retry"] = data["canRetry"]
    else:
        raise DeserializationError(
            "InvalidCrossAccountRoleException_.can_retry required"
        )
    return out


class InvalidCrossAccountRoleException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.inspector#InvalidCrossAccountRoleException``."""

    code: str | None = "InvalidCrossAccountRoleException"

    def __init__(
        self,
        data: InvalidCrossAccountRoleException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidCrossAccountRoleException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidCrossAccountRoleException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
