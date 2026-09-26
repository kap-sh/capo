"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#CreateMicrovmImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda_microvms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_microvms.types.capability_list
    import capo_lambda_microvms.types.code_artifact
    import capo_lambda_microvms.types.cpu_configuration_list
    import capo_lambda_microvms.types.environment_variable_map
    import capo_lambda_microvms.types.hooks
    import capo_lambda_microvms.types.image_name
    import capo_lambda_microvms.types.logging
    import capo_lambda_microvms.types.network_connector_list
    import capo_lambda_microvms.types.non_blank_string
    import capo_lambda_microvms.types.resources_list
    import capo_lambda_microvms.types.role_arn
    import capo_lambda_microvms.types.tags
    import capo_lambda_microvms.types.version


class CreateMicrovmImageRequest(TypedDict, closed=True):
    base_image_arn: "capo_lambda_microvms.types.non_blank_string.NonBlankString"
    """<p>The ARN of the Lambda-managed base MicroVM image to build upon. Use ListManagedMicrovmImages to discover available base images.</p>"""
    base_image_version: NotRequired["capo_lambda_microvms.types.version.Version"]
    """<p>The specific version of the base MicroVM image to use.</p>"""
    build_role_arn: "capo_lambda_microvms.types.role_arn.RoleArn"
    """<p>The ARN of the IAM role assumed during the image build process. This role must have permissions to access the code artifact and any required resources.</p>"""
    description: NotRequired["str"]
    """<p>A description of the MicroVM image.</p>"""
    code_artifact: "capo_lambda_microvms.types.code_artifact.CodeArtifact"
    """<p>The code artifact containing the application code and metadata for the MicroVM image.</p>"""
    logging: NotRequired["capo_lambda_microvms.types.logging.Logging"]
    r"""<p>The logging configuration for build-time and runtime logs. Specify {\"cloudWatch\": {\"logGroup\": \"...\"}} to stream logs to a custom CloudWatch log group, or {\"disabled\": {}} to turn off logging.</p>"""
    egress_network_connectors: NotRequired[
        "capo_lambda_microvms.types.network_connector_list.NetworkConnectorList"
    ]
    """<p>The list of egress network connectors available to the MicroVM at runtime.</p>"""
    cpu_configurations: NotRequired[
        "capo_lambda_microvms.types.cpu_configuration_list.CpuConfigurationList"
    ]
    """<p>The list of supported CPU configurations for the MicroVM.</p>"""
    resources: NotRequired["capo_lambda_microvms.types.resources_list.ResourcesList"]
    """<p>The resource requirements for the MicroVM.</p>"""
    additional_os_capabilities: NotRequired[
        "capo_lambda_microvms.types.capability_list.CapabilityList"
    ]
    """<p>Additional OS capabilities granted to the MicroVM runtime environment.</p>"""
    hooks: NotRequired["capo_lambda_microvms.types.hooks.Hooks"]
    environment_variables: NotRequired[
        "capo_lambda_microvms.types.environment_variable_map.EnvironmentVariableMap"
    ]
    """<p>Environment variables set in the MicroVM runtime environment.</p>"""
    name: "capo_lambda_microvms.types.image_name.ImageName"
    """<p>The name of the MicroVM image. Must be unique within the AWS account.</p>"""
    tags: NotRequired["capo_lambda_microvms.types.tags.Tags"]
    """<p>A set of key-value pairs that you can attach to the resource. Use tags to categorize resources for cost allocation, access control (ABAC), and organization.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token, the operation returns the successful response without performing any further actions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMicrovmImageRequest) -> dict:
    out: dict = {}
    out["baseImageArn"] = value["base_image_arn"]
    if "base_image_version" in value:
        out["baseImageVersion"] = value["base_image_version"]
    out["buildRoleArn"] = value["build_role_arn"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_lambda_microvms.types.code_artifact

    out["codeArtifact"] = capo_lambda_microvms.types.code_artifact.serialize_json(
        value["code_artifact"]
    )
    if "logging" in value:
        import capo_lambda_microvms.types.logging

        out["logging"] = capo_lambda_microvms.types.logging.serialize_json(
            value["logging"]
        )
    if "egress_network_connectors" in value:
        import capo_lambda_microvms.types.network_connector_list

        out["egressNetworkConnectors"] = (
            capo_lambda_microvms.types.network_connector_list.serialize_json(
                value["egress_network_connectors"]
            )
        )
    if "cpu_configurations" in value:
        import capo_lambda_microvms.types.cpu_configuration_list

        out["cpuConfigurations"] = (
            capo_lambda_microvms.types.cpu_configuration_list.serialize_json(
                value["cpu_configurations"]
            )
        )
    if "resources" in value:
        import capo_lambda_microvms.types.resources_list

        out["resources"] = capo_lambda_microvms.types.resources_list.serialize_json(
            value["resources"]
        )
    if "additional_os_capabilities" in value:
        import capo_lambda_microvms.types.capability_list

        out["additionalOsCapabilities"] = (
            capo_lambda_microvms.types.capability_list.serialize_json(
                value["additional_os_capabilities"]
            )
        )
    if "hooks" in value:
        import capo_lambda_microvms.types.hooks

        out["hooks"] = capo_lambda_microvms.types.hooks.serialize_json(value["hooks"])
    if "environment_variables" in value:
        import capo_lambda_microvms.types.environment_variable_map

        out["environmentVariables"] = (
            capo_lambda_microvms.types.environment_variable_map.serialize_json(
                value["environment_variables"]
            )
        )
    out["name"] = value["name"]
    if "tags" in value:
        import capo_lambda_microvms.types.tags

        out["tags"] = capo_lambda_microvms.types.tags.serialize_json(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateMicrovmImageRequest:
    out: CreateMicrovmImageRequest = {}  # type: ignore[typeddict-item]
    if data.get("baseImageArn") is not None:
        out["base_image_arn"] = data["baseImageArn"]
    else:
        raise DeserializationError("CreateMicrovmImageRequest.base_image_arn required")
    if data.get("baseImageVersion") is not None:
        out["base_image_version"] = data["baseImageVersion"]
    if data.get("buildRoleArn") is not None:
        out["build_role_arn"] = data["buildRoleArn"]
    else:
        raise DeserializationError("CreateMicrovmImageRequest.build_role_arn required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("codeArtifact") is not None:
        import capo_lambda_microvms.types.code_artifact

        out["code_artifact"] = (
            capo_lambda_microvms.types.code_artifact.deserialize_json(
                data["codeArtifact"]
            )
        )
    else:
        raise DeserializationError("CreateMicrovmImageRequest.code_artifact required")
    if data.get("logging") is not None:
        import capo_lambda_microvms.types.logging

        out["logging"] = capo_lambda_microvms.types.logging.deserialize_json(
            data["logging"]
        )
    if data.get("egressNetworkConnectors") is not None:
        import capo_lambda_microvms.types.network_connector_list

        out["egress_network_connectors"] = (
            capo_lambda_microvms.types.network_connector_list.deserialize_json(
                data["egressNetworkConnectors"]
            )
        )
    if data.get("cpuConfigurations") is not None:
        import capo_lambda_microvms.types.cpu_configuration_list

        out["cpu_configurations"] = (
            capo_lambda_microvms.types.cpu_configuration_list.deserialize_json(
                data["cpuConfigurations"]
            )
        )
    if data.get("resources") is not None:
        import capo_lambda_microvms.types.resources_list

        out["resources"] = capo_lambda_microvms.types.resources_list.deserialize_json(
            data["resources"]
        )
    if data.get("additionalOsCapabilities") is not None:
        import capo_lambda_microvms.types.capability_list

        out["additional_os_capabilities"] = (
            capo_lambda_microvms.types.capability_list.deserialize_json(
                data["additionalOsCapabilities"]
            )
        )
    if data.get("hooks") is not None:
        import capo_lambda_microvms.types.hooks

        out["hooks"] = capo_lambda_microvms.types.hooks.deserialize_json(data["hooks"])
    if data.get("environmentVariables") is not None:
        import capo_lambda_microvms.types.environment_variable_map

        out["environment_variables"] = (
            capo_lambda_microvms.types.environment_variable_map.deserialize_json(
                data["environmentVariables"]
            )
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateMicrovmImageRequest.name required")
    if data.get("tags") is not None:
        import capo_lambda_microvms.types.tags

        out["tags"] = capo_lambda_microvms.types.tags.deserialize_json(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
