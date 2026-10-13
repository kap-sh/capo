"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobParameters``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_template_arn
    import capo_cleanrooms.types.job_parameter_map


class ProtectedJobParameters(TypedDict, closed=True):
    analysis_template_arn: (
        "capo_cleanrooms.types.analysis_template_arn.AnalysisTemplateArn"
    )
    """<p> The ARN of the analysis template.</p>"""
    parameters: NotRequired["capo_cleanrooms.types.job_parameter_map.JobParameterMap"]
    """<p>Runtime configuration values passed to the PySpark analysis script. Parameter names and types must match those defined in the analysis template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobParameters) -> dict:
    out: dict = {}
    out["analysisTemplateArn"] = value["analysis_template_arn"]
    if "parameters" in value:
        import capo_cleanrooms.types.job_parameter_map

        out["parameters"] = capo_cleanrooms.types.job_parameter_map.serialize_json(
            value["parameters"]
        )
    return out


def deserialize_json(data: dict) -> ProtectedJobParameters:
    out: ProtectedJobParameters = {}  # type: ignore[typeddict-item]
    if data.get("analysisTemplateArn") is not None:
        out["analysis_template_arn"] = data["analysisTemplateArn"]
    else:
        raise DeserializationError(
            "ProtectedJobParameters.analysis_template_arn required"
        )
    if data.get("parameters") is not None:
        import capo_cleanrooms.types.job_parameter_map

        out["parameters"] = capo_cleanrooms.types.job_parameter_map.deserialize_json(
            data["parameters"]
        )
    return out


def redact_sensitive(value: ProtectedJobParameters) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "parameters" in value:
        out["parameters"] = "*** Sensitive Data Redacted ***"
    return out
