"""Generated from Smithy shape ``com.amazonaws.machinelearning#MLModel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_machine_learning.types.algorithm
    import capo_machine_learning.types.aws_user_arn
    import capo_machine_learning.types.entity_id
    import capo_machine_learning.types.entity_status
    import capo_machine_learning.types.epoch_time
    import capo_machine_learning.types.long_type
    import capo_machine_learning.types.message
    import capo_machine_learning.types.ml_model_name
    import capo_machine_learning.types.ml_model_type
    import capo_machine_learning.types.realtime_endpoint_info
    import capo_machine_learning.types.s3_url
    import capo_machine_learning.types.score_threshold
    import capo_machine_learning.types.training_parameters


class MLModel(TypedDict, closed=True):
    ml_model_id: NotRequired["capo_machine_learning.types.entity_id.EntityId"]
    """<p>The ID assigned to the <code>MLModel</code> at creation.</p>"""
    training_data_source_id: NotRequired[
        "capo_machine_learning.types.entity_id.EntityId"
    ]
    """<p>The ID of the training <code>DataSource</code>. The <code>CreateMLModel</code> operation uses the <code>TrainingDataSourceId</code>.</p>"""
    created_by_iam_user: NotRequired[
        "capo_machine_learning.types.aws_user_arn.AwsUserArn"
    ]
    """<p>The AWS user account from which the <code>MLModel</code> was created. The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.</p>"""
    created_at: NotRequired["capo_machine_learning.types.epoch_time.EpochTime"]
    """<p>The time that the <code>MLModel</code> was created. The time is expressed in epoch time.</p>"""
    last_updated_at: NotRequired["capo_machine_learning.types.epoch_time.EpochTime"]
    """<p>The time of the most recent edit to the <code>MLModel</code>. The time is expressed in epoch time.</p>"""
    name: NotRequired["capo_machine_learning.types.ml_model_name.MLModelName"]
    """<p>A user-supplied name or description of the <code>MLModel</code>.</p>"""
    status: NotRequired["capo_machine_learning.types.entity_status.EntityStatus"]
    """<p>The current status of an <code>MLModel</code>. This element can have one of the following values: </p> <ul> <li> <p> <code>PENDING</code> - Amazon Machine Learning (Amazon ML) submitted a request to create an <code>MLModel</code>.</p> </li> <li> <p> <code>INPROGRESS</code> - The creation process is underway.</p> </li> <li> <p> <code>FAILED</code> - The request to create an <code>MLModel</code> didn't run to completion. The model isn't usable.</p> </li> <li> <p> <code>COMPLETED</code> - The creation process completed successfully.</p> </li> <li> <p> <code>DELETED</code> - The <code>MLModel</code> is marked as deleted. It isn't usable.</p> </li> </ul>"""
    size_in_bytes: NotRequired["capo_machine_learning.types.long_type.LongType"]
    endpoint_info: NotRequired[
        "capo_machine_learning.types.realtime_endpoint_info.RealtimeEndpointInfo"
    ]
    """<p>The current endpoint of the <code>MLModel</code>.</p>"""
    training_parameters: NotRequired[
        "capo_machine_learning.types.training_parameters.TrainingParameters"
    ]
    """<p>A list of the training parameters in the <code>MLModel</code>. The list is implemented as a map of key-value pairs.</p> <p>The following is the current set of training parameters:</p> <ul> <li> <p> <code>sgd.maxMLModelSizeInBytes</code> - The maximum allowed size of the model. Depending on the input data, the size of the model might affect its performance.</p> <p> The value is an integer that ranges from <code>100000</code> to <code>2147483648</code>. The default value is <code>33554432</code>.</p> </li> <li> <p> <code>sgd.maxPasses</code> - The number of times that the training process traverses the observations to build the <code>MLModel</code>. The value is an integer that ranges from <code>1</code> to <code>10000</code>. The default value is <code>10</code>.</p> </li> <li> <p> <code>sgd.shuffleType</code> - Whether Amazon ML shuffles the training data. Shuffling the data improves a model's ability to find the optimal solution for a variety of data types. The valid values are <code>auto</code> and <code>none</code>. The default value is <code>none</code>.</p> </li> <li> <p> <code>sgd.l1RegularizationAmount</code> - The coefficient regularization L1 norm, which controls overfitting the data by penalizing large coefficients. This parameter tends to drive coefficients to zero, resulting in sparse feature set. If you use this parameter, start by specifying a small value, such as <code>1.0E-08</code>.</p> <p>The value is a double that ranges from <code>0</code> to <code>MAX_DOUBLE</code>. The default is to not use L1 normalization. This parameter can't be used when <code>L2</code> is specified. Use this parameter sparingly.</p> </li> <li> <p> <code>sgd.l2RegularizationAmount</code> - The coefficient regularization L2 norm, which controls overfitting the data by penalizing large coefficients. This tends to drive coefficients to small, nonzero values. If you use this parameter, start by specifying a small value, such as <code>1.0E-08</code>.</p> <p>The value is a double that ranges from <code>0</code> to <code>MAX_DOUBLE</code>. The default is to not use L2 normalization. This parameter can't be used when <code>L1</code> is specified. Use this parameter sparingly.</p> </li> </ul>"""
    input_data_location_s3: NotRequired["capo_machine_learning.types.s3_url.S3Url"]
    """<p>The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).</p>"""
    algorithm: NotRequired["capo_machine_learning.types.algorithm.Algorithm"]
    """<p>The algorithm used to train the <code>MLModel</code>. The following algorithm is supported:</p> <ul> <li> <p> <code>SGD</code> -- Stochastic gradient descent. The goal of <code>SGD</code> is to minimize the gradient of the loss function. </p> </li> </ul>"""
    ml_model_type: NotRequired["capo_machine_learning.types.ml_model_type.MLModelType"]
    """<p>Identifies the <code>MLModel</code> category. The following are the available types:</p> <ul> <li> <p> <code>REGRESSION</code> - Produces a numeric result. For example, "What price should a house be listed at?"</p> </li> <li> <p> <code>BINARY</code> - Produces one of two possible results. For example, "Is this a child-friendly web site?".</p> </li> <li> <p> <code>MULTICLASS</code> - Produces one of several possible results. For example, "Is this a HIGH-, LOW-, or MEDIUM-risk trade?".</p> </li> </ul>"""
    score_threshold: NotRequired[
        "capo_machine_learning.types.score_threshold.ScoreThreshold"
    ]
    score_threshold_last_updated_at: NotRequired[
        "capo_machine_learning.types.epoch_time.EpochTime"
    ]
    """<p>The time of the most recent edit to the <code>ScoreThreshold</code>. The time is expressed in epoch time.</p>"""
    message: NotRequired["capo_machine_learning.types.message.Message"]
    """<p>A description of the most recent details about accessing the <code>MLModel</code>.</p>"""
    compute_time: NotRequired["capo_machine_learning.types.long_type.LongType"]
    finished_at: NotRequired["capo_machine_learning.types.epoch_time.EpochTime"]
    started_at: NotRequired["capo_machine_learning.types.epoch_time.EpochTime"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MLModel) -> dict:
    out: dict = {}
    if "ml_model_id" in value:
        out["MLModelId"] = value["ml_model_id"]
    if "training_data_source_id" in value:
        out["TrainingDataSourceId"] = value["training_data_source_id"]
    if "created_by_iam_user" in value:
        out["CreatedByIamUser"] = value["created_by_iam_user"]
    if "created_at" in value:
        import capo_machine_learning.types.epoch_time

        out["CreatedAt"] = (
            capo_machine_learning.types.epoch_time.serialize_aws_json_1_1(
                value["created_at"]
            )
        )
    if "last_updated_at" in value:
        import capo_machine_learning.types.epoch_time

        out["LastUpdatedAt"] = (
            capo_machine_learning.types.epoch_time.serialize_aws_json_1_1(
                value["last_updated_at"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import capo_machine_learning.types.entity_status

        out["Status"] = (
            capo_machine_learning.types.entity_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "size_in_bytes" in value:
        out["SizeInBytes"] = value["size_in_bytes"]
    if "endpoint_info" in value:
        import capo_machine_learning.types.realtime_endpoint_info

        out["EndpointInfo"] = (
            capo_machine_learning.types.realtime_endpoint_info.serialize_aws_json_1_1(
                value["endpoint_info"]
            )
        )
    if "training_parameters" in value:
        import capo_machine_learning.types.training_parameters

        out["TrainingParameters"] = (
            capo_machine_learning.types.training_parameters.serialize_aws_json_1_1(
                value["training_parameters"]
            )
        )
    if "input_data_location_s3" in value:
        out["InputDataLocationS3"] = value["input_data_location_s3"]
    if "algorithm" in value:
        import capo_machine_learning.types.algorithm

        out["Algorithm"] = capo_machine_learning.types.algorithm.serialize_aws_json_1_1(
            value["algorithm"]
        )
    if "ml_model_type" in value:
        import capo_machine_learning.types.ml_model_type

        out["MLModelType"] = (
            capo_machine_learning.types.ml_model_type.serialize_aws_json_1_1(
                value["ml_model_type"]
            )
        )
    if "score_threshold" in value:
        out["ScoreThreshold"] = (
            "NaN"
            if value["score_threshold"] != value["score_threshold"]
            else "Infinity"
            if value["score_threshold"] == float("inf")
            else "-Infinity"
            if value["score_threshold"] == float("-inf")
            else value["score_threshold"]
        )
    if "score_threshold_last_updated_at" in value:
        import capo_machine_learning.types.epoch_time

        out["ScoreThresholdLastUpdatedAt"] = (
            capo_machine_learning.types.epoch_time.serialize_aws_json_1_1(
                value["score_threshold_last_updated_at"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "compute_time" in value:
        out["ComputeTime"] = value["compute_time"]
    if "finished_at" in value:
        import capo_machine_learning.types.epoch_time

        out["FinishedAt"] = (
            capo_machine_learning.types.epoch_time.serialize_aws_json_1_1(
                value["finished_at"]
            )
        )
    if "started_at" in value:
        import capo_machine_learning.types.epoch_time

        out["StartedAt"] = (
            capo_machine_learning.types.epoch_time.serialize_aws_json_1_1(
                value["started_at"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MLModel:
    out: MLModel = {}  # type: ignore[typeddict-item]
    if data.get("MLModelId") is not None:
        out["ml_model_id"] = data["MLModelId"]
    if data.get("TrainingDataSourceId") is not None:
        out["training_data_source_id"] = data["TrainingDataSourceId"]
    if data.get("CreatedByIamUser") is not None:
        out["created_by_iam_user"] = data["CreatedByIamUser"]
    if data.get("CreatedAt") is not None:
        import capo_machine_learning.types.epoch_time

        out["created_at"] = (
            capo_machine_learning.types.epoch_time.deserialize_aws_json_1_1(
                data["CreatedAt"]
            )
        )
    if data.get("LastUpdatedAt") is not None:
        import capo_machine_learning.types.epoch_time

        out["last_updated_at"] = (
            capo_machine_learning.types.epoch_time.deserialize_aws_json_1_1(
                data["LastUpdatedAt"]
            )
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        import capo_machine_learning.types.entity_status

        out["status"] = (
            capo_machine_learning.types.entity_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("SizeInBytes") is not None:
        out["size_in_bytes"] = data["SizeInBytes"]
    if data.get("EndpointInfo") is not None:
        import capo_machine_learning.types.realtime_endpoint_info

        out["endpoint_info"] = (
            capo_machine_learning.types.realtime_endpoint_info.deserialize_aws_json_1_1(
                data["EndpointInfo"]
            )
        )
    if data.get("TrainingParameters") is not None:
        import capo_machine_learning.types.training_parameters

        out["training_parameters"] = (
            capo_machine_learning.types.training_parameters.deserialize_aws_json_1_1(
                data["TrainingParameters"]
            )
        )
    if data.get("InputDataLocationS3") is not None:
        out["input_data_location_s3"] = data["InputDataLocationS3"]
    if data.get("Algorithm") is not None:
        import capo_machine_learning.types.algorithm

        out["algorithm"] = (
            capo_machine_learning.types.algorithm.deserialize_aws_json_1_1(
                data["Algorithm"]
            )
        )
    if data.get("MLModelType") is not None:
        import capo_machine_learning.types.ml_model_type

        out["ml_model_type"] = (
            capo_machine_learning.types.ml_model_type.deserialize_aws_json_1_1(
                data["MLModelType"]
            )
        )
    if data.get("ScoreThreshold") is not None:
        out["score_threshold"] = float(data["ScoreThreshold"])
    if data.get("ScoreThresholdLastUpdatedAt") is not None:
        import capo_machine_learning.types.epoch_time

        out["score_threshold_last_updated_at"] = (
            capo_machine_learning.types.epoch_time.deserialize_aws_json_1_1(
                data["ScoreThresholdLastUpdatedAt"]
            )
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ComputeTime") is not None:
        out["compute_time"] = data["ComputeTime"]
    if data.get("FinishedAt") is not None:
        import capo_machine_learning.types.epoch_time

        out["finished_at"] = (
            capo_machine_learning.types.epoch_time.deserialize_aws_json_1_1(
                data["FinishedAt"]
            )
        )
    if data.get("StartedAt") is not None:
        import capo_machine_learning.types.epoch_time

        out["started_at"] = (
            capo_machine_learning.types.epoch_time.deserialize_aws_json_1_1(
                data["StartedAt"]
            )
        )
    return out
