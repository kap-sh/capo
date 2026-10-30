"""Generated from Smithy shape ``com.amazonaws.continuum#PutResourcePolicyOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.resource_policy_document
    import capo_continuum.types.resource_policy_revision_id
    import capo_continuum.types.resource_policy_target_arn


class PutResourcePolicyOutput(TypedDict, closed=True):
    arn: "capo_continuum.types.resource_policy_target_arn.ResourcePolicyTargetArn"
    policy: "capo_continuum.types.resource_policy_document.ResourcePolicyDocument"
    revision_id: (
        "capo_continuum.types.resource_policy_revision_id.ResourcePolicyRevisionId"
    )


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePolicyOutput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["policy"] = value["policy"]
    out["revisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> PutResourcePolicyOutput:
    out: PutResourcePolicyOutput = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    else:
        out["policy"] = ""
    if data.get("revisionId") is not None:
        out["revision_id"] = data["revisionId"]
    else:
        out["revision_id"] = ""
    return out


def redact_sensitive(value: PutResourcePolicyOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "policy" in value:
        out["policy"] = "*** Sensitive Data Redacted ***"
    return out
