"""Generated from Smithy shape ``com.amazonaws.securityagent#ListSecurityRequirementsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.next_token
    import capo_securityagent.types.security_requirement_summary_list


class ListSecurityRequirementsOutput(TypedDict, closed=True):
    security_requirement_summaries: "capo_securityagent.types.security_requirement_summary_list.SecurityRequirementSummaryList"
    """<p>The list of security requirement summaries.</p>"""
    next_token: NotRequired["capo_securityagent.types.next_token.NextToken"]
    """<p>The pagination token to use in a subsequent request to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSecurityRequirementsOutput) -> dict:
    out: dict = {}
    import capo_securityagent.types.security_requirement_summary_list

    out["securityRequirementSummaries"] = (
        capo_securityagent.types.security_requirement_summary_list.serialize_json(
            value["security_requirement_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSecurityRequirementsOutput:
    out: ListSecurityRequirementsOutput = {}  # type: ignore[typeddict-item]
    if data.get("securityRequirementSummaries") is not None:
        import capo_securityagent.types.security_requirement_summary_list

        out["security_requirement_summaries"] = (
            capo_securityagent.types.security_requirement_summary_list.deserialize_json(
                data["securityRequirementSummaries"]
            )
        )
    else:
        out["security_requirement_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
