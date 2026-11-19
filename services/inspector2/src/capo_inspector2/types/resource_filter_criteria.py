"""Generated from Smithy shape ``com.amazonaws.inspector2#ResourceFilterCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.resource_map_filter_list
    import capo_inspector2.types.resource_string_filter_list


class ResourceFilterCriteria(TypedDict, closed=True):
    account_id: NotRequired[
        "capo_inspector2.types.resource_string_filter_list.ResourceStringFilterList"
    ]
    """<p>The account IDs used as resource filter criteria.</p>"""
    resource_id: NotRequired[
        "capo_inspector2.types.resource_string_filter_list.ResourceStringFilterList"
    ]
    """<p>The resource IDs used as resource filter criteria.</p>"""
    resource_type: NotRequired[
        "capo_inspector2.types.resource_string_filter_list.ResourceStringFilterList"
    ]
    """<p>The resource types used as resource filter criteria. Valid values:</p> <ul> <li> <p>Amazon Web Services – <code>AWS_EC2_INSTANCE</code>, <code>AWS_ECR_CONTAINER_IMAGE</code>, <code>AWS_LAMBDA_FUNCTION</code>, or <code>MACHINE_IMAGE</code>.</p> </li> <li> <p>Microsoft Azure – <code>Microsoft.Compute/virtualMachines</code>, <code>Microsoft.ContainerRegistry/registry/containerImage</code>, or <code>Microsoft.Web/sites</code>.</p> </li> <li> <p>Google Cloud Platform (GCP) – <code>compute.googleapis.com/Instance</code>, <code>cloudfunctions.googleapis.com/Function</code>, or <code>artifactregistry.googleapis.com/DockerImage</code>.</p> </li> </ul>"""
    ecr_repository_name: NotRequired[
        "capo_inspector2.types.resource_string_filter_list.ResourceStringFilterList"
    ]
    """<p>The ECR repository names used as resource filter criteria.</p>"""
    lambda_function_name: NotRequired[
        "capo_inspector2.types.resource_string_filter_list.ResourceStringFilterList"
    ]
    """<p>The Amazon Web Services Lambda function name used as resource filter criteria.</p>"""
    ecr_image_tags: NotRequired[
        "capo_inspector2.types.resource_string_filter_list.ResourceStringFilterList"
    ]
    """<p>The ECR image tags used as resource filter criteria.</p>"""
    ec2_instance_tags: NotRequired[
        "capo_inspector2.types.resource_map_filter_list.ResourceMapFilterList"
    ]
    """<p>The EC2 instance tags used as resource filter criteria.</p>"""
    lambda_function_tags: NotRequired[
        "capo_inspector2.types.resource_map_filter_list.ResourceMapFilterList"
    ]
    """<p>The Amazon Web Services Lambda function tags used as resource filter criteria.</p>"""
    cloud_provider: NotRequired[
        "capo_inspector2.types.resource_string_filter_list.ResourceStringFilterList"
    ]
    """<p>The cloud providers used as resource filter criteria. Valid values:</p> <ul> <li> <p> <code>AWS</code> – Amazon Web Services resources.</p> </li> <li> <p> <code>AZURE</code> – Microsoft Azure resources.</p> </li> <li> <p> <code>GCP</code> – Google Cloud Platform (GCP) resources.</p> </li> </ul>"""
    cloud_provider_account_id: NotRequired[
        "capo_inspector2.types.resource_string_filter_list.ResourceStringFilterList"
    ]
    """<p>The cloud provider account IDs used as resource filter criteria. The value format depends on the cloud provider:</p> <ul> <li> <p>An Amazon Web Services account ID.</p> </li> <li> <p>An Azure subscription ID.</p> </li> <li> <p>A Google Cloud Platform (GCP) project ID.</p> </li> </ul>"""
    cloud_provider_org_id: NotRequired[
        "capo_inspector2.types.resource_string_filter_list.ResourceStringFilterList"
    ]
    """<p>The cloud provider organization IDs used as resource filter criteria. The value format depends on the cloud provider:</p> <ul> <li> <p>An Amazon Web Services Organizations organization ID.</p> </li> <li> <p>An Azure tenant ID.</p> </li> <li> <p>A Google Cloud Platform (GCP) organization ID.</p> </li> </ul>"""
    cloud_provider_region: NotRequired[
        "capo_inspector2.types.resource_string_filter_list.ResourceStringFilterList"
    ]
    """<p>The cloud provider regions used as resource filter criteria. The value format depends on the cloud provider:</p> <ul> <li> <p>An Amazon Web Services Region, such as <code>us-east-1</code>.</p> </li> <li> <p>An Azure region, such as <code>eastus</code>.</p> </li> <li> <p>A Google Cloud Platform (GCP) location, such as the region <code>us-central1</code> or the zone <code>us-central1-a</code>.</p> </li> </ul>"""
    cloud_vm_instance_tags: NotRequired[
        "capo_inspector2.types.resource_map_filter_list.ResourceMapFilterList"
    ]
    """<p>The cloud VM instance tags used as resource filter criteria.</p>"""
    cloud_container_image_tags: NotRequired[
        "capo_inspector2.types.resource_string_filter_list.ResourceStringFilterList"
    ]
    """<p>The cloud container image tags used as resource filter criteria.</p>"""
    cloud_container_repository_name: NotRequired[
        "capo_inspector2.types.resource_string_filter_list.ResourceStringFilterList"
    ]
    """<p>The cloud container repository names used as resource filter criteria.</p>"""
    cloud_container_registry_name: NotRequired[
        "capo_inspector2.types.resource_string_filter_list.ResourceStringFilterList"
    ]
    """<p>The cloud container registry names used as resource filter criteria.</p>"""
    cloud_serverless_function_name: NotRequired[
        "capo_inspector2.types.resource_string_filter_list.ResourceStringFilterList"
    ]
    """<p>The cloud serverless function names used as resource filter criteria.</p>"""
    cloud_serverless_function_runtime: NotRequired[
        "capo_inspector2.types.resource_string_filter_list.ResourceStringFilterList"
    ]
    """<p>The cloud serverless function runtimes used as resource filter criteria.</p>"""
    cloud_serverless_function_tags: NotRequired[
        "capo_inspector2.types.resource_map_filter_list.ResourceMapFilterList"
    ]
    """<p>The cloud serverless function tags used as resource filter criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceFilterCriteria) -> dict:
    out: dict = {}
    if "account_id" in value:
        import capo_inspector2.types.resource_string_filter_list

        out["accountId"] = (
            capo_inspector2.types.resource_string_filter_list.serialize_json(
                value["account_id"]
            )
        )
    if "resource_id" in value:
        import capo_inspector2.types.resource_string_filter_list

        out["resourceId"] = (
            capo_inspector2.types.resource_string_filter_list.serialize_json(
                value["resource_id"]
            )
        )
    if "resource_type" in value:
        import capo_inspector2.types.resource_string_filter_list

        out["resourceType"] = (
            capo_inspector2.types.resource_string_filter_list.serialize_json(
                value["resource_type"]
            )
        )
    if "ecr_repository_name" in value:
        import capo_inspector2.types.resource_string_filter_list

        out["ecrRepositoryName"] = (
            capo_inspector2.types.resource_string_filter_list.serialize_json(
                value["ecr_repository_name"]
            )
        )
    if "lambda_function_name" in value:
        import capo_inspector2.types.resource_string_filter_list

        out["lambdaFunctionName"] = (
            capo_inspector2.types.resource_string_filter_list.serialize_json(
                value["lambda_function_name"]
            )
        )
    if "ecr_image_tags" in value:
        import capo_inspector2.types.resource_string_filter_list

        out["ecrImageTags"] = (
            capo_inspector2.types.resource_string_filter_list.serialize_json(
                value["ecr_image_tags"]
            )
        )
    if "ec2_instance_tags" in value:
        import capo_inspector2.types.resource_map_filter_list

        out["ec2InstanceTags"] = (
            capo_inspector2.types.resource_map_filter_list.serialize_json(
                value["ec2_instance_tags"]
            )
        )
    if "lambda_function_tags" in value:
        import capo_inspector2.types.resource_map_filter_list

        out["lambdaFunctionTags"] = (
            capo_inspector2.types.resource_map_filter_list.serialize_json(
                value["lambda_function_tags"]
            )
        )
    if "cloud_provider" in value:
        import capo_inspector2.types.resource_string_filter_list

        out["cloudProvider"] = (
            capo_inspector2.types.resource_string_filter_list.serialize_json(
                value["cloud_provider"]
            )
        )
    if "cloud_provider_account_id" in value:
        import capo_inspector2.types.resource_string_filter_list

        out["cloudProviderAccountId"] = (
            capo_inspector2.types.resource_string_filter_list.serialize_json(
                value["cloud_provider_account_id"]
            )
        )
    if "cloud_provider_org_id" in value:
        import capo_inspector2.types.resource_string_filter_list

        out["cloudProviderOrgId"] = (
            capo_inspector2.types.resource_string_filter_list.serialize_json(
                value["cloud_provider_org_id"]
            )
        )
    if "cloud_provider_region" in value:
        import capo_inspector2.types.resource_string_filter_list

        out["cloudProviderRegion"] = (
            capo_inspector2.types.resource_string_filter_list.serialize_json(
                value["cloud_provider_region"]
            )
        )
    if "cloud_vm_instance_tags" in value:
        import capo_inspector2.types.resource_map_filter_list

        out["cloudVmInstanceTags"] = (
            capo_inspector2.types.resource_map_filter_list.serialize_json(
                value["cloud_vm_instance_tags"]
            )
        )
    if "cloud_container_image_tags" in value:
        import capo_inspector2.types.resource_string_filter_list

        out["cloudContainerImageTags"] = (
            capo_inspector2.types.resource_string_filter_list.serialize_json(
                value["cloud_container_image_tags"]
            )
        )
    if "cloud_container_repository_name" in value:
        import capo_inspector2.types.resource_string_filter_list

        out["cloudContainerRepositoryName"] = (
            capo_inspector2.types.resource_string_filter_list.serialize_json(
                value["cloud_container_repository_name"]
            )
        )
    if "cloud_container_registry_name" in value:
        import capo_inspector2.types.resource_string_filter_list

        out["cloudContainerRegistryName"] = (
            capo_inspector2.types.resource_string_filter_list.serialize_json(
                value["cloud_container_registry_name"]
            )
        )
    if "cloud_serverless_function_name" in value:
        import capo_inspector2.types.resource_string_filter_list

        out["cloudServerlessFunctionName"] = (
            capo_inspector2.types.resource_string_filter_list.serialize_json(
                value["cloud_serverless_function_name"]
            )
        )
    if "cloud_serverless_function_runtime" in value:
        import capo_inspector2.types.resource_string_filter_list

        out["cloudServerlessFunctionRuntime"] = (
            capo_inspector2.types.resource_string_filter_list.serialize_json(
                value["cloud_serverless_function_runtime"]
            )
        )
    if "cloud_serverless_function_tags" in value:
        import capo_inspector2.types.resource_map_filter_list

        out["cloudServerlessFunctionTags"] = (
            capo_inspector2.types.resource_map_filter_list.serialize_json(
                value["cloud_serverless_function_tags"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResourceFilterCriteria:
    out: ResourceFilterCriteria = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        import capo_inspector2.types.resource_string_filter_list

        out["account_id"] = (
            capo_inspector2.types.resource_string_filter_list.deserialize_json(
                data["accountId"]
            )
        )
    if data.get("resourceId") is not None:
        import capo_inspector2.types.resource_string_filter_list

        out["resource_id"] = (
            capo_inspector2.types.resource_string_filter_list.deserialize_json(
                data["resourceId"]
            )
        )
    if data.get("resourceType") is not None:
        import capo_inspector2.types.resource_string_filter_list

        out["resource_type"] = (
            capo_inspector2.types.resource_string_filter_list.deserialize_json(
                data["resourceType"]
            )
        )
    if data.get("ecrRepositoryName") is not None:
        import capo_inspector2.types.resource_string_filter_list

        out["ecr_repository_name"] = (
            capo_inspector2.types.resource_string_filter_list.deserialize_json(
                data["ecrRepositoryName"]
            )
        )
    if data.get("lambdaFunctionName") is not None:
        import capo_inspector2.types.resource_string_filter_list

        out["lambda_function_name"] = (
            capo_inspector2.types.resource_string_filter_list.deserialize_json(
                data["lambdaFunctionName"]
            )
        )
    if data.get("ecrImageTags") is not None:
        import capo_inspector2.types.resource_string_filter_list

        out["ecr_image_tags"] = (
            capo_inspector2.types.resource_string_filter_list.deserialize_json(
                data["ecrImageTags"]
            )
        )
    if data.get("ec2InstanceTags") is not None:
        import capo_inspector2.types.resource_map_filter_list

        out["ec2_instance_tags"] = (
            capo_inspector2.types.resource_map_filter_list.deserialize_json(
                data["ec2InstanceTags"]
            )
        )
    if data.get("lambdaFunctionTags") is not None:
        import capo_inspector2.types.resource_map_filter_list

        out["lambda_function_tags"] = (
            capo_inspector2.types.resource_map_filter_list.deserialize_json(
                data["lambdaFunctionTags"]
            )
        )
    if data.get("cloudProvider") is not None:
        import capo_inspector2.types.resource_string_filter_list

        out["cloud_provider"] = (
            capo_inspector2.types.resource_string_filter_list.deserialize_json(
                data["cloudProvider"]
            )
        )
    if data.get("cloudProviderAccountId") is not None:
        import capo_inspector2.types.resource_string_filter_list

        out["cloud_provider_account_id"] = (
            capo_inspector2.types.resource_string_filter_list.deserialize_json(
                data["cloudProviderAccountId"]
            )
        )
    if data.get("cloudProviderOrgId") is not None:
        import capo_inspector2.types.resource_string_filter_list

        out["cloud_provider_org_id"] = (
            capo_inspector2.types.resource_string_filter_list.deserialize_json(
                data["cloudProviderOrgId"]
            )
        )
    if data.get("cloudProviderRegion") is not None:
        import capo_inspector2.types.resource_string_filter_list

        out["cloud_provider_region"] = (
            capo_inspector2.types.resource_string_filter_list.deserialize_json(
                data["cloudProviderRegion"]
            )
        )
    if data.get("cloudVmInstanceTags") is not None:
        import capo_inspector2.types.resource_map_filter_list

        out["cloud_vm_instance_tags"] = (
            capo_inspector2.types.resource_map_filter_list.deserialize_json(
                data["cloudVmInstanceTags"]
            )
        )
    if data.get("cloudContainerImageTags") is not None:
        import capo_inspector2.types.resource_string_filter_list

        out["cloud_container_image_tags"] = (
            capo_inspector2.types.resource_string_filter_list.deserialize_json(
                data["cloudContainerImageTags"]
            )
        )
    if data.get("cloudContainerRepositoryName") is not None:
        import capo_inspector2.types.resource_string_filter_list

        out["cloud_container_repository_name"] = (
            capo_inspector2.types.resource_string_filter_list.deserialize_json(
                data["cloudContainerRepositoryName"]
            )
        )
    if data.get("cloudContainerRegistryName") is not None:
        import capo_inspector2.types.resource_string_filter_list

        out["cloud_container_registry_name"] = (
            capo_inspector2.types.resource_string_filter_list.deserialize_json(
                data["cloudContainerRegistryName"]
            )
        )
    if data.get("cloudServerlessFunctionName") is not None:
        import capo_inspector2.types.resource_string_filter_list

        out["cloud_serverless_function_name"] = (
            capo_inspector2.types.resource_string_filter_list.deserialize_json(
                data["cloudServerlessFunctionName"]
            )
        )
    if data.get("cloudServerlessFunctionRuntime") is not None:
        import capo_inspector2.types.resource_string_filter_list

        out["cloud_serverless_function_runtime"] = (
            capo_inspector2.types.resource_string_filter_list.deserialize_json(
                data["cloudServerlessFunctionRuntime"]
            )
        )
    if data.get("cloudServerlessFunctionTags") is not None:
        import capo_inspector2.types.resource_map_filter_list

        out["cloud_serverless_function_tags"] = (
            capo_inspector2.types.resource_map_filter_list.deserialize_json(
                data["cloudServerlessFunctionTags"]
            )
        )
    return out
