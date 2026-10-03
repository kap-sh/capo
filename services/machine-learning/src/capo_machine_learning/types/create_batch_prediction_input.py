"""Generated from Smithy shape ``com.amazonaws.machinelearning#CreateBatchPredictionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_machine_learning.errors import DeserializationError

if TYPE_CHECKING:
    import capo_machine_learning.types.entity_id
    import capo_machine_learning.types.entity_name
    import capo_machine_learning.types.s3_url


class CreateBatchPredictionInput(TypedDict, closed=True):
    batch_prediction_id: "capo_machine_learning.types.entity_id.EntityId"
    """<p>A user-supplied ID that uniquely identifies the <code>BatchPrediction</code>.</p>"""
    batch_prediction_name: NotRequired[
        "capo_machine_learning.types.entity_name.EntityName"
    ]
    """<p>A user-supplied name or description of the <code>BatchPrediction</code>. <code>BatchPredictionName</code> can only use the UTF-8 character set.</p>"""
    ml_model_id: "capo_machine_learning.types.entity_id.EntityId"
    """<p>The ID of the <code>MLModel</code> that will generate predictions for the group of observations. </p>"""
    batch_prediction_data_source_id: "capo_machine_learning.types.entity_id.EntityId"
    """<p>The ID of the <code>DataSource</code> that points to the group of observations to predict.</p>"""
    output_uri: "capo_machine_learning.types.s3_url.S3Url"
    """<p>The location of an Amazon Simple Storage Service (Amazon S3) bucket or directory to store the batch prediction results. The following substrings are not allowed in the <code>s3 key</code> portion of the <code>outputURI</code> field: ':', '//', '/./', '/../'.</p> <p>Amazon ML needs permissions to store and retrieve the logs on your behalf. For information about how to set permissions, see the <a href="https://docs.aws.amazon.com/machine-learning/latest/dg">Amazon Machine Learning Developer Guide</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBatchPredictionInput) -> dict:
    out: dict = {}
    out["BatchPredictionId"] = value["batch_prediction_id"]
    if "batch_prediction_name" in value:
        out["BatchPredictionName"] = value["batch_prediction_name"]
    out["MLModelId"] = value["ml_model_id"]
    out["BatchPredictionDataSourceId"] = value["batch_prediction_data_source_id"]
    out["OutputUri"] = value["output_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateBatchPredictionInput:
    out: CreateBatchPredictionInput = {}  # type: ignore[typeddict-item]
    if data.get("BatchPredictionId") is not None:
        out["batch_prediction_id"] = data["BatchPredictionId"]
    else:
        raise DeserializationError(
            "CreateBatchPredictionInput.batch_prediction_id required"
        )
    if data.get("BatchPredictionName") is not None:
        out["batch_prediction_name"] = data["BatchPredictionName"]
    if data.get("MLModelId") is not None:
        out["ml_model_id"] = data["MLModelId"]
    else:
        raise DeserializationError("CreateBatchPredictionInput.ml_model_id required")
    if data.get("BatchPredictionDataSourceId") is not None:
        out["batch_prediction_data_source_id"] = data["BatchPredictionDataSourceId"]
    else:
        raise DeserializationError(
            "CreateBatchPredictionInput.batch_prediction_data_source_id required"
        )
    if data.get("OutputUri") is not None:
        out["output_uri"] = data["OutputUri"]
    else:
        raise DeserializationError("CreateBatchPredictionInput.output_uri required")
    return out
