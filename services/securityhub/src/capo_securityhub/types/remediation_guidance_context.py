"""Generated from Smithy shape ``com.amazonaws.securityhub#RemediationGuidanceContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.remediation_string_list


class RemediationGuidanceContext(TypedDict, closed=True):
    problem_statement: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Explains the cause which directly created the remediation target.</p>"""
    risk_assessment: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>An assessment of the existing risk the remediation target creates.</p>"""
    affected_scope: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The scope of the resources affected by the resolution of the remediation target.</p>"""
    prerequisites: NotRequired[
        "capo_securityhub.types.remediation_string_list.RemediationStringList"
    ]
    """<p>An array of prerequisite steps in resolving the remediation target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemediationGuidanceContext) -> dict:
    out: dict = {}
    if "problem_statement" in value:
        out["ProblemStatement"] = value["problem_statement"]
    if "risk_assessment" in value:
        out["RiskAssessment"] = value["risk_assessment"]
    if "affected_scope" in value:
        out["AffectedScope"] = value["affected_scope"]
    if "prerequisites" in value:
        import capo_securityhub.types.remediation_string_list

        out["Prerequisites"] = (
            capo_securityhub.types.remediation_string_list.serialize_json(
                value["prerequisites"]
            )
        )
    return out


def deserialize_json(data: dict) -> RemediationGuidanceContext:
    out: RemediationGuidanceContext = {}  # type: ignore[typeddict-item]
    if data.get("ProblemStatement") is not None:
        out["problem_statement"] = data["ProblemStatement"]
    if data.get("RiskAssessment") is not None:
        out["risk_assessment"] = data["RiskAssessment"]
    if data.get("AffectedScope") is not None:
        out["affected_scope"] = data["AffectedScope"]
    if data.get("Prerequisites") is not None:
        import capo_securityhub.types.remediation_string_list

        out["prerequisites"] = (
            capo_securityhub.types.remediation_string_list.deserialize_json(
                data["Prerequisites"]
            )
        )
    return out
