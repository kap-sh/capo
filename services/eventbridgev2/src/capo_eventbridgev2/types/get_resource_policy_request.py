"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#GetResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_eventbridgev2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eventbridgev2.types.event_bus_arn
    import capo_eventbridgev2.types.policy_name


class GetResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_eventbridgev2.types.event_bus_arn.EventBusArn"
    policy_name: NotRequired["capo_eventbridgev2.types.policy_name.PolicyName"]
    """Which named policy to read. Defaults to "default" when omitted (a read AWS Resource Access Manager makes on the owner's behalf resolves to "AWS_RAM" instead). Unlike writing, neither name is reserved on a read: the bus owner can read both. There is no fallback between the two, so a bus shared only through Resource Access Manager fails with ResourceNotFoundException until "AWS_RAM" is named explicitly. A well-formed name that is neither of the two fails with InvalidInputException."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetResourcePolicyRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    if "policy_name" in value:
        out["PolicyName"] = value["policy_name"]
    return out


def deserialize_cbor(data: dict) -> GetResourcePolicyRequest:
    out: GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("GetResourcePolicyRequest.resource_arn required")
    if data.get("PolicyName") is not None:
        out["policy_name"] = data["PolicyName"]
    return out
