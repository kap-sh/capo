"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#TemporalStatisticsConfigInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.group_by
    import capo_sagemaker_geospatial.types.string_list_input
    import capo_sagemaker_geospatial.types.temporal_statistics_list_input


class TemporalStatisticsConfigInput(TypedDict, closed=True):
    group_by: NotRequired["capo_sagemaker_geospatial.types.group_by.GroupBy"]
    """<p>The input for the temporal statistics grouping by time frequency option.</p>"""
    statistics: "capo_sagemaker_geospatial.types.temporal_statistics_list_input.TemporalStatisticsListInput"
    """<p>The list of the statistics method options.</p>"""
    target_bands: NotRequired[
        "capo_sagemaker_geospatial.types.string_list_input.StringListInput"
    ]
    """<p>The list of target band names for the temporal statistic to calculate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemporalStatisticsConfigInput) -> dict:
    out: dict = {}
    if "group_by" in value:
        out["GroupBy"] = value["group_by"]
    import capo_sagemaker_geospatial.types.temporal_statistics_list_input

    out["Statistics"] = (
        capo_sagemaker_geospatial.types.temporal_statistics_list_input.serialize_json(
            value["statistics"]
        )
    )
    if "target_bands" in value:
        import capo_sagemaker_geospatial.types.string_list_input

        out["TargetBands"] = (
            capo_sagemaker_geospatial.types.string_list_input.serialize_json(
                value["target_bands"]
            )
        )
    return out


def deserialize_json(data: dict) -> TemporalStatisticsConfigInput:
    out: TemporalStatisticsConfigInput = {}  # type: ignore[typeddict-item]
    if data.get("GroupBy") is not None:
        out["group_by"] = data["GroupBy"]
    if data.get("Statistics") is not None:
        import capo_sagemaker_geospatial.types.temporal_statistics_list_input

        out["statistics"] = (
            capo_sagemaker_geospatial.types.temporal_statistics_list_input.deserialize_json(
                data["Statistics"]
            )
        )
    else:
        out["statistics"] = []
    if data.get("TargetBands") is not None:
        import capo_sagemaker_geospatial.types.string_list_input

        out["target_bands"] = (
            capo_sagemaker_geospatial.types.string_list_input.deserialize_json(
                data["TargetBands"]
            )
        )
    return out
