"""Generated from Smithy shape ``com.amazonaws.odb#ListGiMinorVersionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.gi_minor_version_list


class ListGiMinorVersionsOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    gi_minor_versions: "capo_odb.types.gi_minor_version_list.GiMinorVersionList"
    """<p>The list of GI minor versions.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListGiMinorVersionsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_odb.types.gi_minor_version_list

    out["giMinorVersions"] = (
        capo_odb.types.gi_minor_version_list.serialize_aws_json_1_0(
            value["gi_minor_versions"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListGiMinorVersionsOutput:
    out: ListGiMinorVersionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("giMinorVersions") is not None:
        import capo_odb.types.gi_minor_version_list

        out["gi_minor_versions"] = (
            capo_odb.types.gi_minor_version_list.deserialize_aws_json_1_0(
                data["giMinorVersions"]
            )
        )
    else:
        out["gi_minor_versions"] = []
    return out
