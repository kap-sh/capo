"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListDirectoriesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.directory_list
    import capo_clouddirectory.types.next_token


class ListDirectoriesResponse(TypedDict, closed=True):
    directories: "capo_clouddirectory.types.directory_list.DirectoryList"
    """<p>Lists all directories that are associated with your account in pagination fashion.</p>"""
    next_token: NotRequired["capo_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDirectoriesResponse) -> dict:
    out: dict = {}
    import capo_clouddirectory.types.directory_list

    out["Directories"] = capo_clouddirectory.types.directory_list.serialize_json(
        value["directories"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDirectoriesResponse:
    out: ListDirectoriesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Directories") is not None:
        import capo_clouddirectory.types.directory_list

        out["directories"] = capo_clouddirectory.types.directory_list.deserialize_json(
            data["Directories"]
        )
    else:
        out["directories"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
