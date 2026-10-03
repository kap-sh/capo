"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelCard``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.integer
    import capo_sagemaker.types.model_card_arn
    import capo_sagemaker.types.model_card_content
    import capo_sagemaker.types.model_card_security_config
    import capo_sagemaker.types.model_card_status
    import capo_sagemaker.types.string
    import capo_sagemaker.types.tag_list
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.user_context


class ModelCard(TypedDict, closed=True):
    model_card_arn: NotRequired["capo_sagemaker.types.model_card_arn.ModelCardArn"]
    """<p>The Amazon Resource Name (ARN) of the model card.</p>"""
    model_card_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The unique name of the model card.</p>"""
    model_card_version: NotRequired["capo_sagemaker.types.integer.Integer"]
    """<p>The version of the model card.</p>"""
    content: NotRequired["capo_sagemaker.types.model_card_content.ModelCardContent"]
    """<p>The content of the model card. Content uses the <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html#model-cards-json-schema">model card JSON schema</a> and provided as a string.</p>"""
    model_card_status: NotRequired[
        "capo_sagemaker.types.model_card_status.ModelCardStatus"
    ]
    """<p>The approval status of the model card within your organization. Different organizations might have different criteria for model card review and approval.</p> <ul> <li> <p> <code>Draft</code>: The model card is a work in progress.</p> </li> <li> <p> <code>PendingReview</code>: The model card is pending review.</p> </li> <li> <p> <code>Approved</code>: The model card is approved.</p> </li> <li> <p> <code>Archived</code>: The model card is archived. No more updates should be made to the model card, but it can still be exported.</p> </li> </ul>"""
    security_config: NotRequired[
        "capo_sagemaker.types.model_card_security_config.ModelCardSecurityConfig"
    ]
    """<p>The security configuration used to protect model card data.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the model card was created.</p>"""
    created_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the model card was last modified.</p>"""
    last_modified_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>Key-value pairs used to manage metadata for the model card.</p>"""
    model_id: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The unique name (ID) of the model.</p>"""
    risk_rating: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The risk rating of the model. Different organizations might have different criteria for model card risk ratings. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards-risk-rating.html">Risk ratings</a>.</p>"""
    model_package_group_name: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The model package group that contains the model package. Only relevant for model cards created for model packages in the Amazon SageMaker Model Registry. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelCard) -> dict:
    out: dict = {}
    if "model_card_arn" in value:
        out["ModelCardArn"] = value["model_card_arn"]
    if "model_card_name" in value:
        out["ModelCardName"] = value["model_card_name"]
    if "model_card_version" in value:
        out["ModelCardVersion"] = value["model_card_version"]
    if "content" in value:
        out["Content"] = value["content"]
    if "model_card_status" in value:
        import capo_sagemaker.types.model_card_status

        out["ModelCardStatus"] = (
            capo_sagemaker.types.model_card_status.serialize_aws_json_1_1(
                value["model_card_status"]
            )
        )
    if "security_config" in value:
        import capo_sagemaker.types.model_card_security_config

        out["SecurityConfig"] = (
            capo_sagemaker.types.model_card_security_config.serialize_aws_json_1_1(
                value["security_config"]
            )
        )
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "created_by" in value:
        import capo_sagemaker.types.user_context

        out["CreatedBy"] = capo_sagemaker.types.user_context.serialize_aws_json_1_1(
            value["created_by"]
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
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "model_id" in value:
        out["ModelId"] = value["model_id"]
    if "risk_rating" in value:
        out["RiskRating"] = value["risk_rating"]
    if "model_package_group_name" in value:
        out["ModelPackageGroupName"] = value["model_package_group_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelCard:
    out: ModelCard = {}  # type: ignore[typeddict-item]
    if data.get("ModelCardArn") is not None:
        out["model_card_arn"] = data["ModelCardArn"]
    if data.get("ModelCardName") is not None:
        out["model_card_name"] = data["ModelCardName"]
    if data.get("ModelCardVersion") is not None:
        out["model_card_version"] = data["ModelCardVersion"]
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    if data.get("ModelCardStatus") is not None:
        import capo_sagemaker.types.model_card_status

        out["model_card_status"] = (
            capo_sagemaker.types.model_card_status.deserialize_aws_json_1_1(
                data["ModelCardStatus"]
            )
        )
    if data.get("SecurityConfig") is not None:
        import capo_sagemaker.types.model_card_security_config

        out["security_config"] = (
            capo_sagemaker.types.model_card_security_config.deserialize_aws_json_1_1(
                data["SecurityConfig"]
            )
        )
    if data.get("CreationTime") is not None:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("CreatedBy") is not None:
        import capo_sagemaker.types.user_context

        out["created_by"] = capo_sagemaker.types.user_context.deserialize_aws_json_1_1(
            data["CreatedBy"]
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
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("ModelId") is not None:
        out["model_id"] = data["ModelId"]
    if data.get("RiskRating") is not None:
        out["risk_rating"] = data["RiskRating"]
    if data.get("ModelPackageGroupName") is not None:
        out["model_package_group_name"] = data["ModelPackageGroupName"]
    return out
