"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspaceBundlesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.bundle_list
    import capo_workspaces.types.pagination_token


class DescribeWorkspaceBundlesResult(TypedDict, closed=True):
    bundles: NotRequired["capo_workspaces.types.bundle_list.BundleList"]
    """<p>Information about the bundles.</p>"""
    next_token: NotRequired["capo_workspaces.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return. This token is valid for one day and must be used within that time frame.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspaceBundlesResult) -> dict:
    out: dict = {}
    if "bundles" in value:
        import capo_workspaces.types.bundle_list

        out["Bundles"] = capo_workspaces.types.bundle_list.serialize_aws_json_1_1(
            value["bundles"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspaceBundlesResult:
    out: DescribeWorkspaceBundlesResult = {}  # type: ignore[typeddict-item]
    if data.get("Bundles") is not None:
        import capo_workspaces.types.bundle_list

        out["bundles"] = capo_workspaces.types.bundle_list.deserialize_aws_json_1_1(
            data["Bundles"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeWorkspaceBundlesResult) -> dict:
    out: dict = {}
    if "bundles" in value:
        import capo_workspaces.types.bundle_list

        out["Bundles"] = capo_workspaces.types.bundle_list.serialize_cbor(
            value["bundles"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeWorkspaceBundlesResult:
    out: DescribeWorkspaceBundlesResult = {}  # type: ignore[typeddict-item]
    if data.get("Bundles") is not None:
        import capo_workspaces.types.bundle_list

        out["bundles"] = capo_workspaces.types.bundle_list.deserialize_cbor(
            data["Bundles"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
