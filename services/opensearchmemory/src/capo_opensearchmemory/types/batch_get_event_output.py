"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#BatchGetEventOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.batch_get_event_error_list
    import capo_opensearchmemory.types.event_list


class BatchGetEventOutput(TypedDict, closed=True):
    events: "capo_opensearchmemory.types.event_list.EventList"
    """<p>The events found, in the order that you requested their IDs.</p>"""
    errors: (
        "capo_opensearchmemory.types.batch_get_event_error_list.BatchGetEventErrorList"
    )
    """<p>An entry for each requested event that the call didn't return. Empty when the call returned every event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetEventOutput) -> dict:
    out: dict = {}
    import capo_opensearchmemory.types.event_list

    out["events"] = capo_opensearchmemory.types.event_list.serialize_aws_json_1_0(
        value["events"]
    )
    import capo_opensearchmemory.types.batch_get_event_error_list

    out["errors"] = (
        capo_opensearchmemory.types.batch_get_event_error_list.serialize_aws_json_1_0(
            value["errors"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchGetEventOutput:
    out: BatchGetEventOutput = {}  # type: ignore[typeddict-item]
    if data.get("events") is not None:
        import capo_opensearchmemory.types.event_list

        out["events"] = capo_opensearchmemory.types.event_list.deserialize_aws_json_1_0(
            data["events"]
        )
    else:
        out["events"] = []
    if data.get("errors") is not None:
        import capo_opensearchmemory.types.batch_get_event_error_list

        out["errors"] = (
            capo_opensearchmemory.types.batch_get_event_error_list.deserialize_aws_json_1_0(
                data["errors"]
            )
        )
    else:
        out["errors"] = []
    return out


def redact_sensitive(value: BatchGetEventOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "events" in value:
        import capo_opensearchmemory.types.event_list

        out["events"] = capo_opensearchmemory.types.event_list.redact_sensitive(
            value["events"]
        )
    return out
