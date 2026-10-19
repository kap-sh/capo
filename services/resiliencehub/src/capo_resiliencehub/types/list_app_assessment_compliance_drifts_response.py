"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListAppAssessmentComplianceDriftsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.compliance_drift_list
    import capo_resiliencehub.types.next_token


class ListAppAssessmentComplianceDriftsResponse(TypedDict, closed=True):
    compliance_drifts: (
        "capo_resiliencehub.types.compliance_drift_list.ComplianceDriftList"
    )
    """<p>Indicates compliance drifts (recovery time objective (RTO) and recovery point objective (RPO)) detected for an assessed entity.</p>"""
    next_token: NotRequired["capo_resiliencehub.types.next_token.NextToken"]
    """<p>Null, or the token from a previous call to get the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppAssessmentComplianceDriftsResponse) -> dict:
    out: dict = {}
    import capo_resiliencehub.types.compliance_drift_list

    out["complianceDrifts"] = (
        capo_resiliencehub.types.compliance_drift_list.serialize_json(
            value["compliance_drifts"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAppAssessmentComplianceDriftsResponse:
    out: ListAppAssessmentComplianceDriftsResponse = {}  # type: ignore[typeddict-item]
    if data.get("complianceDrifts") is not None:
        import capo_resiliencehub.types.compliance_drift_list

        out["compliance_drifts"] = (
            capo_resiliencehub.types.compliance_drift_list.deserialize_json(
                data["complianceDrifts"]
            )
        )
    else:
        out["compliance_drifts"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
