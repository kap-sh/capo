"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#Selector``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.bounded_string
    import capo_marketplace_discovery.types.selector_type


class Selector(TypedDict, closed=True):
    type: "capo_marketplace_discovery.types.selector_type.SelectorType"
    """<p>The category of the selector, such as <code>Duration</code>.</p>"""
    value: "capo_marketplace_discovery.types.bounded_string.BoundedString"
    """<p>The value of the selector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Selector) -> dict:
    out: dict = {}
    import capo_marketplace_discovery.types.selector_type

    out["type"] = capo_marketplace_discovery.types.selector_type.serialize_json(
        value["type"]
    )
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Selector:
    out: Selector = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_marketplace_discovery.types.selector_type

        out["type"] = capo_marketplace_discovery.types.selector_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_marketplace_discovery.types.selector_type.SelectorType", ""
        )
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
