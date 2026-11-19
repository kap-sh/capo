"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeAppBlockBuildersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.integer
    import capo_appstream.types.string
    import capo_appstream.types.string_list


class DescribeAppBlockBuildersRequest(TypedDict, closed=True):
    names: NotRequired["capo_appstream.types.string_list.StringList"]
    """<p>The names of the app block builders.</p>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""
    max_results: NotRequired["capo_appstream.types.integer.Integer"]
    """<p>The maximum size of each page of results. The maximum value is 25.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAppBlockBuildersRequest) -> dict:
    out: dict = {}
    if "names" in value:
        import capo_appstream.types.string_list

        out["Names"] = capo_appstream.types.string_list.serialize_aws_json_1_1(
            value["names"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAppBlockBuildersRequest:
    out: DescribeAppBlockBuildersRequest = {}  # type: ignore[typeddict-item]
    if data.get("Names") is not None:
        import capo_appstream.types.string_list

        out["names"] = capo_appstream.types.string_list.deserialize_aws_json_1_1(
            data["Names"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeAppBlockBuildersRequest) -> dict:
    out: dict = {}
    if "names" in value:
        import capo_appstream.types.string_list

        out["Names"] = capo_appstream.types.string_list.serialize_cbor(value["names"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> DescribeAppBlockBuildersRequest:
    out: DescribeAppBlockBuildersRequest = {}  # type: ignore[typeddict-item]
    if data.get("Names") is not None:
        import capo_appstream.types.string_list

        out["names"] = capo_appstream.types.string_list.deserialize_cbor(data["Names"])
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
