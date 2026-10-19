"""Generated from Smithy shape ``com.amazonaws.xray#DeleteResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.policy_name
    import capo_xray.types.policy_revision_id


class DeleteResourcePolicyRequest(TypedDict, closed=True):
    policy_name: "capo_xray.types.policy_name.PolicyName"
    """<p>The name of the resource policy to delete.</p>"""
    policy_revision_id: NotRequired[
        "capo_xray.types.policy_revision_id.PolicyRevisionId"
    ]
    """<p>Specifies a specific policy revision to delete. Provide a <code>PolicyRevisionId</code> to ensure an atomic delete operation. If the provided revision id does not match the latest policy revision id, an <code>InvalidPolicyRevisionIdException</code> exception is returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourcePolicyRequest) -> dict:
    out: dict = {}
    out["PolicyName"] = value["policy_name"]
    if "policy_revision_id" in value:
        out["PolicyRevisionId"] = value["policy_revision_id"]
    return out


def deserialize_json(data: dict) -> DeleteResourcePolicyRequest:
    out: DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("PolicyName") is not None:
        out["policy_name"] = data["PolicyName"]
    else:
        out["policy_name"] = ""
    if data.get("PolicyRevisionId") is not None:
        out["policy_revision_id"] = data["PolicyRevisionId"]
    return out
