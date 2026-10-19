"""Generated from Smithy shape ``com.amazonaws.glue#EventBatchingCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.batch_size
    import capo_glue.types.batch_window


class EventBatchingCondition(TypedDict, closed=True):
    batch_size: "capo_glue.types.batch_size.BatchSize"
    """<p>Number of events that must be received from Amazon EventBridge before EventBridge event trigger fires.</p>"""
    batch_window: NotRequired["capo_glue.types.batch_window.BatchWindow"]
    """<p>Window of time in seconds after which EventBridge event trigger fires. Window starts when first event is received.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventBatchingCondition) -> dict:
    out: dict = {}
    out["BatchSize"] = value["batch_size"]
    if "batch_window" in value:
        out["BatchWindow"] = value["batch_window"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EventBatchingCondition:
    out: EventBatchingCondition = {}  # type: ignore[typeddict-item]
    if data.get("BatchSize") is not None:
        out["batch_size"] = data["BatchSize"]
    else:
        out["batch_size"] = 0
    if data.get("BatchWindow") is not None:
        out["batch_window"] = data["BatchWindow"]
    return out
