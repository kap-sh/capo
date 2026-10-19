"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#PutResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.event_bus_arn
    import capo_eventbridgev2.types.policy_name
    import capo_eventbridgev2.types.policy_revision_id


class PutResourcePolicyResponse(TypedDict, closed=True):
    resource_arn: "capo_eventbridgev2.types.event_bus_arn.EventBusArn"
    policy_name: "capo_eventbridgev2.types.policy_name.PolicyName"
    revision_id: NotRequired[
        "capo_eventbridgev2.types.policy_revision_id.PolicyRevisionId"
    ]
    """Absent when the write removed the policy; a removal produces no new revision."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutResourcePolicyResponse) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["PolicyName"] = value["policy_name"]
    if "revision_id" in value:
        out["RevisionId"] = value["revision_id"]
    return out


def deserialize_cbor(data: dict) -> PutResourcePolicyResponse:
    out: PutResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("PolicyName") is not None:
        out["policy_name"] = data["PolicyName"]
    else:
        out["policy_name"] = ""
    if data.get("RevisionId") is not None:
        out["revision_id"] = data["RevisionId"]
    return out
