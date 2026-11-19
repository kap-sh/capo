"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeApplicationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.arn_list
    import capo_appstream.types.integer
    import capo_appstream.types.string


class DescribeApplicationsRequest(TypedDict, closed=True):
    arns: NotRequired["capo_appstream.types.arn_list.ArnList"]
    """<p>The ARNs for the applications.</p>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""
    max_results: NotRequired["capo_appstream.types.integer.Integer"]
    """<p>The maximum size of each page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApplicationsRequest) -> dict:
    out: dict = {}
    if "arns" in value:
        import capo_appstream.types.arn_list

        out["Arns"] = capo_appstream.types.arn_list.serialize_aws_json_1_1(
            value["arns"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApplicationsRequest:
    out: DescribeApplicationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Arns") is not None:
        import capo_appstream.types.arn_list

        out["arns"] = capo_appstream.types.arn_list.deserialize_aws_json_1_1(
            data["Arns"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeApplicationsRequest) -> dict:
    out: dict = {}
    if "arns" in value:
        import capo_appstream.types.arn_list

        out["Arns"] = capo_appstream.types.arn_list.serialize_cbor(value["arns"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> DescribeApplicationsRequest:
    out: DescribeApplicationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Arns") is not None:
        import capo_appstream.types.arn_list

        out["arns"] = capo_appstream.types.arn_list.deserialize_cbor(data["Arns"])
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
