"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeImageBuildersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.integer
    import capo_appstream.types.string
    import capo_appstream.types.string_list


class DescribeImageBuildersRequest(TypedDict, closed=True):
    names: NotRequired["capo_appstream.types.string_list.StringList"]
    """<p>The names of the image builders to describe.</p>"""
    max_results: NotRequired["capo_appstream.types.integer.Integer"]
    """<p>The maximum size of each page of results.</p>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImageBuildersRequest) -> dict:
    out: dict = {}
    if "names" in value:
        import capo_appstream.types.string_list

        out["Names"] = capo_appstream.types.string_list.serialize_aws_json_1_1(
            value["names"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImageBuildersRequest:
    out: DescribeImageBuildersRequest = {}  # type: ignore[typeddict-item]
    if data.get("Names") is not None:
        import capo_appstream.types.string_list

        out["names"] = capo_appstream.types.string_list.deserialize_aws_json_1_1(
            data["Names"]
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeImageBuildersRequest) -> dict:
    out: dict = {}
    if "names" in value:
        import capo_appstream.types.string_list

        out["Names"] = capo_appstream.types.string_list.serialize_cbor(value["names"])
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeImageBuildersRequest:
    out: DescribeImageBuildersRequest = {}  # type: ignore[typeddict-item]
    if data.get("Names") is not None:
        import capo_appstream.types.string_list

        out["names"] = capo_appstream.types.string_list.deserialize_cbor(data["Names"])
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
