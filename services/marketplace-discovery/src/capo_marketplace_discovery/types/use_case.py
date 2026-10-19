"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#UseCase``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.non_empty_string


class UseCase(TypedDict, closed=True):
    description: "capo_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>A description of the use case.</p>"""
    display_name: "capo_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The human-readable name of the use case.</p>"""
    value: "capo_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The machine-readable identifier of the use case.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UseCase) -> dict:
    out: dict = {}
    out["description"] = value["description"]
    out["displayName"] = value["display_name"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> UseCase:
    out: UseCase = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
