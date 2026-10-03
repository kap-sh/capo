"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#PutResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_eventbridgev2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eventbridgev2.types.event_bus_arn
    import capo_eventbridgev2.types.policy_document
    import capo_eventbridgev2.types.policy_name
    import capo_eventbridgev2.types.policy_revision_id


class PutResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_eventbridgev2.types.event_bus_arn.EventBusArn"
    policy_document: "capo_eventbridgev2.types.policy_document.PolicyDocument"
    policy_name: NotRequired["capo_eventbridgev2.types.policy_name.PolicyName"]
    """Which named policy to write. Defaults to "default", the customer-managed policy, when omitted (a write AWS Resource Access Manager makes on the owner's behalf resolves to "AWS_RAM" instead). The two writers are exclusive in both directions — only Resource Access Manager can write "AWS_RAM", and only the bus owner can write "default" — so naming the other party's policy fails with AccessDeniedException. A well-formed name that is neither of the two fails with InvalidInputException."""
    expected_revision_id: NotRequired[
        "capo_eventbridgev2.types.policy_revision_id.PolicyRevisionId"
    ]
    """The write succeeds only if the named policy's current revision ID matches this value; a policy that does not exist yet matches only the sentinel "NO_POLICY" (create-only). On mismatch the operation fails with ConflictException. When omitted, the write is unconditional. Every attempt stores a newly generated revision ID, so retrying an unanswered request can conflict with the caller's own earlier attempt; read the policy back and compare it with the one you intended before treating a conflict as another writer's change."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutResourcePolicyRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["PolicyDocument"] = value["policy_document"]
    if "policy_name" in value:
        out["PolicyName"] = value["policy_name"]
    if "expected_revision_id" in value:
        out["ExpectedRevisionId"] = value["expected_revision_id"]
    return out


def deserialize_cbor(data: dict) -> PutResourcePolicyRequest:
    out: PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("PutResourcePolicyRequest.resource_arn required")
    if data.get("PolicyDocument") is not None:
        out["policy_document"] = data["PolicyDocument"]
    else:
        raise DeserializationError("PutResourcePolicyRequest.policy_document required")
    if data.get("PolicyName") is not None:
        out["policy_name"] = data["PolicyName"]
    if data.get("ExpectedRevisionId") is not None:
        out["expected_revision_id"] = data["ExpectedRevisionId"]
    return out
