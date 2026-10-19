"""Generated from Smithy shape ``com.amazonaws.billing#DimensionValues``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billing.types.dimension
    import capo_billing.types.values


class DimensionValues(TypedDict, closed=True):
    key: "capo_billing.types.dimension.Dimension"
    """<p> The names of the metadata types that you can use to filter and group your results. </p>"""
    values: "capo_billing.types.values.Values"
    """<p> The metadata values that you can use to filter and group your results. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DimensionValues) -> dict:
    out: dict = {}
    import capo_billing.types.dimension

    out["key"] = capo_billing.types.dimension.serialize_aws_json_1_0(value["key"])
    import capo_billing.types.values

    out["values"] = capo_billing.types.values.serialize_aws_json_1_0(value["values"])
    return out


def deserialize_aws_json_1_0(data: dict) -> DimensionValues:
    out: DimensionValues = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        import capo_billing.types.dimension

        out["key"] = capo_billing.types.dimension.deserialize_aws_json_1_0(data["key"])
    else:
        import typing

        out["key"] = typing.cast("capo_billing.types.dimension.Dimension", "")
    if data.get("values") is not None:
        import capo_billing.types.values

        out["values"] = capo_billing.types.values.deserialize_aws_json_1_0(
            data["values"]
        )
    else:
        out["values"] = []
    return out
