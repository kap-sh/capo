"""Generated from Smithy shape ``com.amazonaws.ec2#GetSpotPlacementScoresRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.instance_requirements_with_metadata_request
    import capo_ec2.types.instance_types
    import capo_ec2.types.region_names
    import capo_ec2.types.spot_placement_scores_max_results
    import capo_ec2.types.spot_placement_scores_target_capacity
    import capo_ec2.types.string
    import capo_ec2.types.target_capacity_unit_type


class GetSpotPlacementScoresRequest(TypedDict, closed=True):
    instance_types: NotRequired["capo_ec2.types.instance_types.InstanceTypes"]
    """<p>The instance types. We recommend that you specify at least three instance types. If you specify one or two instance types, or specify variations of a single instance type (for example, an <code>m3.xlarge</code> with and without instance storage), the returned placement score will always be low. </p> <p>If you specify <code>InstanceTypes</code>, you can't specify <code>InstanceRequirementsWithMetadata</code>.</p>"""
    target_capacity: NotRequired[
        "capo_ec2.types.spot_placement_scores_target_capacity.SpotPlacementScoresTargetCapacity"
    ]
    """<p>The target capacity.</p>"""
    target_capacity_unit_type: NotRequired[
        "capo_ec2.types.target_capacity_unit_type.TargetCapacityUnitType"
    ]
    """<p>The unit for the target capacity.</p>"""
    single_availability_zone: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Specify <code>true</code> so that the response returns a list of scored Availability Zones. Otherwise, the response returns a list of scored Regions.</p> <p>A list of scored Availability Zones is useful if you want to launch all of your Spot capacity into a single Availability Zone.</p>"""
    region_names: NotRequired["capo_ec2.types.region_names.RegionNames"]
    """<p>The Regions used to narrow down the list of Regions to be scored. Enter the Region code, for example, <code>us-east-1</code>.</p>"""
    instance_requirements_with_metadata: NotRequired[
        "capo_ec2.types.instance_requirements_with_metadata_request.InstanceRequirementsWithMetadataRequest"
    ]
    """<p>The attributes for the instance types. When you specify instance attributes, Amazon EC2 will identify instance types with those attributes.</p> <p>If you specify <code>InstanceRequirementsWithMetadata</code>, you can't specify <code>InstanceTypes</code>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    max_results: NotRequired[
        "capo_ec2.types.spot_placement_scores_max_results.SpotPlacementScoresMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination">Pagination</a>.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    include_local_zones: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Specify <code>true</code> so that the response returns scores that include Local Zones. Otherwise, the response ignores Local Zones.</p> <p>When you request regional scores, Local Zone capacity counts toward its parent Region.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetSpotPlacementScoresRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_types" in value:
        import capo_ec2.types.instance_types

        capo_ec2.types.instance_types.serialize_ec2_query(
            value["instance_types"], pairs, f"{key_prefix}InstanceType"
        )
    if "target_capacity" in value:
        pairs.append((f"{key_prefix}TargetCapacity", str(value["target_capacity"])))
    if "target_capacity_unit_type" in value:
        import capo_ec2.types.target_capacity_unit_type

        capo_ec2.types.target_capacity_unit_type.serialize_ec2_query(
            value["target_capacity_unit_type"],
            pairs,
            f"{key_prefix}TargetCapacityUnitType",
        )
    if "single_availability_zone" in value:
        pairs.append(
            (
                f"{key_prefix}SingleAvailabilityZone",
                "true" if value["single_availability_zone"] else "false",
            )
        )
    if "region_names" in value:
        import capo_ec2.types.region_names

        capo_ec2.types.region_names.serialize_ec2_query(
            value["region_names"], pairs, f"{key_prefix}RegionName"
        )
    if "instance_requirements_with_metadata" in value:
        import capo_ec2.types.instance_requirements_with_metadata_request

        capo_ec2.types.instance_requirements_with_metadata_request.serialize_ec2_query(
            value["instance_requirements_with_metadata"],
            pairs,
            f"{key_prefix}InstanceRequirementsWithMetadata",
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "include_local_zones" in value:
        pairs.append(
            (
                f"{key_prefix}IncludeLocalZones",
                "true" if value["include_local_zones"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> GetSpotPlacementScoresRequest:
    out: GetSpotPlacementScoresRequest = {}  # type: ignore[typeddict-item]
    child_instance_types = el.find("InstanceType")
    if child_instance_types is not None:
        import capo_ec2.types.instance_types

        out["instance_types"] = capo_ec2.types.instance_types.deserialize_ec2_query(
            child_instance_types
        )
    child_target_capacity = el.find("TargetCapacity")
    if child_target_capacity is not None:
        out["target_capacity"] = int(child_target_capacity.text or "")
    child_target_capacity_unit_type = el.find("TargetCapacityUnitType")
    if child_target_capacity_unit_type is not None:
        import capo_ec2.types.target_capacity_unit_type

        out["target_capacity_unit_type"] = (
            capo_ec2.types.target_capacity_unit_type.deserialize_ec2_query(
                child_target_capacity_unit_type
            )
        )
    child_single_availability_zone = el.find("SingleAvailabilityZone")
    if child_single_availability_zone is not None:
        out["single_availability_zone"] = (
            child_single_availability_zone.text or ""
        ).lower() == "true"
    child_region_names = el.find("RegionName")
    if child_region_names is not None:
        import capo_ec2.types.region_names

        out["region_names"] = capo_ec2.types.region_names.deserialize_ec2_query(
            child_region_names
        )
    child_instance_requirements_with_metadata = el.find(
        "InstanceRequirementsWithMetadata"
    )
    if child_instance_requirements_with_metadata is not None:
        import capo_ec2.types.instance_requirements_with_metadata_request

        out["instance_requirements_with_metadata"] = (
            capo_ec2.types.instance_requirements_with_metadata_request.deserialize_ec2_query(
                child_instance_requirements_with_metadata
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_include_local_zones = el.find("IncludeLocalZones")
    if child_include_local_zones is not None:
        out["include_local_zones"] = (
            child_include_local_zones.text or ""
        ).lower() == "true"
    return out
