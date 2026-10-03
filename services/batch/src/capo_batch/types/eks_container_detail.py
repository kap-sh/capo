"""Generated from Smithy shape ``com.amazonaws.batch#EksContainerDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.eks_container_environment_variables
    import capo_batch.types.eks_container_resource_requirements
    import capo_batch.types.eks_container_security_context
    import capo_batch.types.eks_container_volume_mounts
    import capo_batch.types.integer
    import capo_batch.types.string
    import capo_batch.types.string_list


class EksContainerDetail(TypedDict, closed=True):
    name: NotRequired["capo_batch.types.string.String"]
    """<p>The name of the container. If the name isn't specified, the default name "<code>Default</code>" is used. Each container in a pod must have a unique name.</p>"""
    image: NotRequired["capo_batch.types.string.String"]
    """<p>The Docker image used to start the container.</p>"""
    image_pull_policy: NotRequired["capo_batch.types.string.String"]
    """<p>The image pull policy for the container. Supported values are <code>Always</code>, <code>IfNotPresent</code>, and <code>Never</code>. This parameter defaults to <code>Always</code> if the <code>:latest</code> tag is specified, <code>IfNotPresent</code> otherwise. For more information, see <a href="https://kubernetes.io/docs/concepts/containers/images/#updating-images">Updating images</a> in the <i>Kubernetes documentation</i>.</p>"""
    command: NotRequired["capo_batch.types.string_list.StringList"]
    """<p>The entrypoint for the container. For more information, see <a href="https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#entrypoint">Entrypoint</a> in the <i>Kubernetes documentation</i>.</p>"""
    args: NotRequired["capo_batch.types.string_list.StringList"]
    """<p>An array of arguments to the entrypoint. If this isn't specified, the <code>CMD</code> of the container image is used. This corresponds to the <code>args</code> member in the <a href="https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#entrypoint">Entrypoint</a> portion of the <a href="https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/">Pod</a> in Kubernetes. Environment variable references are expanded using the container's environment.</p> <p>If the referenced environment variable doesn't exist, the reference in the command isn't changed. For example, if the reference is to "<code>$(NAME1)</code>" and the <code>NAME1</code> environment variable doesn't exist, the command string will remain "<code>$(NAME1)</code>". <code>$$</code> is replaced with <code>$</code> and the resulting string isn't expanded. For example, <code>$$(VAR_NAME)</code> is passed as <code>$(VAR_NAME)</code> whether or not the <code>VAR_NAME</code> environment variable exists. For more information, see <a href="https://docs.docker.com/engine/reference/builder/#cmd">Dockerfile reference: CMD</a> and <a href="https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/">Define a command and arguments for a pod</a> in the <i>Kubernetes documentation</i>.</p>"""
    env: NotRequired[
        "capo_batch.types.eks_container_environment_variables.EksContainerEnvironmentVariables"
    ]
    """<p>The environment variables to pass to a container.</p> <note> <p>Environment variables cannot start with "<code>AWS_BATCH</code>". This naming convention is reserved for variables that Batch sets.</p> </note>"""
    resources: NotRequired[
        "capo_batch.types.eks_container_resource_requirements.EksContainerResourceRequirements"
    ]
    """<p>The type and amount of resources to assign to a container. The supported resources include <code>memory</code>, <code>cpu</code>, and <code>nvidia.com/gpu</code>. For more information, see <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/">Resource management for pods and containers</a> in the <i>Kubernetes documentation</i>.</p>"""
    exit_code: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The exit code returned for the job attempt. A non-zero exit code is considered failed.</p>"""
    reason: NotRequired["capo_batch.types.string.String"]
    """<p>A short human-readable string to provide additional details for a running or stopped container. It can be up to 255 characters long.</p>"""
    volume_mounts: NotRequired[
        "capo_batch.types.eks_container_volume_mounts.EksContainerVolumeMounts"
    ]
    """<p>The volume mounts for the container. Batch supports <code>emptyDir</code>, <code>hostPath</code>, and <code>secret</code> volume types. For more information about volumes and volume mounts in Kubernetes, see <a href="https://kubernetes.io/docs/concepts/storage/volumes/">Volumes</a> in the <i>Kubernetes documentation</i>.</p>"""
    security_context: NotRequired[
        "capo_batch.types.eks_container_security_context.EksContainerSecurityContext"
    ]
    """<p>The security context for a job. For more information, see <a href="https://kubernetes.io/docs/tasks/configure-pod-container/security-context/">Configure a security context for a pod or container</a> in the <i>Kubernetes documentation</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksContainerDetail) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "image" in value:
        out["image"] = value["image"]
    if "image_pull_policy" in value:
        out["imagePullPolicy"] = value["image_pull_policy"]
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
    if "exit_code" in value:
        out["exitCode"] = value["exit_code"]
    if "reason" in value:
        out["reason"] = value["reason"]
    if "volume_mounts" in value:
        import capo_batch.types.eks_container_volume_mounts

        out["volumeMounts"] = (
            capo_batch.types.eks_container_volume_mounts.serialize_json(
                value["volume_mounts"]
            )
        )
    if "security_context" in value:
        import capo_batch.types.eks_container_security_context

        out["securityContext"] = (
            capo_batch.types.eks_container_security_context.serialize_json(
                value["security_context"]
            )
        )
    return out


def deserialize_json(data: dict) -> EksContainerDetail:
    out: EksContainerDetail = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("image") is not None:
        out["image"] = data["image"]
    if data.get("imagePullPolicy") is not None:
        out["image_pull_policy"] = data["imagePullPolicy"]
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
    if data.get("exitCode") is not None:
        out["exit_code"] = data["exitCode"]
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    if data.get("volumeMounts") is not None:
        import capo_batch.types.eks_container_volume_mounts

        out["volume_mounts"] = (
            capo_batch.types.eks_container_volume_mounts.deserialize_json(
                data["volumeMounts"]
            )
        )
    if data.get("securityContext") is not None:
        import capo_batch.types.eks_container_security_context

        out["security_context"] = (
            capo_batch.types.eks_container_security_context.deserialize_json(
                data["securityContext"]
            )
        )
    return out
