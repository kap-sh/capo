"""Generated from Smithy shape ``com.amazonaws.kinesis#QueueAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.dead_letter_configuration
    import capo_kinesis.types.visibility_timeout_seconds


class QueueAttributes(TypedDict, closed=True):
    visibility_timeout_seconds: NotRequired[
        "capo_kinesis.types.visibility_timeout_seconds.VisibilityTimeoutSeconds"
    ]
    """<p>The duration, in seconds, that a record is in flight and not visible to any consumer instance after it is received. A record that is not acknowledged before this duration elapses becomes visible in the queue again and can be received by any consumer instance. If you omit this attribute when you create a queue, the queue uses 30 seconds.</p>"""
    dead_letter_configuration: NotRequired[
        "capo_kinesis.types.dead_letter_configuration.DeadLetterConfiguration"
    ]
    """<p>The dead-letter handling configuration for the queue. If you omit this attribute, dead-letter handling is enabled with a <code>MaxReceiveCount</code> of 6. If you specify it with a <code>TargetType</code> of <code>BUILT_IN</code>, you must also specify <code>MaxReceiveCount</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueueAttributes) -> dict:
    out: dict = {}
    if "visibility_timeout_seconds" in value:
        out["VisibilityTimeoutSeconds"] = value["visibility_timeout_seconds"]
    if "dead_letter_configuration" in value:
        import capo_kinesis.types.dead_letter_configuration

        out["DeadLetterConfiguration"] = (
            capo_kinesis.types.dead_letter_configuration.serialize_aws_json_1_1(
                value["dead_letter_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> QueueAttributes:
    out: QueueAttributes = {}  # type: ignore[typeddict-item]
    if data.get("VisibilityTimeoutSeconds") is not None:
        out["visibility_timeout_seconds"] = data["VisibilityTimeoutSeconds"]
    if data.get("DeadLetterConfiguration") is not None:
        import capo_kinesis.types.dead_letter_configuration

        out["dead_letter_configuration"] = (
            capo_kinesis.types.dead_letter_configuration.deserialize_aws_json_1_1(
                data["DeadLetterConfiguration"]
            )
        )
    return out
