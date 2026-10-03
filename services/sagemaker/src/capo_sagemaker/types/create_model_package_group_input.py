"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateModelPackageGroupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.entity_description
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.managed_configuration
    import capo_sagemaker.types.tag_list


class CreateModelPackageGroupInput(TypedDict, closed=True):
    model_package_group_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the model group.</p>"""
    model_package_group_description: NotRequired[
        "capo_sagemaker.types.entity_description.EntityDescription"
    ]
    """<p>A description for the model group.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>A list of key value pairs associated with the model group. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a> in the <i>Amazon Web Services General Reference Guide</i>.</p>"""
    managed_configuration: NotRequired[
        "capo_sagemaker.types.managed_configuration.ManagedConfiguration"
    ]
    """<p>The managed configuration of the model package group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateModelPackageGroupInput) -> dict:
    out: dict = {}
    if "model_package_group_name" in value:
        out["ModelPackageGroupName"] = value["model_package_group_name"]
    if "model_package_group_description" in value:
        out["ModelPackageGroupDescription"] = value["model_package_group_description"]
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "managed_configuration" in value:
        import capo_sagemaker.types.managed_configuration

        out["ManagedConfiguration"] = (
            capo_sagemaker.types.managed_configuration.serialize_aws_json_1_1(
                value["managed_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateModelPackageGroupInput:
    out: CreateModelPackageGroupInput = {}  # type: ignore[typeddict-item]
    if data.get("ModelPackageGroupName") is not None:
        out["model_package_group_name"] = data["ModelPackageGroupName"]
    if data.get("ModelPackageGroupDescription") is not None:
        out["model_package_group_description"] = data["ModelPackageGroupDescription"]
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("ManagedConfiguration") is not None:
        import capo_sagemaker.types.managed_configuration

        out["managed_configuration"] = (
            capo_sagemaker.types.managed_configuration.deserialize_aws_json_1_1(
                data["ManagedConfiguration"]
            )
        )
    return out
