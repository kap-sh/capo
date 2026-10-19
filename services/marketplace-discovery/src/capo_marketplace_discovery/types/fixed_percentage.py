"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#FixedPercentage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.bounded_string


class FixedPercentage(TypedDict, closed=True):
    percentage_value: "capo_marketplace_discovery.types.bounded_string.BoundedString"
    """<p>The percentage value applied at each renewal cycle.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FixedPercentage) -> dict:
    out: dict = {}
    out["percentageValue"] = value["percentage_value"]
    return out


def deserialize_json(data: dict) -> FixedPercentage:
    out: FixedPercentage = {}  # type: ignore[typeddict-item]
    if data.get("percentageValue") is not None:
        out["percentage_value"] = data["percentageValue"]
    else:
        out["percentage_value"] = ""
    return out
