"""Generated from Smithy shape ``com.amazonaws.devopsguru#PerformanceInsightsReferenceData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.performance_insights_reference_comparison_values
    import capo_devops_guru.types.performance_insights_reference_name


class PerformanceInsightsReferenceData(TypedDict, closed=True):
    name: NotRequired[
        "capo_devops_guru.types.performance_insights_reference_name.PerformanceInsightsReferenceName"
    ]
    """<p>The name of the reference data.</p>"""
    comparison_values: NotRequired[
        "capo_devops_guru.types.performance_insights_reference_comparison_values.PerformanceInsightsReferenceComparisonValues"
    ]
    """<p>The specific reference values used to evaluate the Performance Insights. For more information, see <code> <a href="https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_PerformanceInsightsReferenceComparisonValues.html">PerformanceInsightsReferenceComparisonValues</a> </code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PerformanceInsightsReferenceData) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "comparison_values" in value:
        import capo_devops_guru.types.performance_insights_reference_comparison_values

        out["ComparisonValues"] = (
            capo_devops_guru.types.performance_insights_reference_comparison_values.serialize_json(
                value["comparison_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> PerformanceInsightsReferenceData:
    out: PerformanceInsightsReferenceData = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ComparisonValues") is not None:
        import capo_devops_guru.types.performance_insights_reference_comparison_values

        out["comparison_values"] = (
            capo_devops_guru.types.performance_insights_reference_comparison_values.deserialize_json(
                data["ComparisonValues"]
            )
        )
    return out
