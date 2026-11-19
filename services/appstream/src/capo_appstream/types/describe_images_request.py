"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeImagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.arn_list
    import capo_appstream.types.describe_images_max_results
    import capo_appstream.types.string
    import capo_appstream.types.string_list
    import capo_appstream.types.visibility_type


class DescribeImagesRequest(TypedDict, closed=True):
    names: NotRequired["capo_appstream.types.string_list.StringList"]
    """<p>The names of the public or private images to describe.</p>"""
    arns: NotRequired["capo_appstream.types.arn_list.ArnList"]
    """<p>The ARNs of the public, private, and shared images to describe.</p>"""
    type: NotRequired["capo_appstream.types.visibility_type.VisibilityType"]
    """<p>The type of image (public, private, or shared) to describe. </p>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>"""
    max_results: NotRequired[
        "capo_appstream.types.describe_images_max_results.DescribeImagesMaxResults"
    ]
    """<p>The maximum size of each page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImagesRequest) -> dict:
    out: dict = {}
    if "names" in value:
        import capo_appstream.types.string_list

        out["Names"] = capo_appstream.types.string_list.serialize_aws_json_1_1(
            value["names"]
        )
    if "arns" in value:
        import capo_appstream.types.arn_list

        out["Arns"] = capo_appstream.types.arn_list.serialize_aws_json_1_1(
            value["arns"]
        )
    if "type" in value:
        import capo_appstream.types.visibility_type

        out["Type"] = capo_appstream.types.visibility_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImagesRequest:
    out: DescribeImagesRequest = {}  # type: ignore[typeddict-item]
    if data.get("Names") is not None:
        import capo_appstream.types.string_list

        out["names"] = capo_appstream.types.string_list.deserialize_aws_json_1_1(
            data["Names"]
        )
    if data.get("Arns") is not None:
        import capo_appstream.types.arn_list

        out["arns"] = capo_appstream.types.arn_list.deserialize_aws_json_1_1(
            data["Arns"]
        )
    if data.get("Type") is not None:
        import capo_appstream.types.visibility_type

        out["type"] = capo_appstream.types.visibility_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeImagesRequest) -> dict:
    out: dict = {}
    if "names" in value:
        import capo_appstream.types.string_list

        out["Names"] = capo_appstream.types.string_list.serialize_cbor(value["names"])
    if "arns" in value:
        import capo_appstream.types.arn_list

        out["Arns"] = capo_appstream.types.arn_list.serialize_cbor(value["arns"])
    if "type" in value:
        import capo_appstream.types.visibility_type

        out["Type"] = capo_appstream.types.visibility_type.serialize_cbor(value["type"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> DescribeImagesRequest:
    out: DescribeImagesRequest = {}  # type: ignore[typeddict-item]
    if data.get("Names") is not None:
        import capo_appstream.types.string_list

        out["names"] = capo_appstream.types.string_list.deserialize_cbor(data["Names"])
    if data.get("Arns") is not None:
        import capo_appstream.types.arn_list

        out["arns"] = capo_appstream.types.arn_list.deserialize_cbor(data["Arns"])
    if data.get("Type") is not None:
        import capo_appstream.types.visibility_type

        out["type"] = capo_appstream.types.visibility_type.deserialize_cbor(
            data["Type"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
