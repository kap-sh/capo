"""Generated from Smithy shape ``com.amazonaws.cloudhsm#CloudHsmInternalException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudhsm.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudhsm.types.boolean
    import capo_cloudhsm.types.string


class CloudHsmInternalException_(TypedDict, closed=True):
    message: NotRequired["capo_cloudhsm.types.string.String"]
    """<p>Additional information about the error.</p>"""
    retryable: "capo_cloudhsm.types.boolean.Boolean"
    """<p>Indicates if the action can be retried.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudHsmInternalException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    out["retryable"] = value.get("retryable", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudHsmInternalException_:
    out: CloudHsmInternalException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("retryable") is not None:
        out["retryable"] = data["retryable"]
    else:
        out["retryable"] = False
    return out


class CloudHsmInternalException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudhsm#CloudHsmInternalException``."""

    code: str | None = "CloudHsmInternalException"

    def __init__(
        self,
        data: CloudHsmInternalException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="CloudHsmInternalException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "CloudHsmInternalException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
