"""Generated from Smithy shape ``com.amazonaws.sagemaker#MetricDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.metric_name
    import capo_sagemaker.types.metric_regex


class MetricDefinition(TypedDict, closed=True):
    name: NotRequired["capo_sagemaker.types.metric_name.MetricName"]
    """<p>The name of the metric.</p>"""
    regex: NotRequired["capo_sagemaker.types.metric_regex.MetricRegex"]
    """<p>A regular expression that searches the output of a training job and gets the value of the metric. For more information about using regular expressions to define metrics, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html">Defining metrics and environment variables</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricDefinition) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "regex" in value:
        out["Regex"] = value["regex"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricDefinition:
    out: MetricDefinition = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Regex") is not None:
        out["regex"] = data["Regex"]
    return out
