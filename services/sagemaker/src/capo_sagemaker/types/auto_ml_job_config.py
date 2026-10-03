"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLJobConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_ml_candidate_generation_config
    import capo_sagemaker.types.auto_ml_data_split_config
    import capo_sagemaker.types.auto_ml_job_completion_criteria
    import capo_sagemaker.types.auto_ml_mode
    import capo_sagemaker.types.auto_ml_security_config


class AutoMLJobConfig(TypedDict, closed=True):
    completion_criteria: NotRequired[
        "capo_sagemaker.types.auto_ml_job_completion_criteria.AutoMLJobCompletionCriteria"
    ]
    """<p>How long an AutoML job is allowed to run, or how many candidates a job is allowed to generate.</p>"""
    security_config: NotRequired[
        "capo_sagemaker.types.auto_ml_security_config.AutoMLSecurityConfig"
    ]
    """<p>The security configuration for traffic encryption or Amazon VPC settings.</p>"""
    candidate_generation_config: NotRequired[
        "capo_sagemaker.types.auto_ml_candidate_generation_config.AutoMLCandidateGenerationConfig"
    ]
    """<p>The configuration for generating a candidate for an AutoML job (optional). </p>"""
    data_split_config: NotRequired[
        "capo_sagemaker.types.auto_ml_data_split_config.AutoMLDataSplitConfig"
    ]
    """<p>The configuration for splitting the input training dataset.</p> <p>Type: AutoMLDataSplitConfig</p>"""
    mode: NotRequired["capo_sagemaker.types.auto_ml_mode.AutoMLMode"]
    """<p>The method that Autopilot uses to train the data. You can either specify the mode manually or let Autopilot choose for you based on the dataset size by selecting <code>AUTO</code>. In <code>AUTO</code> mode, Autopilot chooses <code>ENSEMBLING</code> for datasets smaller than 100 MB, and <code>HYPERPARAMETER_TUNING</code> for larger ones.</p> <p>The <code>ENSEMBLING</code> mode uses a multi-stack ensemble model to predict classification and regression tasks directly from your dataset. This machine learning mode combines several base models to produce an optimal predictive model. It then uses a stacking ensemble method to combine predictions from contributing members. A multi-stack ensemble model can provide better performance over a single model by combining the predictive capabilities of multiple models. See <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-model-support-validation.html#autopilot-algorithm-support">Autopilot algorithm support</a> for a list of algorithms supported by <code>ENSEMBLING</code> mode.</p> <p>The <code>HYPERPARAMETER_TUNING</code> (HPO) mode uses the best hyperparameters to train the best version of a model. HPO automatically selects an algorithm for the type of problem you want to solve. Then HPO finds the best hyperparameters according to your objective metric. See <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-model-support-validation.html#autopilot-algorithm-support">Autopilot algorithm support</a> for a list of algorithms supported by <code>HYPERPARAMETER_TUNING</code> mode.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLJobConfig) -> dict:
    out: dict = {}
    if "completion_criteria" in value:
        import capo_sagemaker.types.auto_ml_job_completion_criteria

        out["CompletionCriteria"] = (
            capo_sagemaker.types.auto_ml_job_completion_criteria.serialize_aws_json_1_1(
                value["completion_criteria"]
            )
        )
    if "security_config" in value:
        import capo_sagemaker.types.auto_ml_security_config

        out["SecurityConfig"] = (
            capo_sagemaker.types.auto_ml_security_config.serialize_aws_json_1_1(
                value["security_config"]
            )
        )
    if "candidate_generation_config" in value:
        import capo_sagemaker.types.auto_ml_candidate_generation_config

        out["CandidateGenerationConfig"] = (
            capo_sagemaker.types.auto_ml_candidate_generation_config.serialize_aws_json_1_1(
                value["candidate_generation_config"]
            )
        )
    if "data_split_config" in value:
        import capo_sagemaker.types.auto_ml_data_split_config

        out["DataSplitConfig"] = (
            capo_sagemaker.types.auto_ml_data_split_config.serialize_aws_json_1_1(
                value["data_split_config"]
            )
        )
    if "mode" in value:
        import capo_sagemaker.types.auto_ml_mode

        out["Mode"] = capo_sagemaker.types.auto_ml_mode.serialize_aws_json_1_1(
            value["mode"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoMLJobConfig:
    out: AutoMLJobConfig = {}  # type: ignore[typeddict-item]
    if data.get("CompletionCriteria") is not None:
        import capo_sagemaker.types.auto_ml_job_completion_criteria

        out["completion_criteria"] = (
            capo_sagemaker.types.auto_ml_job_completion_criteria.deserialize_aws_json_1_1(
                data["CompletionCriteria"]
            )
        )
    if data.get("SecurityConfig") is not None:
        import capo_sagemaker.types.auto_ml_security_config

        out["security_config"] = (
            capo_sagemaker.types.auto_ml_security_config.deserialize_aws_json_1_1(
                data["SecurityConfig"]
            )
        )
    if data.get("CandidateGenerationConfig") is not None:
        import capo_sagemaker.types.auto_ml_candidate_generation_config

        out["candidate_generation_config"] = (
            capo_sagemaker.types.auto_ml_candidate_generation_config.deserialize_aws_json_1_1(
                data["CandidateGenerationConfig"]
            )
        )
    if data.get("DataSplitConfig") is not None:
        import capo_sagemaker.types.auto_ml_data_split_config

        out["data_split_config"] = (
            capo_sagemaker.types.auto_ml_data_split_config.deserialize_aws_json_1_1(
                data["DataSplitConfig"]
            )
        )
    if data.get("Mode") is not None:
        import capo_sagemaker.types.auto_ml_mode

        out["mode"] = capo_sagemaker.types.auto_ml_mode.deserialize_aws_json_1_1(
            data["Mode"]
        )
    return out
