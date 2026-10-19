"""Generated from Smithy shape ``com.amazonaws.odb#ListSystemVersionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.system_version_list


class ListSystemVersionsOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    system_versions: "capo_odb.types.system_version_list.SystemVersionList"
    """<p>The list of system versions.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListSystemVersionsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_odb.types.system_version_list

    out["systemVersions"] = capo_odb.types.system_version_list.serialize_aws_json_1_0(
        value["system_versions"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListSystemVersionsOutput:
    out: ListSystemVersionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("systemVersions") is not None:
        import capo_odb.types.system_version_list

        out["system_versions"] = (
            capo_odb.types.system_version_list.deserialize_aws_json_1_0(
                data["systemVersions"]
            )
        )
    else:
        out["system_versions"] = []
    return out
