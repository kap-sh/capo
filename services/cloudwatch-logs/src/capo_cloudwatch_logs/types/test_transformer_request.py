"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#TestTransformerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.processors
    import capo_cloudwatch_logs.types.test_event_messages


class TestTransformerRequest(TypedDict, closed=True):
    transformer_config: "capo_cloudwatch_logs.types.processors.Processors"
    """<p>This structure contains the configuration of this log transformer that you want to test. A log transformer is an array of processors, where each processor applies one type of transformation to the log events that are ingested.</p>"""
    log_event_messages: (
        "capo_cloudwatch_logs.types.test_event_messages.TestEventMessages"
    )
    """<p>An array of the raw log events that you want to use to test this transformer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestTransformerRequest) -> dict:
    out: dict = {}
    import capo_cloudwatch_logs.types.processors

    out["transformerConfig"] = (
        capo_cloudwatch_logs.types.processors.serialize_aws_json_1_1(
            value["transformer_config"]
        )
    )
    import capo_cloudwatch_logs.types.test_event_messages

    out["logEventMessages"] = (
        capo_cloudwatch_logs.types.test_event_messages.serialize_aws_json_1_1(
            value["log_event_messages"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TestTransformerRequest:
    out: TestTransformerRequest = {}  # type: ignore[typeddict-item]
    if data.get("transformerConfig") is not None:
        import capo_cloudwatch_logs.types.processors

        out["transformer_config"] = (
            capo_cloudwatch_logs.types.processors.deserialize_aws_json_1_1(
                data["transformerConfig"]
            )
        )
    else:
        out["transformer_config"] = []
    if data.get("logEventMessages") is not None:
        import capo_cloudwatch_logs.types.test_event_messages

        out["log_event_messages"] = (
            capo_cloudwatch_logs.types.test_event_messages.deserialize_aws_json_1_1(
                data["logEventMessages"]
            )
        )
    else:
        out["log_event_messages"] = []
    return out
