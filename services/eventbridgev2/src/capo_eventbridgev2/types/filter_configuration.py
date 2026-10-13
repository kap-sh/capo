"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#FilterConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.filter_language
    import capo_eventbridgev2.types.filter_list


class FilterConfiguration(TypedDict, closed=True):
    language: NotRequired["capo_eventbridgev2.types.filter_language.FilterLanguage"]
    """Defaults to EVENT_BRIDGE_PATTERN when not specified."""
    filters: NotRequired["capo_eventbridgev2.types.filter_list.FilterList"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FilterConfiguration) -> dict:
    out: dict = {}
    if "language" in value:
        import capo_eventbridgev2.types.filter_language

        out["Language"] = capo_eventbridgev2.types.filter_language.serialize_cbor(
            value["language"]
        )
    if "filters" in value:
        import capo_eventbridgev2.types.filter_list

        out["Filters"] = capo_eventbridgev2.types.filter_list.serialize_cbor(
            value["filters"]
        )
    return out


def deserialize_cbor(data: dict) -> FilterConfiguration:
    out: FilterConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Language") is not None:
        import capo_eventbridgev2.types.filter_language

        out["language"] = capo_eventbridgev2.types.filter_language.deserialize_cbor(
            data["Language"]
        )
    if data.get("Filters") is not None:
        import capo_eventbridgev2.types.filter_list

        out["filters"] = capo_eventbridgev2.types.filter_list.deserialize_cbor(
            data["Filters"]
        )
    return out


def redact_sensitive(value: FilterConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "filters" in value:
        import capo_eventbridgev2.types.filter_list

        out["filters"] = capo_eventbridgev2.types.filter_list.redact_sensitive(
            value["filters"]
        )
    return out
