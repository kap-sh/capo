"""Generated from Smithy shape ``com.amazonaws.ssm#HierarchyTypeMismatchException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class HierarchyTypeMismatchException_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]
    """<p>Parameter Store doesn't support changing a parameter type in a hierarchy. For example, you can't change a parameter from a <code>String</code> type to a <code>SecureString</code> type. You must create a new, unique parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HierarchyTypeMismatchException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HierarchyTypeMismatchException_:
    out: HierarchyTypeMismatchException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class HierarchyTypeMismatchException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#HierarchyTypeMismatchException``."""

    code: str | None = "HierarchyTypeMismatchException"

    def __init__(
        self,
        data: HierarchyTypeMismatchException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="HierarchyTypeMismatchException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "HierarchyTypeMismatchException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
