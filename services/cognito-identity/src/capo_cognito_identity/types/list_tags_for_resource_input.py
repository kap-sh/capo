"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#ListTagsForResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity.types.arn_string


class ListTagsForResourceInput(TypedDict, closed=True):
    resource_arn: "capo_cognito_identity.types.arn_string.ARNString"
    """<p>The Amazon Resource Name (ARN) of the identity pool that the tags are assigned to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceInput) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceInput:
    out: ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    return out
