"""Generated from Smithy shape ``com.amazonaws.iot#AggregationType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.aggregation_type_name
    import capo_iot.types.aggregation_type_values


class AggregationType(TypedDict, closed=True):
    name: "capo_iot.types.aggregation_type_name.AggregationTypeName"
    """<p>The name of the aggregation type.</p>"""
    values: NotRequired["capo_iot.types.aggregation_type_values.AggregationTypeValues"]
    """<p>A list of the values of aggregation types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AggregationType) -> dict:
    out: dict = {}
    import capo_iot.types.aggregation_type_name

    out["name"] = capo_iot.types.aggregation_type_name.serialize_json(value["name"])
    if "values" in value:
        import capo_iot.types.aggregation_type_values

        out["values"] = capo_iot.types.aggregation_type_values.serialize_json(
            value["values"]
        )
    return out


def deserialize_json(data: dict) -> AggregationType:
    out: AggregationType = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_iot.types.aggregation_type_name

        out["name"] = capo_iot.types.aggregation_type_name.deserialize_json(
            data["name"]
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_iot.types.aggregation_type_name.AggregationTypeName", ""
        )
    if data.get("values") is not None:
        import capo_iot.types.aggregation_type_values

        out["values"] = capo_iot.types.aggregation_type_values.deserialize_json(
            data["values"]
        )
    return out
