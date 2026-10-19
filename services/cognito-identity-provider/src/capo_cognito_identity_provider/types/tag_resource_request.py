"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.arn_type
    import capo_cognito_identity_provider.types.user_pool_tags_type


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_cognito_identity_provider.types.arn_type.ArnType"
    """<p>The Amazon Resource Name (ARN) of the user pool to assign the tags to.</p>"""
    tags: "capo_cognito_identity_provider.types.user_pool_tags_type.UserPoolTagsType"
    """<p>An array of tag keys and values that you want to assign to the user pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_cognito_identity_provider.types.user_pool_tags_type

    out["Tags"] = (
        capo_cognito_identity_provider.types.user_pool_tags_type.serialize_aws_json_1_1(
            value["tags"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("Tags") is not None:
        import capo_cognito_identity_provider.types.user_pool_tags_type

        out["tags"] = (
            capo_cognito_identity_provider.types.user_pool_tags_type.deserialize_aws_json_1_1(
                data["Tags"]
            )
        )
    else:
        out["tags"] = {}
    return out
