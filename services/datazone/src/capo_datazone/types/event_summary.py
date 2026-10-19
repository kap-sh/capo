"""Generated from Smithy shape ``com.amazonaws.datazone#EventSummary``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.open_lineage_run_event_summary


class _EventSummary_openLineageRunEventSummary(TypedDict, closed=True):
    openLineageRunEventSummary: (
        "capo_datazone.types.open_lineage_run_event_summary.OpenLineageRunEventSummary"
    )


EventSummary: TypeAlias = _EventSummary_openLineageRunEventSummary | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: EventSummary) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"EventSummary: cannot serialize unknown variant {value.name!r}"
        )
    elif "openLineageRunEventSummary" in value:
        import capo_datazone.types.open_lineage_run_event_summary

        return {
            "openLineageRunEventSummary": capo_datazone.types.open_lineage_run_event_summary.serialize_json(
                value["openLineageRunEventSummary"]
            )
        }
    else:
        raise SerializationError("EventSummary: no variant present")


def deserialize_json(data: dict) -> EventSummary:
    if data.get("openLineageRunEventSummary") is not None:
        import capo_datazone.types.open_lineage_run_event_summary

        return {
            "openLineageRunEventSummary": capo_datazone.types.open_lineage_run_event_summary.deserialize_json(
                data["openLineageRunEventSummary"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("EventSummary: no recognized variant key")
