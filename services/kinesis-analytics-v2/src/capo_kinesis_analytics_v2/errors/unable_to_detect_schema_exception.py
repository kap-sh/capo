"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#UnableToDetectSchemaException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_kinesis_analytics_v2.errors import ServiceError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.error_message
    import capo_kinesis_analytics_v2.types.processed_input_records
    import capo_kinesis_analytics_v2.types.raw_input_records


class UnableToDetectSchemaException_(TypedDict, closed=True):
    message: NotRequired["capo_kinesis_analytics_v2.types.error_message.ErrorMessage"]
    raw_input_records: NotRequired[
        "capo_kinesis_analytics_v2.types.raw_input_records.RawInputRecords"
    ]
    """<p>Raw stream data that was sampled to infer the schema.</p>"""
    processed_input_records: NotRequired[
        "capo_kinesis_analytics_v2.types.processed_input_records.ProcessedInputRecords"
    ]
    """<p>Stream data that was modified by the processor specified in the <code>InputProcessingConfiguration</code> parameter. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnableToDetectSchemaException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "raw_input_records" in value:
        import capo_kinesis_analytics_v2.types.raw_input_records

        out["RawInputRecords"] = (
            capo_kinesis_analytics_v2.types.raw_input_records.serialize_aws_json_1_1(
                value["raw_input_records"]
            )
        )
    if "processed_input_records" in value:
        import capo_kinesis_analytics_v2.types.processed_input_records

        out["ProcessedInputRecords"] = (
            capo_kinesis_analytics_v2.types.processed_input_records.serialize_aws_json_1_1(
                value["processed_input_records"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UnableToDetectSchemaException_:
    out: UnableToDetectSchemaException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("RawInputRecords") is not None:
        import capo_kinesis_analytics_v2.types.raw_input_records

        out["raw_input_records"] = (
            capo_kinesis_analytics_v2.types.raw_input_records.deserialize_aws_json_1_1(
                data["RawInputRecords"]
            )
        )
    if data.get("ProcessedInputRecords") is not None:
        import capo_kinesis_analytics_v2.types.processed_input_records

        out["processed_input_records"] = (
            capo_kinesis_analytics_v2.types.processed_input_records.deserialize_aws_json_1_1(
                data["ProcessedInputRecords"]
            )
        )
    return out


class UnableToDetectSchemaException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesisanalyticsv2#UnableToDetectSchemaException``."""

    code: str | None = "UnableToDetectSchemaException"

    def __init__(
        self,
        data: UnableToDetectSchemaException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnableToDetectSchemaException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "UnableToDetectSchemaException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
