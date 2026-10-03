"""Generated from Smithy shape ``com.amazonaws.pipes#BatchContainerOverrides``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.batch_environment_variable_list
    import capo_pipes.types.batch_resource_requirements_list
    import capo_pipes.types.string_list


class BatchContainerOverrides(TypedDict, closed=True):
    command: NotRequired["capo_pipes.types.string_list.StringList"]
    """<p>The command to send to the container that overrides the default command from the Docker image or the task definition.</p>"""
    environment: NotRequired[
        "capo_pipes.types.batch_environment_variable_list.BatchEnvironmentVariableList"
    ]
    """<p>The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition.</p> <note> <p>Environment variables cannot start with "<code>Batch</code>". This naming convention is reserved for variables that Batch sets.</p> </note>"""
    instance_type: NotRequired["str"]
    """<p>The instance type to use for a multi-node parallel job.</p> <note> <p>This parameter isn't applicable to single-node container jobs or jobs that run on Fargate resources, and shouldn't be provided.</p> </note>"""
    resource_requirements: NotRequired[
        "capo_pipes.types.batch_resource_requirements_list.BatchResourceRequirementsList"
    ]
    """<p>The type and amount of resources to assign to a container. This overrides the settings in the job definition. The supported resources include <code>GPU</code>, <code>MEMORY</code>, and <code>VCPU</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchContainerOverrides) -> dict:
    out: dict = {}
    if "command" in value:
        import capo_pipes.types.string_list

        out["Command"] = capo_pipes.types.string_list.serialize_json(value["command"])
    if "environment" in value:
        import capo_pipes.types.batch_environment_variable_list

        out["Environment"] = (
            capo_pipes.types.batch_environment_variable_list.serialize_json(
                value["environment"]
            )
        )
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "resource_requirements" in value:
        import capo_pipes.types.batch_resource_requirements_list

        out["ResourceRequirements"] = (
            capo_pipes.types.batch_resource_requirements_list.serialize_json(
                value["resource_requirements"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchContainerOverrides:
    out: BatchContainerOverrides = {}  # type: ignore[typeddict-item]
    if data.get("Command") is not None:
        import capo_pipes.types.string_list

        out["command"] = capo_pipes.types.string_list.deserialize_json(data["Command"])
    if data.get("Environment") is not None:
        import capo_pipes.types.batch_environment_variable_list

        out["environment"] = (
            capo_pipes.types.batch_environment_variable_list.deserialize_json(
                data["Environment"]
            )
        )
    if data.get("InstanceType") is not None:
        out["instance_type"] = data["InstanceType"]
    if data.get("ResourceRequirements") is not None:
        import capo_pipes.types.batch_resource_requirements_list

        out["resource_requirements"] = (
            capo_pipes.types.batch_resource_requirements_list.deserialize_json(
                data["ResourceRequirements"]
            )
        )
    return out
