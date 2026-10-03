"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateTrainingJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.profiler_config_for_update
    import capo_sagemaker.types.profiler_rule_configurations
    import capo_sagemaker.types.remote_debug_config_for_update
    import capo_sagemaker.types.resource_config_for_update
    import capo_sagemaker.types.training_job_name


class UpdateTrainingJobRequest(TypedDict, closed=True):
    training_job_name: NotRequired[
        "capo_sagemaker.types.training_job_name.TrainingJobName"
    ]
    """<p>The name of a training job to update the Debugger profiling configuration.</p>"""
    profiler_config: NotRequired[
        "capo_sagemaker.types.profiler_config_for_update.ProfilerConfigForUpdate"
    ]
    """<p>Configuration information for Amazon SageMaker Debugger system monitoring, framework profiling, and storage paths.</p>"""
    profiler_rule_configurations: NotRequired[
        "capo_sagemaker.types.profiler_rule_configurations.ProfilerRuleConfigurations"
    ]
    """<p>Configuration information for Amazon SageMaker Debugger rules for profiling system and framework metrics.</p>"""
    resource_config: NotRequired[
        "capo_sagemaker.types.resource_config_for_update.ResourceConfigForUpdate"
    ]
    """<p>The training job <code>ResourceConfig</code> to update warm pool retention length.</p>"""
    remote_debug_config: NotRequired[
        "capo_sagemaker.types.remote_debug_config_for_update.RemoteDebugConfigForUpdate"
    ]
    """<p>Configuration for remote debugging while the training job is running. You can update the remote debugging configuration when the <code>SecondaryStatus</code> of the job is <code>Downloading</code> or <code>Training</code>.To learn more about the remote debugging functionality of SageMaker, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/train-remote-debugging.html">Access a training container through Amazon Web Services Systems Manager (SSM) for remote debugging</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTrainingJobRequest) -> dict:
    out: dict = {}
    if "training_job_name" in value:
        out["TrainingJobName"] = value["training_job_name"]
    if "profiler_config" in value:
        import capo_sagemaker.types.profiler_config_for_update

        out["ProfilerConfig"] = (
            capo_sagemaker.types.profiler_config_for_update.serialize_aws_json_1_1(
                value["profiler_config"]
            )
        )
    if "profiler_rule_configurations" in value:
        import capo_sagemaker.types.profiler_rule_configurations

        out["ProfilerRuleConfigurations"] = (
            capo_sagemaker.types.profiler_rule_configurations.serialize_aws_json_1_1(
                value["profiler_rule_configurations"]
            )
        )
    if "resource_config" in value:
        import capo_sagemaker.types.resource_config_for_update

        out["ResourceConfig"] = (
            capo_sagemaker.types.resource_config_for_update.serialize_aws_json_1_1(
                value["resource_config"]
            )
        )
    if "remote_debug_config" in value:
        import capo_sagemaker.types.remote_debug_config_for_update

        out["RemoteDebugConfig"] = (
            capo_sagemaker.types.remote_debug_config_for_update.serialize_aws_json_1_1(
                value["remote_debug_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTrainingJobRequest:
    out: UpdateTrainingJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("TrainingJobName") is not None:
        out["training_job_name"] = data["TrainingJobName"]
    if data.get("ProfilerConfig") is not None:
        import capo_sagemaker.types.profiler_config_for_update

        out["profiler_config"] = (
            capo_sagemaker.types.profiler_config_for_update.deserialize_aws_json_1_1(
                data["ProfilerConfig"]
            )
        )
    if data.get("ProfilerRuleConfigurations") is not None:
        import capo_sagemaker.types.profiler_rule_configurations

        out["profiler_rule_configurations"] = (
            capo_sagemaker.types.profiler_rule_configurations.deserialize_aws_json_1_1(
                data["ProfilerRuleConfigurations"]
            )
        )
    if data.get("ResourceConfig") is not None:
        import capo_sagemaker.types.resource_config_for_update

        out["resource_config"] = (
            capo_sagemaker.types.resource_config_for_update.deserialize_aws_json_1_1(
                data["ResourceConfig"]
            )
        )
    if data.get("RemoteDebugConfig") is not None:
        import capo_sagemaker.types.remote_debug_config_for_update

        out["remote_debug_config"] = (
            capo_sagemaker.types.remote_debug_config_for_update.deserialize_aws_json_1_1(
                data["RemoteDebugConfig"]
            )
        )
    return out
