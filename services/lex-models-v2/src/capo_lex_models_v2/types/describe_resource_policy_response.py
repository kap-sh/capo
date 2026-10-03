"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.amazon_resource_name
    import capo_lex_models_v2.types.policy
    import capo_lex_models_v2.types.revision_id


class DescribeResourcePolicyResponse(TypedDict, closed=True):
    resource_arn: NotRequired[
        "capo_lex_models_v2.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.</p>"""
    policy: NotRequired["capo_lex_models_v2.types.policy.Policy"]
    """<p>The JSON structure that contains the resource policy. For more information about the contents of a JSON policy document, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html"> IAM JSON policy reference </a>.</p>"""
    revision_id: NotRequired["capo_lex_models_v2.types.revision_id.RevisionId"]
    """<p>The current revision of the resource policy. Use the revision ID to make sure that you are updating the most current version of a resource policy when you add a policy statement to a resource, delete a resource, or update a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeResourcePolicyResponse) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "policy" in value:
        out["policy"] = value["policy"]
    if "revision_id" in value:
        out["revisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> DescribeResourcePolicyResponse:
    out: DescribeResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    if data.get("revisionId") is not None:
        out["revision_id"] = data["revisionId"]
    return out
