"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspaceDirectoriesFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.describe_workspace_directories_filter_name
    import capo_workspaces.types.describe_workspace_directories_filter_values


class DescribeWorkspaceDirectoriesFilter(TypedDict, closed=True):
    name: "capo_workspaces.types.describe_workspace_directories_filter_name.DescribeWorkspaceDirectoriesFilterName"
    """<p>The name of the WorkSpaces to filter.</p>"""
    values: "capo_workspaces.types.describe_workspace_directories_filter_values.DescribeWorkspaceDirectoriesFilterValues"
    """<p>The values for filtering WorkSpaces</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspaceDirectoriesFilter) -> dict:
    out: dict = {}
    import capo_workspaces.types.describe_workspace_directories_filter_name

    out["Name"] = (
        capo_workspaces.types.describe_workspace_directories_filter_name.serialize_aws_json_1_1(
            value["name"]
        )
    )
    import capo_workspaces.types.describe_workspace_directories_filter_values

    out["Values"] = (
        capo_workspaces.types.describe_workspace_directories_filter_values.serialize_aws_json_1_1(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspaceDirectoriesFilter:
    out: DescribeWorkspaceDirectoriesFilter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        import capo_workspaces.types.describe_workspace_directories_filter_name

        out["name"] = (
            capo_workspaces.types.describe_workspace_directories_filter_name.deserialize_aws_json_1_1(
                data["Name"]
            )
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_workspaces.types.describe_workspace_directories_filter_name.DescribeWorkspaceDirectoriesFilterName",
            "",
        )
    if data.get("Values") is not None:
        import capo_workspaces.types.describe_workspace_directories_filter_values

        out["values"] = (
            capo_workspaces.types.describe_workspace_directories_filter_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        out["values"] = []
    return out
