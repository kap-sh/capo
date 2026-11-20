"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#GetEventOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_opensearchmemory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearchmemory.types.event


class GetEventOutput(TypedDict, closed=True):
    event: "capo_opensearchmemory.types.event.Event"
    """<p>The event, including its payload.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEventOutput) -> dict:
    out: dict = {}
    import capo_opensearchmemory.types.event

    out["event"] = capo_opensearchmemory.types.event.serialize_aws_json_1_0(
        value["event"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEventOutput:
    out: GetEventOutput = {}  # type: ignore[typeddict-item]
    if data.get("event") is not None:
        import capo_opensearchmemory.types.event

        out["event"] = capo_opensearchmemory.types.event.deserialize_aws_json_1_0(
            data["event"]
        )
    else:
        raise DeserializationError("GetEventOutput.event required")
    return out


def redact_sensitive(value: GetEventOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "event" in value:
        import capo_opensearchmemory.types.event

        out["event"] = capo_opensearchmemory.types.event.redact_sensitive(
            value["event"]
        )
    return out
