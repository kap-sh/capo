"""Generated from Smithy shape ``com.amazonaws.sagemaker#SearchRecord``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.endpoint
    import capo_sagemaker.types.experiment
    import capo_sagemaker.types.feature_group
    import capo_sagemaker.types.feature_metadata
    import capo_sagemaker.types.hub_content
    import capo_sagemaker.types.hyper_parameter_tuning_job_search_entity
    import capo_sagemaker.types.job
    import capo_sagemaker.types.model_card
    import capo_sagemaker.types.model_dashboard_model
    import capo_sagemaker.types.model_package
    import capo_sagemaker.types.model_package_group
    import capo_sagemaker.types.pipeline
    import capo_sagemaker.types.pipeline_execution
    import capo_sagemaker.types.pipeline_version
    import capo_sagemaker.types.project
    import capo_sagemaker.types.training_job
    import capo_sagemaker.types.trial
    import capo_sagemaker.types.trial_component


class SearchRecord(TypedDict, closed=True):
    training_job: NotRequired["capo_sagemaker.types.training_job.TrainingJob"]
    """<p>The properties of a training job.</p>"""
    experiment: NotRequired["capo_sagemaker.types.experiment.Experiment"]
    """<p>The properties of an experiment.</p>"""
    trial: NotRequired["capo_sagemaker.types.trial.Trial"]
    """<p>The properties of a trial.</p>"""
    trial_component: NotRequired["capo_sagemaker.types.trial_component.TrialComponent"]
    """<p>The properties of a trial component.</p>"""
    endpoint: NotRequired["capo_sagemaker.types.endpoint.Endpoint"]
    model_package: NotRequired["capo_sagemaker.types.model_package.ModelPackage"]
    model_package_group: NotRequired[
        "capo_sagemaker.types.model_package_group.ModelPackageGroup"
    ]
    pipeline: NotRequired["capo_sagemaker.types.pipeline.Pipeline"]
    pipeline_execution: NotRequired[
        "capo_sagemaker.types.pipeline_execution.PipelineExecution"
    ]
    pipeline_version: NotRequired[
        "capo_sagemaker.types.pipeline_version.PipelineVersion"
    ]
    """<p>The version of the pipeline.</p>"""
    feature_group: NotRequired["capo_sagemaker.types.feature_group.FeatureGroup"]
    feature_metadata: NotRequired[
        "capo_sagemaker.types.feature_metadata.FeatureMetadata"
    ]
    """<p>The feature metadata used to search through the features.</p>"""
    project: NotRequired["capo_sagemaker.types.project.Project"]
    """<p>The properties of a project.</p>"""
    hyper_parameter_tuning_job: NotRequired[
        "capo_sagemaker.types.hyper_parameter_tuning_job_search_entity.HyperParameterTuningJobSearchEntity"
    ]
    """<p>The properties of a hyperparameter tuning job.</p>"""
    model_card: NotRequired["capo_sagemaker.types.model_card.ModelCard"]
    """<p>An Amazon SageMaker Model Card that documents details about a machine learning model.</p>"""
    model: NotRequired["capo_sagemaker.types.model_dashboard_model.ModelDashboardModel"]
    job: NotRequired["capo_sagemaker.types.job.Job"]
    """<p>The properties of a job.</p>"""
    hub_content: NotRequired["capo_sagemaker.types.hub_content.HubContent"]
    """<p>The properties of a hub content resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchRecord) -> dict:
    out: dict = {}
    if "training_job" in value:
        import capo_sagemaker.types.training_job

        out["TrainingJob"] = capo_sagemaker.types.training_job.serialize_aws_json_1_1(
            value["training_job"]
        )
    if "experiment" in value:
        import capo_sagemaker.types.experiment

        out["Experiment"] = capo_sagemaker.types.experiment.serialize_aws_json_1_1(
            value["experiment"]
        )
    if "trial" in value:
        import capo_sagemaker.types.trial

        out["Trial"] = capo_sagemaker.types.trial.serialize_aws_json_1_1(value["trial"])
    if "trial_component" in value:
        import capo_sagemaker.types.trial_component

        out["TrialComponent"] = (
            capo_sagemaker.types.trial_component.serialize_aws_json_1_1(
                value["trial_component"]
            )
        )
    if "endpoint" in value:
        import capo_sagemaker.types.endpoint

        out["Endpoint"] = capo_sagemaker.types.endpoint.serialize_aws_json_1_1(
            value["endpoint"]
        )
    if "model_package" in value:
        import capo_sagemaker.types.model_package

        out["ModelPackage"] = capo_sagemaker.types.model_package.serialize_aws_json_1_1(
            value["model_package"]
        )
    if "model_package_group" in value:
        import capo_sagemaker.types.model_package_group

        out["ModelPackageGroup"] = (
            capo_sagemaker.types.model_package_group.serialize_aws_json_1_1(
                value["model_package_group"]
            )
        )
    if "pipeline" in value:
        import capo_sagemaker.types.pipeline

        out["Pipeline"] = capo_sagemaker.types.pipeline.serialize_aws_json_1_1(
            value["pipeline"]
        )
    if "pipeline_execution" in value:
        import capo_sagemaker.types.pipeline_execution

        out["PipelineExecution"] = (
            capo_sagemaker.types.pipeline_execution.serialize_aws_json_1_1(
                value["pipeline_execution"]
            )
        )
    if "pipeline_version" in value:
        import capo_sagemaker.types.pipeline_version

        out["PipelineVersion"] = (
            capo_sagemaker.types.pipeline_version.serialize_aws_json_1_1(
                value["pipeline_version"]
            )
        )
    if "feature_group" in value:
        import capo_sagemaker.types.feature_group

        out["FeatureGroup"] = capo_sagemaker.types.feature_group.serialize_aws_json_1_1(
            value["feature_group"]
        )
    if "feature_metadata" in value:
        import capo_sagemaker.types.feature_metadata

        out["FeatureMetadata"] = (
            capo_sagemaker.types.feature_metadata.serialize_aws_json_1_1(
                value["feature_metadata"]
            )
        )
    if "project" in value:
        import capo_sagemaker.types.project

        out["Project"] = capo_sagemaker.types.project.serialize_aws_json_1_1(
            value["project"]
        )
    if "hyper_parameter_tuning_job" in value:
        import capo_sagemaker.types.hyper_parameter_tuning_job_search_entity

        out["HyperParameterTuningJob"] = (
            capo_sagemaker.types.hyper_parameter_tuning_job_search_entity.serialize_aws_json_1_1(
                value["hyper_parameter_tuning_job"]
            )
        )
    if "model_card" in value:
        import capo_sagemaker.types.model_card

        out["ModelCard"] = capo_sagemaker.types.model_card.serialize_aws_json_1_1(
            value["model_card"]
        )
    if "model" in value:
        import capo_sagemaker.types.model_dashboard_model

        out["Model"] = (
            capo_sagemaker.types.model_dashboard_model.serialize_aws_json_1_1(
                value["model"]
            )
        )
    if "job" in value:
        import capo_sagemaker.types.job

        out["Job"] = capo_sagemaker.types.job.serialize_aws_json_1_1(value["job"])
    if "hub_content" in value:
        import capo_sagemaker.types.hub_content

        out["HubContent"] = capo_sagemaker.types.hub_content.serialize_aws_json_1_1(
            value["hub_content"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchRecord:
    out: SearchRecord = {}  # type: ignore[typeddict-item]
    if data.get("TrainingJob") is not None:
        import capo_sagemaker.types.training_job

        out["training_job"] = (
            capo_sagemaker.types.training_job.deserialize_aws_json_1_1(
                data["TrainingJob"]
            )
        )
    if data.get("Experiment") is not None:
        import capo_sagemaker.types.experiment

        out["experiment"] = capo_sagemaker.types.experiment.deserialize_aws_json_1_1(
            data["Experiment"]
        )
    if data.get("Trial") is not None:
        import capo_sagemaker.types.trial

        out["trial"] = capo_sagemaker.types.trial.deserialize_aws_json_1_1(
            data["Trial"]
        )
    if data.get("TrialComponent") is not None:
        import capo_sagemaker.types.trial_component

        out["trial_component"] = (
            capo_sagemaker.types.trial_component.deserialize_aws_json_1_1(
                data["TrialComponent"]
            )
        )
    if data.get("Endpoint") is not None:
        import capo_sagemaker.types.endpoint

        out["endpoint"] = capo_sagemaker.types.endpoint.deserialize_aws_json_1_1(
            data["Endpoint"]
        )
    if data.get("ModelPackage") is not None:
        import capo_sagemaker.types.model_package

        out["model_package"] = (
            capo_sagemaker.types.model_package.deserialize_aws_json_1_1(
                data["ModelPackage"]
            )
        )
    if data.get("ModelPackageGroup") is not None:
        import capo_sagemaker.types.model_package_group

        out["model_package_group"] = (
            capo_sagemaker.types.model_package_group.deserialize_aws_json_1_1(
                data["ModelPackageGroup"]
            )
        )
    if data.get("Pipeline") is not None:
        import capo_sagemaker.types.pipeline

        out["pipeline"] = capo_sagemaker.types.pipeline.deserialize_aws_json_1_1(
            data["Pipeline"]
        )
    if data.get("PipelineExecution") is not None:
        import capo_sagemaker.types.pipeline_execution

        out["pipeline_execution"] = (
            capo_sagemaker.types.pipeline_execution.deserialize_aws_json_1_1(
                data["PipelineExecution"]
            )
        )
    if data.get("PipelineVersion") is not None:
        import capo_sagemaker.types.pipeline_version

        out["pipeline_version"] = (
            capo_sagemaker.types.pipeline_version.deserialize_aws_json_1_1(
                data["PipelineVersion"]
            )
        )
    if data.get("FeatureGroup") is not None:
        import capo_sagemaker.types.feature_group

        out["feature_group"] = (
            capo_sagemaker.types.feature_group.deserialize_aws_json_1_1(
                data["FeatureGroup"]
            )
        )
    if data.get("FeatureMetadata") is not None:
        import capo_sagemaker.types.feature_metadata

        out["feature_metadata"] = (
            capo_sagemaker.types.feature_metadata.deserialize_aws_json_1_1(
                data["FeatureMetadata"]
            )
        )
    if data.get("Project") is not None:
        import capo_sagemaker.types.project

        out["project"] = capo_sagemaker.types.project.deserialize_aws_json_1_1(
            data["Project"]
        )
    if data.get("HyperParameterTuningJob") is not None:
        import capo_sagemaker.types.hyper_parameter_tuning_job_search_entity

        out["hyper_parameter_tuning_job"] = (
            capo_sagemaker.types.hyper_parameter_tuning_job_search_entity.deserialize_aws_json_1_1(
                data["HyperParameterTuningJob"]
            )
        )
    if data.get("ModelCard") is not None:
        import capo_sagemaker.types.model_card

        out["model_card"] = capo_sagemaker.types.model_card.deserialize_aws_json_1_1(
            data["ModelCard"]
        )
    if data.get("Model") is not None:
        import capo_sagemaker.types.model_dashboard_model

        out["model"] = (
            capo_sagemaker.types.model_dashboard_model.deserialize_aws_json_1_1(
                data["Model"]
            )
        )
    if data.get("Job") is not None:
        import capo_sagemaker.types.job

        out["job"] = capo_sagemaker.types.job.deserialize_aws_json_1_1(data["Job"])
    if data.get("HubContent") is not None:
        import capo_sagemaker.types.hub_content

        out["hub_content"] = capo_sagemaker.types.hub_content.deserialize_aws_json_1_1(
            data["HubContent"]
        )
    return out


def redact_sensitive(value: SearchRecord) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "model_package" in value:
        import capo_sagemaker.types.model_package

        out["model_package"] = capo_sagemaker.types.model_package.redact_sensitive(
            value["model_package"]
        )
    if "model_card" in value:
        import capo_sagemaker.types.model_card

        out["model_card"] = capo_sagemaker.types.model_card.redact_sensitive(
            value["model_card"]
        )
    return out
