"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#RejectedRecordsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_timestream_write.errors import ServiceError

if TYPE_CHECKING:
    import capo_timestream_write.types.error_message
    import capo_timestream_write.types.rejected_records


class RejectedRecordsException_(TypedDict, closed=True):
    message: NotRequired["capo_timestream_write.types.error_message.ErrorMessage"]
    rejected_records: NotRequired[
        "capo_timestream_write.types.rejected_records.RejectedRecords"
    ]
    """<p> </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RejectedRecordsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "rejected_records" in value:
        import capo_timestream_write.types.rejected_records

        out["RejectedRecords"] = (
            capo_timestream_write.types.rejected_records.serialize_aws_json_1_0(
                value["rejected_records"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RejectedRecordsException_:
    out: RejectedRecordsException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("RejectedRecords") is not None:
        import capo_timestream_write.types.rejected_records

        out["rejected_records"] = (
            capo_timestream_write.types.rejected_records.deserialize_aws_json_1_0(
                data["RejectedRecords"]
            )
        )
    return out


class RejectedRecordsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.timestreamwrite#RejectedRecordsException``."""

    code: str | None = "RejectedRecordsException"

    def __init__(
        self,
        data: RejectedRecordsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RejectedRecordsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "RejectedRecordsException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
