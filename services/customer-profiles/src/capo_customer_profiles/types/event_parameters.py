"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EventParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.double
    import capo_customer_profiles.types.event_parameters_event_type_string
    import capo_customer_profiles.types.event_parameters_event_weight_double


class EventParameters(TypedDict, closed=True):
    event_type: "capo_customer_profiles.types.event_parameters_event_type_string.EventParametersEventTypeString"
    """<p>The type of event being tracked (e.g., 'click', 'purchase', 'view').</p>"""
    event_value_threshold: NotRequired["capo_customer_profiles.types.double.Double"]
    """<p>The minimum value threshold that an event must meet to be considered valid.</p>"""
    event_weight: NotRequired[
        "capo_customer_profiles.types.event_parameters_event_weight_double.EventParametersEventWeightDouble"
    ]
    """<p>The weight of the event type. A higher weight means higher importance of the event type for the created solution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventParameters) -> dict:
    out: dict = {}
    out["EventType"] = value["event_type"]
    if "event_value_threshold" in value:
        out["EventValueThreshold"] = (
            "NaN"
            if value["event_value_threshold"] != value["event_value_threshold"]
            else "Infinity"
            if value["event_value_threshold"] == float("inf")
            else "-Infinity"
            if value["event_value_threshold"] == float("-inf")
            else value["event_value_threshold"]
        )
    if "event_weight" in value:
        out["EventWeight"] = (
            "NaN"
            if value["event_weight"] != value["event_weight"]
            else "Infinity"
            if value["event_weight"] == float("inf")
            else "-Infinity"
            if value["event_weight"] == float("-inf")
            else value["event_weight"]
        )
    return out


def deserialize_json(data: dict) -> EventParameters:
    out: EventParameters = {}  # type: ignore[typeddict-item]
    if data.get("EventType") is not None:
        out["event_type"] = data["EventType"]
    else:
        out["event_type"] = ""
    if data.get("EventValueThreshold") is not None:
        out["event_value_threshold"] = float(data["EventValueThreshold"])
    if data.get("EventWeight") is not None:
        out["event_weight"] = float(data["EventWeight"])
    return out
