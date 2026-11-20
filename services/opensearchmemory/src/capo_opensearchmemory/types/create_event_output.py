"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#CreateEventOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_opensearchmemory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearchmemory.types.event_detail


class CreateEventOutput(TypedDict, closed=True):
    event: "capo_opensearchmemory.types.event_detail.EventDetail"
    """<p>The stored event's identifiers: its ID, session, and timestamp.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateEventOutput) -> dict:
    out: dict = {}
    import capo_opensearchmemory.types.event_detail

    out["event"] = capo_opensearchmemory.types.event_detail.serialize_aws_json_1_0(
        value["event"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateEventOutput:
    out: CreateEventOutput = {}  # type: ignore[typeddict-item]
    if data.get("event") is not None:
        import capo_opensearchmemory.types.event_detail

        out["event"] = (
            capo_opensearchmemory.types.event_detail.deserialize_aws_json_1_0(
                data["event"]
            )
        )
    else:
        raise DeserializationError("CreateEventOutput.event required")
    return out
