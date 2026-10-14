"""Generated from Smithy shape ``com.amazonaws.evs#TagPolicyException``."""

import zapros
from typing_extensions import TypedDict

from capo_evs.errors import DeserializationError, ServiceError


class TagPolicyException_(TypedDict, closed=True):
    message: "str"
    """<p>Describes the error encountered</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagPolicyException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TagPolicyException_:
    out: TagPolicyException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("TagPolicyException_.message required")
    return out


class TagPolicyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.evs#TagPolicyException``."""

    code: str | None = "TagPolicyException"

    def __init__(
        self,
        data: TagPolicyException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TagPolicyException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "TagPolicyException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
