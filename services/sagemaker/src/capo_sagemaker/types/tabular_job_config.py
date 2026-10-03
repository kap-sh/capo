"""Generated from Smithy shape ``com.amazonaws.sagemaker#TabularJobConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_ml_job_completion_criteria
    import capo_sagemaker.types.auto_ml_mode
    import capo_sagemaker.types.candidate_generation_config
    import capo_sagemaker.types.generate_candidate_definitions_only
    import capo_sagemaker.types.problem_type
    import capo_sagemaker.types.s3_uri
    import capo_sagemaker.types.sample_weight_attribute_name
    import capo_sagemaker.types.target_attribute_name


class TabularJobConfig(TypedDict, closed=True):
    candidate_generation_config: NotRequired[
        "capo_sagemaker.types.candidate_generation_config.CandidateGenerationConfig"
    ]
    """<p>The configuration information of how model candidates are generated.</p>"""
    completion_criteria: NotRequired[
        "capo_sagemaker.types.auto_ml_job_completion_criteria.AutoMLJobCompletionCriteria"
    ]
    feature_specification_s3_uri: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>A URL to the Amazon S3 data source containing selected features from the input data source to run an Autopilot job V2. You can input <code>FeatureAttributeNames</code> (optional) in JSON format as shown below: </p> <p> <code>{ "FeatureAttributeNames":["col1", "col2", ...] }</code>.</p> <p>You can also specify the data type of the feature (optional) in the format shown below:</p> <p> <code>{ "FeatureDataTypes":{"col1":"numeric", "col2":"categorical" ... } }</code> </p> <note> <p>These column keys may not include the target column.</p> </note> <p>In ensembling mode, Autopilot only supports the following data types: <code>numeric</code>, <code>categorical</code>, <code>text</code>, and <code>datetime</code>. In HPO mode, Autopilot can support <code>numeric</code>, <code>categorical</code>, <code>text</code>, <code>datetime</code>, and <code>sequence</code>.</p> <p>If only <code>FeatureDataTypes</code> is provided, the column keys (<code>col1</code>, <code>col2</code>,..) should be a subset of the column names in the input data. </p> <p>If both <code>FeatureDataTypes</code> and <code>FeatureAttributeNames</code> are provided, then the column keys should be a subset of the column names provided in <code>FeatureAttributeNames</code>. </p> <p>The key name <code>FeatureAttributeNames</code> is fixed. The values listed in <code>["col1", "col2", ...]</code> are case sensitive and should be a list of strings containing unique values that are a subset of the column names in the input data. The list of columns provided must not include the target column.</p>"""
    mode: NotRequired["capo_sagemaker.types.auto_ml_mode.AutoMLMode"]
    """<p>The method that Autopilot uses to train the data. You can either specify the mode manually or let Autopilot choose for you based on the dataset size by selecting <code>AUTO</code>. In <code>AUTO</code> mode, Autopilot chooses <code>ENSEMBLING</code> for datasets smaller than 100 MB, and <code>HYPERPARAMETER_TUNING</code> for larger ones.</p> <p>The <code>ENSEMBLING</code> mode uses a multi-stack ensemble model to predict classification and regression tasks directly from your dataset. This machine learning mode combines several base models to produce an optimal predictive model. It then uses a stacking ensemble method to combine predictions from contributing members. A multi-stack ensemble model can provide better performance over a single model by combining the predictive capabilities of multiple models. See <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-model-support-validation.html#autopilot-algorithm-support">Autopilot algorithm support</a> for a list of algorithms supported by <code>ENSEMBLING</code> mode.</p> <p>The <code>HYPERPARAMETER_TUNING</code> (HPO) mode uses the best hyperparameters to train the best version of a model. HPO automatically selects an algorithm for the type of problem you want to solve. Then HPO finds the best hyperparameters according to your objective metric. See <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-model-support-validation.html#autopilot-algorithm-support">Autopilot algorithm support</a> for a list of algorithms supported by <code>HYPERPARAMETER_TUNING</code> mode.</p>"""
    generate_candidate_definitions_only: NotRequired[
        "capo_sagemaker.types.generate_candidate_definitions_only.GenerateCandidateDefinitionsOnly"
    ]
    """<p>Generates possible candidates without training the models. A model candidate is a combination of data preprocessors, algorithms, and algorithm parameter settings.</p>"""
    problem_type: NotRequired["capo_sagemaker.types.problem_type.ProblemType"]
    """<p>The type of supervised learning problem available for the model candidates of the AutoML job V2. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-datasets-problem-types.html#autopilot-problem-types"> SageMaker Autopilot problem types</a>.</p> <note> <p>You must either specify the type of supervised learning problem in <code>ProblemType</code> and provide the <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html#sagemaker-CreateAutoMLJobV2-request-AutoMLJobObjective">AutoMLJobObjective</a> metric, or none at all.</p> </note>"""
    target_attribute_name: NotRequired[
        "capo_sagemaker.types.target_attribute_name.TargetAttributeName"
    ]
    """<p>The name of the target variable in supervised learning, usually represented by 'y'.</p>"""
    sample_weight_attribute_name: NotRequired[
        "capo_sagemaker.types.sample_weight_attribute_name.SampleWeightAttributeName"
    ]
    """<p>If specified, this column name indicates which column of the dataset should be treated as sample weights for use by the objective metric during the training, evaluation, and the selection of the best model. This column is not considered as a predictive feature. For more information on Autopilot metrics, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-metrics-validation.html">Metrics and validation</a>.</p> <p>Sample weights should be numeric, non-negative, with larger values indicating which rows are more important than others. Data points that have invalid or no weight value are excluded.</p> <p>Support for sample weights is available in <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLAlgorithmConfig.html">Ensembling</a> mode only.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TabularJobConfig) -> dict:
    out: dict = {}
    if "candidate_generation_config" in value:
        import capo_sagemaker.types.candidate_generation_config

        out["CandidateGenerationConfig"] = (
            capo_sagemaker.types.candidate_generation_config.serialize_aws_json_1_1(
                value["candidate_generation_config"]
            )
        )
    if "completion_criteria" in value:
        import capo_sagemaker.types.auto_ml_job_completion_criteria

        out["CompletionCriteria"] = (
            capo_sagemaker.types.auto_ml_job_completion_criteria.serialize_aws_json_1_1(
                value["completion_criteria"]
            )
        )
    if "feature_specification_s3_uri" in value:
        out["FeatureSpecificationS3Uri"] = value["feature_specification_s3_uri"]
    if "mode" in value:
        import capo_sagemaker.types.auto_ml_mode

        out["Mode"] = capo_sagemaker.types.auto_ml_mode.serialize_aws_json_1_1(
            value["mode"]
        )
    if "generate_candidate_definitions_only" in value:
        out["GenerateCandidateDefinitionsOnly"] = value[
            "generate_candidate_definitions_only"
        ]
    if "problem_type" in value:
        import capo_sagemaker.types.problem_type

        out["ProblemType"] = capo_sagemaker.types.problem_type.serialize_aws_json_1_1(
            value["problem_type"]
        )
    if "target_attribute_name" in value:
        out["TargetAttributeName"] = value["target_attribute_name"]
    if "sample_weight_attribute_name" in value:
        out["SampleWeightAttributeName"] = value["sample_weight_attribute_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TabularJobConfig:
    out: TabularJobConfig = {}  # type: ignore[typeddict-item]
    if data.get("CandidateGenerationConfig") is not None:
        import capo_sagemaker.types.candidate_generation_config

        out["candidate_generation_config"] = (
            capo_sagemaker.types.candidate_generation_config.deserialize_aws_json_1_1(
                data["CandidateGenerationConfig"]
            )
        )
    if data.get("CompletionCriteria") is not None:
        import capo_sagemaker.types.auto_ml_job_completion_criteria

        out["completion_criteria"] = (
            capo_sagemaker.types.auto_ml_job_completion_criteria.deserialize_aws_json_1_1(
                data["CompletionCriteria"]
            )
        )
    if data.get("FeatureSpecificationS3Uri") is not None:
        out["feature_specification_s3_uri"] = data["FeatureSpecificationS3Uri"]
    if data.get("Mode") is not None:
        import capo_sagemaker.types.auto_ml_mode

        out["mode"] = capo_sagemaker.types.auto_ml_mode.deserialize_aws_json_1_1(
            data["Mode"]
        )
    if data.get("GenerateCandidateDefinitionsOnly") is not None:
        out["generate_candidate_definitions_only"] = data[
            "GenerateCandidateDefinitionsOnly"
        ]
    if data.get("ProblemType") is not None:
        import capo_sagemaker.types.problem_type

        out["problem_type"] = (
            capo_sagemaker.types.problem_type.deserialize_aws_json_1_1(
                data["ProblemType"]
            )
        )
    if data.get("TargetAttributeName") is not None:
        out["target_attribute_name"] = data["TargetAttributeName"]
    if data.get("SampleWeightAttributeName") is not None:
        out["sample_weight_attribute_name"] = data["SampleWeightAttributeName"]
    return out
