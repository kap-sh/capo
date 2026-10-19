"""Generated from Smithy shape ``com.amazonaws.connect#BatchUpdateDataTableValueFailureResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.data_table_name
    import capo_connect.types.primary_values_set
    import capo_connect.types.string


class BatchUpdateDataTableValueFailureResult(TypedDict, closed=True):
    primary_values: "capo_connect.types.primary_values_set.PrimaryValuesSet"
    """<p>The result's primary values.</p>"""
    attribute_name: "capo_connect.types.data_table_name.DataTableName"
    """<p>The result's attribute name.</p>"""
    message: "capo_connect.types.string.String"
    """<p>The result's message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateDataTableValueFailureResult) -> dict:
    out: dict = {}
    import capo_connect.types.primary_values_set

    out["PrimaryValues"] = capo_connect.types.primary_values_set.serialize_json(
        value["primary_values"]
    )
    out["AttributeName"] = value["attribute_name"]
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchUpdateDataTableValueFailureResult:
    out: BatchUpdateDataTableValueFailureResult = {}  # type: ignore[typeddict-item]
    if data.get("PrimaryValues") is not None:
        import capo_connect.types.primary_values_set

        out["primary_values"] = capo_connect.types.primary_values_set.deserialize_json(
            data["PrimaryValues"]
        )
    else:
        out["primary_values"] = []
    if data.get("AttributeName") is not None:
        out["attribute_name"] = data["AttributeName"]
    else:
        out["attribute_name"] = ""
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    return out
