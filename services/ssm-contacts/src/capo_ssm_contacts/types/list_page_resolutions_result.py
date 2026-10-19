"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ListPageResolutionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.pagination_token
    import capo_ssm_contacts.types.resolution_list


class ListPageResolutionsResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ssm_contacts.types.pagination_token.PaginationToken"]
    """<p>The token for the next set of items to return. Use this token to get the next set of results.</p>"""
    page_resolutions: "capo_ssm_contacts.types.resolution_list.ResolutionList"
    """<p>Information about the resolution for an engagement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPageResolutionsResult) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_ssm_contacts.types.resolution_list

    out["PageResolutions"] = (
        capo_ssm_contacts.types.resolution_list.serialize_aws_json_1_1(
            value["page_resolutions"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPageResolutionsResult:
    out: ListPageResolutionsResult = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("PageResolutions") is not None:
        import capo_ssm_contacts.types.resolution_list

        out["page_resolutions"] = (
            capo_ssm_contacts.types.resolution_list.deserialize_aws_json_1_1(
                data["PageResolutions"]
            )
        )
    else:
        out["page_resolutions"] = []
    return out
