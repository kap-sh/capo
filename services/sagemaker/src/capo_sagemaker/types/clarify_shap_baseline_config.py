"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClarifyShapBaselineConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.clarify_mime_type
    import capo_sagemaker.types.clarify_shap_baseline
    import capo_sagemaker.types.url


class ClarifyShapBaselineConfig(TypedDict, closed=True):
    mime_type: NotRequired["capo_sagemaker.types.clarify_mime_type.ClarifyMimeType"]
    """<p>The MIME type of the baseline data. Choose from <code>'text/csv'</code> or <code>'application/jsonlines'</code>. Defaults to <code>'text/csv'</code>.</p>"""
    shap_baseline: NotRequired[
        "capo_sagemaker.types.clarify_shap_baseline.ClarifyShapBaseline"
    ]
    """<p>The inline SHAP baseline data in string format. <code>ShapBaseline</code> can have one or multiple records to be used as the baseline dataset. The format of the SHAP baseline file should be the same format as the training dataset. For example, if the training dataset is in CSV format and each record contains four features, and all features are numerical, then the format of the baseline data should also share these characteristics. For natural language processing (NLP) of text columns, the baseline value should be the value used to replace the unit of text specified by the <code>Granularity</code> of the <code>TextConfig</code> parameter. The size limit for <code>ShapBasline</code> is 4 KB. Use the <code>ShapBaselineUri</code> parameter if you want to provide more than 4 KB of baseline data.</p>"""
    shap_baseline_uri: NotRequired["capo_sagemaker.types.url.Url"]
    """<p>The uniform resource identifier (URI) of the S3 bucket where the SHAP baseline file is stored. The format of the SHAP baseline file should be the same format as the format of the training dataset. For example, if the training dataset is in CSV format, and each record in the training dataset has four features, and all features are numerical, then the baseline file should also have this same format. Each record should contain only the features. If you are using a virtual private cloud (VPC), the <code>ShapBaselineUri</code> should be accessible to the VPC. For more information about setting up endpoints with Amazon Virtual Private Cloud, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html">Give SageMaker access to Resources in your Amazon Virtual Private Cloud</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClarifyShapBaselineConfig) -> dict:
    out: dict = {}
    if "mime_type" in value:
        out["MimeType"] = value["mime_type"]
    if "shap_baseline" in value:
        out["ShapBaseline"] = value["shap_baseline"]
    if "shap_baseline_uri" in value:
        out["ShapBaselineUri"] = value["shap_baseline_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClarifyShapBaselineConfig:
    out: ClarifyShapBaselineConfig = {}  # type: ignore[typeddict-item]
    if data.get("MimeType") is not None:
        out["mime_type"] = data["MimeType"]
    if data.get("ShapBaseline") is not None:
        out["shap_baseline"] = data["ShapBaseline"]
    if data.get("ShapBaselineUri") is not None:
        out["shap_baseline_uri"] = data["ShapBaselineUri"]
    return out
