"""Generated from Smithy shape ``com.amazonaws.efs#PutFileSystemPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_efs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_efs.types.bypass_policy_lockout_safety_check
    import capo_efs.types.file_system_id
    import capo_efs.types.policy


class PutFileSystemPolicyRequest(TypedDict, closed=True):
    file_system_id: "capo_efs.types.file_system_id.FileSystemId"
    """<p>The ID of the EFS file system that you want to create or update the <code>FileSystemPolicy</code> for.</p>"""
    policy: "capo_efs.types.policy.Policy"
    """<p>The <code>FileSystemPolicy</code> that you're creating. Accepts a JSON formatted policy definition. EFS file system policies have a 20,000 character limit. To find out more about the elements that make up a file system policy, see <a href="https://docs.aws.amazon.com/efs/latest/ug/security_iam_service-with-iam.html#security_iam_service-with-iam-resource-based-policies">Resource-based policies within Amazon EFS</a>. </p>"""
    bypass_policy_lockout_safety_check: "capo_efs.types.bypass_policy_lockout_safety_check.BypassPolicyLockoutSafetyCheck"
    """<p>(Optional) A boolean that specifies whether or not to bypass the <code>FileSystemPolicy</code> lockout safety check. The lockout safety check determines whether the policy in the request will lock out, or prevent, the IAM principal that is making the request from making future <code>PutFileSystemPolicy</code> requests on this file system. Set <code>BypassPolicyLockoutSafetyCheck</code> to <code>True</code> only when you intend to prevent the IAM principal that is making the request from making subsequent <code>PutFileSystemPolicy</code> requests on this file system. The default value is <code>False</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutFileSystemPolicyRequest) -> dict:
    out: dict = {}
    out["Policy"] = value["policy"]
    out["BypassPolicyLockoutSafetyCheck"] = value.get(
        "bypass_policy_lockout_safety_check", False
    )
    return out


def deserialize_json(data: dict) -> PutFileSystemPolicyRequest:
    out: PutFileSystemPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    else:
        raise DeserializationError("PutFileSystemPolicyRequest.policy required")
    if data.get("BypassPolicyLockoutSafetyCheck") is not None:
        out["bypass_policy_lockout_safety_check"] = data[
            "BypassPolicyLockoutSafetyCheck"
        ]
    else:
        out["bypass_policy_lockout_safety_check"] = False
    return out
