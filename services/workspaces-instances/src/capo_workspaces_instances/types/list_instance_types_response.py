"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ListInstanceTypesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.instance_types
    import capo_workspaces_instances.types.next_token


class ListInstanceTypesResponse(TypedDict, closed=True):
    instance_types: "capo_workspaces_instances.types.instance_types.InstanceTypes"
    """<p>Collection of supported instance types for WorkSpaces Instances.</p>"""
    next_token: NotRequired["capo_workspaces_instances.types.next_token.NextToken"]
    """<p>Token for retrieving additional instance types if the result set is paginated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListInstanceTypesResponse) -> dict:
    out: dict = {}
    import capo_workspaces_instances.types.instance_types

    out["InstanceTypes"] = (
        capo_workspaces_instances.types.instance_types.serialize_aws_json_1_0(
            value["instance_types"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListInstanceTypesResponse:
    out: ListInstanceTypesResponse = {}  # type: ignore[typeddict-item]
    if data.get("InstanceTypes") is not None:
        import capo_workspaces_instances.types.instance_types

        out["instance_types"] = (
            capo_workspaces_instances.types.instance_types.deserialize_aws_json_1_0(
                data["InstanceTypes"]
            )
        )
    else:
        out["instance_types"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListInstanceTypesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
