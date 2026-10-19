"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity.types.arn_string
    import capo_cognito_identity.types.identity_pool_tags_type


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_cognito_identity.types.arn_string.ARNString"
    """<p>The Amazon Resource Name (ARN) of the identity pool.</p>"""
    tags: "capo_cognito_identity.types.identity_pool_tags_type.IdentityPoolTagsType"
    """<p>The tags to assign to the identity pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceInput) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_cognito_identity.types.identity_pool_tags_type

    out["Tags"] = (
        capo_cognito_identity.types.identity_pool_tags_type.serialize_aws_json_1_1(
            value["tags"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("Tags") is not None:
        import capo_cognito_identity.types.identity_pool_tags_type

        out["tags"] = (
            capo_cognito_identity.types.identity_pool_tags_type.deserialize_aws_json_1_1(
                data["Tags"]
            )
        )
    else:
        out["tags"] = {}
    return out
