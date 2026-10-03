"""Generated from Smithy shape ``com.amazonaws.ssoadmin#AttachedManagedPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.managed_policy_arn
    import capo_sso_admin.types.name


class AttachedManagedPolicy(TypedDict, closed=True):
    name: NotRequired["capo_sso_admin.types.name.Name"]
    """<p>The name of the Amazon Web Services managed policy.</p>"""
    arn: NotRequired["capo_sso_admin.types.managed_policy_arn.ManagedPolicyArn"]
    """<p>The ARN of the Amazon Web Services managed policy. For more information about ARNs, see <a href="/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachedManagedPolicy) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AttachedManagedPolicy:
    out: AttachedManagedPolicy = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    return out
