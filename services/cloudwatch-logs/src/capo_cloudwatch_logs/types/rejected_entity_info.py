"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#RejectedEntityInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.entity_rejection_error_type


class RejectedEntityInfo(TypedDict, closed=True):
    error_type: "capo_cloudwatch_logs.types.entity_rejection_error_type.EntityRejectionErrorType"
    """<p>The type of error that caused the rejection of the entity when calling <code>PutLogEvents</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RejectedEntityInfo) -> dict:
    out: dict = {}
    import capo_cloudwatch_logs.types.entity_rejection_error_type

    out["errorType"] = (
        capo_cloudwatch_logs.types.entity_rejection_error_type.serialize_aws_json_1_1(
            value["error_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RejectedEntityInfo:
    out: RejectedEntityInfo = {}  # type: ignore[typeddict-item]
    if data.get("errorType") is not None:
        import capo_cloudwatch_logs.types.entity_rejection_error_type

        out["error_type"] = (
            capo_cloudwatch_logs.types.entity_rejection_error_type.deserialize_aws_json_1_1(
                data["errorType"]
            )
        )
    else:
        import typing

        out["error_type"] = typing.cast(
            "capo_cloudwatch_logs.types.entity_rejection_error_type.EntityRejectionErrorType",
            "",
        )
    return out
