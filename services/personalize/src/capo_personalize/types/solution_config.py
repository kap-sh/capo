"""Generated from Smithy shape ``com.amazonaws.personalize#SolutionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.auto_ml_config
    import capo_personalize.types.auto_training_config
    import capo_personalize.types.event_value_threshold
    import capo_personalize.types.events_config
    import capo_personalize.types.feature_transformation_parameters
    import capo_personalize.types.hpo_config
    import capo_personalize.types.hyper_parameters
    import capo_personalize.types.optimization_objective
    import capo_personalize.types.training_data_config


class SolutionConfig(TypedDict, closed=True):
    event_value_threshold: NotRequired[
        "capo_personalize.types.event_value_threshold.EventValueThreshold"
    ]
    """<p>Only events with a value greater than or equal to this threshold are used for training a model.</p>"""
    hpo_config: NotRequired["capo_personalize.types.hpo_config.HPOConfig"]
    """<p>Describes the properties for hyperparameter optimization (HPO).</p>"""
    algorithm_hyper_parameters: NotRequired[
        "capo_personalize.types.hyper_parameters.HyperParameters"
    ]
    """<p>Lists the algorithm hyperparameters and their values.</p>"""
    feature_transformation_parameters: NotRequired[
        "capo_personalize.types.feature_transformation_parameters.FeatureTransformationParameters"
    ]
    """<p>Lists the feature transformation parameters.</p>"""
    auto_ml_config: NotRequired["capo_personalize.types.auto_ml_config.AutoMLConfig"]
    """<p>The <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_AutoMLConfig.html">AutoMLConfig</a> object containing a list of recipes to search when AutoML is performed.</p>"""
    events_config: NotRequired["capo_personalize.types.events_config.EventsConfig"]
    """<p>Describes the configuration of an event, which includes a list of event parameters. You can specify up to 10 event parameters. Events are used in solution creation.</p>"""
    optimization_objective: NotRequired[
        "capo_personalize.types.optimization_objective.OptimizationObjective"
    ]
    """<p>Describes the additional objective for the solution, such as maximizing streaming minutes or increasing revenue. For more information see <a href="https://docs.aws.amazon.com/personalize/latest/dg/optimizing-solution-for-objective.html">Optimizing a solution</a>.</p>"""
    training_data_config: NotRequired[
        "capo_personalize.types.training_data_config.TrainingDataConfig"
    ]
    """<p> Specifies the training data configuration to use when creating a custom solution version (trained model). </p>"""
    auto_training_config: NotRequired[
        "capo_personalize.types.auto_training_config.AutoTrainingConfig"
    ]
    """<p>Specifies the automatic training configuration to use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SolutionConfig) -> dict:
    out: dict = {}
    if "event_value_threshold" in value:
        out["eventValueThreshold"] = value["event_value_threshold"]
    if "hpo_config" in value:
        import capo_personalize.types.hpo_config

        out["hpoConfig"] = capo_personalize.types.hpo_config.serialize_aws_json_1_1(
            value["hpo_config"]
        )
    if "algorithm_hyper_parameters" in value:
        import capo_personalize.types.hyper_parameters

        out["algorithmHyperParameters"] = (
            capo_personalize.types.hyper_parameters.serialize_aws_json_1_1(
                value["algorithm_hyper_parameters"]
            )
        )
    if "feature_transformation_parameters" in value:
        import capo_personalize.types.feature_transformation_parameters

        out["featureTransformationParameters"] = (
            capo_personalize.types.feature_transformation_parameters.serialize_aws_json_1_1(
                value["feature_transformation_parameters"]
            )
        )
    if "auto_ml_config" in value:
        import capo_personalize.types.auto_ml_config

        out["autoMLConfig"] = (
            capo_personalize.types.auto_ml_config.serialize_aws_json_1_1(
                value["auto_ml_config"]
            )
        )
    if "events_config" in value:
        import capo_personalize.types.events_config

        out["eventsConfig"] = (
            capo_personalize.types.events_config.serialize_aws_json_1_1(
                value["events_config"]
            )
        )
    if "optimization_objective" in value:
        import capo_personalize.types.optimization_objective

        out["optimizationObjective"] = (
            capo_personalize.types.optimization_objective.serialize_aws_json_1_1(
                value["optimization_objective"]
            )
        )
    if "training_data_config" in value:
        import capo_personalize.types.training_data_config

        out["trainingDataConfig"] = (
            capo_personalize.types.training_data_config.serialize_aws_json_1_1(
                value["training_data_config"]
            )
        )
    if "auto_training_config" in value:
        import capo_personalize.types.auto_training_config

        out["autoTrainingConfig"] = (
            capo_personalize.types.auto_training_config.serialize_aws_json_1_1(
                value["auto_training_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SolutionConfig:
    out: SolutionConfig = {}  # type: ignore[typeddict-item]
    if data.get("eventValueThreshold") is not None:
        out["event_value_threshold"] = data["eventValueThreshold"]
    if data.get("hpoConfig") is not None:
        import capo_personalize.types.hpo_config

        out["hpo_config"] = capo_personalize.types.hpo_config.deserialize_aws_json_1_1(
            data["hpoConfig"]
        )
    if data.get("algorithmHyperParameters") is not None:
        import capo_personalize.types.hyper_parameters

        out["algorithm_hyper_parameters"] = (
            capo_personalize.types.hyper_parameters.deserialize_aws_json_1_1(
                data["algorithmHyperParameters"]
            )
        )
    if data.get("featureTransformationParameters") is not None:
        import capo_personalize.types.feature_transformation_parameters

        out["feature_transformation_parameters"] = (
            capo_personalize.types.feature_transformation_parameters.deserialize_aws_json_1_1(
                data["featureTransformationParameters"]
            )
        )
    if data.get("autoMLConfig") is not None:
        import capo_personalize.types.auto_ml_config

        out["auto_ml_config"] = (
            capo_personalize.types.auto_ml_config.deserialize_aws_json_1_1(
                data["autoMLConfig"]
            )
        )
    if data.get("eventsConfig") is not None:
        import capo_personalize.types.events_config

        out["events_config"] = (
            capo_personalize.types.events_config.deserialize_aws_json_1_1(
                data["eventsConfig"]
            )
        )
    if data.get("optimizationObjective") is not None:
        import capo_personalize.types.optimization_objective

        out["optimization_objective"] = (
            capo_personalize.types.optimization_objective.deserialize_aws_json_1_1(
                data["optimizationObjective"]
            )
        )
    if data.get("trainingDataConfig") is not None:
        import capo_personalize.types.training_data_config

        out["training_data_config"] = (
            capo_personalize.types.training_data_config.deserialize_aws_json_1_1(
                data["trainingDataConfig"]
            )
        )
    if data.get("autoTrainingConfig") is not None:
        import capo_personalize.types.auto_training_config

        out["auto_training_config"] = (
            capo_personalize.types.auto_training_config.deserialize_aws_json_1_1(
                data["autoTrainingConfig"]
            )
        )
    return out
