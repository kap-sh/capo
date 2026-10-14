"""Generated from Smithy shape ``com.amazonaws.sfn#KmsInvalidStateException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_sfn.errors import ServiceError

if TYPE_CHECKING:
    import capo_sfn.types.error_message
    import capo_sfn.types.kms_key_state


class KmsInvalidStateException_(TypedDict, closed=True):
    kms_key_state: NotRequired["capo_sfn.types.kms_key_state.KmsKeyState"]
    """<p>Current status of the KMS; key. For example: <code>DISABLED</code>, <code>PENDING_DELETION</code>, <code>PENDING_IMPORT</code>, <code>UNAVAILABLE</code>, <code>CREATING</code>.</p>"""
    message: NotRequired["capo_sfn.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KmsInvalidStateException_) -> dict:
    out: dict = {}
    if "kms_key_state" in value:
        import capo_sfn.types.kms_key_state

        out["kmsKeyState"] = capo_sfn.types.kms_key_state.serialize_aws_json_1_0(
            value["kms_key_state"]
        )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> KmsInvalidStateException_:
    out: KmsInvalidStateException_ = {}  # type: ignore[typeddict-item]
    if data.get("kmsKeyState") is not None:
        import capo_sfn.types.kms_key_state

        out["kms_key_state"] = capo_sfn.types.kms_key_state.deserialize_aws_json_1_0(
            data["kmsKeyState"]
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class KmsInvalidStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sfn#KmsInvalidStateException``."""

    code: str | None = "KmsInvalidStateException"

    def __init__(
        self,
        data: KmsInvalidStateException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="KmsInvalidStateException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "KmsInvalidStateException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
