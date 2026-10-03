"""Generated from Smithy shape ``com.amazonaws.batch#EksContainerOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.eks_container_environment_variables
    import capo_batch.types.eks_container_resource_requirements
    import capo_batch.types.string
    import capo_batch.types.string_list


class EksContainerOverride(TypedDict, closed=True):
    name: NotRequired["capo_batch.types.string.String"]
    """<p>A pointer to the container that you want to override. The name must match a unique container name that you wish to override.</p>"""
    image: NotRequired["capo_batch.types.string.String"]
    """<p>The override of the Docker image that's used to start the container.</p>"""
    command: NotRequired["capo_batch.types.string_list.StringList"]
    """<p>The command to send to the container that overrides the default command from the Docker image or the job definition.</p>"""
    args: NotRequired["capo_batch.types.string_list.StringList"]
    """<p>The arguments to the entrypoint to send to the container that overrides the default arguments from the Docker image or the job definition. For more information, see <a href="https://docs.docker.com/engine/reference/builder/#cmd">Dockerfile reference: CMD</a> and <a href="https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/">Define a command an arguments for a pod</a> in the <i>Kubernetes documentation</i>.</p>"""
    env: NotRequired[
        "capo_batch.types.eks_container_environment_variables.EksContainerEnvironmentVariables"
    ]
    """<p>The environment variables to send to the container. You can add new environment variables, which are added to the container at launch. Or, you can override the existing environment variables from the Docker image or the job definition.</p> <note> <p>Environment variables cannot start with "<code>AWS_BATCH</code>". This naming convention is reserved for variables that Batch sets.</p> </note>"""
    resources: NotRequired[
        "capo_batch.types.eks_container_resource_requirements.EksContainerResourceRequirements"
    ]
    """<p>The type and amount of resources to assign to a container. These override the settings in the job definition. The supported resources include <code>memory</code>, <code>cpu</code>, and <code>nvidia.com/gpu</code>. For more information, see <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/">Resource management for pods and containers</a> in the <i>Kubernetes documentation</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksContainerOverride) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "image" in value:
        out["image"] = value["image"]
    if "command" in value:
        import capo_batch.types.string_list

        out["command"] = capo_batch.types.string_list.serialize_json(value["command"])
    if "args" in value:
        import capo_batch.types.string_list

        out["args"] = capo_batch.types.string_list.serialize_json(value["args"])
    if "env" in value:
        import capo_batch.types.eks_container_environment_variables

        out["env"] = (
            capo_batch.types.eks_container_environment_variables.serialize_json(
                value["env"]
            )
        )
    if "resources" in value:
        import capo_batch.types.eks_container_resource_requirements

        out["resources"] = (
            capo_batch.types.eks_container_resource_requirements.serialize_json(
                value["resources"]
            )
        )
    return out


def deserialize_json(data: dict) -> EksContainerOverride:
    out: EksContainerOverride = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("image") is not None:
        out["image"] = data["image"]
    if data.get("command") is not None:
        import capo_batch.types.string_list

        out["command"] = capo_batch.types.string_list.deserialize_json(data["command"])
    if data.get("args") is not None:
        import capo_batch.types.string_list

        out["args"] = capo_batch.types.string_list.deserialize_json(data["args"])
    if data.get("env") is not None:
        import capo_batch.types.eks_container_environment_variables

        out["env"] = (
            capo_batch.types.eks_container_environment_variables.deserialize_json(
                data["env"]
            )
        )
    if data.get("resources") is not None:
        import capo_batch.types.eks_container_resource_requirements

        out["resources"] = (
            capo_batch.types.eks_container_resource_requirements.deserialize_json(
                data["resources"]
            )
        )
    return out
