"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLCandidateGenerationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_ml_algorithms_config
    import capo_sagemaker.types.s3_uri


class AutoMLCandidateGenerationConfig(TypedDict, closed=True):
    feature_specification_s3_uri: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>A URL to the Amazon S3 data source containing selected features from the input data source to run an Autopilot job. You can input <code>FeatureAttributeNames</code> (optional) in JSON format as shown below: </p> <p> <code>{ "FeatureAttributeNames":["col1", "col2", ...] }</code>.</p> <p>You can also specify the data type of the feature (optional) in the format shown below:</p> <p> <code>{ "FeatureDataTypes":{"col1":"numeric", "col2":"categorical" ... } }</code> </p> <note> <p>These column keys may not include the target column.</p> </note> <p>In ensembling mode, Autopilot only supports the following data types: <code>numeric</code>, <code>categorical</code>, <code>text</code>, and <code>datetime</code>. In HPO mode, Autopilot can support <code>numeric</code>, <code>categorical</code>, <code>text</code>, <code>datetime</code>, and <code>sequence</code>.</p> <p>If only <code>FeatureDataTypes</code> is provided, the column keys (<code>col1</code>, <code>col2</code>,..) should be a subset of the column names in the input data. </p> <p>If both <code>FeatureDataTypes</code> and <code>FeatureAttributeNames</code> are provided, then the column keys should be a subset of the column names provided in <code>FeatureAttributeNames</code>. </p> <p>The key name <code>FeatureAttributeNames</code> is fixed. The values listed in <code>["col1", "col2", ...]</code> are case sensitive and should be a list of strings containing unique values that are a subset of the column names in the input data. The list of columns provided must not include the target column.</p>"""
    algorithms_config: NotRequired[
        "capo_sagemaker.types.auto_ml_algorithms_config.AutoMLAlgorithmsConfig"
    ]
    """<p>Stores the configuration information for the selection of algorithms trained on tabular data.</p> <p>The list of available algorithms to choose from depends on the training mode set in <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TabularJobConfig.html"> <code>TabularJobConfig.Mode</code> </a>.</p> <ul> <li> <p> <code>AlgorithmsConfig</code> should not be set if the training mode is set on <code>AUTO</code>.</p> </li> <li> <p>When <code>AlgorithmsConfig</code> is provided, one <code>AutoMLAlgorithms</code> attribute must be set and one only.</p> <p>If the list of algorithms provided as values for <code>AutoMLAlgorithms</code> is empty, <code>CandidateGenerationConfig</code> uses the full set of algorithms for the given training mode.</p> </li> <li> <p>When <code>AlgorithmsConfig</code> is not provided, <code>CandidateGenerationConfig</code> uses the full set of algorithms for the given training mode.</p> </li> </ul> <p>For the list of all algorithms per problem type and training mode, see <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLAlgorithmConfig.html"> AutoMLAlgorithmConfig</a>.</p> <p>For more information on each algorithm, see the <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-model-support-validation.html#autopilot-algorithm-support">Algorithm support</a> section in Autopilot developer guide.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLCandidateGenerationConfig) -> dict:
    out: dict = {}
    if "feature_specification_s3_uri" in value:
        out["FeatureSpecificationS3Uri"] = value["feature_specification_s3_uri"]
    if "algorithms_config" in value:
        import capo_sagemaker.types.auto_ml_algorithms_config

        out["AlgorithmsConfig"] = (
            capo_sagemaker.types.auto_ml_algorithms_config.serialize_aws_json_1_1(
                value["algorithms_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoMLCandidateGenerationConfig:
    out: AutoMLCandidateGenerationConfig = {}  # type: ignore[typeddict-item]
    if data.get("FeatureSpecificationS3Uri") is not None:
        out["feature_specification_s3_uri"] = data["FeatureSpecificationS3Uri"]
    if data.get("AlgorithmsConfig") is not None:
        import capo_sagemaker.types.auto_ml_algorithms_config

        out["algorithms_config"] = (
            capo_sagemaker.types.auto_ml_algorithms_config.deserialize_aws_json_1_1(
                data["AlgorithmsConfig"]
            )
        )
    return out
