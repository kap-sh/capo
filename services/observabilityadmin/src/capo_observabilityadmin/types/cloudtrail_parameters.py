"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#CloudtrailParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.advanced_event_selectors


class CloudtrailParameters(TypedDict, closed=True):
    advanced_event_selectors: (
        "capo_observabilityadmin.types.advanced_event_selectors.AdvancedEventSelectors"
    )
    """<p> The advanced event selectors to use for filtering Amazon Web Services CloudTrail events. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudtrailParameters) -> dict:
    out: dict = {}
    import capo_observabilityadmin.types.advanced_event_selectors

    out["AdvancedEventSelectors"] = (
        capo_observabilityadmin.types.advanced_event_selectors.serialize_json(
            value["advanced_event_selectors"]
        )
    )
    return out


def deserialize_json(data: dict) -> CloudtrailParameters:
    out: CloudtrailParameters = {}  # type: ignore[typeddict-item]
    if data.get("AdvancedEventSelectors") is not None:
        import capo_observabilityadmin.types.advanced_event_selectors

        out["advanced_event_selectors"] = (
            capo_observabilityadmin.types.advanced_event_selectors.deserialize_json(
                data["AdvancedEventSelectors"]
            )
        )
    else:
        out["advanced_event_selectors"] = []
    return out
