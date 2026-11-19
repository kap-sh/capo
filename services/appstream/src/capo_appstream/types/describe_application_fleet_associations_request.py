"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeApplicationFleetAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.arn
    import capo_appstream.types.integer
    import capo_appstream.types.name
    import capo_appstream.types.string


class DescribeApplicationFleetAssociationsRequest(TypedDict, closed=True):
    fleet_name: NotRequired["capo_appstream.types.name.Name"]
    """<p>The name of the fleet.</p>"""
    application_arn: NotRequired["capo_appstream.types.arn.Arn"]
    """<p>The ARN of the application.</p>"""
    max_results: NotRequired["capo_appstream.types.integer.Integer"]
    """<p>The maximum size of each page of results.</p>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApplicationFleetAssociationsRequest) -> dict:
    out: dict = {}
    if "fleet_name" in value:
        out["FleetName"] = value["fleet_name"]
    if "application_arn" in value:
        out["ApplicationArn"] = value["application_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApplicationFleetAssociationsRequest:
    out: DescribeApplicationFleetAssociationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("FleetName") is not None:
        out["fleet_name"] = data["FleetName"]
    if data.get("ApplicationArn") is not None:
        out["application_arn"] = data["ApplicationArn"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeApplicationFleetAssociationsRequest) -> dict:
    out: dict = {}
    if "fleet_name" in value:
        out["FleetName"] = value["fleet_name"]
    if "application_arn" in value:
        out["ApplicationArn"] = value["application_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeApplicationFleetAssociationsRequest:
    out: DescribeApplicationFleetAssociationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("FleetName") is not None:
        out["fleet_name"] = data["FleetName"]
    if data.get("ApplicationArn") is not None:
        out["application_arn"] = data["ApplicationArn"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
