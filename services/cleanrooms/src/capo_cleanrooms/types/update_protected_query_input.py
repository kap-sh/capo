"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateProtectedQueryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.protected_query_identifier
    import capo_cleanrooms.types.target_protected_query_status


class UpdateProtectedQueryInput(TypedDict, closed=True):
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The identifier for a member of a protected query instance.</p>"""
    protected_query_identifier: (
        "capo_cleanrooms.types.protected_query_identifier.ProtectedQueryIdentifier"
    )
    """<p>The identifier for a protected query instance.</p>"""
    target_status: (
        "capo_cleanrooms.types.target_protected_query_status.TargetProtectedQueryStatus"
    )
    """<p>The target status of a query. Used to update the execution status of a currently running query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProtectedQueryInput) -> dict:
    out: dict = {}
    out["targetStatus"] = value["target_status"]
    return out


def deserialize_json(data: dict) -> UpdateProtectedQueryInput:
    out: UpdateProtectedQueryInput = {}  # type: ignore[typeddict-item]
    if data.get("targetStatus") is not None:
        out["target_status"] = data["targetStatus"]
    else:
        out["target_status"] = ""
    return out
