"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspacesPoolsFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.describe_workspaces_pools_filter_name
    import capo_workspaces.types.describe_workspaces_pools_filter_operator
    import capo_workspaces.types.describe_workspaces_pools_filter_values


class DescribeWorkspacesPoolsFilter(TypedDict, closed=True):
    name: "capo_workspaces.types.describe_workspaces_pools_filter_name.DescribeWorkspacesPoolsFilterName"
    """<p>The name of the pool to filter.</p>"""
    values: "capo_workspaces.types.describe_workspaces_pools_filter_values.DescribeWorkspacesPoolsFilterValues"
    """<p>The values for filtering WorkSpaces Pools.</p>"""
    operator: "capo_workspaces.types.describe_workspaces_pools_filter_operator.DescribeWorkspacesPoolsFilterOperator"
    """<p>The operator values for filtering WorkSpaces Pools.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspacesPoolsFilter) -> dict:
    out: dict = {}
    import capo_workspaces.types.describe_workspaces_pools_filter_name

    out["Name"] = (
        capo_workspaces.types.describe_workspaces_pools_filter_name.serialize_aws_json_1_1(
            value["name"]
        )
    )
    import capo_workspaces.types.describe_workspaces_pools_filter_values

    out["Values"] = (
        capo_workspaces.types.describe_workspaces_pools_filter_values.serialize_aws_json_1_1(
            value["values"]
        )
    )
    import capo_workspaces.types.describe_workspaces_pools_filter_operator

    out["Operator"] = (
        capo_workspaces.types.describe_workspaces_pools_filter_operator.serialize_aws_json_1_1(
            value["operator"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspacesPoolsFilter:
    out: DescribeWorkspacesPoolsFilter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        import capo_workspaces.types.describe_workspaces_pools_filter_name

        out["name"] = (
            capo_workspaces.types.describe_workspaces_pools_filter_name.deserialize_aws_json_1_1(
                data["Name"]
            )
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_workspaces.types.describe_workspaces_pools_filter_name.DescribeWorkspacesPoolsFilterName",
            "",
        )
    if data.get("Values") is not None:
        import capo_workspaces.types.describe_workspaces_pools_filter_values

        out["values"] = (
            capo_workspaces.types.describe_workspaces_pools_filter_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        out["values"] = []
    if data.get("Operator") is not None:
        import capo_workspaces.types.describe_workspaces_pools_filter_operator

        out["operator"] = (
            capo_workspaces.types.describe_workspaces_pools_filter_operator.deserialize_aws_json_1_1(
                data["Operator"]
            )
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_workspaces.types.describe_workspaces_pools_filter_operator.DescribeWorkspacesPoolsFilterOperator",
            "",
        )
    return out
