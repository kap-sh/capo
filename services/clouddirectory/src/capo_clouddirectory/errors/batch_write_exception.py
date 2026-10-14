"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchWriteException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_clouddirectory.errors import ServiceError

if TYPE_CHECKING:
    import capo_clouddirectory.types.batch_operation_index
    import capo_clouddirectory.types.batch_write_exception_type
    import capo_clouddirectory.types.exception_message


class BatchWriteException_(TypedDict, closed=True):
    index: "capo_clouddirectory.types.batch_operation_index.BatchOperationIndex"
    type: NotRequired[
        "capo_clouddirectory.types.batch_write_exception_type.BatchWriteExceptionType"
    ]
    message: NotRequired["capo_clouddirectory.types.exception_message.ExceptionMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: BatchWriteException_) -> dict:
    out: dict = {}
    out["Index"] = value.get("index", 0)
    if "type" in value:
        import capo_clouddirectory.types.batch_write_exception_type

        out["Type"] = (
            capo_clouddirectory.types.batch_write_exception_type.serialize_json(
                value["type"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchWriteException_:
    out: BatchWriteException_ = {}  # type: ignore[typeddict-item]
    if data.get("Index") is not None:
        out["index"] = data["Index"]
    else:
        out["index"] = 0
    if data.get("Type") is not None:
        import capo_clouddirectory.types.batch_write_exception_type

        out["type"] = (
            capo_clouddirectory.types.batch_write_exception_type.deserialize_json(
                data["Type"]
            )
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class BatchWriteException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.clouddirectory#BatchWriteException``."""

    code: str | None = "BatchWriteException"

    def __init__(
        self,
        data: BatchWriteException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BatchWriteException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "BatchWriteException":
        return cls(deserialize_json(data), message, response=response)
