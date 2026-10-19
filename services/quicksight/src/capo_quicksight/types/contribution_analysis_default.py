"""Generated from Smithy shape ``com.amazonaws.quicksight#ContributionAnalysisDefault``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.contributor_dimension_list
    import capo_quicksight.types.field_id


class ContributionAnalysisDefault(TypedDict, closed=True):
    measure_field_id: "capo_quicksight.types.field_id.FieldId"
    """<p>The measure field that is used in the contribution analysis.</p>"""
    contributor_dimensions: (
        "capo_quicksight.types.contributor_dimension_list.ContributorDimensionList"
    )
    """<p>The dimensions columns that are used in the contribution analysis, usually a list of <code>ColumnIdentifiers</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContributionAnalysisDefault) -> dict:
    out: dict = {}
    out["MeasureFieldId"] = value["measure_field_id"]
    import capo_quicksight.types.contributor_dimension_list

    out["ContributorDimensions"] = (
        capo_quicksight.types.contributor_dimension_list.serialize_json(
            value["contributor_dimensions"]
        )
    )
    return out


def deserialize_json(data: dict) -> ContributionAnalysisDefault:
    out: ContributionAnalysisDefault = {}  # type: ignore[typeddict-item]
    if data.get("MeasureFieldId") is not None:
        out["measure_field_id"] = data["MeasureFieldId"]
    else:
        out["measure_field_id"] = ""
    if data.get("ContributorDimensions") is not None:
        import capo_quicksight.types.contributor_dimension_list

        out["contributor_dimensions"] = (
            capo_quicksight.types.contributor_dimension_list.deserialize_json(
                data["ContributorDimensions"]
            )
        )
    else:
        out["contributor_dimensions"] = []
    return out
