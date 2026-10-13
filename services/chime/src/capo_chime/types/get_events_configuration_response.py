"""Generated from Smithy shape ``com.amazonaws.chime#GetEventsConfigurationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.events_configuration


class GetEventsConfigurationResponse(TypedDict, closed=True):
    events_configuration: NotRequired[
        "capo_chime.types.events_configuration.EventsConfiguration"
    ]
    """<p>The events configuration details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEventsConfigurationResponse) -> dict:
    out: dict = {}
    if "events_configuration" in value:
        import capo_chime.types.events_configuration

        out["EventsConfiguration"] = (
            capo_chime.types.events_configuration.serialize_json(
                value["events_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetEventsConfigurationResponse:
    out: GetEventsConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("EventsConfiguration") is not None:
        import capo_chime.types.events_configuration

        out["events_configuration"] = (
            capo_chime.types.events_configuration.deserialize_json(
                data["EventsConfiguration"]
            )
        )
    return out


def redact_sensitive(value: GetEventsConfigurationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "events_configuration" in value:
        import capo_chime.types.events_configuration

        out["events_configuration"] = (
            capo_chime.types.events_configuration.redact_sensitive(
                value["events_configuration"]
            )
        )
    return out
