"""Generated from Smithy shape ``com.amazonaws.securityhub#RemediationGuidanceMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.remediation_string_list
    import capo_securityhub.types.timestamp


class RemediationGuidanceMetadata(TypedDict, closed=True):
    resource_type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The resource type of the remediation target.</p>"""
    exposure_type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The exposure type of the related exposure findings.</p>"""
    trait_titles: NotRequired[
        "capo_securityhub.types.remediation_string_list.RemediationStringList"
    ]
    """<p>The titles of traits this guidance applies to.</p>"""
    reversibility: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The extent to which changes made in accordance with the guidance can be reversed, for example <code>Fully reversible</code>.</p>"""
    fix_effect: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>When the fix takes effect, for example <code>Immediate</code> or <code>Deferred</code>.</p>"""
    risk_level: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The risk when implementing the guidance provided.</p>"""
    automation_level: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The extent to which the guidance can be automated, for example <code>Full</code>.</p>"""
    human_review_required: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Specifies whether human review is required.</p>"""
    generated_at: NotRequired["capo_securityhub.types.timestamp.Timestamp"]
    """<p>Timestamp of when the guidance was generated.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    verification_status: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Verification status of the guidance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemediationGuidanceMetadata) -> dict:
    out: dict = {}
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "exposure_type" in value:
        out["ExposureType"] = value["exposure_type"]
    if "trait_titles" in value:
        import capo_securityhub.types.remediation_string_list

        out["TraitTitles"] = (
            capo_securityhub.types.remediation_string_list.serialize_json(
                value["trait_titles"]
            )
        )
    if "reversibility" in value:
        out["Reversibility"] = value["reversibility"]
    if "fix_effect" in value:
        out["FixEffect"] = value["fix_effect"]
    if "risk_level" in value:
        out["RiskLevel"] = value["risk_level"]
    if "automation_level" in value:
        out["AutomationLevel"] = value["automation_level"]
    if "human_review_required" in value:
        out["HumanReviewRequired"] = value["human_review_required"]
    if "generated_at" in value:
        import capo_securityhub.types.timestamp

        out["GeneratedAt"] = capo_securityhub.types.timestamp.serialize_json(
            value["generated_at"]
        )
    if "verification_status" in value:
        out["VerificationStatus"] = value["verification_status"]
    return out


def deserialize_json(data: dict) -> RemediationGuidanceMetadata:
    out: RemediationGuidanceMetadata = {}  # type: ignore[typeddict-item]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("ExposureType") is not None:
        out["exposure_type"] = data["ExposureType"]
    if data.get("TraitTitles") is not None:
        import capo_securityhub.types.remediation_string_list

        out["trait_titles"] = (
            capo_securityhub.types.remediation_string_list.deserialize_json(
                data["TraitTitles"]
            )
        )
    if data.get("Reversibility") is not None:
        out["reversibility"] = data["Reversibility"]
    if data.get("FixEffect") is not None:
        out["fix_effect"] = data["FixEffect"]
    if data.get("RiskLevel") is not None:
        out["risk_level"] = data["RiskLevel"]
    if data.get("AutomationLevel") is not None:
        out["automation_level"] = data["AutomationLevel"]
    if data.get("HumanReviewRequired") is not None:
        out["human_review_required"] = data["HumanReviewRequired"]
    if data.get("GeneratedAt") is not None:
        import capo_securityhub.types.timestamp

        out["generated_at"] = capo_securityhub.types.timestamp.deserialize_json(
            data["GeneratedAt"]
        )
    if data.get("VerificationStatus") is not None:
        out["verification_status"] = data["VerificationStatus"]
    return out
