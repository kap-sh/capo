"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateProjectInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.create_template_provider_list
    import capo_sagemaker.types.entity_description
    import capo_sagemaker.types.project_entity_name
    import capo_sagemaker.types.service_catalog_provisioning_details
    import capo_sagemaker.types.tag_list


class CreateProjectInput(TypedDict, closed=True):
    project_name: NotRequired[
        "capo_sagemaker.types.project_entity_name.ProjectEntityName"
    ]
    """<p>The name of the project.</p>"""
    project_description: NotRequired[
        "capo_sagemaker.types.entity_description.EntityDescription"
    ]
    """<p>A description for the project.</p>"""
    service_catalog_provisioning_details: NotRequired[
        "capo_sagemaker.types.service_catalog_provisioning_details.ServiceCatalogProvisioningDetails"
    ]
    """<p>The product ID and provisioning artifact ID to provision a service catalog. The provisioning artifact ID will default to the latest provisioning artifact ID of the product, if you don't provide the provisioning artifact ID. For more information, see <a href="https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html">What is Amazon Web Services Service Catalog</a>.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>An array of key-value pairs that you want to use to organize and track your Amazon Web Services resource costs. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a> in the <i>Amazon Web Services General Reference Guide</i>.</p>"""
    template_providers: NotRequired[
        "capo_sagemaker.types.create_template_provider_list.CreateTemplateProviderList"
    ]
    """<p> An array of template provider configurations for creating infrastructure resources for the project. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateProjectInput) -> dict:
    out: dict = {}
    if "project_name" in value:
        out["ProjectName"] = value["project_name"]
    if "project_description" in value:
        out["ProjectDescription"] = value["project_description"]
    if "service_catalog_provisioning_details" in value:
        import capo_sagemaker.types.service_catalog_provisioning_details

        out["ServiceCatalogProvisioningDetails"] = (
            capo_sagemaker.types.service_catalog_provisioning_details.serialize_aws_json_1_1(
                value["service_catalog_provisioning_details"]
            )
        )
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "template_providers" in value:
        import capo_sagemaker.types.create_template_provider_list

        out["TemplateProviders"] = (
            capo_sagemaker.types.create_template_provider_list.serialize_aws_json_1_1(
                value["template_providers"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateProjectInput:
    out: CreateProjectInput = {}  # type: ignore[typeddict-item]
    if data.get("ProjectName") is not None:
        out["project_name"] = data["ProjectName"]
    if data.get("ProjectDescription") is not None:
        out["project_description"] = data["ProjectDescription"]
    if data.get("ServiceCatalogProvisioningDetails") is not None:
        import capo_sagemaker.types.service_catalog_provisioning_details

        out["service_catalog_provisioning_details"] = (
            capo_sagemaker.types.service_catalog_provisioning_details.deserialize_aws_json_1_1(
                data["ServiceCatalogProvisioningDetails"]
            )
        )
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("TemplateProviders") is not None:
        import capo_sagemaker.types.create_template_provider_list

        out["template_providers"] = (
            capo_sagemaker.types.create_template_provider_list.deserialize_aws_json_1_1(
                data["TemplateProviders"]
            )
        )
    return out
