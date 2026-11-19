"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PopulationAnalysisJobParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_template_arn


class PopulationAnalysisJobParameters(TypedDict, closed=True):
    analysis_template_arn: (
        "capo_cleanrooms.types.analysis_template_arn.AnalysisTemplateArn"
    )
    """<p>Specifies the ARN of the PySpark analysis template that populates the intermediate table. Provide this ARN in <code>jobParameters</code> when you populate the intermediate table with results from a PySpark job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PopulationAnalysisJobParameters) -> dict:
    out: dict = {}
    out["analysisTemplateArn"] = value["analysis_template_arn"]
    return out


def deserialize_json(data: dict) -> PopulationAnalysisJobParameters:
    out: PopulationAnalysisJobParameters = {}  # type: ignore[typeddict-item]
    if data.get("analysisTemplateArn") is not None:
        out["analysis_template_arn"] = data["analysisTemplateArn"]
    else:
        out["analysis_template_arn"] = ""
    return out
