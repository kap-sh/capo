"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeImagePermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.aws_account_id_list
    import capo_appstream.types.max_results
    import capo_appstream.types.name
    import capo_appstream.types.string


class DescribeImagePermissionsRequest(TypedDict, closed=True):
    name: NotRequired["capo_appstream.types.name.Name"]
    """<p>The name of the private image for which to describe permissions. The image must be one that you own. </p>"""
    max_results: NotRequired["capo_appstream.types.max_results.MaxResults"]
    """<p>The maximum size of each page of results.</p>"""
    shared_aws_account_ids: NotRequired[
        "capo_appstream.types.aws_account_id_list.AwsAccountIdList"
    ]
    """<p>The 12-digit identifier of one or more AWS accounts with which the image is shared.</p>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImagePermissionsRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "shared_aws_account_ids" in value:
        import capo_appstream.types.aws_account_id_list

        out["SharedAwsAccountIds"] = (
            capo_appstream.types.aws_account_id_list.serialize_aws_json_1_1(
                value["shared_aws_account_ids"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImagePermissionsRequest:
    out: DescribeImagePermissionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("SharedAwsAccountIds") is not None:
        import capo_appstream.types.aws_account_id_list

        out["shared_aws_account_ids"] = (
            capo_appstream.types.aws_account_id_list.deserialize_aws_json_1_1(
                data["SharedAwsAccountIds"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeImagePermissionsRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "shared_aws_account_ids" in value:
        import capo_appstream.types.aws_account_id_list

        out["SharedAwsAccountIds"] = (
            capo_appstream.types.aws_account_id_list.serialize_cbor(
                value["shared_aws_account_ids"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeImagePermissionsRequest:
    out: DescribeImagePermissionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("SharedAwsAccountIds") is not None:
        import capo_appstream.types.aws_account_id_list

        out["shared_aws_account_ids"] = (
            capo_appstream.types.aws_account_id_list.deserialize_cbor(
                data["SharedAwsAccountIds"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
