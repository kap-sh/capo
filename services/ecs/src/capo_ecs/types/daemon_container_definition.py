"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonContainerDefinition``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_boolean
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.container_dependencies
    import capo_ecs.types.container_restart_policy
    import capo_ecs.types.daemon_linux_parameters
    import capo_ecs.types.environment_files
    import capo_ecs.types.environment_variables
    import capo_ecs.types.firelens_configuration
    import capo_ecs.types.health_check
    import capo_ecs.types.integer
    import capo_ecs.types.log_configuration
    import capo_ecs.types.mount_point_list
    import capo_ecs.types.repository_credentials
    import capo_ecs.types.secret_list
    import capo_ecs.types.string
    import capo_ecs.types.string_list
    import capo_ecs.types.system_controls
    import capo_ecs.types.ulimit_list


class DaemonContainerDefinition(TypedDict, closed=True):
    name: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of the container. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed.</p>"""
    image: "capo_ecs.types.string.String"
    """<p>The image used to start the container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with either <code> <i>repository-url</i>/<i>image</i>:<i>tag</i> </code> or <code> <i>repository-url</i>/<i>image</i>@<i>digest</i> </code>.</p>"""
    memory: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The amount (in MiB) of memory to present to the container. If the container attempts to exceed the memory specified here, the container is killed.</p>"""
    memory_reservation: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The soft limit (in MiB) of memory to reserve for the container.</p>"""
    repository_credentials: NotRequired[
        "capo_ecs.types.repository_credentials.RepositoryCredentials"
    ]
    """<p>The private repository authentication credentials to use.</p>"""
    health_check: NotRequired["capo_ecs.types.health_check.HealthCheck"]
    """<p>The container health check command and associated configuration parameters for the container.</p>"""
    cpu: "capo_ecs.types.integer.Integer"
    """<p>The number of <code>cpu</code> units reserved for the container.</p>"""
    essential: NotRequired["capo_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>If the <code>essential</code> parameter of a container is marked as <code>true</code>, and that container fails or stops for any reason, all other containers that are part of the task are stopped.</p>"""
    entry_point: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>The entry point that's passed to the container.</p>"""
    command: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>The command that's passed to the container.</p>"""
    working_directory: NotRequired["capo_ecs.types.string.String"]
    """<p>The working directory to run commands inside the container in.</p>"""
    environment_files: NotRequired["capo_ecs.types.environment_files.EnvironmentFiles"]
    """<p>A list of files containing the environment variables to pass to a container.</p>"""
    environment: NotRequired[
        "capo_ecs.types.environment_variables.EnvironmentVariables"
    ]
    """<p>The environment variables to pass to a container.</p>"""
    secrets: NotRequired["capo_ecs.types.secret_list.SecretList"]
    """<p>The secrets to pass to the container.</p>"""
    readonly_root_filesystem: NotRequired["capo_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>When this parameter is true, the container is given read-only access to its root file system.</p>"""
    mount_points: NotRequired["capo_ecs.types.mount_point_list.MountPointList"]
    """<p>The mount points for data volumes in your container.</p>"""
    log_configuration: NotRequired["capo_ecs.types.log_configuration.LogConfiguration"]
    """<p>The log configuration specification for the container.</p>"""
    firelens_configuration: NotRequired[
        "capo_ecs.types.firelens_configuration.FirelensConfiguration"
    ]
    """<p>The FireLens configuration for the container. This is used to specify and configure a log router for container logs.</p>"""
    privileged: NotRequired["capo_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>When this parameter is true, the container is given elevated privileges on the host container instance (similar to the <code>root</code> user).</p>"""
    user: NotRequired["capo_ecs.types.string.String"]
    """<p>The user to use inside the container.</p>"""
    ulimits: NotRequired["capo_ecs.types.ulimit_list.UlimitList"]
    """<p>A list of <code>ulimits</code> to set in the container.</p>"""
    linux_parameters: NotRequired[
        "capo_ecs.types.daemon_linux_parameters.DaemonLinuxParameters"
    ]
    """<p>Linux-specific modifications that are applied to the container configuration, such as Linux kernel capabilities.</p>"""
    depends_on: NotRequired[
        "capo_ecs.types.container_dependencies.ContainerDependencies"
    ]
    """<p>The dependencies defined for container startup and shutdown. A container can contain multiple dependencies on other containers in a task definition.</p>"""
    start_timeout: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>Time duration (in seconds) to wait before giving up on resolving dependencies for a container.</p>"""
    stop_timeout: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>Time duration (in seconds) to wait before the container is forcefully killed if it doesn't exit normally on its own.</p>"""
    system_controls: NotRequired["capo_ecs.types.system_controls.SystemControls"]
    """<p>A list of namespaced kernel parameters to set in the container.</p>"""
    interactive: NotRequired["capo_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>When this parameter is <code>true</code>, you can deploy containerized applications that require <code>stdin</code> or a <code>tty</code> to be allocated.</p>"""
    pseudo_terminal: NotRequired["capo_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>When this parameter is <code>true</code>, a TTY is allocated.</p>"""
    restart_policy: NotRequired[
        "capo_ecs.types.container_restart_policy.ContainerRestartPolicy"
    ]
    """<p>The restart policy for the container. When you set up a restart policy, Amazon ECS can restart the container without needing to replace the task.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonContainerDefinition) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    out["image"] = value["image"]
    if "memory" in value:
        out["memory"] = value["memory"]
    if "memory_reservation" in value:
        out["memoryReservation"] = value["memory_reservation"]
    if "repository_credentials" in value:
        import capo_ecs.types.repository_credentials

        out["repositoryCredentials"] = (
            capo_ecs.types.repository_credentials.serialize_aws_json_1_1(
                value["repository_credentials"]
            )
        )
    if "health_check" in value:
        import capo_ecs.types.health_check

        out["healthCheck"] = capo_ecs.types.health_check.serialize_aws_json_1_1(
            value["health_check"]
        )
    out["cpu"] = value.get("cpu", 0)
    if "essential" in value:
        out["essential"] = value["essential"]
    if "entry_point" in value:
        import capo_ecs.types.string_list

        out["entryPoint"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
            value["entry_point"]
        )
    if "command" in value:
        import capo_ecs.types.string_list

        out["command"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
            value["command"]
        )
    if "working_directory" in value:
        out["workingDirectory"] = value["working_directory"]
    if "environment_files" in value:
        import capo_ecs.types.environment_files

        out["environmentFiles"] = (
            capo_ecs.types.environment_files.serialize_aws_json_1_1(
                value["environment_files"]
            )
        )
    if "environment" in value:
        import capo_ecs.types.environment_variables

        out["environment"] = (
            capo_ecs.types.environment_variables.serialize_aws_json_1_1(
                value["environment"]
            )
        )
    if "secrets" in value:
        import capo_ecs.types.secret_list

        out["secrets"] = capo_ecs.types.secret_list.serialize_aws_json_1_1(
            value["secrets"]
        )
    if "readonly_root_filesystem" in value:
        out["readonlyRootFilesystem"] = value["readonly_root_filesystem"]
    if "mount_points" in value:
        import capo_ecs.types.mount_point_list

        out["mountPoints"] = capo_ecs.types.mount_point_list.serialize_aws_json_1_1(
            value["mount_points"]
        )
    if "log_configuration" in value:
        import capo_ecs.types.log_configuration

        out["logConfiguration"] = (
            capo_ecs.types.log_configuration.serialize_aws_json_1_1(
                value["log_configuration"]
            )
        )
    if "firelens_configuration" in value:
        import capo_ecs.types.firelens_configuration

        out["firelensConfiguration"] = (
            capo_ecs.types.firelens_configuration.serialize_aws_json_1_1(
                value["firelens_configuration"]
            )
        )
    if "privileged" in value:
        out["privileged"] = value["privileged"]
    if "user" in value:
        out["user"] = value["user"]
    if "ulimits" in value:
        import capo_ecs.types.ulimit_list

        out["ulimits"] = capo_ecs.types.ulimit_list.serialize_aws_json_1_1(
            value["ulimits"]
        )
    if "linux_parameters" in value:
        import capo_ecs.types.daemon_linux_parameters

        out["linuxParameters"] = (
            capo_ecs.types.daemon_linux_parameters.serialize_aws_json_1_1(
                value["linux_parameters"]
            )
        )
    if "depends_on" in value:
        import capo_ecs.types.container_dependencies

        out["dependsOn"] = capo_ecs.types.container_dependencies.serialize_aws_json_1_1(
            value["depends_on"]
        )
    if "start_timeout" in value:
        out["startTimeout"] = value["start_timeout"]
    if "stop_timeout" in value:
        out["stopTimeout"] = value["stop_timeout"]
    if "system_controls" in value:
        import capo_ecs.types.system_controls

        out["systemControls"] = capo_ecs.types.system_controls.serialize_aws_json_1_1(
            value["system_controls"]
        )
    if "interactive" in value:
        out["interactive"] = value["interactive"]
    if "pseudo_terminal" in value:
        out["pseudoTerminal"] = value["pseudo_terminal"]
    if "restart_policy" in value:
        import capo_ecs.types.container_restart_policy

        out["restartPolicy"] = (
            capo_ecs.types.container_restart_policy.serialize_aws_json_1_1(
                value["restart_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DaemonContainerDefinition:
    out: DaemonContainerDefinition = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("image") is not None:
        out["image"] = data["image"]
    else:
        out["image"] = ""
    if data.get("memory") is not None:
        out["memory"] = data["memory"]
    if data.get("memoryReservation") is not None:
        out["memory_reservation"] = data["memoryReservation"]
    if data.get("repositoryCredentials") is not None:
        import capo_ecs.types.repository_credentials

        out["repository_credentials"] = (
            capo_ecs.types.repository_credentials.deserialize_aws_json_1_1(
                data["repositoryCredentials"]
            )
        )
    if data.get("healthCheck") is not None:
        import capo_ecs.types.health_check

        out["health_check"] = capo_ecs.types.health_check.deserialize_aws_json_1_1(
            data["healthCheck"]
        )
    if data.get("cpu") is not None:
        out["cpu"] = data["cpu"]
    else:
        out["cpu"] = 0
    if data.get("essential") is not None:
        out["essential"] = data["essential"]
    if data.get("entryPoint") is not None:
        import capo_ecs.types.string_list

        out["entry_point"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["entryPoint"]
        )
    if data.get("command") is not None:
        import capo_ecs.types.string_list

        out["command"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["command"]
        )
    if data.get("workingDirectory") is not None:
        out["working_directory"] = data["workingDirectory"]
    if data.get("environmentFiles") is not None:
        import capo_ecs.types.environment_files

        out["environment_files"] = (
            capo_ecs.types.environment_files.deserialize_aws_json_1_1(
                data["environmentFiles"]
            )
        )
    if data.get("environment") is not None:
        import capo_ecs.types.environment_variables

        out["environment"] = (
            capo_ecs.types.environment_variables.deserialize_aws_json_1_1(
                data["environment"]
            )
        )
    if data.get("secrets") is not None:
        import capo_ecs.types.secret_list

        out["secrets"] = capo_ecs.types.secret_list.deserialize_aws_json_1_1(
            data["secrets"]
        )
    if data.get("readonlyRootFilesystem") is not None:
        out["readonly_root_filesystem"] = data["readonlyRootFilesystem"]
    if data.get("mountPoints") is not None:
        import capo_ecs.types.mount_point_list

        out["mount_points"] = capo_ecs.types.mount_point_list.deserialize_aws_json_1_1(
            data["mountPoints"]
        )
    if data.get("logConfiguration") is not None:
        import capo_ecs.types.log_configuration

        out["log_configuration"] = (
            capo_ecs.types.log_configuration.deserialize_aws_json_1_1(
                data["logConfiguration"]
            )
        )
    if data.get("firelensConfiguration") is not None:
        import capo_ecs.types.firelens_configuration

        out["firelens_configuration"] = (
            capo_ecs.types.firelens_configuration.deserialize_aws_json_1_1(
                data["firelensConfiguration"]
            )
        )
    if data.get("privileged") is not None:
        out["privileged"] = data["privileged"]
    if data.get("user") is not None:
        out["user"] = data["user"]
    if data.get("ulimits") is not None:
        import capo_ecs.types.ulimit_list

        out["ulimits"] = capo_ecs.types.ulimit_list.deserialize_aws_json_1_1(
            data["ulimits"]
        )
    if data.get("linuxParameters") is not None:
        import capo_ecs.types.daemon_linux_parameters

        out["linux_parameters"] = (
            capo_ecs.types.daemon_linux_parameters.deserialize_aws_json_1_1(
                data["linuxParameters"]
            )
        )
    if data.get("dependsOn") is not None:
        import capo_ecs.types.container_dependencies

        out["depends_on"] = (
            capo_ecs.types.container_dependencies.deserialize_aws_json_1_1(
                data["dependsOn"]
            )
        )
    if data.get("startTimeout") is not None:
        out["start_timeout"] = data["startTimeout"]
    if data.get("stopTimeout") is not None:
        out["stop_timeout"] = data["stopTimeout"]
    if data.get("systemControls") is not None:
        import capo_ecs.types.system_controls

        out["system_controls"] = (
            capo_ecs.types.system_controls.deserialize_aws_json_1_1(
                data["systemControls"]
            )
        )
    if data.get("interactive") is not None:
        out["interactive"] = data["interactive"]
    if data.get("pseudoTerminal") is not None:
        out["pseudo_terminal"] = data["pseudoTerminal"]
    if data.get("restartPolicy") is not None:
        import capo_ecs.types.container_restart_policy

        out["restart_policy"] = (
            capo_ecs.types.container_restart_policy.deserialize_aws_json_1_1(
                data["restartPolicy"]
            )
        )
    return out


def redact_sensitive(value: DaemonContainerDefinition) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "repository_credentials" in value:
        out["repository_credentials"] = "*** Sensitive Data Redacted ***"
    if "environment" in value:
        out["environment"] = "*** Sensitive Data Redacted ***"
    return out
