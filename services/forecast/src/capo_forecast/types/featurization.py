"""Generated from Smithy shape ``com.amazonaws.forecast#Featurization``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.featurization_pipeline
    import capo_forecast.types.name


class Featurization(TypedDict, closed=True):
    attribute_name: "capo_forecast.types.name.Name"
    """<p>The name of the schema attribute that specifies the data field to be featurized. Amazon Forecast supports the target field of the <code>TARGET_TIME_SERIES</code> and the <code>RELATED_TIME_SERIES</code> datasets. For example, for the <code>RETAIL</code> domain, the target is <code>demand</code>, and for the <code>CUSTOM</code> domain, the target is <code>target_value</code>. For more information, see <a>howitworks-missing-values</a>.</p>"""
    featurization_pipeline: NotRequired[
        "capo_forecast.types.featurization_pipeline.FeaturizationPipeline"
    ]
    """<p>An array of one <code>FeaturizationMethod</code> object that specifies the feature transformation method.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Featurization) -> dict:
    out: dict = {}
    out["AttributeName"] = value["attribute_name"]
    if "featurization_pipeline" in value:
        import capo_forecast.types.featurization_pipeline

        out["FeaturizationPipeline"] = (
            capo_forecast.types.featurization_pipeline.serialize_aws_json_1_1(
                value["featurization_pipeline"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Featurization:
    out: Featurization = {}  # type: ignore[typeddict-item]
    if data.get("AttributeName") is not None:
        out["attribute_name"] = data["AttributeName"]
    else:
        out["attribute_name"] = ""
    if data.get("FeaturizationPipeline") is not None:
        import capo_forecast.types.featurization_pipeline

        out["featurization_pipeline"] = (
            capo_forecast.types.featurization_pipeline.deserialize_aws_json_1_1(
                data["FeaturizationPipeline"]
            )
        )
    return out
