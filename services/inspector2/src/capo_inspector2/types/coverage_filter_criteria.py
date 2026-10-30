"""Generated from Smithy shape ``com.amazonaws.inspector2#CoverageFilterCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.coverage_date_filter_list
    import capo_inspector2.types.coverage_map_filter_list
    import capo_inspector2.types.coverage_number_filter_list
    import capo_inspector2.types.coverage_string_filter_list


class CoverageFilterCriteria(TypedDict, closed=True):
    scan_status_code: NotRequired[
        "capo_inspector2.types.coverage_string_filter_list.CoverageStringFilterList"
    ]
    """<p>The scan status code to filter on. Valid values are: <code>ValidationException</code>, <code>InternalServerException</code>, <code>ResourceNotFoundException</code>, <code>BadRequestException</code>, and <code>ThrottlingException</code>.</p>"""
    scan_status_reason: NotRequired[
        "capo_inspector2.types.coverage_string_filter_list.CoverageStringFilterList"
    ]
    """<p>The scan status reason to filter on.</p>"""
    account_id: NotRequired[
        "capo_inspector2.types.coverage_string_filter_list.CoverageStringFilterList"
    ]
    """<p>An array of Amazon Web Services account IDs to return coverage statistics for.</p>"""
    resource_id: NotRequired[
        "capo_inspector2.types.coverage_string_filter_list.CoverageStringFilterList"
    ]
    """<p>An array of Amazon Web Services resource IDs to return coverage statistics for.</p>"""
    resource_type: NotRequired[
        "capo_inspector2.types.coverage_string_filter_list.CoverageStringFilterList"
    ]
    """<p>An array of Amazon Web Services resource types to return coverage statistics for. The values can be <code>AWS_EC2_INSTANCE</code>, <code>AWS_LAMBDA_FUNCTION</code>, <code>AWS_ECR_CONTAINER_IMAGE</code>, <code>AWS_ECR_REPOSITORY</code> or <code>AWS_ACCOUNT</code>.</p>"""
    scan_type: NotRequired[
        "capo_inspector2.types.coverage_string_filter_list.CoverageStringFilterList"
    ]
    """<p>An array of Amazon Inspector scan types to return coverage statistics for.</p>"""
    ecr_repository_name: NotRequired[
        "capo_inspector2.types.coverage_string_filter_list.CoverageStringFilterList"
    ]
    """<p>The Amazon ECR repository name to filter on.</p>"""
    ecr_image_tags: NotRequired[
        "capo_inspector2.types.coverage_string_filter_list.CoverageStringFilterList"
    ]
    """<p>The Amazon ECR image tags to filter on.</p>"""
    ec2_instance_tags: NotRequired[
        "capo_inspector2.types.coverage_map_filter_list.CoverageMapFilterList"
    ]
    """<p>The Amazon EC2 instance tags to filter on.</p>"""
    lambda_function_name: NotRequired[
        "capo_inspector2.types.coverage_string_filter_list.CoverageStringFilterList"
    ]
    """<p>Returns coverage statistics for Amazon Web Services Lambda functions filtered by function names.</p>"""
    lambda_function_tags: NotRequired[
        "capo_inspector2.types.coverage_map_filter_list.CoverageMapFilterList"
    ]
    """<p>Returns coverage statistics for Amazon Web Services Lambda functions filtered by tag.</p>"""
    lambda_function_runtime: NotRequired[
        "capo_inspector2.types.coverage_string_filter_list.CoverageStringFilterList"
    ]
    """<p>Returns coverage statistics for Amazon Web Services Lambda functions filtered by runtime.</p>"""
    machine_image_tags: NotRequired[
        "capo_inspector2.types.coverage_map_filter_list.CoverageMapFilterList"
    ]
    """<p>The machine image tags to filter coverage results by.</p>"""
    last_scanned_at: NotRequired[
        "capo_inspector2.types.coverage_date_filter_list.CoverageDateFilterList"
    ]
    """<p>Filters Amazon Web Services resources based on whether Amazon Inspector has checked them for vulnerabilities within the specified time range.</p>"""
    scan_mode: NotRequired[
        "capo_inspector2.types.coverage_string_filter_list.CoverageStringFilterList"
    ]
    """<p>The filter to search for Amazon EC2 instance coverage by scan mode. Valid values are <code>EC2_SSM_AGENT_BASED</code>, <code>EC2_AGENTLESS</code>, and <code>EC2_INSPECTOR_AGENT_BASED</code>.</p>"""
    image_pulled_at: NotRequired[
        "capo_inspector2.types.coverage_date_filter_list.CoverageDateFilterList"
    ]
    """<p>The date an image was last pulled at.</p>"""
    ecr_image_last_in_use_at: NotRequired[
        "capo_inspector2.types.coverage_date_filter_list.CoverageDateFilterList"
    ]
    """<p>The Amazon ECR image that was last in use.</p>"""
    ecr_image_in_use_count: NotRequired[
        "capo_inspector2.types.coverage_number_filter_list.CoverageNumberFilterList"
    ]
    """<p>The number of Amazon ECR images in use.</p>"""
    code_repository_project_name: NotRequired[
        "capo_inspector2.types.coverage_string_filter_list.CoverageStringFilterList"
    ]
    """<p>Filter criteria for code repositories based on project name.</p>"""
    code_repository_provider_type: NotRequired[
        "capo_inspector2.types.coverage_string_filter_list.CoverageStringFilterList"
    ]
    """<p>Filter criteria for code repositories based on provider type (such as GitHub, GitLab, etc.).</p>"""
    code_repository_provider_type_visibility: NotRequired[
        "capo_inspector2.types.coverage_string_filter_list.CoverageStringFilterList"
    ]
    """<p>Filter criteria for code repositories based on visibility setting (public or private).</p>"""
    last_scanned_commit_id: NotRequired[
        "capo_inspector2.types.coverage_string_filter_list.CoverageStringFilterList"
    ]
    """<p>Filter criteria for code repositories based on the ID of the last scanned commit.</p>"""
    cloud_provider: NotRequired[
        "capo_inspector2.types.coverage_string_filter_list.CoverageStringFilterList"
    ]
    """<p>The cloud provider to filter coverage results by.</p>"""
    cloud_provider_account_id: NotRequired[
        "capo_inspector2.types.coverage_string_filter_list.CoverageStringFilterList"
    ]
    """<p>The cloud provider account ID to filter coverage results by.</p>"""
    cloud_provider_region: NotRequired[
        "capo_inspector2.types.coverage_string_filter_list.CoverageStringFilterList"
    ]
    """<p>The cloud provider region to filter coverage results by.</p>"""
    cloud_vm_instance_tags: NotRequired[
        "capo_inspector2.types.coverage_map_filter_list.CoverageMapFilterList"
    ]
    """<p>The cloud VM instance tags to filter coverage results by.</p>"""
    cloud_container_image_tags: NotRequired[
        "capo_inspector2.types.coverage_string_filter_list.CoverageStringFilterList"
    ]
    """<p>The cloud container image tags to filter coverage results by.</p>"""
    cloud_container_repository_name: NotRequired[
        "capo_inspector2.types.coverage_string_filter_list.CoverageStringFilterList"
    ]
    """<p>The cloud container repository name to filter coverage results by.</p>"""
    cloud_container_registry_name: NotRequired[
        "capo_inspector2.types.coverage_string_filter_list.CoverageStringFilterList"
    ]
    """<p>The cloud container registry name to filter coverage results by.</p>"""
    cloud_serverless_function_name: NotRequired[
        "capo_inspector2.types.coverage_string_filter_list.CoverageStringFilterList"
    ]
    """<p>The cloud serverless function name to filter coverage results by.</p>"""
    cloud_serverless_function_runtime: NotRequired[
        "capo_inspector2.types.coverage_string_filter_list.CoverageStringFilterList"
    ]
    """<p>The cloud serverless function runtime to filter coverage results by.</p>"""
    cloud_serverless_function_tags: NotRequired[
        "capo_inspector2.types.coverage_map_filter_list.CoverageMapFilterList"
    ]
    """<p>The cloud serverless function tags to filter coverage results by.</p>"""
    cloud_provider_org_id: NotRequired[
        "capo_inspector2.types.coverage_string_filter_list.CoverageStringFilterList"
    ]
    """<p>The cloud provider organization ID to filter coverage results by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoverageFilterCriteria) -> dict:
    out: dict = {}
    if "scan_status_code" in value:
        import capo_inspector2.types.coverage_string_filter_list

        out["scanStatusCode"] = (
            capo_inspector2.types.coverage_string_filter_list.serialize_json(
                value["scan_status_code"]
            )
        )
    if "scan_status_reason" in value:
        import capo_inspector2.types.coverage_string_filter_list

        out["scanStatusReason"] = (
            capo_inspector2.types.coverage_string_filter_list.serialize_json(
                value["scan_status_reason"]
            )
        )
    if "account_id" in value:
        import capo_inspector2.types.coverage_string_filter_list

        out["accountId"] = (
            capo_inspector2.types.coverage_string_filter_list.serialize_json(
                value["account_id"]
            )
        )
    if "resource_id" in value:
        import capo_inspector2.types.coverage_string_filter_list

        out["resourceId"] = (
            capo_inspector2.types.coverage_string_filter_list.serialize_json(
                value["resource_id"]
            )
        )
    if "resource_type" in value:
        import capo_inspector2.types.coverage_string_filter_list

        out["resourceType"] = (
            capo_inspector2.types.coverage_string_filter_list.serialize_json(
                value["resource_type"]
            )
        )
    if "scan_type" in value:
        import capo_inspector2.types.coverage_string_filter_list

        out["scanType"] = (
            capo_inspector2.types.coverage_string_filter_list.serialize_json(
                value["scan_type"]
            )
        )
    if "ecr_repository_name" in value:
        import capo_inspector2.types.coverage_string_filter_list

        out["ecrRepositoryName"] = (
            capo_inspector2.types.coverage_string_filter_list.serialize_json(
                value["ecr_repository_name"]
            )
        )
    if "ecr_image_tags" in value:
        import capo_inspector2.types.coverage_string_filter_list

        out["ecrImageTags"] = (
            capo_inspector2.types.coverage_string_filter_list.serialize_json(
                value["ecr_image_tags"]
            )
        )
    if "ec2_instance_tags" in value:
        import capo_inspector2.types.coverage_map_filter_list

        out["ec2InstanceTags"] = (
            capo_inspector2.types.coverage_map_filter_list.serialize_json(
                value["ec2_instance_tags"]
            )
        )
    if "lambda_function_name" in value:
        import capo_inspector2.types.coverage_string_filter_list

        out["lambdaFunctionName"] = (
            capo_inspector2.types.coverage_string_filter_list.serialize_json(
                value["lambda_function_name"]
            )
        )
    if "lambda_function_tags" in value:
        import capo_inspector2.types.coverage_map_filter_list

        out["lambdaFunctionTags"] = (
            capo_inspector2.types.coverage_map_filter_list.serialize_json(
                value["lambda_function_tags"]
            )
        )
    if "lambda_function_runtime" in value:
        import capo_inspector2.types.coverage_string_filter_list

        out["lambdaFunctionRuntime"] = (
            capo_inspector2.types.coverage_string_filter_list.serialize_json(
                value["lambda_function_runtime"]
            )
        )
    if "machine_image_tags" in value:
        import capo_inspector2.types.coverage_map_filter_list

        out["machineImageTags"] = (
            capo_inspector2.types.coverage_map_filter_list.serialize_json(
                value["machine_image_tags"]
            )
        )
    if "last_scanned_at" in value:
        import capo_inspector2.types.coverage_date_filter_list

        out["lastScannedAt"] = (
            capo_inspector2.types.coverage_date_filter_list.serialize_json(
                value["last_scanned_at"]
            )
        )
    if "scan_mode" in value:
        import capo_inspector2.types.coverage_string_filter_list

        out["scanMode"] = (
            capo_inspector2.types.coverage_string_filter_list.serialize_json(
                value["scan_mode"]
            )
        )
    if "image_pulled_at" in value:
        import capo_inspector2.types.coverage_date_filter_list

        out["imagePulledAt"] = (
            capo_inspector2.types.coverage_date_filter_list.serialize_json(
                value["image_pulled_at"]
            )
        )
    if "ecr_image_last_in_use_at" in value:
        import capo_inspector2.types.coverage_date_filter_list

        out["ecrImageLastInUseAt"] = (
            capo_inspector2.types.coverage_date_filter_list.serialize_json(
                value["ecr_image_last_in_use_at"]
            )
        )
    if "ecr_image_in_use_count" in value:
        import capo_inspector2.types.coverage_number_filter_list

        out["ecrImageInUseCount"] = (
            capo_inspector2.types.coverage_number_filter_list.serialize_json(
                value["ecr_image_in_use_count"]
            )
        )
    if "code_repository_project_name" in value:
        import capo_inspector2.types.coverage_string_filter_list

        out["codeRepositoryProjectName"] = (
            capo_inspector2.types.coverage_string_filter_list.serialize_json(
                value["code_repository_project_name"]
            )
        )
    if "code_repository_provider_type" in value:
        import capo_inspector2.types.coverage_string_filter_list

        out["codeRepositoryProviderType"] = (
            capo_inspector2.types.coverage_string_filter_list.serialize_json(
                value["code_repository_provider_type"]
            )
        )
    if "code_repository_provider_type_visibility" in value:
        import capo_inspector2.types.coverage_string_filter_list

        out["codeRepositoryProviderTypeVisibility"] = (
            capo_inspector2.types.coverage_string_filter_list.serialize_json(
                value["code_repository_provider_type_visibility"]
            )
        )
    if "last_scanned_commit_id" in value:
        import capo_inspector2.types.coverage_string_filter_list

        out["lastScannedCommitId"] = (
            capo_inspector2.types.coverage_string_filter_list.serialize_json(
                value["last_scanned_commit_id"]
            )
        )
    if "cloud_provider" in value:
        import capo_inspector2.types.coverage_string_filter_list

        out["cloudProvider"] = (
            capo_inspector2.types.coverage_string_filter_list.serialize_json(
                value["cloud_provider"]
            )
        )
    if "cloud_provider_account_id" in value:
        import capo_inspector2.types.coverage_string_filter_list

        out["cloudProviderAccountId"] = (
            capo_inspector2.types.coverage_string_filter_list.serialize_json(
                value["cloud_provider_account_id"]
            )
        )
    if "cloud_provider_region" in value:
        import capo_inspector2.types.coverage_string_filter_list

        out["cloudProviderRegion"] = (
            capo_inspector2.types.coverage_string_filter_list.serialize_json(
                value["cloud_provider_region"]
            )
        )
    if "cloud_vm_instance_tags" in value:
        import capo_inspector2.types.coverage_map_filter_list

        out["cloudVmInstanceTags"] = (
            capo_inspector2.types.coverage_map_filter_list.serialize_json(
                value["cloud_vm_instance_tags"]
            )
        )
    if "cloud_container_image_tags" in value:
        import capo_inspector2.types.coverage_string_filter_list

        out["cloudContainerImageTags"] = (
            capo_inspector2.types.coverage_string_filter_list.serialize_json(
                value["cloud_container_image_tags"]
            )
        )
    if "cloud_container_repository_name" in value:
        import capo_inspector2.types.coverage_string_filter_list

        out["cloudContainerRepositoryName"] = (
            capo_inspector2.types.coverage_string_filter_list.serialize_json(
                value["cloud_container_repository_name"]
            )
        )
    if "cloud_container_registry_name" in value:
        import capo_inspector2.types.coverage_string_filter_list

        out["cloudContainerRegistryName"] = (
            capo_inspector2.types.coverage_string_filter_list.serialize_json(
                value["cloud_container_registry_name"]
            )
        )
    if "cloud_serverless_function_name" in value:
        import capo_inspector2.types.coverage_string_filter_list

        out["cloudServerlessFunctionName"] = (
            capo_inspector2.types.coverage_string_filter_list.serialize_json(
                value["cloud_serverless_function_name"]
            )
        )
    if "cloud_serverless_function_runtime" in value:
        import capo_inspector2.types.coverage_string_filter_list

        out["cloudServerlessFunctionRuntime"] = (
            capo_inspector2.types.coverage_string_filter_list.serialize_json(
                value["cloud_serverless_function_runtime"]
            )
        )
    if "cloud_serverless_function_tags" in value:
        import capo_inspector2.types.coverage_map_filter_list

        out["cloudServerlessFunctionTags"] = (
            capo_inspector2.types.coverage_map_filter_list.serialize_json(
                value["cloud_serverless_function_tags"]
            )
        )
    if "cloud_provider_org_id" in value:
        import capo_inspector2.types.coverage_string_filter_list

        out["cloudProviderOrgId"] = (
            capo_inspector2.types.coverage_string_filter_list.serialize_json(
                value["cloud_provider_org_id"]
            )
        )
    return out


