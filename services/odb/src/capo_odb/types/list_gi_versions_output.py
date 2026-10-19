"""Generated from Smithy shape ``com.amazonaws.odb#ListGiVersionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.gi_version_list


class ListGiVersionsOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    gi_versions: "capo_odb.types.gi_version_list.GiVersionList"
    """<p>The list of GI versions and their properties.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListGiVersionsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_odb.types.gi_version_list

    out["giVersions"] = capo_odb.types.gi_version_list.serialize_aws_json_1_0(
        value["gi_versions"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListGiVersionsOutput:
    out: ListGiVersionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("giVersions") is not None:
        import capo_odb.types.gi_version_list

        out["gi_versions"] = capo_odb.types.gi_version_list.deserialize_aws_json_1_0(
            data["giVersions"]
        )
    else:
        out["gi_versions"] = []
    return out
