"""Generated from Smithy shape ``com.amazonaws.m2#ListApplicationVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_m2.types.application_version_summary_list
    import capo_m2.types.next_token


class ListApplicationVersionsResponse(TypedDict, closed=True):
    application_versions: (
        "capo_m2.types.application_version_summary_list.ApplicationVersionSummaryList"
    )
    """<p>The list of application versions.</p>"""
    next_token: NotRequired["capo_m2.types.next_token.NextToken"]
    """<p>If there are more items to return, this contains a token that is passed to a subsequent call to this operation to retrieve the next set of items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationVersionsResponse) -> dict:
    out: dict = {}
    import capo_m2.types.application_version_summary_list

    out["applicationVersions"] = (
        capo_m2.types.application_version_summary_list.serialize_json(
            value["application_versions"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListApplicationVersionsResponse:
    out: ListApplicationVersionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("applicationVersions") is not None:
        import capo_m2.types.application_version_summary_list

        out["application_versions"] = (
            capo_m2.types.application_version_summary_list.deserialize_json(
                data["applicationVersions"]
            )
        )
    else:
        out["application_versions"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
