"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.attribute_filters
    import capo_application_signals.types.attributes
    import capo_application_signals.types.latest_change_events


class ServiceState(TypedDict, closed=True):
    attribute_filters: NotRequired[
        "capo_application_signals.types.attribute_filters.AttributeFilters"
    ]
    """<p>The attribute filters that were applied when retrieving this service state information.</p>"""
    service: "capo_application_signals.types.attributes.Attributes"
    """<p>The key attributes that identify this service, including Type, Name, and Environment information.</p>"""
    latest_change_events: (
        "capo_application_signals.types.latest_change_events.LatestChangeEvents"
    )
    """<p>An array containing the most recent change events for this service, such as deployments, with information about when they occurred and who initiated them.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceState) -> dict:
    out: dict = {}
    if "attribute_filters" in value:
        import capo_application_signals.types.attribute_filters

        out["AttributeFilters"] = (
            capo_application_signals.types.attribute_filters.serialize_json(
                value["attribute_filters"]
            )
        )
    import capo_application_signals.types.attributes

    out["Service"] = capo_application_signals.types.attributes.serialize_json(
        value["service"]
    )
    import capo_application_signals.types.latest_change_events

    out["LatestChangeEvents"] = (
        capo_application_signals.types.latest_change_events.serialize_json(
            value["latest_change_events"]
        )
    )
    return out


def deserialize_json(data: dict) -> ServiceState:
    out: ServiceState = {}  # type: ignore[typeddict-item]
    if data.get("AttributeFilters") is not None:
        import capo_application_signals.types.attribute_filters

        out["attribute_filters"] = (
            capo_application_signals.types.attribute_filters.deserialize_json(
                data["AttributeFilters"]
            )
        )
    if data.get("Service") is not None:
        import capo_application_signals.types.attributes

        out["service"] = capo_application_signals.types.attributes.deserialize_json(
            data["Service"]
        )
    else:
        out["service"] = {}
    if data.get("LatestChangeEvents") is not None:
        import capo_application_signals.types.latest_change_events

        out["latest_change_events"] = (
            capo_application_signals.types.latest_change_events.deserialize_json(
                data["LatestChangeEvents"]
            )
        )
    else:
        out["latest_change_events"] = []
    return out
