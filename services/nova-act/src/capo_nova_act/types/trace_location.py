"""Generated from Smithy shape ``com.amazonaws.novaact#TraceLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_nova_act.types.non_blank_string
    import capo_nova_act.types.trace_location_type


class TraceLocation(TypedDict, closed=True):
    location_type: "capo_nova_act.types.trace_location_type.TraceLocationType"
    """<p>The type of storage location for the trace data.</p>"""
    location: "capo_nova_act.types.non_blank_string.NonBlankString"
    """<p>The specific location where the trace data is stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TraceLocation) -> dict:
    out: dict = {}
    import capo_nova_act.types.trace_location_type

    out["locationType"] = capo_nova_act.types.trace_location_type.serialize_json(
        value["location_type"]
    )
    out["location"] = value["location"]
    return out


def deserialize_json(data: dict) -> TraceLocation:
    out: TraceLocation = {}  # type: ignore[typeddict-item]
    if data.get("locationType") is not None:
        import capo_nova_act.types.trace_location_type

        out["location_type"] = capo_nova_act.types.trace_location_type.deserialize_json(
            data["locationType"]
        )
    else:
        import typing

        out["location_type"] = typing.cast(
            "capo_nova_act.types.trace_location_type.TraceLocationType", ""
        )
    if data.get("location") is not None:
        out["location"] = data["location"]
    else:
        out["location"] = ""
    return out
