"""Generated from Smithy shape ``com.amazonaws.iam#SendDelegationTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.delegation_request_id_type


class SendDelegationTokenRequest(TypedDict, closed=True):
    delegation_request_id: (
        "capo_iam.types.delegation_request_id_type.delegationRequestIdType"
    )
    """<p>The unique identifier of the delegation request for which to send the token.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SendDelegationTokenRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append(
        (f"{key_prefix}DelegationRequestId", str(value["delegation_request_id"]))
    )


def deserialize_query(el: Element) -> SendDelegationTokenRequest:
    out: SendDelegationTokenRequest = {}  # type: ignore[typeddict-item]
    child_delegation_request_id = el.find("DelegationRequestId")
    if child_delegation_request_id is not None:
        out["delegation_request_id"] = str(child_delegation_request_id.text or "")
    else:
        out["delegation_request_id"] = ""
    return out
