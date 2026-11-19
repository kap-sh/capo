"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeApplicationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.pagination_token
    import capo_workspaces.types.work_space_application_list


class DescribeApplicationsResult(TypedDict, closed=True):
    applications: NotRequired[
        "capo_workspaces.types.work_space_application_list.WorkSpaceApplicationList"
    ]
    """<p>List of information about the specified applications.</p>"""
    next_token: NotRequired["capo_workspaces.types.pagination_token.PaginationToken"]
    """<p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApplicationsResult) -> dict:
    out: dict = {}
    if "applications" in value:
        import capo_workspaces.types.work_space_application_list

        out["Applications"] = (
            capo_workspaces.types.work_space_application_list.serialize_aws_json_1_1(
                value["applications"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApplicationsResult:
    out: DescribeApplicationsResult = {}  # type: ignore[typeddict-item]
    if data.get("Applications") is not None:
        import capo_workspaces.types.work_space_application_list

        out["applications"] = (
            capo_workspaces.types.work_space_application_list.deserialize_aws_json_1_1(
                data["Applications"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeApplicationsResult) -> dict:
    out: dict = {}
    if "applications" in value:
        import capo_workspaces.types.work_space_application_list

        out["Applications"] = (
            capo_workspaces.types.work_space_application_list.serialize_cbor(
                value["applications"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeApplicationsResult:
    out: DescribeApplicationsResult = {}  # type: ignore[typeddict-item]
    if data.get("Applications") is not None:
        import capo_workspaces.types.work_space_application_list

        out["applications"] = (
            capo_workspaces.types.work_space_application_list.deserialize_cbor(
                data["Applications"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
