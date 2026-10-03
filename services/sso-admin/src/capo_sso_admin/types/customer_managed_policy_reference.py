"""Generated from Smithy shape ``com.amazonaws.ssoadmin#CustomerManagedPolicyReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sso_admin.types.managed_policy_name
    import capo_sso_admin.types.managed_policy_path


class CustomerManagedPolicyReference(TypedDict, closed=True):
    name: "capo_sso_admin.types.managed_policy_name.ManagedPolicyName"
    """<p>The name of the IAM policy that you have configured in each account where you want to deploy your permission set.</p>"""
    path: NotRequired["capo_sso_admin.types.managed_policy_path.ManagedPolicyPath"]
    """<p>The path to the IAM policy that you have configured in each account where you want to deploy your permission set. The default is <code>/</code>. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-friendly-names">Friendly names and paths</a> in the <i>IAM User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomerManagedPolicyReference) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "path" in value:
        out["Path"] = value["path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomerManagedPolicyReference:
    out: CustomerManagedPolicyReference = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CustomerManagedPolicyReference.name required")
    if data.get("Path") is not None:
        out["path"] = data["Path"]
    return out
