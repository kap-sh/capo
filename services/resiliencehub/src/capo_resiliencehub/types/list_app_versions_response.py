"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListAppVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.app_version_list
    import capo_resiliencehub.types.next_token


class ListAppVersionsResponse(TypedDict, closed=True):
    app_versions: "capo_resiliencehub.types.app_version_list.AppVersionList"
    """<p>The version of the application.</p>"""
    next_token: NotRequired["capo_resiliencehub.types.next_token.NextToken"]
    """<p>Token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppVersionsResponse) -> dict:
    out: dict = {}
    import capo_resiliencehub.types.app_version_list

    out["appVersions"] = capo_resiliencehub.types.app_version_list.serialize_json(
        value["app_versions"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAppVersionsResponse:
    out: ListAppVersionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("appVersions") is not None:
        import capo_resiliencehub.types.app_version_list

        out["app_versions"] = (
            capo_resiliencehub.types.app_version_list.deserialize_json(
                data["appVersions"]
            )
        )
    else:
        out["app_versions"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
