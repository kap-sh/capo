"""Generated from Smithy shape ``com.amazonaws.resiliencehub#Field``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.field_aggregation_type
    import capo_resiliencehub.types.string255


class Field(TypedDict, closed=True):
    name: "capo_resiliencehub.types.string255.String255"
    """<p>Name of the field.</p>"""
    aggregation: NotRequired[
        "capo_resiliencehub.types.field_aggregation_type.FieldAggregationType"
    ]
    """<p>(Optional) Indicates the type of aggregation or summary operation (such as Sum, Average, and so on) to be performed on a particular field or set of data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Field) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "aggregation" in value:
        import capo_resiliencehub.types.field_aggregation_type

        out["aggregation"] = (
            capo_resiliencehub.types.field_aggregation_type.serialize_json(
                value["aggregation"]
            )
        )
    return out


def deserialize_json(data: dict) -> Field:
    out: Field = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("aggregation") is not None:
        import capo_resiliencehub.types.field_aggregation_type

        out["aggregation"] = (
            capo_resiliencehub.types.field_aggregation_type.deserialize_json(
                data["aggregation"]
            )
        )
    return out
