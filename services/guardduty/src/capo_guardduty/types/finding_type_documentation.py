"""Generated from Smithy shape ``com.amazonaws.guardduty#FindingTypeDocumentation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.fetch_learn_more_links
    import capo_guardduty.types.investigation_text
    import capo_guardduty.types.string


class FindingTypeDocumentation(TypedDict, closed=True):
    description: NotRequired[
        "capo_guardduty.types.investigation_text.InvestigationText"
    ]
    """<p>A short description of the finding type.</p>"""
    severity: NotRequired["capo_guardduty.types.string.String"]
    """<p>The severity of the finding type, as stated in the documentation.</p>"""
    feature: NotRequired["capo_guardduty.types.string.String"]
    """<p>The label that the documentation uses for the GuardDuty capability associated with the finding type. This value isn't a detector feature name.</p>"""
    full_description: NotRequired[
        "capo_guardduty.types.investigation_text.InvestigationText"
    ]
    """<p>The full description of the finding type.</p>"""
    remediation: NotRequired[
        "capo_guardduty.types.investigation_text.InvestigationText"
    ]
    """<p>The recommended steps to remediate the finding type.</p>"""
    learn_more_links: NotRequired[
        "capo_guardduty.types.fetch_learn_more_links.FetchLearnMoreLinks"
    ]
    """<p>Links to more information about the finding type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingTypeDocumentation) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "severity" in value:
        out["severity"] = value["severity"]
    if "feature" in value:
        out["feature"] = value["feature"]
    if "full_description" in value:
        out["fullDescription"] = value["full_description"]
    if "remediation" in value:
        out["remediation"] = value["remediation"]
    if "learn_more_links" in value:
        import capo_guardduty.types.fetch_learn_more_links

        out["learnMoreLinks"] = (
            capo_guardduty.types.fetch_learn_more_links.serialize_json(
                value["learn_more_links"]
            )
        )
    return out


def deserialize_json(data: dict) -> FindingTypeDocumentation:
    out: FindingTypeDocumentation = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("severity") is not None:
        out["severity"] = data["severity"]
    if data.get("feature") is not None:
        out["feature"] = data["feature"]
    if data.get("fullDescription") is not None:
        out["full_description"] = data["fullDescription"]
    if data.get("remediation") is not None:
        out["remediation"] = data["remediation"]
    if data.get("learnMoreLinks") is not None:
        import capo_guardduty.types.fetch_learn_more_links

        out["learn_more_links"] = (
            capo_guardduty.types.fetch_learn_more_links.deserialize_json(
                data["learnMoreLinks"]
            )
        )
    return out
