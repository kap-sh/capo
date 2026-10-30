"""Generated from Smithy shape ``com.amazonaws.continuum#PutResourcePolicyInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.resource_policy_input_document
    import capo_continuum.types.resource_policy_revision_id
    import capo_continuum.types.resource_policy_target_arn


class PutResourcePolicyInput(TypedDict, closed=True):
    arn: "capo_continuum.types.resource_policy_target_arn.ResourcePolicyTargetArn"
    """The ARN of a resource in the caller's account."""
    policy: NotRequired[
        "capo_continuum.types.resource_policy_input_document.ResourcePolicyInputDocument"
    ]
    """Omit or supply an empty Statement array to clear resource-policy grants and store the canonical empty-statement policy. Cross-account access is denied; same-account access remains subject to identity policies. Use an explicit Deny statement to deny same-account principals too."""
    expected_revision_id: NotRequired[
        "capo_continuum.types.resource_policy_revision_id.ResourcePolicyRevisionId"
    ]
    """Optional optimistic-concurrency token for the currently observed policy."""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePolicyInput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "policy" in value:
        out["policy"] = value["policy"]
    if "expected_revision_id" in value:
        out["expectedRevisionId"] = value["expected_revision_id"]
    return out


def deserialize_json(data: dict) -> PutResourcePolicyInput:
    out: PutResourcePolicyInput = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    if data.get("expectedRevisionId") is not None:
        out["expected_revision_id"] = data["expectedRevisionId"]
    return out


def redact_sensitive(value: PutResourcePolicyInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "policy" in value:
        out["policy"] = "*** Sensitive Data Redacted ***"
    return out
