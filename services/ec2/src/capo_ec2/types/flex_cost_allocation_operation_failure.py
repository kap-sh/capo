"""Generated from Smithy shape ``com.amazonaws.ec2#FlexCostAllocationOperationFailure``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class FlexCostAllocationOperationFailure(TypedDict, closed=True):
    resource_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the resource that could not be processed.</p>"""
    failure_code: NotRequired["capo_ec2.types.string.String"]
    """<p>The code that identifies the type of failure. Possible values are:</p> <ul> <li> <p> <code>ResourceNotFound</code> - (<code>DeleteNetworkingFlexCostAllocationPolicies</code>) The policy doesn't exist or isn't owned by your account.</p> </li> <li> <p> <code>InvalidResourceState</code> - (<code>DeleteNetworkingFlexCostAllocationPolicies</code>) The policy has active associations.</p> </li> <li> <p> <code>InvalidResource</code> - (<code>AssociateNetworkingFlexCostAllocationPolicy</code>) The resource ID is malformed, the resource type doesn't match the policy, or the scope is an account other than yours. (<code>DisassociateNetworkingFlexCostAllocationPolicy</code>) The association doesn't exist or was already removed.</p> </li> <li> <p> <code>ResourceAlreadyAssociated</code> - (<code>AssociateNetworkingFlexCostAllocationPolicy</code>) The resource already has an active association.</p> </li> <li> <p> <code>InternalError</code> - An internal error occurred. Retry the request.</p> </li> </ul>"""
    failure_reason: NotRequired["capo_ec2.types.string.String"]
    """<p>The reason for the failure.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FlexCostAllocationOperationFailure, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "resource_id" in value:
        pairs.append((f"{key_prefix}ResourceId", str(value["resource_id"])))
    if "failure_code" in value:
        pairs.append((f"{key_prefix}FailureCode", str(value["failure_code"])))
    if "failure_reason" in value:
        pairs.append((f"{key_prefix}FailureReason", str(value["failure_reason"])))


def deserialize_ec2_query(el: Element) -> FlexCostAllocationOperationFailure:
    out: FlexCostAllocationOperationFailure = {}  # type: ignore[typeddict-item]
    child_resource_id = el.find("resourceId")
    if child_resource_id is not None:
        out["resource_id"] = str(child_resource_id.text or "")
    child_failure_code = el.find("failureCode")
    if child_failure_code is not None:
        out["failure_code"] = str(child_failure_code.text or "")
    child_failure_reason = el.find("failureReason")
    if child_failure_reason is not None:
        out["failure_reason"] = str(child_failure_reason.text or "")
    return out
