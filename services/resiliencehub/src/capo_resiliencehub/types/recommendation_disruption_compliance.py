"""Generated from Smithy shape ``com.amazonaws.resiliencehub#RecommendationDisruptionCompliance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.compliance_status
    import capo_resiliencehub.types.seconds
    import capo_resiliencehub.types.string500


class RecommendationDisruptionCompliance(TypedDict, closed=True):
    expected_compliance_status: (
        "capo_resiliencehub.types.compliance_status.ComplianceStatus"
    )
    """<p>The expected compliance status after applying the recommended configuration change.</p>"""
    expected_rto_in_secs: "capo_resiliencehub.types.seconds.Seconds"
    """<p>The expected RTO after applying the recommended configuration change.</p>"""
    expected_rto_description: NotRequired[
        "capo_resiliencehub.types.string500.String500"
    ]
    """<p>The expected Recovery Time Objective (RTO) description after applying the recommended configuration change.</p>"""
    expected_rpo_in_secs: "capo_resiliencehub.types.seconds.Seconds"
    """<p>The expected RPO after applying the recommended configuration change.</p>"""
    expected_rpo_description: NotRequired[
        "capo_resiliencehub.types.string500.String500"
    ]
    """<p>The expected Recovery Point Objective (RPO) description after applying the recommended configuration change.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationDisruptionCompliance) -> dict:
    out: dict = {}
    import capo_resiliencehub.types.compliance_status

    out["expectedComplianceStatus"] = (
        capo_resiliencehub.types.compliance_status.serialize_json(
            value["expected_compliance_status"]
        )
    )
    out["expectedRtoInSecs"] = value.get("expected_rto_in_secs", 0)
    if "expected_rto_description" in value:
        out["expectedRtoDescription"] = value["expected_rto_description"]
    out["expectedRpoInSecs"] = value.get("expected_rpo_in_secs", 0)
    if "expected_rpo_description" in value:
        out["expectedRpoDescription"] = value["expected_rpo_description"]
    return out


def deserialize_json(data: dict) -> RecommendationDisruptionCompliance:
    out: RecommendationDisruptionCompliance = {}  # type: ignore[typeddict-item]
    if data.get("expectedComplianceStatus") is not None:
        import capo_resiliencehub.types.compliance_status

        out["expected_compliance_status"] = (
            capo_resiliencehub.types.compliance_status.deserialize_json(
                data["expectedComplianceStatus"]
            )
        )
    else:
        import typing

        out["expected_compliance_status"] = typing.cast(
            "capo_resiliencehub.types.compliance_status.ComplianceStatus", ""
        )
    if data.get("expectedRtoInSecs") is not None:
        out["expected_rto_in_secs"] = data["expectedRtoInSecs"]
    else:
        out["expected_rto_in_secs"] = 0
    if data.get("expectedRtoDescription") is not None:
        out["expected_rto_description"] = data["expectedRtoDescription"]
    if data.get("expectedRpoInSecs") is not None:
        out["expected_rpo_in_secs"] = data["expectedRpoInSecs"]
    else:
        out["expected_rpo_in_secs"] = 0
    if data.get("expectedRpoDescription") is not None:
        out["expected_rpo_description"] = data["expectedRpoDescription"]
    return out
