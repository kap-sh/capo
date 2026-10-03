"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelPackageGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.creation_time
    import capo_sagemaker.types.entity_description
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.model_package_group_arn
    import capo_sagemaker.types.model_package_group_status
    import capo_sagemaker.types.tag_list
    import capo_sagemaker.types.user_context


class ModelPackageGroup(TypedDict, closed=True):
    model_package_group_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the model group.</p>"""
    model_package_group_arn: NotRequired[
        "capo_sagemaker.types.model_package_group_arn.ModelPackageGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the model group.</p>"""
    model_package_group_description: NotRequired[
        "capo_sagemaker.types.entity_description.EntityDescription"
    ]
    """<p>The description for the model group.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.creation_time.CreationTime"]
    """<p>The time that the model group was created.</p>"""
    created_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    model_package_group_status: NotRequired[
        "capo_sagemaker.types.model_package_group_status.ModelPackageGroupStatus"
    ]
    """<p>The status of the model group. This can be one of the following values.</p> <ul> <li> <p> <code>PENDING</code> - The model group is pending being created.</p> </li> <li> <p> <code>IN_PROGRESS</code> - The model group is in the process of being created.</p> </li> <li> <p> <code>COMPLETED</code> - The model group was successfully created.</p> </li> <li> <p> <code>FAILED</code> - The model group failed.</p> </li> <li> <p> <code>DELETING</code> - The model group is in the process of being deleted.</p> </li> <li> <p> <code>DELETE_FAILED</code> - SageMaker failed to delete the model group.</p> </li> </ul>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>A list of the tags associated with the model group. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a> in the <i>Amazon Web Services General Reference Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelPackageGroup) -> dict:
    out: dict = {}
    if "model_package_group_name" in value:
        out["ModelPackageGroupName"] = value["model_package_group_name"]
    if "model_package_group_arn" in value:
        out["ModelPackageGroupArn"] = value["model_package_group_arn"]
    if "model_package_group_description" in value:
        out["ModelPackageGroupDescription"] = value["model_package_group_description"]
    if "creation_time" in value:
        import capo_sagemaker.types.creation_time

        out["CreationTime"] = capo_sagemaker.types.creation_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "created_by" in value:
        import capo_sagemaker.types.user_context

        out["CreatedBy"] = capo_sagemaker.types.user_context.serialize_aws_json_1_1(
            value["created_by"]
        )
    if "model_package_group_status" in value:
        import capo_sagemaker.types.model_package_group_status

        out["ModelPackageGroupStatus"] = (
            capo_sagemaker.types.model_package_group_status.serialize_aws_json_1_1(
                value["model_package_group_status"]
            )
        )
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelPackageGroup:
    out: ModelPackageGroup = {}  # type: ignore[typeddict-item]
    if data.get("ModelPackageGroupName") is not None:
        out["model_package_group_name"] = data["ModelPackageGroupName"]
    if data.get("ModelPackageGroupArn") is not None:
        out["model_package_group_arn"] = data["ModelPackageGroupArn"]
    if data.get("ModelPackageGroupDescription") is not None:
        out["model_package_group_description"] = data["ModelPackageGroupDescription"]
    if data.get("CreationTime") is not None:
        import capo_sagemaker.types.creation_time

        out["creation_time"] = (
            capo_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if data.get("CreatedBy") is not None:
        import capo_sagemaker.types.user_context

        out["created_by"] = capo_sagemaker.types.user_context.deserialize_aws_json_1_1(
            data["CreatedBy"]
        )
    if data.get("ModelPackageGroupStatus") is not None:
        import capo_sagemaker.types.model_package_group_status

        out["model_package_group_status"] = (
            capo_sagemaker.types.model_package_group_status.deserialize_aws_json_1_1(
                data["ModelPackageGroupStatus"]
            )
        )
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
