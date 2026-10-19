"""Generated from Smithy shape ``com.amazonaws.m2#ListEngineVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_m2.types.engine_versions_summary_list
    import capo_m2.types.next_token


class ListEngineVersionsResponse(TypedDict, closed=True):
    engine_versions: (
        "capo_m2.types.engine_versions_summary_list.EngineVersionsSummaryList"
    )
    """<p>Returns the engine versions.</p>"""
    next_token: NotRequired["capo_m2.types.next_token.NextToken"]
    """<p>If there are more items to return, this contains a token that is passed to a subsequent call to this operation to retrieve the next set of items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEngineVersionsResponse) -> dict:
    out: dict = {}
    import capo_m2.types.engine_versions_summary_list

    out["engineVersions"] = capo_m2.types.engine_versions_summary_list.serialize_json(
        value["engine_versions"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEngineVersionsResponse:
    out: ListEngineVersionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("engineVersions") is not None:
        import capo_m2.types.engine_versions_summary_list

        out["engine_versions"] = (
            capo_m2.types.engine_versions_summary_list.deserialize_json(
                data["engineVersions"]
            )
        )
    else:
        out["engine_versions"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
