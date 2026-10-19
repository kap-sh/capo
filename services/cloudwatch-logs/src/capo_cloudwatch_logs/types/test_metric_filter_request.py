"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#TestMetricFilterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.filter_pattern
    import capo_cloudwatch_logs.types.test_event_messages


class TestMetricFilterRequest(TypedDict, closed=True):
    filter_pattern: "capo_cloudwatch_logs.types.filter_pattern.FilterPattern"
    log_event_messages: (
        "capo_cloudwatch_logs.types.test_event_messages.TestEventMessages"
    )
    """<p>The log event messages to test.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestMetricFilterRequest) -> dict:
    out: dict = {}
    out["filterPattern"] = value["filter_pattern"]
    import capo_cloudwatch_logs.types.test_event_messages

    out["logEventMessages"] = (
        capo_cloudwatch_logs.types.test_event_messages.serialize_aws_json_1_1(
            value["log_event_messages"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TestMetricFilterRequest:
    out: TestMetricFilterRequest = {}  # type: ignore[typeddict-item]
    if data.get("filterPattern") is not None:
        out["filter_pattern"] = data["filterPattern"]
    else:
        out["filter_pattern"] = ""
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
