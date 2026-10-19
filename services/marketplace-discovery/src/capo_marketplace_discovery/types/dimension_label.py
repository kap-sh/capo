"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#DimensionLabel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.bounded_string
    import capo_marketplace_discovery.types.dimension_label_type


class DimensionLabel(TypedDict, closed=True):
    label_type: (
        "capo_marketplace_discovery.types.dimension_label_type.DimensionLabelType"
    )
    """<p>The type of the dimension label, such as <code>Region</code> or <code>SagemakerOption</code>.</p>"""
    label_value: "capo_marketplace_discovery.types.bounded_string.BoundedString"
    """<p>The value used to group dimensions together.</p>"""
    display_name: NotRequired[
        "capo_marketplace_discovery.types.bounded_string.BoundedString"
    ]
    """<p>The human-readable display name of the label.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DimensionLabel) -> dict:
    out: dict = {}
    import capo_marketplace_discovery.types.dimension_label_type

    out["labelType"] = (
        capo_marketplace_discovery.types.dimension_label_type.serialize_json(
            value["label_type"]
        )
    )
    out["labelValue"] = value["label_value"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> DimensionLabel:
    out: DimensionLabel = {}  # type: ignore[typeddict-item]
    if data.get("labelType") is not None:
        import capo_marketplace_discovery.types.dimension_label_type

        out["label_type"] = (
            capo_marketplace_discovery.types.dimension_label_type.deserialize_json(
                data["labelType"]
            )
        )
    else:
        import typing

        out["label_type"] = typing.cast(
            "capo_marketplace_discovery.types.dimension_label_type.DimensionLabelType",
            "",
        )
    if data.get("labelValue") is not None:
        out["label_value"] = data["labelValue"]
    else:
        out["label_value"] = ""
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    return out
