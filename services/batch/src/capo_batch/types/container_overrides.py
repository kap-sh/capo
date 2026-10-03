"""Generated from Smithy shape ``com.amazonaws.batch#ContainerOverrides``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.environment_variables
    import capo_batch.types.integer
    import capo_batch.types.resource_requirements
    import capo_batch.types.string
    import capo_batch.types.string_list


class ContainerOverrides(TypedDict, closed=True):
    vcpus: NotRequired["capo_batch.types.integer.Integer"]
    """<p>This parameter is deprecated, use <code>resourceRequirements</code> to override the <code>vcpus</code> parameter that's set in the job definition. It's not supported for jobs running on Fargate resources. For jobs that run on Amazon EC2 resources, it overrides the <code>vcpus</code> parameter set in the job definition, but doesn't override any vCPU requirement specified in the <code>resourceRequirements</code> structure in the job definition. To override vCPU requirements that are specified in the <code>resourceRequirements</code> structure in the job definition, <code>resourceRequirements</code> must be specified in the <code>SubmitJob</code> request, with <code>type</code> set to <code>VCPU</code> and <code>value</code> set to the new value. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/troubleshooting.html#override-resource-requirements">Can't override job definition resource requirements</a> in the <i>Batch User Guide</i>.</p>"""
    memory: NotRequired["capo_batch.types.integer.Integer"]
    """<p>This parameter is deprecated, use <code>resourceRequirements</code> to override the memory requirements specified in the job definition. It's not supported for jobs running on Fargate resources. For jobs that run on Amazon EC2 resources, it overrides the <code>memory</code> parameter set in the job definition, but doesn't override any memory requirement that's specified in the <code>resourceRequirements</code> structure in the job definition. To override memory requirements that are specified in the <code>resourceRequirements</code> structure in the job definition, <code>resourceRequirements</code> must be specified in the <code>SubmitJob</code> request, with <code>type</code> set to <code>MEMORY</code> and <code>value</code> set to the new value. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/troubleshooting.html#override-resource-requirements">Can't override job definition resource requirements</a> in the <i>Batch User Guide</i>.</p>"""
    command: NotRequired["capo_batch.types.string_list.StringList"]
    """<p>The command to send to the container that overrides the default command from the Docker image or the job definition.</p> <note> <p>This parameter can't contain an empty string.</p> </note>"""
    instance_type: NotRequired["capo_batch.types.string.String"]
    """<p>The instance type to use for a multi-node parallel job.</p> <note> <p>This parameter isn't applicable to single-node container jobs or jobs that run on Fargate resources, and shouldn't be provided.</p> </note>"""
    environment: NotRequired[
        "capo_batch.types.environment_variables.EnvironmentVariables"
    ]
    """<p>The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the job definition.</p> <note> <p>Environment variables cannot start with "<code>AWS_BATCH</code>". This naming convention is reserved for variables that Batch sets.</p> </note>"""
    resource_requirements: NotRequired[
        "capo_batch.types.resource_requirements.ResourceRequirements"
    ]
    """<p>The type and amount of resources to assign to a container. This overrides the settings in the job definition. The supported resources include <code>GPU</code>, <code>MEMORY</code>, and <code>VCPU</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContainerOverrides) -> dict:
    out: dict = {}
    if "vcpus" in value:
        out["vcpus"] = value["vcpus"]
    if "memory" in value:
        out["memory"] = value["memory"]
    if "command" in value:
        import capo_batch.types.string_list

        out["command"] = capo_batch.types.string_list.serialize_json(value["command"])
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    if "environment" in value:
        import capo_batch.types.environment_variables

        out["environment"] = capo_batch.types.environment_variables.serialize_json(
            value["environment"]
        )
    if "resource_requirements" in value:
        import capo_batch.types.resource_requirements

        out["resourceRequirements"] = (
            capo_batch.types.resource_requirements.serialize_json(
                value["resource_requirements"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContainerOverrides:
    out: ContainerOverrides = {}  # type: ignore[typeddict-item]
    if data.get("vcpus") is not None:
        out["vcpus"] = data["vcpus"]
    if data.get("memory") is not None:
        out["memory"] = data["memory"]
    if data.get("command") is not None:
        import capo_batch.types.string_list

        out["command"] = capo_batch.types.string_list.deserialize_json(data["command"])
    if data.get("instanceType") is not None:
        out["instance_type"] = data["instanceType"]
    if data.get("environment") is not None:
        import capo_batch.types.environment_variables

        out["environment"] = capo_batch.types.environment_variables.deserialize_json(
            data["environment"]
        )
    if data.get("resourceRequirements") is not None:
        import capo_batch.types.resource_requirements

        out["resource_requirements"] = (
            capo_batch.types.resource_requirements.deserialize_json(
                data["resourceRequirements"]
            )
        )
    return out
