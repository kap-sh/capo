"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspaceBundlesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.bundle_id_list
    import capo_workspaces.types.bundle_owner
    import capo_workspaces.types.pagination_token


class DescribeWorkspaceBundlesRequest(TypedDict, closed=True):
    bundle_ids: NotRequired["capo_workspaces.types.bundle_id_list.BundleIdList"]
    """<p>The identifiers of the bundles. You cannot combine this parameter with any other filter.</p>"""
    owner: NotRequired["capo_workspaces.types.bundle_owner.BundleOwner"]
    """<p>The owner of the bundles. You cannot combine this parameter with any other filter.</p> <p>To describe the bundles provided by Amazon Web Services, specify <code>AMAZON</code>. To describe the bundles that belong to your account, don't specify a value.</p>"""
    next_token: NotRequired["capo_workspaces.types.pagination_token.PaginationToken"]
    """<p>The token for the next set of results. (You received this token from a previous call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspaceBundlesRequest) -> dict:
    out: dict = {}
    if "bundle_ids" in value:
        import capo_workspaces.types.bundle_id_list

        out["BundleIds"] = capo_workspaces.types.bundle_id_list.serialize_aws_json_1_1(
            value["bundle_ids"]
        )
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspaceBundlesRequest:
    out: DescribeWorkspaceBundlesRequest = {}  # type: ignore[typeddict-item]
    if data.get("BundleIds") is not None:
        import capo_workspaces.types.bundle_id_list

        out["bundle_ids"] = (
            capo_workspaces.types.bundle_id_list.deserialize_aws_json_1_1(
                data["BundleIds"]
            )
        )
    if data.get("Owner") is not None:
        out["owner"] = data["Owner"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeWorkspaceBundlesRequest) -> dict:
    out: dict = {}
    if "bundle_ids" in value:
        import capo_workspaces.types.bundle_id_list

        out["BundleIds"] = capo_workspaces.types.bundle_id_list.serialize_cbor(
            value["bundle_ids"]
        )
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeWorkspaceBundlesRequest:
    out: DescribeWorkspaceBundlesRequest = {}  # type: ignore[typeddict-item]
    if data.get("BundleIds") is not None:
        import capo_workspaces.types.bundle_id_list

        out["bundle_ids"] = capo_workspaces.types.bundle_id_list.deserialize_cbor(
            data["BundleIds"]
        )
    if data.get("Owner") is not None:
        out["owner"] = data["Owner"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
