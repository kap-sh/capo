"""Generated from Smithy shape ``com.amazonaws.connect#DataTableValueIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.data_table_name
    import capo_connect.types.primary_values_set


class DataTableValueIdentifier(TypedDict, closed=True):
    primary_values: NotRequired[
        "capo_connect.types.primary_values_set.PrimaryValuesSet"
    ]
    """<p>The identifier's primary values.</p>"""
    attribute_name: "capo_connect.types.data_table_name.DataTableName"
    """<p>The identifier's attribute name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataTableValueIdentifier) -> dict:
    out: dict = {}
    if "primary_values" in value:
        import capo_connect.types.primary_values_set

        out["PrimaryValues"] = capo_connect.types.primary_values_set.serialize_json(
            value["primary_values"]
        )
    out["AttributeName"] = value["attribute_name"]
    return out


def deserialize_json(data: dict) -> DataTableValueIdentifier:
    out: DataTableValueIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("PrimaryValues") is not None:
        import capo_connect.types.primary_values_set

        out["primary_values"] = capo_connect.types.primary_values_set.deserialize_json(
            data["PrimaryValues"]
        )
    if data.get("AttributeName") is not None:
        out["attribute_name"] = data["AttributeName"]
    else:
        out["attribute_name"] = ""
    return out
