"""Generated from Smithy shape ``com.amazonaws.iamtoolbox#GetRequestAuthorizationPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iam_toolbox.types.authorization_id
    import capo_iam_toolbox.types.policy_uri


class GetRequestAuthorizationPolicyInput(TypedDict, closed=True):
    authorization_id: "capo_iam_toolbox.types.authorization_id.AuthorizationId"
    """<p>The authorization ID received in the access denied error message. This ID identifies the request whose evaluated policy you want to retrieve.</p>"""
    policy_uri: "capo_iam_toolbox.types.policy_uri.PolicyUri"
    """<p>The URI of the policy to retrieve. Use the <code>uri</code> value from the <code>policies</code> list returned by <code>GetRequestAuthorizationDetails</code> for the same authorization ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRequestAuthorizationPolicyInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRequestAuthorizationPolicyInput:
    out: GetRequestAuthorizationPolicyInput = {}  # type: ignore[typeddict-item]
    return out
