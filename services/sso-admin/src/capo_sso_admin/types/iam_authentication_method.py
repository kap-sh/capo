"""Generated from Smithy shape ``com.amazonaws.ssoadmin#IamAuthenticationMethod``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.actor_policy_document


class IamAuthenticationMethod(TypedDict, closed=True):
    actor_policy: "capo_sso_admin.types.actor_policy_document.ActorPolicyDocument"
    """<p>An IAM policy document in JSON.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IamAuthenticationMethod) -> dict:
    out: dict = {}
    out["ActorPolicy"] = value["actor_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IamAuthenticationMethod:
    out: IamAuthenticationMethod = {}  # type: ignore[typeddict-item]
    if data.get("ActorPolicy") is not None:
        out["actor_policy"] = data["ActorPolicy"]
    else:
        out["actor_policy"] = None
    return out
