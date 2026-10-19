"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#DimensionValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.dimension
    import capo_bcm_dashboards.types.match_options
    import capo_bcm_dashboards.types.string_list


class DimensionValues(TypedDict, closed=True):
    key: "capo_bcm_dashboards.types.dimension.Dimension"
    """<p>The key of the dimension to filter on (for example, <code>SERVICE</code>, <code>USAGE_TYPE</code>, or <code>OPERATION</code>).</p>"""
    values: "capo_bcm_dashboards.types.string_list.StringList"
    """<p>The values to match for the specified dimension key.</p>"""
    match_options: NotRequired["capo_bcm_dashboards.types.match_options.MatchOptions"]
    """<p>The match options for dimension values, such as <code>EQUALS</code>, <code>CONTAINS</code>, <code>STARTS_WITH</code>, or <code>ENDS_WITH</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DimensionValues) -> dict:
    out: dict = {}
    import capo_bcm_dashboards.types.dimension

    out["key"] = capo_bcm_dashboards.types.dimension.serialize_aws_json_1_0(
        value["key"]
    )
    import capo_bcm_dashboards.types.string_list

    out["values"] = capo_bcm_dashboards.types.string_list.serialize_aws_json_1_0(
        value["values"]
    )
    if "match_options" in value:
        import capo_bcm_dashboards.types.match_options

        out["matchOptions"] = (
            capo_bcm_dashboards.types.match_options.serialize_aws_json_1_0(
                value["match_options"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DimensionValues:
    out: DimensionValues = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        import capo_bcm_dashboards.types.dimension

        out["key"] = capo_bcm_dashboards.types.dimension.deserialize_aws_json_1_0(
            data["key"]
        )
    else:
        import typing

        out["key"] = typing.cast("capo_bcm_dashboards.types.dimension.Dimension", "")
    if data.get("values") is not None:
        import capo_bcm_dashboards.types.string_list

        out["values"] = capo_bcm_dashboards.types.string_list.deserialize_aws_json_1_0(
            data["values"]
        )
    else:
        out["values"] = []
    if data.get("matchOptions") is not None:
        import capo_bcm_dashboards.types.match_options

        out["match_options"] = (
            capo_bcm_dashboards.types.match_options.deserialize_aws_json_1_0(
                data["matchOptions"]
            )
        )
    return out
