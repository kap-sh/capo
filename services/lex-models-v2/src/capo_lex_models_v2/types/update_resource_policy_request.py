"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UpdateResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.amazon_resource_name
    import capo_lex_models_v2.types.policy
    import capo_lex_models_v2.types.revision_id


class UpdateResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_lex_models_v2.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.</p>"""
    policy: "capo_lex_models_v2.types.policy.Policy"
    """<p>A resource policy to add to the resource. The policy is a JSON structure that contains one or more statements that define the policy. The policy must follow the IAM syntax. For more information about the contents of a JSON policy document, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html"> IAM JSON policy reference </a>. </p> <p>If the policy isn't valid, Amazon Lex returns a validation exception.</p>"""
    expected_revision_id: NotRequired["capo_lex_models_v2.types.revision_id.RevisionId"]
    """<p>The identifier of the revision of the policy to update. If this revision ID doesn't match the current revision ID, Amazon Lex throws an exception.</p> <p>If you don't specify a revision, Amazon Lex overwrites the contents of the policy with the new values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResourcePolicyRequest) -> dict:
    out: dict = {}
    out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> UpdateResourcePolicyRequest:
    out: UpdateResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    else:
        raise DeserializationError("UpdateResourcePolicyRequest.policy required")
    return out
