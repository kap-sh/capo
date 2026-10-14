"""Generated from Smithy shape ``com.amazonaws.servicediscovery#DuplicateRequest``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_servicediscovery.errors import ServiceError

if TYPE_CHECKING:
    import capo_servicediscovery.types.error_message
    import capo_servicediscovery.types.operation_id


class DuplicateRequest_(TypedDict, closed=True):
    message: NotRequired["capo_servicediscovery.types.error_message.ErrorMessage"]
    duplicate_operation_id: NotRequired[
        "capo_servicediscovery.types.operation_id.OperationId"
    ]
    """<p>The ID of the operation that's already in progress.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DuplicateRequest_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "duplicate_operation_id" in value:
        out["DuplicateOperationId"] = value["duplicate_operation_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DuplicateRequest_:
    out: DuplicateRequest_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("DuplicateOperationId") is not None:
        out["duplicate_operation_id"] = data["DuplicateOperationId"]
    return out


class DuplicateRequest(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.servicediscovery#DuplicateRequest``."""

    code: str | None = "DuplicateRequest"

    def __init__(
        self,
        data: DuplicateRequest_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DuplicateRequest",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DuplicateRequest":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
