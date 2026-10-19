"""Generated from Smithy shape ``com.amazonaws.ssmsap#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_sap.types.filter_name
    import capo_ssm_sap.types.filter_operator
    import capo_ssm_sap.types.filter_value


class Filter(TypedDict, closed=True):
    name: "capo_ssm_sap.types.filter_name.FilterName"
    """<p>The name of the filter. Filter names are case-sensitive. </p>"""
    value: "capo_ssm_sap.types.filter_value.FilterValue"
    """<p>The filter values. Filter values are case-sensitive. If you specify multiple values for a filter, the values are joined with an OR, and the request returns all results that match any of the specified values</p>"""
    operator: "capo_ssm_sap.types.filter_operator.FilterOperator"
    """<p>The operator for the filter. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Filter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Value"] = value["value"]
    import capo_ssm_sap.types.filter_operator

    out["Operator"] = capo_ssm_sap.types.filter_operator.serialize_json(
        value["operator"]
    )
    return out


def deserialize_json(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    if data.get("Operator") is not None:
        import capo_ssm_sap.types.filter_operator

        out["operator"] = capo_ssm_sap.types.filter_operator.deserialize_json(
            data["Operator"]
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_ssm_sap.types.filter_operator.FilterOperator", ""
        )
    return out
