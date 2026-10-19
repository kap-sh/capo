"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EventsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.event_parameters_list


class EventsConfig(TypedDict, closed=True):
    event_parameters_list: (
        "capo_customer_profiles.types.event_parameters_list.EventParametersList"
    )
    """<p>A list of event parameters configurations that specify how different event types should be handled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventsConfig) -> dict:
    out: dict = {}
    import capo_customer_profiles.types.event_parameters_list

    out["EventParametersList"] = (
        capo_customer_profiles.types.event_parameters_list.serialize_json(
            value["event_parameters_list"]
        )
    )
    return out


def deserialize_json(data: dict) -> EventsConfig:
    out: EventsConfig = {}  # type: ignore[typeddict-item]
    if data.get("EventParametersList") is not None:
        import capo_customer_profiles.types.event_parameters_list

        out["event_parameters_list"] = (
            capo_customer_profiles.types.event_parameters_list.deserialize_json(
                data["EventParametersList"]
            )
        )
    else:
        out["event_parameters_list"] = []
    return out
