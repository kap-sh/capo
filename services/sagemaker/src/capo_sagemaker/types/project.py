"""Generated from Smithy shape ``com.amazonaws.sagemaker#Project``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.entity_description
    import capo_sagemaker.types.project_arn
    import capo_sagemaker.types.project_entity_name
    import capo_sagemaker.types.project_id
    import capo_sagemaker.types.project_status
    import capo_sagemaker.types.service_catalog_provisioned_product_details
    import capo_sagemaker.types.service_catalog_provisioning_details
    import capo_sagemaker.types.tag_list
    import capo_sagemaker.types.template_provider_detail_list
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.user_context


class Project(TypedDict, closed=True):
    project_arn: NotRequired["capo_sagemaker.types.project_arn.ProjectArn"]
    """<p>The Amazon Resource Name (ARN) of the project.</p>"""
    project_name: NotRequired[
        "capo_sagemaker.types.project_entity_name.ProjectEntityName"
    ]
    """<p>The name of the project.</p>"""
    project_id: NotRequired["capo_sagemaker.types.project_id.ProjectId"]
    """<p>The ID of the project.</p>"""
    project_description: NotRequired[
        "capo_sagemaker.types.entity_description.EntityDescription"
    ]
    """<p>The description of the project.</p>"""
    service_catalog_provisioning_details: NotRequired[
        "capo_sagemaker.types.service_catalog_provisioning_details.ServiceCatalogProvisioningDetails"
    ]
    service_catalog_provisioned_product_details: NotRequired[
        "capo_sagemaker.types.service_catalog_provisioned_product_details.ServiceCatalogProvisionedProductDetails"
    ]
    project_status: NotRequired["capo_sagemaker.types.project_status.ProjectStatus"]
    """<p>The status of the project.</p>"""
    created_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    """<p>Who created the project.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp specifying when the project was created.</p>"""
    template_provider_details: NotRequired[
        "capo_sagemaker.types.template_provider_detail_list.TemplateProviderDetailList"
    ]
    """<p> An array of template providers associated with the project. </p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>An array of key-value pairs. You can use tags to categorize your Amazon Web Services resources in different ways, for example, by purpose, owner, or environment. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services Resources</a>.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp container for when the project was last modified.</p>"""
    last_modified_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Project) -> dict:
    out: dict = {}
    if "project_arn" in value:
        out["ProjectArn"] = value["project_arn"]
    if "project_name" in value:
        out["ProjectName"] = value["project_name"]
    if "project_id" in value:
        out["ProjectId"] = value["project_id"]
    if "project_description" in value:
        out["ProjectDescription"] = value["project_description"]
    if "service_catalog_provisioning_details" in value:
        import capo_sagemaker.types.service_catalog_provisioning_details

        out["ServiceCatalogProvisioningDetails"] = (
            capo_sagemaker.types.service_catalog_provisioning_details.serialize_aws_json_1_1(
                value["service_catalog_provisioning_details"]
            )
        )
    if "service_catalog_provisioned_product_details" in value:
        import capo_sagemaker.types.service_catalog_provisioned_product_details

        out["ServiceCatalogProvisionedProductDetails"] = (
            capo_sagemaker.types.service_catalog_provisioned_product_details.serialize_aws_json_1_1(
                value["service_catalog_provisioned_product_details"]
            )
        )
    if "project_status" in value:
        import capo_sagemaker.types.project_status

        out["ProjectStatus"] = (
            capo_sagemaker.types.project_status.serialize_aws_json_1_1(
                value["project_status"]
            )
        )
    if "created_by" in value:
        import capo_sagemaker.types.user_context

        out["CreatedBy"] = capo_sagemaker.types.user_context.serialize_aws_json_1_1(
            value["created_by"]
        )
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "template_provider_details" in value:
        import capo_sagemaker.types.template_provider_detail_list

        out["TemplateProviderDetails"] = (
            capo_sagemaker.types.template_provider_detail_list.serialize_aws_json_1_1(
                value["template_provider_details"]
            )
        )
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "last_modified_by" in value:
        import capo_sagemaker.types.user_context

        out["LastModifiedBy"] = (
            capo_sagemaker.types.user_context.serialize_aws_json_1_1(
                value["last_modified_by"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Project:
    out: Project = {}  # type: ignore[typeddict-item]
    if data.get("ProjectArn") is not None:
        out["project_arn"] = data["ProjectArn"]
    if data.get("ProjectName") is not None:
        out["project_name"] = data["ProjectName"]
    if data.get("ProjectId") is not None:
        out["project_id"] = data["ProjectId"]
    if data.get("ProjectDescription") is not None:
        out["project_description"] = data["ProjectDescription"]
    if data.get("ServiceCatalogProvisioningDetails") is not None:
        import capo_sagemaker.types.service_catalog_provisioning_details

        out["service_catalog_provisioning_details"] = (
            capo_sagemaker.types.service_catalog_provisioning_details.deserialize_aws_json_1_1(
                data["ServiceCatalogProvisioningDetails"]
            )
        )
    if data.get("ServiceCatalogProvisionedProductDetails") is not None:
        import capo_sagemaker.types.service_catalog_provisioned_product_details

        out["service_catalog_provisioned_product_details"] = (
            capo_sagemaker.types.service_catalog_provisioned_product_details.deserialize_aws_json_1_1(
                data["ServiceCatalogProvisionedProductDetails"]
            )
        )
    if data.get("ProjectStatus") is not None:
        import capo_sagemaker.types.project_status

        out["project_status"] = (
            capo_sagemaker.types.project_status.deserialize_aws_json_1_1(
                data["ProjectStatus"]
            )
        )
    if data.get("CreatedBy") is not None:
        import capo_sagemaker.types.user_context

        out["created_by"] = capo_sagemaker.types.user_context.deserialize_aws_json_1_1(
            data["CreatedBy"]
        )
    if data.get("CreationTime") is not None:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("TemplateProviderDetails") is not None:
        import capo_sagemaker.types.template_provider_detail_list

        out["template_provider_details"] = (
            capo_sagemaker.types.template_provider_detail_list.deserialize_aws_json_1_1(
                data["TemplateProviderDetails"]
            )
        )
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if data.get("LastModifiedBy") is not None:
        import capo_sagemaker.types.user_context

        out["last_modified_by"] = (
            capo_sagemaker.types.user_context.deserialize_aws_json_1_1(
                data["LastModifiedBy"]
            )
        )
    return out
