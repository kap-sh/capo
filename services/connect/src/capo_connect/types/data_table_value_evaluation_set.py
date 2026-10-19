"""Generated from Smithy shape ``com.amazonaws.connect#DataTableValueEvaluationSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.attribute_name_list
    import capo_connect.types.primary_values_set


class DataTableValueEvaluationSet(TypedDict, closed=True):
    primary_values: NotRequired[
        "capo_connect.types.primary_values_set.PrimaryValuesSet"
    ]
    """<p>The set's primary values.</p>"""
    attribute_names: "capo_connect.types.attribute_name_list.AttributeNameList"
    """<p>The set's attribute names.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataTableValueEvaluationSet) -> dict:
    out: dict = {}
    if "primary_values" in value:
        import capo_connect.types.primary_values_set

        out["PrimaryValues"] = capo_connect.types.primary_values_set.serialize_json(
            value["primary_values"]
        )
    import capo_connect.types.attribute_name_list

    out["AttributeNames"] = capo_connect.types.attribute_name_list.serialize_json(
        value["attribute_names"]
    )
    return out


def deserialize_json(data: dict) -> DataTableValueEvaluationSet:
    out: DataTableValueEvaluationSet = {}  # type: ignore[typeddict-item]
    if data.get("PrimaryValues") is not None:
        import capo_connect.types.primary_values_set

        out["primary_values"] = capo_connect.types.primary_values_set.deserialize_json(
            data["PrimaryValues"]
        )
    if data.get("AttributeNames") is not None:
        import capo_connect.types.attribute_name_list

        out["attribute_names"] = (
            capo_connect.types.attribute_name_list.deserialize_json(
                data["AttributeNames"]
            )
        )
    else:
        out["attribute_names"] = []
    return out
