"""Generated from Smithy shape ``com.amazonaws.iam#AttachGroupPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.group_name_type


class AttachGroupPolicyRequest(TypedDict, closed=True):
    group_name: "capo_iam.types.group_name_type.groupNameType"
    """<p>The name (friendly name, not ARN) of the group to attach the policy to.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    policy_arn: "capo_iam.types.arn_type.arnType"
    """<p>The Amazon Resource Name (ARN) of the IAM policy you want to attach.</p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AttachGroupPolicyRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}GroupName", str(value["group_name"])))
    pairs.append((f"{key_prefix}PolicyArn", str(value["policy_arn"])))


def deserialize_query(el: Element) -> AttachGroupPolicyRequest:
    out: AttachGroupPolicyRequest = {}  # type: ignore[typeddict-item]
    child_group_name = el.find("GroupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    else:
        raise DeserializationError("AttachGroupPolicyRequest.group_name required")
    child_policy_arn = el.find("PolicyArn")
    if child_policy_arn is not None:
        out["policy_arn"] = str(child_policy_arn.text or "")
    else:
        raise DeserializationError("AttachGroupPolicyRequest.policy_arn required")
    return out
