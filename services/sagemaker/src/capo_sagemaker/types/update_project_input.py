"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateProjectInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.entity_description
    import capo_sagemaker.types.project_entity_name
    import capo_sagemaker.types.service_catalog_provisioning_update_details
    import capo_sagemaker.types.tag_list
    import capo_sagemaker.types.update_template_provider_list


class UpdateProjectInput(TypedDict, closed=True):
    project_name: NotRequired[
        "capo_sagemaker.types.project_entity_name.ProjectEntityName"
    ]
    """<p>The name of the project.</p>"""
    project_description: NotRequired[
        "capo_sagemaker.types.entity_description.EntityDescription"
    ]
    """<p>The description for the project.</p>"""
    service_catalog_provisioning_update_details: NotRequired[
        "capo_sagemaker.types.service_catalog_provisioning_update_details.ServiceCatalogProvisioningUpdateDetails"
    ]
    """<p>The product ID and provisioning artifact ID to provision a service catalog. The provisioning artifact ID will default to the latest provisioning artifact ID of the product, if you don't provide the provisioning artifact ID. For more information, see <a href="https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html">What is Amazon Web Services Service Catalog</a>. </p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>An array of key-value pairs. You can use tags to categorize your Amazon Web Services resources in different ways, for example, by purpose, owner, or environment. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services Resources</a>. In addition, the project must have tag update constraints set in order to include this parameter in the request. For more information, see <a href="https://docs.aws.amazon.com/servicecatalog/latest/adminguide/constraints-resourceupdate.html">Amazon Web Services Service Catalog Tag Update Constraints</a>.</p>"""
    template_providers_to_update: NotRequired[
        "capo_sagemaker.types.update_template_provider_list.UpdateTemplateProviderList"
    ]
    """<p> The template providers to update in the project. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateProjectInput) -> dict:
    out: dict = {}
    if "project_name" in value:
        out["ProjectName"] = value["project_name"]
    if "project_description" in value:
        out["ProjectDescription"] = value["project_description"]
    if "service_catalog_provisioning_update_details" in value:
        import capo_sagemaker.types.service_catalog_provisioning_update_details

        out["ServiceCatalogProvisioningUpdateDetails"] = (
            capo_sagemaker.types.service_catalog_provisioning_update_details.serialize_aws_json_1_1(
                value["service_catalog_provisioning_update_details"]
            )
        )
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "template_providers_to_update" in value:
        import capo_sagemaker.types.update_template_provider_list

        out["TemplateProvidersToUpdate"] = (
            capo_sagemaker.types.update_template_provider_list.serialize_aws_json_1_1(
                value["template_providers_to_update"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateProjectInput:
    out: UpdateProjectInput = {}  # type: ignore[typeddict-item]
    if data.get("ProjectName") is not None:
        out["project_name"] = data["ProjectName"]
    if data.get("ProjectDescription") is not None:
        out["project_description"] = data["ProjectDescription"]
    if data.get("ServiceCatalogProvisioningUpdateDetails") is not None:
        import capo_sagemaker.types.service_catalog_provisioning_update_details

        out["service_catalog_provisioning_update_details"] = (
            capo_sagemaker.types.service_catalog_provisioning_update_details.deserialize_aws_json_1_1(
                data["ServiceCatalogProvisioningUpdateDetails"]
            )
        )
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("TemplateProvidersToUpdate") is not None:
        import capo_sagemaker.types.update_template_provider_list

        out["template_providers_to_update"] = (
            capo_sagemaker.types.update_template_provider_list.deserialize_aws_json_1_1(
                data["TemplateProvidersToUpdate"]
            )
        )
    return out
