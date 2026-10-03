"""Generated from Smithy shape ``com.amazonaws.sesv2#CreateEmailIdentityPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sesv2.types.identity
    import capo_sesv2.types.policy
    import capo_sesv2.types.policy_name


class CreateEmailIdentityPolicyRequest(TypedDict, closed=True):
    email_identity: "capo_sesv2.types.identity.Identity"
    """<p>The email identity.</p>"""
    policy_name: "capo_sesv2.types.policy_name.PolicyName"
    """<p>The name of the policy.</p> <p>The policy name cannot exceed 64 characters and can only include alphanumeric characters, dashes, and underscores.</p>"""
    policy: "capo_sesv2.types.policy.Policy"
    """<p>The text of the policy in JSON format. The policy cannot exceed 4 KB.</p> <p>For information about the syntax of sending authorization policies, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization-policies.html">Amazon SES Developer Guide</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEmailIdentityPolicyRequest) -> dict:
    out: dict = {}
    out["Policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> CreateEmailIdentityPolicyRequest:
    out: CreateEmailIdentityPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    else:
        raise DeserializationError("CreateEmailIdentityPolicyRequest.policy required")
    return out
