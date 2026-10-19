"""Generated from Smithy shape ``com.amazonaws.auditmanager#BatchDeleteDelegationByAssessmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.delegation_ids
    import capo_auditmanager.types.uuid


class BatchDeleteDelegationByAssessmentRequest(TypedDict, closed=True):
    delegation_ids: "capo_auditmanager.types.delegation_ids.DelegationIds"
    """<p> The identifiers for the delegations. </p>"""
    assessment_id: "capo_auditmanager.types.uuid.UUID"
    """<p> The identifier for the assessment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteDelegationByAssessmentRequest) -> dict:
    out: dict = {}
    import capo_auditmanager.types.delegation_ids

    out["delegationIds"] = capo_auditmanager.types.delegation_ids.serialize_json(
        value["delegation_ids"]
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteDelegationByAssessmentRequest:
    out: BatchDeleteDelegationByAssessmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("delegationIds") is not None:
        import capo_auditmanager.types.delegation_ids

        out["delegation_ids"] = capo_auditmanager.types.delegation_ids.deserialize_json(
            data["delegationIds"]
        )
    else:
        out["delegation_ids"] = []
    return out
