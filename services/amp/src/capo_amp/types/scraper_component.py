"""Generated from Smithy shape ``com.amazonaws.amp#ScraperComponent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amp.types.component_config
    import capo_amp.types.scraper_component_type


class ScraperComponent(TypedDict, closed=True):
    type: "capo_amp.types.scraper_component_type.ScraperComponentType"
    """<p>The type of the scraper component.</p>"""
    config: NotRequired["capo_amp.types.component_config.ComponentConfig"]
    """<p>The configuration settings for the scraper component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScraperComponent) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    if "config" in value:
        import capo_amp.types.component_config

        out["config"] = capo_amp.types.component_config.serialize_json(value["config"])
    return out


def deserialize_json(data: dict) -> ScraperComponent:
    out: ScraperComponent = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("config") is not None:
        import capo_amp.types.component_config

        out["config"] = capo_amp.types.component_config.deserialize_json(data["config"])
    return out
