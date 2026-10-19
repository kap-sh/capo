"""Generated from Smithy shape ``com.amazonaws.odb#ListGiMinorVersionsInput``."""

from typing_extensions import NotRequired, TypedDict


class ListGiMinorVersionsInput(TypedDict, closed=True):
    gi_version: "str"
    """<p>The Oracle Grid Infrastructure (GI) major version.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>"""
    next_token: NotRequired["str"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    shape_family: NotRequired["str"]
    """<p>The shape family for the GI minor version.</p>"""
    availability_zone: NotRequired["str"]
    """<p>The Availability Zone to filter GI minor versions.</p>"""
    availability_zone_id: NotRequired["str"]
    """<p>The Availability Zone ID to filter GI minor versions.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListGiMinorVersionsInput) -> dict:
    out: dict = {}
    out["giVersion"] = value["gi_version"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "shape_family" in value:
        out["shapeFamily"] = value["shape_family"]
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "availability_zone_id" in value:
        out["availabilityZoneId"] = value["availability_zone_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListGiMinorVersionsInput:
    out: ListGiMinorVersionsInput = {}  # type: ignore[typeddict-item]
    if data.get("giVersion") is not None:
        out["gi_version"] = data["giVersion"]
    else:
        out["gi_version"] = ""
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("shapeFamily") is not None:
        out["shape_family"] = data["shapeFamily"]
    if data.get("availabilityZone") is not None:
        out["availability_zone"] = data["availabilityZone"]
    if data.get("availabilityZoneId") is not None:
        out["availability_zone_id"] = data["availabilityZoneId"]
    return out
