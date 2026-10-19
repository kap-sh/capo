"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#Trail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.cloud_trail_arn
    import capo_accessanalyzer.types.region_list


class Trail(TypedDict, closed=True):
    cloud_trail_arn: "capo_accessanalyzer.types.cloud_trail_arn.CloudTrailArn"
    """<p>Specifies the ARN of the trail. The format of a trail ARN is <code>arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail</code>.</p>"""
    regions: NotRequired["capo_accessanalyzer.types.region_list.RegionList"]
    """<p>A list of regions to get CloudTrail data from and analyze to generate a policy.</p>"""
    all_regions: NotRequired["bool"]
    """<p>Possible values are <code>true</code> or <code>false</code>. If set to <code>true</code>, IAM Access Analyzer retrieves CloudTrail data from all regions to analyze and generate a policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Trail) -> dict:
    out: dict = {}
    out["cloudTrailArn"] = value["cloud_trail_arn"]
    if "regions" in value:
        import capo_accessanalyzer.types.region_list

        out["regions"] = capo_accessanalyzer.types.region_list.serialize_json(
            value["regions"]
        )
    if "all_regions" in value:
        out["allRegions"] = value["all_regions"]
    return out


def deserialize_json(data: dict) -> Trail:
    out: Trail = {}  # type: ignore[typeddict-item]
    if data.get("cloudTrailArn") is not None:
        out["cloud_trail_arn"] = data["cloudTrailArn"]
    else:
        out["cloud_trail_arn"] = ""
    if data.get("regions") is not None:
        import capo_accessanalyzer.types.region_list

        out["regions"] = capo_accessanalyzer.types.region_list.deserialize_json(
            data["regions"]
        )
    if data.get("allRegions") is not None:
        out["all_regions"] = data["allRegions"]
    return out
