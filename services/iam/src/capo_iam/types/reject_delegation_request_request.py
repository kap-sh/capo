"""Generated from Smithy shape ``com.amazonaws.iam#RejectDelegationRequestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.delegation_request_id_type
    import capo_iam.types.notes_type


class RejectDelegationRequestRequest(TypedDict, closed=True):
    delegation_request_id: (
        "capo_iam.types.delegation_request_id_type.delegationRequestIdType"
    )
    """<p>The unique identifier of the delegation request to reject.</p>"""
    notes: NotRequired["capo_iam.types.notes_type.notesType"]
    """<p>Optional notes explaining the reason for rejecting the delegation request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RejectDelegationRequestRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append(
        (f"{key_prefix}DelegationRequestId", str(value["delegation_request_id"]))
    )
    if "notes" in value:
        pairs.append((f"{key_prefix}Notes", str(value["notes"])))


def deserialize_query(el: Element) -> RejectDelegationRequestRequest:
    out: RejectDelegationRequestRequest = {}  # type: ignore[typeddict-item]
    child_delegation_request_id = el.find("DelegationRequestId")
    if child_delegation_request_id is not None:
        out["delegation_request_id"] = str(child_delegation_request_id.text or "")
    else:
        out["delegation_request_id"] = ""
    child_notes = el.find("Notes")
    if child_notes is not None:
        out["notes"] = str(child_notes.text or "")
    return out
