"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ListEngagementsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.engagements_list
    import capo_ssm_contacts.types.pagination_token


class ListEngagementsResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ssm_contacts.types.pagination_token.PaginationToken"]
    """<p>The pagination token to continue to the next page of results.</p>"""
    engagements: "capo_ssm_contacts.types.engagements_list.EngagementsList"
    """<p>A list of each engagement that occurred during the specified time range of an incident.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEngagementsResult) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_ssm_contacts.types.engagements_list

    out["Engagements"] = (
        capo_ssm_contacts.types.engagements_list.serialize_aws_json_1_1(
            value["engagements"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEngagementsResult:
    out: ListEngagementsResult = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Engagements") is not None:
        import capo_ssm_contacts.types.engagements_list

        out["engagements"] = (
            capo_ssm_contacts.types.engagements_list.deserialize_aws_json_1_1(
                data["Engagements"]
            )
        )
    else:
        out["engagements"] = []
    return out
