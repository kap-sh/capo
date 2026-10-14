"""Generated from Smithy shape ``com.amazonaws.cloudtrail#InsufficientDependencyServiceAccessPermissionException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudtrail.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudtrail.types.error_message


class InsufficientDependencyServiceAccessPermissionException_(TypedDict, closed=True):
    message: NotRequired["capo_cloudtrail.types.error_message.ErrorMessage"]
    """<p>Brief description of the exception returned by the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: InsufficientDependencyServiceAccessPermissionException_,
) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> InsufficientDependencyServiceAccessPermissionException_:
    out: InsufficientDependencyServiceAccessPermissionException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InsufficientDependencyServiceAccessPermissionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudtrail#InsufficientDependencyServiceAccessPermissionException``."""

    code: str | None = "InsufficientDependencyServiceAccessPermissionException"

    def __init__(
        self,
        data: InsufficientDependencyServiceAccessPermissionException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InsufficientDependencyServiceAccessPermissionException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InsufficientDependencyServiceAccessPermissionException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
