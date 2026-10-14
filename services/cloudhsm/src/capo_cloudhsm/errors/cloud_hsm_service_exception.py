"""Generated from Smithy shape ``com.amazonaws.cloudhsm#CloudHsmServiceException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudhsm.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudhsm.types.boolean
    import capo_cloudhsm.types.string


class CloudHsmServiceException_(TypedDict, closed=True):
    message: NotRequired["capo_cloudhsm.types.string.String"]
    """<p>Additional information about the error.</p>"""
    retryable: "capo_cloudhsm.types.boolean.Boolean"
    """<p>Indicates if the action can be retried.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudHsmServiceException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    out["retryable"] = value.get("retryable", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudHsmServiceException_:
    out: CloudHsmServiceException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("retryable") is not None:
        out["retryable"] = data["retryable"]
    else:
        out["retryable"] = False
    return out


class CloudHsmServiceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudhsm#CloudHsmServiceException``."""

    code: str | None = "CloudHsmServiceException"

    def __init__(
        self,
        data: CloudHsmServiceException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CloudHsmServiceException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "CloudHsmServiceException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
