"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ValidatePolicyFinding``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.issue_code
    import capo_accessanalyzer.types.learn_more_link
    import capo_accessanalyzer.types.location_list
    import capo_accessanalyzer.types.validate_policy_finding_type


class ValidatePolicyFinding(TypedDict, closed=True):
    finding_details: "str"
    """<p>A localized message that explains the finding and provides guidance on how to address it.</p>"""
    finding_type: "capo_accessanalyzer.types.validate_policy_finding_type.ValidatePolicyFindingType"
    """<p>The impact of the finding.</p> <p>Security warnings report when the policy allows access that we consider overly permissive.</p> <p>Errors report when a part of the policy is not functional.</p> <p>Warnings report non-security issues when a policy does not conform to policy writing best practices.</p> <p>Suggestions recommend stylistic improvements in the policy that do not impact access.</p>"""
    issue_code: "capo_accessanalyzer.types.issue_code.IssueCode"
    """<p>The issue code provides an identifier of the issue associated with this finding.</p>"""
    learn_more_link: "capo_accessanalyzer.types.learn_more_link.LearnMoreLink"
    """<p>A link to additional documentation about the type of finding.</p>"""
    locations: "capo_accessanalyzer.types.location_list.LocationList"
    """<p>The list of locations in the policy document that are related to the finding. The issue code provides a summary of an issue identified by the finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidatePolicyFinding) -> dict:
    out: dict = {}
    out["findingDetails"] = value["finding_details"]
    out["findingType"] = value["finding_type"]
    out["issueCode"] = value["issue_code"]
    out["learnMoreLink"] = value["learn_more_link"]
    import capo_accessanalyzer.types.location_list

    out["locations"] = capo_accessanalyzer.types.location_list.serialize_json(
        value["locations"]
    )
    return out


def deserialize_json(data: dict) -> ValidatePolicyFinding:
    out: ValidatePolicyFinding = {}  # type: ignore[typeddict-item]
    if data.get("findingDetails") is not None:
        out["finding_details"] = data["findingDetails"]
    else:
        out["finding_details"] = ""
    if data.get("findingType") is not None:
        out["finding_type"] = data["findingType"]
    else:
        out["finding_type"] = ""
    if data.get("issueCode") is not None:
        out["issue_code"] = data["issueCode"]
    else:
        out["issue_code"] = ""
    if data.get("learnMoreLink") is not None:
        out["learn_more_link"] = data["learnMoreLink"]
    else:
        out["learn_more_link"] = ""
    if data.get("locations") is not None:
        import capo_accessanalyzer.types.location_list

        out["locations"] = capo_accessanalyzer.types.location_list.deserialize_json(
            data["locations"]
        )
    else:
        out["locations"] = []
    return out
