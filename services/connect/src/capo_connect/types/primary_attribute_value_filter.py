"""Generated from Smithy shape ``com.amazonaws.connect#PrimaryAttributeValueFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.data_table_name
    import capo_connect.types.value_list


class PrimaryAttributeValueFilter(TypedDict, closed=True):
    attribute_name: "capo_connect.types.data_table_name.DataTableName"
    """<p>The filter's attribute name.</p>"""
    values: "capo_connect.types.value_list.ValueList"
    """<p>The filter's values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrimaryAttributeValueFilter) -> dict:
    out: dict = {}
    out["AttributeName"] = value["attribute_name"]
    import capo_connect.types.value_list

    out["Values"] = capo_connect.types.value_list.serialize_json(value["values"])
    return out


def deserialize_json(data: dict) -> PrimaryAttributeValueFilter:
    out: PrimaryAttributeValueFilter = {}  # type: ignore[typeddict-item]
    if data.get("AttributeName") is not None:
        out["attribute_name"] = data["AttributeName"]
    else:
        out["attribute_name"] = ""
    if data.get("Values") is not None:
        import capo_connect.types.value_list

        out["values"] = capo_connect.types.value_list.deserialize_json(data["Values"])
    else:
        out["values"] = []
    return out
