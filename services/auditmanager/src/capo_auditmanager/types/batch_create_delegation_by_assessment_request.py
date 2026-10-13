"""Generated from Smithy shape ``com.amazonaws.auditmanager#BatchCreateDelegationByAssessmentRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_auditmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_auditmanager.types.create_delegation_requests
    import capo_auditmanager.types.uuid


class BatchCreateDelegationByAssessmentRequest(TypedDict, closed=True):
    create_delegation_requests: (
        "capo_auditmanager.types.create_delegation_requests.CreateDelegationRequests"
    )
    """<p> The API request to batch create delegations in Audit Manager. </p>"""
    assessment_id: "capo_auditmanager.types.uuid.UUID"
    """<p> The identifier for the assessment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateDelegationByAssessmentRequest) -> dict:
    out: dict = {}
    import capo_auditmanager.types.create_delegation_requests

    out["createDelegationRequests"] = (
        capo_auditmanager.types.create_delegation_requests.serialize_json(
            value["create_delegation_requests"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchCreateDelegationByAssessmentRequest:
    out: BatchCreateDelegationByAssessmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("createDelegationRequests") is not None:
        import capo_auditmanager.types.create_delegation_requests

        out["create_delegation_requests"] = (
            capo_auditmanager.types.create_delegation_requests.deserialize_json(
                data["createDelegationRequests"]
            )
        )
    else:
        raise DeserializationError(
            "BatchCreateDelegationByAssessmentRequest.create_delegation_requests required"
        )
    return out


def redact_sensitive(value: BatchCreateDelegationByAssessmentRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "create_delegation_requests" in value:
        out["create_delegation_requests"] = "*** Sensitive Data Redacted ***"
    return out
