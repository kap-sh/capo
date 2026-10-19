"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ModelDiagnosticsS3OutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.s3_bucket
    import capo_lookoutequipment.types.s3_prefix


class ModelDiagnosticsS3OutputConfiguration(TypedDict, closed=True):
    bucket: "capo_lookoutequipment.types.s3_bucket.S3Bucket"
    """<p>The name of the Amazon S3 bucket where the pointwise model diagnostics are located. You must be the owner of the Amazon S3 bucket. </p>"""
    prefix: NotRequired["capo_lookoutequipment.types.s3_prefix.S3Prefix"]
    """<p>The Amazon S3 prefix for the location of the pointwise model diagnostics. The prefix specifies the folder and evaluation result file name. (<code>bucket</code>).</p> <p>When you call <code>CreateModel</code> or <code>UpdateModel</code>, specify the path within the bucket that you want Lookout for Equipment to save the model to. During training, Lookout for Equipment creates the model evaluation model as a compressed JSON file with the name <code>model_diagnostics_results.json.gz</code>.</p> <p>When you call <code>DescribeModel</code> or <code>DescribeModelVersion</code>, <code>prefix</code> contains the file path and filename of the model evaluation file. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ModelDiagnosticsS3OutputConfiguration) -> dict:
    out: dict = {}
    out["Bucket"] = value["bucket"]
    if "prefix" in value:
        out["Prefix"] = value["prefix"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ModelDiagnosticsS3OutputConfiguration:
    out: ModelDiagnosticsS3OutputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Bucket") is not None:
        out["bucket"] = data["Bucket"]
    else:
        out["bucket"] = ""
    if data.get("Prefix") is not None:
        out["prefix"] = data["Prefix"]
    return out
