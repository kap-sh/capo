"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#ResourcePolicySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.policy_name
    import capo_eventbridgev2.types.policy_revision_id


class ResourcePolicySummary(TypedDict, closed=True):
    policy_name: "capo_eventbridgev2.types.policy_name.PolicyName"
    revision_id: "capo_eventbridgev2.types.policy_revision_id.PolicyRevisionId"


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourcePolicySummary) -> dict:
    out: dict = {}
    out["PolicyName"] = value["policy_name"]
    out["RevisionId"] = value["revision_id"]
    return out


def deserialize_cbor(data: dict) -> ResourcePolicySummary:
    out: ResourcePolicySummary = {}  # type: ignore[typeddict-item]
    if data.get("PolicyName") is not None:
        out["policy_name"] = data["PolicyName"]
    else:
        out["policy_name"] = ""
    if data.get("RevisionId") is not None:
        out["revision_id"] = data["RevisionId"]
    else:
        out["revision_id"] = ""
    return out
