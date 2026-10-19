"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#GetResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.event_bus_arn
    import capo_eventbridgev2.types.policy_document
    import capo_eventbridgev2.types.policy_name
    import capo_eventbridgev2.types.policy_revision_id


class GetResourcePolicyResponse(TypedDict, closed=True):
    resource_arn: "capo_eventbridgev2.types.event_bus_arn.EventBusArn"
    policy_document: "capo_eventbridgev2.types.policy_document.PolicyDocument"
    policy_name: "capo_eventbridgev2.types.policy_name.PolicyName"
    revision_id: "capo_eventbridgev2.types.policy_revision_id.PolicyRevisionId"


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetResourcePolicyResponse) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["PolicyDocument"] = value["policy_document"]
    out["PolicyName"] = value["policy_name"]
    out["RevisionId"] = value["revision_id"]
    return out


def deserialize_cbor(data: dict) -> GetResourcePolicyResponse:
    out: GetResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("PolicyDocument") is not None:
        out["policy_document"] = data["PolicyDocument"]
    else:
        out["policy_document"] = ""
    if data.get("PolicyName") is not None:
        out["policy_name"] = data["PolicyName"]
    else:
        out["policy_name"] = ""
    if data.get("RevisionId") is not None:
        out["revision_id"] = data["RevisionId"]
    else:
        out["revision_id"] = ""
    return out
