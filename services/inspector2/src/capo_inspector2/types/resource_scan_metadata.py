"""Generated from Smithy shape ``com.amazonaws.inspector2#ResourceScanMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.code_repository_metadata
    import capo_inspector2.types.container_image_metadata
    import capo_inspector2.types.container_registry_metadata
    import capo_inspector2.types.container_repository_metadata
    import capo_inspector2.types.ec2_metadata
    import capo_inspector2.types.ecr_container_image_metadata
    import capo_inspector2.types.ecr_repository_metadata
    import capo_inspector2.types.lambda_function_metadata
    import capo_inspector2.types.machine_image_metadata
    import capo_inspector2.types.serverless_function_metadata
    import capo_inspector2.types.vm_instance_metadata


class ResourceScanMetadata(TypedDict, closed=True):
    ecr_repository: NotRequired[
        "capo_inspector2.types.ecr_repository_metadata.EcrRepositoryMetadata"
    ]
    """<p>An object that contains details about the repository an Amazon ECR image resides in.</p>"""
    ecr_image: NotRequired[
        "capo_inspector2.types.ecr_container_image_metadata.EcrContainerImageMetadata"
    ]
    """<p>An object that contains details about the container metadata for an Amazon ECR image.</p>"""
    ec2: NotRequired["capo_inspector2.types.ec2_metadata.Ec2Metadata"]
    """<p>An object that contains metadata details for an Amazon EC2 instance.</p>"""
    lambda_function: NotRequired[
        "capo_inspector2.types.lambda_function_metadata.LambdaFunctionMetadata"
    ]
    """<p>An object that contains metadata details for an Amazon Web Services Lambda function.</p>"""
    code_repository: NotRequired[
        "capo_inspector2.types.code_repository_metadata.CodeRepositoryMetadata"
    ]
    """<p>Contains metadata about scan coverage for a code repository resource.</p>"""
    vm_instance: NotRequired[
        "capo_inspector2.types.vm_instance_metadata.VmInstanceMetadata"
    ]
    """<p>The VM instance metadata associated with a covered resource.</p>"""
    container_image: NotRequired[
        "capo_inspector2.types.container_image_metadata.ContainerImageMetadata"
    ]
    """<p>The container image metadata associated with a covered resource.</p>"""
    container_repository: NotRequired[
        "capo_inspector2.types.container_repository_metadata.ContainerRepositoryMetadata"
    ]
    """<p>The container repository metadata associated with a covered resource.</p>"""
    container_registry: NotRequired[
        "capo_inspector2.types.container_registry_metadata.ContainerRegistryMetadata"
    ]
    """<p>The container registry metadata associated with a covered resource.</p>"""
    serverless_function: NotRequired[
        "capo_inspector2.types.serverless_function_metadata.ServerlessFunctionMetadata"
    ]
    """<p>The serverless function metadata associated with a covered resource.</p>"""
    machine_image: NotRequired[
        "capo_inspector2.types.machine_image_metadata.MachineImageMetadata"
    ]
    """<p>The machine image metadata associated with a covered resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceScanMetadata) -> dict:
    out: dict = {}
    if "ecr_repository" in value:
        import capo_inspector2.types.ecr_repository_metadata

        out["ecrRepository"] = (
            capo_inspector2.types.ecr_repository_metadata.serialize_json(
                value["ecr_repository"]
            )
        )
    if "ecr_image" in value:
        import capo_inspector2.types.ecr_container_image_metadata

        out["ecrImage"] = (
            capo_inspector2.types.ecr_container_image_metadata.serialize_json(
                value["ecr_image"]
            )
        )
    if "ec2" in value:
        import capo_inspector2.types.ec2_metadata

        out["ec2"] = capo_inspector2.types.ec2_metadata.serialize_json(value["ec2"])
    if "lambda_function" in value:
        import capo_inspector2.types.lambda_function_metadata

        out["lambdaFunction"] = (
            capo_inspector2.types.lambda_function_metadata.serialize_json(
                value["lambda_function"]
            )
        )
    if "code_repository" in value:
        import capo_inspector2.types.code_repository_metadata

        out["codeRepository"] = (
            capo_inspector2.types.code_repository_metadata.serialize_json(
                value["code_repository"]
            )
        )
    if "vm_instance" in value:
        import capo_inspector2.types.vm_instance_metadata

        out["vmInstance"] = capo_inspector2.types.vm_instance_metadata.serialize_json(
            value["vm_instance"]
        )
    if "container_image" in value:
        import capo_inspector2.types.container_image_metadata

        out["containerImage"] = (
            capo_inspector2.types.container_image_metadata.serialize_json(
                value["container_image"]
            )
        )
    if "container_repository" in value:
        import capo_inspector2.types.container_repository_metadata

        out["containerRepository"] = (
            capo_inspector2.types.container_repository_metadata.serialize_json(
                value["container_repository"]
            )
        )
    if "container_registry" in value:
        import capo_inspector2.types.container_registry_metadata

        out["containerRegistry"] = (
            capo_inspector2.types.container_registry_metadata.serialize_json(
                value["container_registry"]
            )
        )
    if "serverless_function" in value:
        import capo_inspector2.types.serverless_function_metadata

        out["serverlessFunction"] = (
            capo_inspector2.types.serverless_function_metadata.serialize_json(
                value["serverless_function"]
            )
        )
    if "machine_image" in value:
        import capo_inspector2.types.machine_image_metadata

        out["machineImage"] = (
            capo_inspector2.types.machine_image_metadata.serialize_json(
                value["machine_image"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResourceScanMetadata:
    out: ResourceScanMetadata = {}  # type: ignore[typeddict-item]
    if data.get("ecrRepository") is not None:
        import capo_inspector2.types.ecr_repository_metadata

        out["ecr_repository"] = (
            capo_inspector2.types.ecr_repository_metadata.deserialize_json(
                data["ecrRepository"]
            )
        )
    if data.get("ecrImage") is not None:
        import capo_inspector2.types.ecr_container_image_metadata

        out["ecr_image"] = (
            capo_inspector2.types.ecr_container_image_metadata.deserialize_json(
                data["ecrImage"]
            )
        )
    if data.get("ec2") is not None:
        import capo_inspector2.types.ec2_metadata

        out["ec2"] = capo_inspector2.types.ec2_metadata.deserialize_json(data["ec2"])
    if data.get("lambdaFunction") is not None:
        import capo_inspector2.types.lambda_function_metadata

        out["lambda_function"] = (
            capo_inspector2.types.lambda_function_metadata.deserialize_json(
                data["lambdaFunction"]
            )
        )
    if data.get("codeRepository") is not None:
        import capo_inspector2.types.code_repository_metadata

        out["code_repository"] = (
            capo_inspector2.types.code_repository_metadata.deserialize_json(
                data["codeRepository"]
            )
        )
    if data.get("vmInstance") is not None:
        import capo_inspector2.types.vm_instance_metadata

        out["vm_instance"] = (
            capo_inspector2.types.vm_instance_metadata.deserialize_json(
                data["vmInstance"]
            )
        )
    if data.get("containerImage") is not None:
        import capo_inspector2.types.container_image_metadata

        out["container_image"] = (
            capo_inspector2.types.container_image_metadata.deserialize_json(
                data["containerImage"]
            )
        )
    if data.get("containerRepository") is not None:
        import capo_inspector2.types.container_repository_metadata

        out["container_repository"] = (
            capo_inspector2.types.container_repository_metadata.deserialize_json(
                data["containerRepository"]
            )
        )
    if data.get("containerRegistry") is not None:
        import capo_inspector2.types.container_registry_metadata

        out["container_registry"] = (
            capo_inspector2.types.container_registry_metadata.deserialize_json(
                data["containerRegistry"]
            )
        )
    if data.get("serverlessFunction") is not None:
        import capo_inspector2.types.serverless_function_metadata

        out["serverless_function"] = (
            capo_inspector2.types.serverless_function_metadata.deserialize_json(
                data["serverlessFunction"]
            )
        )
    if data.get("machineImage") is not None:
        import capo_inspector2.types.machine_image_metadata

        out["machine_image"] = (
            capo_inspector2.types.machine_image_metadata.deserialize_json(
                data["machineImage"]
            )
        )
    return out
