"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ListPagesByContactResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.pages_list
    import capo_ssm_contacts.types.pagination_token


class ListPagesByContactResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ssm_contacts.types.pagination_token.PaginationToken"]
    """<p>The pagination token to continue to the next page of results.</p>"""
    pages: "capo_ssm_contacts.types.pages_list.PagesList"
    """<p>The list of engagements to a contact's contact channel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPagesByContactResult) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_ssm_contacts.types.pages_list

    out["Pages"] = capo_ssm_contacts.types.pages_list.serialize_aws_json_1_1(
        value["pages"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPagesByContactResult:
    out: ListPagesByContactResult = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Pages") is not None:
        import capo_ssm_contacts.types.pages_list

        out["pages"] = capo_ssm_contacts.types.pages_list.deserialize_aws_json_1_1(
            data["Pages"]
        )
    else:
        out["pages"] = []
    return out
