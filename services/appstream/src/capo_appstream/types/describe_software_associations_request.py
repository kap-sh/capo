"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeSoftwareAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.arn
    import capo_appstream.types.integer
    import capo_appstream.types.string


class DescribeSoftwareAssociationsRequest(TypedDict, closed=True):
    associated_resource: NotRequired["capo_appstream.types.arn.Arn"]
    """<p>The ARN of the resource to describe software associations. Possible resources are Image and ImageBuilder.</p>"""
    max_results: NotRequired["capo_appstream.types.integer.Integer"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSoftwareAssociationsRequest) -> dict:
    out: dict = {}
    if "associated_resource" in value:
        out["AssociatedResource"] = value["associated_resource"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSoftwareAssociationsRequest:
    out: DescribeSoftwareAssociationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("AssociatedResource") is not None:
        out["associated_resource"] = data["AssociatedResource"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeSoftwareAssociationsRequest) -> dict:
    out: dict = {}
    if "associated_resource" in value:
        out["AssociatedResource"] = value["associated_resource"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeSoftwareAssociationsRequest:
    out: DescribeSoftwareAssociationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("AssociatedResource") is not None:
        out["associated_resource"] = data["AssociatedResource"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
