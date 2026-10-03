"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ModelVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.model_arn
    import capo_lookoutequipment.types.model_name
    import capo_lookoutequipment.types.model_quality
    import capo_lookoutequipment.types.model_version
    import capo_lookoutequipment.types.model_version_arn
    import capo_lookoutequipment.types.model_version_source_type
    import capo_lookoutequipment.types.model_version_status
    import capo_lookoutequipment.types.timestamp


class ModelVersionSummary(TypedDict, closed=True):
    model_name: NotRequired["capo_lookoutequipment.types.model_name.ModelName"]
    """<p>The name of the model that this model version is a version of.</p>"""
    model_arn: NotRequired["capo_lookoutequipment.types.model_arn.ModelArn"]
    """<p>The Amazon Resource Name (ARN) of the model that this model version is a version of.</p>"""
    model_version: NotRequired["capo_lookoutequipment.types.model_version.ModelVersion"]
    """<p>The version of the model.</p>"""
    model_version_arn: NotRequired[
        "capo_lookoutequipment.types.model_version_arn.ModelVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the model version.</p>"""
    created_at: NotRequired["capo_lookoutequipment.types.timestamp.Timestamp"]
    """<p>The time when this model version was created.</p>"""
    status: NotRequired[
        "capo_lookoutequipment.types.model_version_status.ModelVersionStatus"
    ]
    """<p>The current status of the model version.</p>"""
    source_type: NotRequired[
        "capo_lookoutequipment.types.model_version_source_type.ModelVersionSourceType"
    ]
    """<p>Indicates how this model version was generated.</p>"""
    model_quality: NotRequired["capo_lookoutequipment.types.model_quality.ModelQuality"]
    """<p>Provides a quality assessment for a model that uses labels. If Lookout for Equipment determines that the model quality is poor based on training metrics, the value is <code>POOR_QUALITY_DETECTED</code>. Otherwise, the value is <code>QUALITY_THRESHOLD_MET</code>. </p> <p>If the model is unlabeled, the model quality can't be assessed and the value of <code>ModelQuality</code> is <code>CANNOT_DETERMINE_QUALITY</code>. In this situation, you can get a model quality assessment by adding labels to the input dataset and retraining the model.</p> <p>For information about improving the quality of a model, see <a href="https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/best-practices.html">Best practices with Amazon Lookout for Equipment</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ModelVersionSummary) -> dict:
    out: dict = {}
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
    if "model_version" in value:
        out["ModelVersion"] = value["model_version"]
    if "model_version_arn" in value:
        out["ModelVersionArn"] = value["model_version_arn"]
    if "created_at" in value:
        import capo_lookoutequipment.types.timestamp

        out["CreatedAt"] = capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "status" in value:
        import capo_lookoutequipment.types.model_version_status

        out["Status"] = (
            capo_lookoutequipment.types.model_version_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "source_type" in value:
        import capo_lookoutequipment.types.model_version_source_type

        out["SourceType"] = (
            capo_lookoutequipment.types.model_version_source_type.serialize_aws_json_1_0(
                value["source_type"]
            )
        )
    if "model_quality" in value:
        import capo_lookoutequipment.types.model_quality

        out["ModelQuality"] = (
            capo_lookoutequipment.types.model_quality.serialize_aws_json_1_0(
                value["model_quality"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ModelVersionSummary:
    out: ModelVersionSummary = {}  # type: ignore[typeddict-item]
    if data.get("ModelName") is not None:
        out["model_name"] = data["ModelName"]
    if data.get("ModelArn") is not None:
        out["model_arn"] = data["ModelArn"]
    if data.get("ModelVersion") is not None:
        out["model_version"] = data["ModelVersion"]
    if data.get("ModelVersionArn") is not None:
        out["model_version_arn"] = data["ModelVersionArn"]
    if data.get("CreatedAt") is not None:
        import capo_lookoutequipment.types.timestamp

        out["created_at"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    if data.get("Status") is not None:
        import capo_lookoutequipment.types.model_version_status

        out["status"] = (
            capo_lookoutequipment.types.model_version_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if data.get("SourceType") is not None:
        import capo_lookoutequipment.types.model_version_source_type

        out["source_type"] = (
            capo_lookoutequipment.types.model_version_source_type.deserialize_aws_json_1_0(
                data["SourceType"]
            )
        )
    if data.get("ModelQuality") is not None:
        import capo_lookoutequipment.types.model_quality

        out["model_quality"] = (
            capo_lookoutequipment.types.model_quality.deserialize_aws_json_1_0(
                data["ModelQuality"]
            )
        )
    return out
