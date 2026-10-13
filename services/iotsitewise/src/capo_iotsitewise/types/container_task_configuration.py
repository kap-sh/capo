"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ContainerTaskConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.command_list
    import capo_iotsitewise.types.ecr_uri
    import capo_iotsitewise.types.environment_variables_map
    import capo_iotsitewise.types.ephemeral_storage_configuration
    import capo_iotsitewise.types.iam_role_arn
    import capo_iotsitewise.types.mount_list
    import capo_iotsitewise.types.processing_type
    import capo_iotsitewise.types.processing_unit
    import capo_iotsitewise.types.timeout_seconds


class ContainerTaskConfiguration(TypedDict, closed=True):
    ecr_uri: "capo_iotsitewise.types.ecr_uri.EcrUri"
    """<p>The Amazon ECR image URI for the task container.</p>"""
    task_execution_role: "capo_iotsitewise.types.iam_role_arn.IamRoleArn"
    """<p>The ARN of the IAM role that grants the containerized workload permissions to access AWS resources.</p>"""
    processing_type: "capo_iotsitewise.types.processing_type.ProcessingType"
    """<p>The processing type for compute resources.</p>"""
    processing_unit: "capo_iotsitewise.types.processing_unit.ProcessingUnit"
    """<p>The processing unit allocation that determines the vCPU, memory, and GPU resources.</p>"""
    ephemeral_storage_configuration: NotRequired[
        "capo_iotsitewise.types.ephemeral_storage_configuration.EphemeralStorageConfiguration"
    ]
    """<p>Ephemeral storage configuration for the container task.</p>"""
    command: NotRequired["capo_iotsitewise.types.command_list.CommandList"]
    """<p>The command to execute in the container.</p>"""
    timeout_seconds: NotRequired[
        "capo_iotsitewise.types.timeout_seconds.TimeoutSeconds"
    ]
    """<p>The timeout in seconds for task execution. Default: 3600 (1 hour).</p>"""
    environment_variables: NotRequired[
        "capo_iotsitewise.types.environment_variables_map.EnvironmentVariablesMap"
    ]
    """<p>Environment variables passed to the container at runtime.</p>"""
    mounts: NotRequired["capo_iotsitewise.types.mount_list.MountList"]
    """<p>Mounts attached to the container filesystem. Each mount exposes an external data source as a local directory inside the container. The service assigns each mount a container path based on the mount name. The container reads files through that path as if the data were on the local filesystem.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContainerTaskConfiguration) -> dict:
    out: dict = {}
    out["ecrUri"] = value["ecr_uri"]
    out["taskExecutionRole"] = value["task_execution_role"]
    import capo_iotsitewise.types.processing_type

    out["processingType"] = capo_iotsitewise.types.processing_type.serialize_json(
        value["processing_type"]
    )
    import capo_iotsitewise.types.processing_unit

    out["processingUnit"] = capo_iotsitewise.types.processing_unit.serialize_json(
        value["processing_unit"]
    )
    if "ephemeral_storage_configuration" in value:
        import capo_iotsitewise.types.ephemeral_storage_configuration

        out["ephemeralStorageConfiguration"] = (
            capo_iotsitewise.types.ephemeral_storage_configuration.serialize_json(
                value["ephemeral_storage_configuration"]
            )
        )
    if "command" in value:
        import capo_iotsitewise.types.command_list

        out["command"] = capo_iotsitewise.types.command_list.serialize_json(
            value["command"]
        )
    if "timeout_seconds" in value:
        out["timeoutSeconds"] = value["timeout_seconds"]
    if "environment_variables" in value:
        import capo_iotsitewise.types.environment_variables_map

        out["environmentVariables"] = (
            capo_iotsitewise.types.environment_variables_map.serialize_json(
                value["environment_variables"]
            )
        )
    if "mounts" in value:
        import capo_iotsitewise.types.mount_list

        out["mounts"] = capo_iotsitewise.types.mount_list.serialize_json(
            value["mounts"]
        )
    return out


def deserialize_json(data: dict) -> ContainerTaskConfiguration:
    out: ContainerTaskConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ecrUri") is not None:
        out["ecr_uri"] = data["ecrUri"]
    else:
        raise DeserializationError("ContainerTaskConfiguration.ecr_uri required")
    if data.get("taskExecutionRole") is not None:
        out["task_execution_role"] = data["taskExecutionRole"]
    else:
        raise DeserializationError(
            "ContainerTaskConfiguration.task_execution_role required"
        )
    if data.get("processingType") is not None:
        import capo_iotsitewise.types.processing_type

        out["processing_type"] = (
            capo_iotsitewise.types.processing_type.deserialize_json(
                data["processingType"]
            )
        )
    else:
        raise DeserializationError(
            "ContainerTaskConfiguration.processing_type required"
        )
    if data.get("processingUnit") is not None:
        import capo_iotsitewise.types.processing_unit

        out["processing_unit"] = (
            capo_iotsitewise.types.processing_unit.deserialize_json(
                data["processingUnit"]
            )
        )
    else:
        raise DeserializationError(
            "ContainerTaskConfiguration.processing_unit required"
        )
    if data.get("ephemeralStorageConfiguration") is not None:
        import capo_iotsitewise.types.ephemeral_storage_configuration

        out["ephemeral_storage_configuration"] = (
            capo_iotsitewise.types.ephemeral_storage_configuration.deserialize_json(
                data["ephemeralStorageConfiguration"]
            )
        )
    if data.get("command") is not None:
        import capo_iotsitewise.types.command_list

        out["command"] = capo_iotsitewise.types.command_list.deserialize_json(
            data["command"]
        )
    if data.get("timeoutSeconds") is not None:
        out["timeout_seconds"] = data["timeoutSeconds"]
    if data.get("environmentVariables") is not None:
        import capo_iotsitewise.types.environment_variables_map

        out["environment_variables"] = (
            capo_iotsitewise.types.environment_variables_map.deserialize_json(
                data["environmentVariables"]
            )
        )
    if data.get("mounts") is not None:
        import capo_iotsitewise.types.mount_list

        out["mounts"] = capo_iotsitewise.types.mount_list.deserialize_json(
            data["mounts"]
        )
    return out


def redact_sensitive(value: ContainerTaskConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ecr_uri" in value:
        out["ecr_uri"] = "*** Sensitive Data Redacted ***"
    if "task_execution_role" in value:
        out["task_execution_role"] = "*** Sensitive Data Redacted ***"
    if "command" in value:
        out["command"] = "*** Sensitive Data Redacted ***"
    if "environment_variables" in value:
        out["environment_variables"] = "*** Sensitive Data Redacted ***"
    return out
