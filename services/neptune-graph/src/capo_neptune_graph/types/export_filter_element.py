"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ExportFilterElement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptune_graph.types.export_filter_property_map


class ExportFilterElement(TypedDict, closed=True):
    properties: NotRequired[
        "capo_neptune_graph.types.export_filter_property_map.ExportFilterPropertyMap"
    ]
    """<p>Each property is defined by a key-value pair, where the key is the desired output property name (e.g. "name"), and the value is an object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportFilterElement) -> dict:
    out: dict = {}
    if "properties" in value:
        import capo_neptune_graph.types.export_filter_property_map

        out["properties"] = (
            capo_neptune_graph.types.export_filter_property_map.serialize_json(
                value["properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExportFilterElement:
    out: ExportFilterElement = {}  # type: ignore[typeddict-item]
    if data.get("properties") is not None:
        import capo_neptune_graph.types.export_filter_property_map

        out["properties"] = (
            capo_neptune_graph.types.export_filter_property_map.deserialize_json(
                data["properties"]
            )
        )
    return out
