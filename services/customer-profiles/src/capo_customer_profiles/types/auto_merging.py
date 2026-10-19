"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AutoMerging``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.conflict_resolution
    import capo_customer_profiles.types.consolidation
    import capo_customer_profiles.types.double0_to1
    import capo_customer_profiles.types.optional_boolean


class AutoMerging(TypedDict, closed=True):
    enabled: "capo_customer_profiles.types.optional_boolean.optionalBoolean"
    """<p>The flag that enables the auto-merging of duplicate profiles.</p>"""
    consolidation: NotRequired[
        "capo_customer_profiles.types.consolidation.Consolidation"
    ]
    """<p>A list of matching attributes that represent matching criteria. If two profiles meet at least one of the requirements in the matching attributes list, they will be merged.</p>"""
    conflict_resolution: NotRequired[
        "capo_customer_profiles.types.conflict_resolution.ConflictResolution"
    ]
    """<p>How the auto-merging process should resolve conflicts between different profiles. For example, if Profile A and Profile B have the same <code>FirstName</code> and <code>LastName</code> (and that is the matching criteria), which <code>EmailAddress</code> should be used? </p>"""
    min_allowed_confidence_score_for_merging: NotRequired[
        "capo_customer_profiles.types.double0_to1.Double0To1"
    ]
    """<p>A number between 0 and 1 that represents the minimum confidence score required for profiles within a matching group to be merged during the auto-merge process. A higher score means higher similarity required to merge profiles. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoMerging) -> dict:
    out: dict = {}
    out["Enabled"] = value["enabled"]
    if "consolidation" in value:
        import capo_customer_profiles.types.consolidation

        out["Consolidation"] = (
            capo_customer_profiles.types.consolidation.serialize_json(
                value["consolidation"]
            )
        )
    if "conflict_resolution" in value:
        import capo_customer_profiles.types.conflict_resolution

        out["ConflictResolution"] = (
            capo_customer_profiles.types.conflict_resolution.serialize_json(
                value["conflict_resolution"]
            )
        )
    if "min_allowed_confidence_score_for_merging" in value:
        out["MinAllowedConfidenceScoreForMerging"] = (
            "NaN"
            if value["min_allowed_confidence_score_for_merging"]
            != value["min_allowed_confidence_score_for_merging"]
            else "Infinity"
            if value["min_allowed_confidence_score_for_merging"] == float("inf")
            else "-Infinity"
            if value["min_allowed_confidence_score_for_merging"] == float("-inf")
            else value["min_allowed_confidence_score_for_merging"]
        )
    return out


def deserialize_json(data: dict) -> AutoMerging:
    out: AutoMerging = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    if data.get("Consolidation") is not None:
        import capo_customer_profiles.types.consolidation

        out["consolidation"] = (
            capo_customer_profiles.types.consolidation.deserialize_json(
                data["Consolidation"]
            )
        )
    if data.get("ConflictResolution") is not None:
        import capo_customer_profiles.types.conflict_resolution

        out["conflict_resolution"] = (
            capo_customer_profiles.types.conflict_resolution.deserialize_json(
                data["ConflictResolution"]
            )
        )
    if data.get("MinAllowedConfidenceScoreForMerging") is not None:
        out["min_allowed_confidence_score_for_merging"] = float(
            data["MinAllowedConfidenceScoreForMerging"]
        )
    return out
