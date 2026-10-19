"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity.types.arn_string
    import capo_cognito_identity.types.identity_pool_tags_list_type


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_cognito_identity.types.arn_string.ARNString"
    """<p>The Amazon Resource Name (ARN) of the identity pool.</p>"""
    tag_keys: "capo_cognito_identity.types.identity_pool_tags_list_type.IdentityPoolTagsListType"
    """<p>The keys of the tags to remove from the user pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceInput) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_cognito_identity.types.identity_pool_tags_list_type

    out["TagKeys"] = (
        capo_cognito_identity.types.identity_pool_tags_list_type.serialize_aws_json_1_1(
            value["tag_keys"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("TagKeys") is not None:
        import capo_cognito_identity.types.identity_pool_tags_list_type

        out["tag_keys"] = (
            capo_cognito_identity.types.identity_pool_tags_list_type.deserialize_aws_json_1_1(
                data["TagKeys"]
            )
        )
    else:
        out["tag_keys"] = []
    return out
