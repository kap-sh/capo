"""Generated from Smithy shape ``com.amazonaws.organizations#PutResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_organizations.types.resource_policy_content
    import capo_organizations.types.tags


class PutResourcePolicyRequest(TypedDict, closed=True):
    content: "capo_organizations.types.resource_policy_content.ResourcePolicyContent"
    """<p>If provided, the new content for the resource policy. The text must be correctly formatted JSON that complies with the syntax for the resource policy's type. For more information, see <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_syntax.html">SCP syntax</a> in the <i>Organizations User Guide</i>.</p>"""
    tags: NotRequired["capo_organizations.types.tags.Tags"]
    """<p>A list of tags that you want to attach to the newly created resource policy. For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to <code>null</code>. For more information about tagging, see <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tagging.html">Tagging Organizations resources</a> in the Organizations User Guide.</p> <note> <p>Calls with tags apply to the initial creation of the resource policy, otherwise an exception is thrown. If any one of the tags is not valid or if you exceed the allowed number of tags for the resource policy, then the entire request fails and the resource policy is not created. </p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutResourcePolicyRequest) -> dict:
    out: dict = {}
    out["Content"] = value["content"]
    if "tags" in value:
        import capo_organizations.types.tags

        out["Tags"] = capo_organizations.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutResourcePolicyRequest:
    out: PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    else:
        raise DeserializationError("PutResourcePolicyRequest.content required")
    if data.get("Tags") is not None:
        import capo_organizations.types.tags

        out["tags"] = capo_organizations.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
