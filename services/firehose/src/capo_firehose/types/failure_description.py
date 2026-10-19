"""Generated from Smithy shape ``com.amazonaws.firehose#FailureDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.delivery_stream_failure_type
    import capo_firehose.types.non_empty_string


class FailureDescription(TypedDict, closed=True):
    type: "capo_firehose.types.delivery_stream_failure_type.DeliveryStreamFailureType"
    """<p>The type of error that caused the failure.</p>"""
    details: "capo_firehose.types.non_empty_string.NonEmptyString"
    """<p>A message providing details about the error that caused the failure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailureDescription) -> dict:
    out: dict = {}
    import capo_firehose.types.delivery_stream_failure_type

    out["Type"] = (
        capo_firehose.types.delivery_stream_failure_type.serialize_aws_json_1_1(
            value["type"]
        )
    )
    out["Details"] = value["details"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FailureDescription:
    out: FailureDescription = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_firehose.types.delivery_stream_failure_type

        out["type"] = (
            capo_firehose.types.delivery_stream_failure_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_firehose.types.delivery_stream_failure_type.DeliveryStreamFailureType",
            "",
        )
    if data.get("Details") is not None:
        out["details"] = data["Details"]
    else:
        out["details"] = ""
    return out
