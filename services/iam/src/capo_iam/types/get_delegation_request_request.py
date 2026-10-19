"""Generated from Smithy shape ``com.amazonaws.iam#GetDelegationRequestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.boolean_type
    import capo_iam.types.delegation_request_id_type


class GetDelegationRequestRequest(TypedDict, closed=True):
    delegation_request_id: (
        "capo_iam.types.delegation_request_id_type.delegationRequestIdType"
    )
    """<p>The unique identifier of the delegation request to retrieve.</p>"""
    delegation_permission_check: NotRequired["capo_iam.types.boolean_type.booleanType"]
    """<p>Specifies whether to perform a permission check for the delegation request.</p> <p>If set to true, the <code>GetDelegationRequest</code> API call will start a permission check process. This process calculates whether the caller has sufficient permissions to cover the asks from this delegation request.</p> <p>Setting this parameter to true does not guarantee an answer in the response. See the <code>PermissionCheckStatus</code> and the <code>PermissionCheckResult</code> response attributes for further details.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetDelegationRequestRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append(
        (f"{key_prefix}DelegationRequestId", str(value["delegation_request_id"]))
    )
    if "delegation_permission_check" in value:
        pairs.append(
            (
                f"{key_prefix}DelegationPermissionCheck",
                "true" if value["delegation_permission_check"] else "false",
            )
        )


def deserialize_query(el: Element) -> GetDelegationRequestRequest:
    out: GetDelegationRequestRequest = {}  # type: ignore[typeddict-item]
    child_delegation_request_id = el.find("DelegationRequestId")
    if child_delegation_request_id is not None:
        out["delegation_request_id"] = str(child_delegation_request_id.text or "")
    else:
        raise DeserializationError(
            "GetDelegationRequestRequest.delegation_request_id required"
        )
    child_delegation_permission_check = el.find("DelegationPermissionCheck")
    if child_delegation_permission_check is not None:
        out["delegation_permission_check"] = (
            child_delegation_permission_check.text or ""
        ).lower() == "true"
    return out
