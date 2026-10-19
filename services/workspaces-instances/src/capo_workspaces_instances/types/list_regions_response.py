"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ListRegionsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.next_token
    import capo_workspaces_instances.types.region_list


class ListRegionsResponse(TypedDict, closed=True):
    regions: "capo_workspaces_instances.types.region_list.RegionList"
    """<p>Collection of AWS regions supported by WorkSpaces Instances.</p>"""
    next_token: NotRequired["capo_workspaces_instances.types.next_token.NextToken"]
    """<p>Token for retrieving additional regions if the result set is paginated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRegionsResponse) -> dict:
    out: dict = {}
    import capo_workspaces_instances.types.region_list

    out["Regions"] = capo_workspaces_instances.types.region_list.serialize_aws_json_1_0(
        value["regions"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRegionsResponse:
    out: ListRegionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Regions") is not None:
        import capo_workspaces_instances.types.region_list

        out["regions"] = (
            capo_workspaces_instances.types.region_list.deserialize_aws_json_1_0(
                data["Regions"]
            )
        )
    else:
        out["regions"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListRegionsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
