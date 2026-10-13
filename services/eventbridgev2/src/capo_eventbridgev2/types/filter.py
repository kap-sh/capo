"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#Filter``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_eventbridgev2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eventbridgev2.types.event_pattern
    import capo_eventbridgev2.types.filter_scope


class Filter(TypedDict, closed=True):
    pattern: "capo_eventbridgev2.types.event_pattern.EventPattern"
    scope: "capo_eventbridgev2.types.filter_scope.FilterScope"


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Filter) -> dict:
    out: dict = {}
    out["Pattern"] = value["pattern"]
    import capo_eventbridgev2.types.filter_scope

    out["Scope"] = capo_eventbridgev2.types.filter_scope.serialize_cbor(value["scope"])
    return out


def deserialize_cbor(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if data.get("Pattern") is not None:
        out["pattern"] = data["Pattern"]
    else:
        raise DeserializationError("Filter.pattern required")
    if data.get("Scope") is not None:
        import capo_eventbridgev2.types.filter_scope

        out["scope"] = capo_eventbridgev2.types.filter_scope.deserialize_cbor(
            data["Scope"]
        )
    else:
        raise DeserializationError("Filter.scope required")
    return out


def redact_sensitive(value: Filter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "pattern" in value:
        out["pattern"] = "*** Sensitive Data Redacted ***"
    return out
