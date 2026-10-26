"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ItemIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_incidents.types.item_type
    import capo_ssm_incidents.types.item_value


class ItemIdentifier(TypedDict, closed=True):
    value: "capo_ssm_incidents.types.item_value.ItemValue"
    """<p>Details about the related item.</p>"""
    type: "capo_ssm_incidents.types.item_type.ItemType"
    """<p>The type of related item. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ItemIdentifier) -> dict:
    out: dict = {}
    import capo_ssm_incidents.types.item_value

    out["value"] = capo_ssm_incidents.types.item_value.serialize_json(value["value"])
    out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> ItemIdentifier:
    out: ItemIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        import capo_ssm_incidents.types.item_value

        out["value"] = capo_ssm_incidents.types.item_value.deserialize_json(
            data["value"]
        )
    else:
        out["value"] = {"$unknown": {"name": ""}}
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    return out
