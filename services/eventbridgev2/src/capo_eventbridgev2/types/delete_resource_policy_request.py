"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#DeleteResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_eventbridgev2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eventbridgev2.types.event_bus_arn
    import capo_eventbridgev2.types.policy_name
    import capo_eventbridgev2.types.policy_revision_id


class DeleteResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_eventbridgev2.types.event_bus_arn.EventBusArn"
    policy_name: NotRequired["capo_eventbridgev2.types.policy_name.PolicyName"]
    """Which named policy to delete. Defaults to "default" when omitted (a delete AWS Resource Access Manager makes on the owner's behalf resolves to "AWS_RAM" instead). The two writers are exclusive in both directions — only Resource Access Manager can delete "AWS_RAM", and only the bus owner can delete "default" — so naming the other party's policy fails with AccessDeniedException. A well-formed name that is neither of the two fails with InvalidInputException."""
    expected_revision_id: NotRequired[
        "capo_eventbridgev2.types.policy_revision_id.PolicyRevisionId"
    ]
    """The delete succeeds only if the named policy's current revision ID matches this value; if it differs or the policy does not exist, the operation fails with ConflictException. The "NO_POLICY" sentinel is not valid here. When omitted, deleting an absent policy is an idempotent success. Supplying this value makes the delete non-idempotent: once it succeeds the expected revision no longer exists, so retrying an unanswered request fails with ConflictException even though the policy was deleted. To establish the outcome, read the policy back: ResourceNotFoundException means the delete took effect."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteResourcePolicyRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    if "policy_name" in value:
        out["PolicyName"] = value["policy_name"]
    if "expected_revision_id" in value:
        out["ExpectedRevisionId"] = value["expected_revision_id"]
    return out


def deserialize_cbor(data: dict) -> DeleteResourcePolicyRequest:
    out: DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("DeleteResourcePolicyRequest.resource_arn required")
    if data.get("PolicyName") is not None:
        out["policy_name"] = data["PolicyName"]
    if data.get("ExpectedRevisionId") is not None:
        out["expected_revision_id"] = data["ExpectedRevisionId"]
    return out
