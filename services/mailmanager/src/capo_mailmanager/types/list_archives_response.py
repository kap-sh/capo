"""Generated from Smithy shape ``com.amazonaws.mailmanager#ListArchivesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.archives_list
    import capo_mailmanager.types.pagination_token


class ListArchivesResponse(TypedDict, closed=True):
    archives: "capo_mailmanager.types.archives_list.ArchivesList"
    """<p>The list of archive details.</p>"""
    next_token: NotRequired["capo_mailmanager.types.pagination_token.PaginationToken"]
    """<p>If present, use to retrieve the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListArchivesResponse) -> dict:
    out: dict = {}
    import capo_mailmanager.types.archives_list

    out["Archives"] = capo_mailmanager.types.archives_list.serialize_aws_json_1_0(
        value["archives"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListArchivesResponse:
    out: ListArchivesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Archives") is not None:
        import capo_mailmanager.types.archives_list

        out["archives"] = capo_mailmanager.types.archives_list.deserialize_aws_json_1_0(
            data["Archives"]
        )
    else:
        out["archives"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
