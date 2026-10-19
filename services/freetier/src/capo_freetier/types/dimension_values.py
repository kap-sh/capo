"""Generated from Smithy shape ``com.amazonaws.freetier#DimensionValues``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_freetier.types.dimension
    import capo_freetier.types.match_options
    import capo_freetier.types.values


class DimensionValues(TypedDict, closed=True):
    key: "capo_freetier.types.dimension.Dimension"
    """<p>The name of the dimension that you want to filter on.</p>"""
    values: "capo_freetier.types.values.Values"
    """<p>The metadata values you can specify to filter upon, so that the results all match at least one of the specified values.</p>"""
    match_options: "capo_freetier.types.match_options.MatchOptions"
    """<p>The match options that you can use to filter your results. You can specify only one of these values in the array.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DimensionValues) -> dict:
    out: dict = {}
    import capo_freetier.types.dimension

    out["Key"] = capo_freetier.types.dimension.serialize_aws_json_1_0(value["key"])
    import capo_freetier.types.values

    out["Values"] = capo_freetier.types.values.serialize_aws_json_1_0(value["values"])
    import capo_freetier.types.match_options

    out["MatchOptions"] = capo_freetier.types.match_options.serialize_aws_json_1_0(
        value["match_options"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DimensionValues:
    out: DimensionValues = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        import capo_freetier.types.dimension

        out["key"] = capo_freetier.types.dimension.deserialize_aws_json_1_0(data["Key"])
    else:
        import typing

        out["key"] = typing.cast("capo_freetier.types.dimension.Dimension", "")
    if data.get("Values") is not None:
        import capo_freetier.types.values

        out["values"] = capo_freetier.types.values.deserialize_aws_json_1_0(
            data["Values"]
        )
    else:
        out["values"] = []
    if data.get("MatchOptions") is not None:
        import capo_freetier.types.match_options

        out["match_options"] = (
            capo_freetier.types.match_options.deserialize_aws_json_1_0(
                data["MatchOptions"]
            )
        )
    else:
        out["match_options"] = []
    return out
