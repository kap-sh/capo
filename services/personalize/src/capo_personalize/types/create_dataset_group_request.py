"""Generated from Smithy shape ``com.amazonaws.personalize#CreateDatasetGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import capo_personalize.types.domain
    import capo_personalize.types.kms_key_arn
    import capo_personalize.types.name
    import capo_personalize.types.role_arn
    import capo_personalize.types.tags


class CreateDatasetGroupRequest(TypedDict, closed=True):
    name: "capo_personalize.types.name.Name"
    """<p>The name for the new dataset group.</p>"""
    role_arn: NotRequired["capo_personalize.types.role_arn.RoleArn"]
    """<p>The ARN of the Identity and Access Management (IAM) role that has permissions to access the Key Management Service (KMS) key. Supplying an IAM role is only valid when also specifying a KMS key.</p>"""
    kms_key_arn: NotRequired["capo_personalize.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of a Key Management Service (KMS) key used to encrypt the datasets.</p>"""
    domain: NotRequired["capo_personalize.types.domain.Domain"]
    """<p>The domain of the dataset group. Specify a domain to create a Domain dataset group. The domain you specify determines the default schemas for datasets and the use cases available for recommenders. If you don't specify a domain, you create a Custom dataset group with solution versions that you deploy with a campaign. </p>"""
    tags: NotRequired["capo_personalize.types.tags.Tags"]
    """<p>A list of <a href="https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html">tags</a> to apply to the dataset group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDatasetGroupRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "domain" in value:
        import capo_personalize.types.domain

        out["domain"] = capo_personalize.types.domain.serialize_aws_json_1_1(
            value["domain"]
        )
    if "tags" in value:
        import capo_personalize.types.tags

        out["tags"] = capo_personalize.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDatasetGroupRequest:
    out: CreateDatasetGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateDatasetGroupRequest.name required")
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("domain") is not None:
        import capo_personalize.types.domain

        out["domain"] = capo_personalize.types.domain.deserialize_aws_json_1_1(
            data["domain"]
        )
    if data.get("tags") is not None:
        import capo_personalize.types.tags

        out["tags"] = capo_personalize.types.tags.deserialize_aws_json_1_1(data["tags"])
    return out
