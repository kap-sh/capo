"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateProtectedJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.protected_job_identifier
    import capo_cleanrooms.types.target_protected_job_status


class UpdateProtectedJobInput(TypedDict, closed=True):
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The identifier for a member of a protected job instance.</p>"""
    protected_job_identifier: (
        "capo_cleanrooms.types.protected_job_identifier.ProtectedJobIdentifier"
    )
    """<p> The identifier of the protected job to update.</p>"""
    target_status: (
        "capo_cleanrooms.types.target_protected_job_status.TargetProtectedJobStatus"
    )
    """<p>The target status of a protected job. Used to update the execution status of a currently running job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProtectedJobInput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.target_protected_job_status

    out["targetStatus"] = (
        capo_cleanrooms.types.target_protected_job_status.serialize_json(
            value["target_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateProtectedJobInput:
    out: UpdateProtectedJobInput = {}  # type: ignore[typeddict-item]
    if data.get("targetStatus") is not None:
        import capo_cleanrooms.types.target_protected_job_status

        out["target_status"] = (
            capo_cleanrooms.types.target_protected_job_status.deserialize_json(
                data["targetStatus"]
            )
        )
    else:
        import typing

        out["target_status"] = typing.cast(
            "capo_cleanrooms.types.target_protected_job_status.TargetProtectedJobStatus",
            "",
        )
    return out