def deserialize_json(data: dict) -> CoverageFilterCriteria:
    out: CoverageFilterCriteria = {}  # type: ignore[typeddict-item]
    if data.get("scanStatusCode") is not None:
        import capo_inspector2.types.coverage_string_filter_list

        out["scan_status_code"] = (
            capo_inspector2.types.coverage_string_filter_list.deserialize_json(
                data["scanStatusCode"]
            )
        )
    if data.get("scanStatusReason") is not None:
        import capo_inspector2.types.coverage_string_filter_list

        out["scan_status_reason"] = (
            capo_inspector2.types.coverage_string_filter_list.deserialize_json(
                data["scanStatusReason"]
            )
        )
    if data.get("accountId") is not None:
        import capo_inspector2.types.coverage_string_filter_list

        out["account_id"] = (
            capo_inspector2.types.coverage_string_filter_list.deserialize_json(
                data["accountId"]
            )
        )
    if data.get("resourceId") is not None:
        import capo_inspector2.types.coverage_string_filter_list

        out["resource_id"] = (
            capo_inspector2.types.coverage_string_filter_list.deserialize_json(
                data["resourceId"]
            )
        )
    if data.get("resourceType") is not None:
        import capo_inspector2.types.coverage_string_filter_list

        out["resource_type"] = (
            capo_inspector2.types.coverage_string_filter_list.deserialize_json(
                data["resourceType"]
            )
        )
    if data.get("scanType") is not None:
        import capo_inspector2.types.coverage_string_filter_list

        out["scan_type"] = (
            capo_inspector2.types.coverage_string_filter_list.deserialize_json(
                data["scanType"]
            )
        )
    if data.get("ecrRepositoryName") is not None:
        import capo_inspector2.types.coverage_string_filter_list

        out["ecr_repository_name"] = (
            capo_inspector2.types.coverage_string_filter_list.deserialize_json(
                data["ecrRepositoryName"]
            )
        )
    if data.get("ecrImageTags") is not None:
        import capo_inspector2.types.coverage_string_filter_list

        out["ecr_image_tags"] = (
            capo_inspector2.types.coverage_string_filter_list.deserialize_json(
                data["ecrImageTags"]
            )
        )
    if data.get("ec2InstanceTags") is not None:
        import capo_inspector2.types.coverage_map_filter_list

        out["ec2_instance_tags"] = (
            capo_inspector2.types.coverage_map_filter_list.deserialize_json(
                data["ec2InstanceTags"]
            )
        )
    if data.get("lambdaFunctionName") is not None:
        import capo_inspector2.types.coverage_string_filter_list

        out["lambda_function_name"] = (
            capo_inspector2.types.coverage_string_filter_list.deserialize_json(
                data["lambdaFunctionName"]
            )
        )
    if data.get("lambdaFunctionTags") is not None:
        import capo_inspector2.types.coverage_map_filter_list

        out["lambda_function_tags"] = (
            capo_inspector2.types.coverage_map_filter_list.deserialize_json(
                data["lambdaFunctionTags"]
            )
        )
    if data.get("lambdaFunctionRuntime") is not None:
        import capo_inspector2.types.coverage_string_filter_list

        out["lambda_function_runtime"] = (
            capo_inspector2.types.coverage_string_filter_list.deserialize_json(
                data["lambdaFunctionRuntime"]
            )
        )
    if data.get("machineImageTags") is not None:
        import capo_inspector2.types.coverage_map_filter_list

        out["machine_image_tags"] = (
            capo_inspector2.types.coverage_map_filter_list.deserialize_json(
                data["machineImageTags"]
            )
        )
    if data.get("lastScannedAt") is not None:
        import capo_inspector2.types.coverage_date_filter_list

        out["last_scanned_at"] = (
            capo_inspector2.types.coverage_date_filter_list.deserialize_json(
                data["lastScannedAt"]
            )
        )
    if data.get("scanMode") is not None:
        import capo_inspector2.types.coverage_string_filter_list

        out["scan_mode"] = (
            capo_inspector2.types.coverage_string_filter_list.deserialize_json(
                data["scanMode"]
            )
        )
    if data.get("imagePulledAt") is not None:
        import capo_inspector2.types.coverage_date_filter_list

        out["image_pulled_at"] = (
            capo_inspector2.types.coverage_date_filter_list.deserialize_json(
                data["imagePulledAt"]
            )
        )
    if data.get("ecrImageLastInUseAt") is not None:
        import capo_inspector2.types.coverage_date_filter_list

        out["ecr_image_last_in_use_at"] = (
            capo_inspector2.types.coverage_date_filter_list.deserialize_json(
                data["ecrImageLastInUseAt"]
            )
        )
    if data.get("ecrImageInUseCount") is not None:
        import capo_inspector2.types.coverage_number_filter_list

        out["ecr_image_in_use_count"] = (
            capo_inspector2.types.coverage_number_filter_list.deserialize_json(
                data["ecrImageInUseCount"]
            )
        )
    if data.get("codeRepositoryProjectName") is not None:
        import capo_inspector2.types.coverage_string_filter_list

        out["code_repository_project_name"] = (
            capo_inspector2.types.coverage_string_filter_list.deserialize_json(
                data["codeRepositoryProjectName"]
            )
        )
    if data.get("codeRepositoryProviderType") is not None:
        import capo_inspector2.types.coverage_string_filter_list

        out["code_repository_provider_type"] = (
            capo_inspector2.types.coverage_string_filter_list.deserialize_json(
                data["codeRepositoryProviderType"]
            )
        )
    if data.get("codeRepositoryProviderTypeVisibility") is not None:
        import capo_inspector2.types.coverage_string_filter_list

        out["code_repository_provider_type_visibility"] = (
            capo_inspector2.types.coverage_string_filter_list.deserialize_json(
                data["codeRepositoryProviderTypeVisibility"]
            )
        )
    if data.get("lastScannedCommitId") is not None:
        import capo_inspector2.types.coverage_string_filter_list

        out["last_scanned_commit_id"] = (
            capo_inspector2.types.coverage_string_filter_list.deserialize_json(
                data["lastScannedCommitId"]
            )
        )
    if data.get("cloudProvider") is not None:
        import capo_inspector2.types.coverage_string_filter_list

        out["cloud_provider"] = (
            capo_inspector2.types.coverage_string_filter_list.deserialize_json(
                data["cloudProvider"]
            )
        )
    if data.get("cloudProviderAccountId") is not None:
        import capo_inspector2.types.coverage_string_filter_list

        out["cloud_provider_account_id"] = (
            capo_inspector2.types.coverage_string_filter_list.deserialize_json(
                data["cloudProviderAccountId"]
            )
        )
    if data.get("cloudProviderRegion") is not None:
        import capo_inspector2.types.coverage_string_filter_list

        out["cloud_provider_region"] = (
            capo_inspector2.types.coverage_string_filter_list.deserialize_json(
                data["cloudProviderRegion"]
            )
        )
    if data.get("cloudVmInstanceTags") is not None:
        import capo_inspector2.types.coverage_map_filter_list

        out["cloud_vm_instance_tags"] = (
            capo_inspector2.types.coverage_map_filter_list.deserialize_json(
                data["cloudVmInstanceTags"]
            )
        )
    if data.get("cloudContainerImageTags") is not None:
        import capo_inspector2.types.coverage_string_filter_list

        out["cloud_container_image_tags"] = (
            capo_inspector2.types.coverage_string_filter_list.deserialize_json(
                data["cloudContainerImageTags"]
            )
        )
    if data.get("cloudContainerRepositoryName") is not None:
        import capo_inspector2.types.coverage_string_filter_list

        out["cloud_container_repository_name"] = (
            capo_inspector2.types.coverage_string_filter_list.deserialize_json(
                data["cloudContainerRepositoryName"]
            )
        )
    if data.get("cloudContainerRegistryName") is not None:
        import capo_inspector2.types.coverage_string_filter_list

        out["cloud_container_registry_name"] = (
            capo_inspector2.types.coverage_string_filter_list.deserialize_json(
                data["cloudContainerRegistryName"]
            )
        )
    if data.get("cloudServerlessFunctionName") is not None:
        import capo_inspector2.types.coverage_string_filter_list

        out["cloud_serverless_function_name"] = (
            capo_inspector2.types.coverage_string_filter_list.deserialize_json(
                data["cloudServerlessFunctionName"]
            )
        )
    if data.get("cloudServerlessFunctionRuntime") is not None:
        import capo_inspector2.types.coverage_string_filter_list

        out["cloud_serverless_function_runtime"] = (
            capo_inspector2.types.coverage_string_filter_list.deserialize_json(
                data["cloudServerlessFunctionRuntime"]
            )
        )
    if data.get("cloudServerlessFunctionTags") is not None:
        import capo_inspector2.types.coverage_map_filter_list

        out["cloud_serverless_function_tags"] = (
            capo_inspector2.types.coverage_map_filter_list.deserialize_json(
                data["cloudServerlessFunctionTags"]
            )
        )
    if data.get("cloudProviderOrgId") is not None:
        import capo_inspector2.types.coverage_string_filter_list

        out["cloud_provider_org_id"] = (
            capo_inspector2.types.coverage_string_filter_list.deserialize_json(
                data["cloudProviderOrgId"]
            )
        )
    return out
