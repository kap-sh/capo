"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeReservedInstancesOfferingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.availability_zone_id
    import capo_ec2.types.boolean
    import capo_ec2.types.filter_list
    import capo_ec2.types.instance_type
    import capo_ec2.types.integer
    import capo_ec2.types.long
    import capo_ec2.types.offering_class_type
    import capo_ec2.types.offering_type_values
    import capo_ec2.types.reserved_instances_offering_id_string_list
    import capo_ec2.types.ri_product_description
    import capo_ec2.types.string
    import capo_ec2.types.tenancy


class DescribeReservedInstancesOfferingsRequest(TypedDict, closed=True):
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone in which the Reserved Instance can be used.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> can be specified, but not both.</p>"""
    include_marketplace: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Include Reserved Instance Marketplace offerings in the response.</p>"""
    instance_type: NotRequired["capo_ec2.types.instance_type.InstanceType"]
    """<p>The instance type that the reservation will cover (for example, <code>m1.small</code>). For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html">Amazon EC2 instance types</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    max_duration: NotRequired["capo_ec2.types.long.Long"]
    """<p>The maximum duration (in seconds) to filter when searching for offerings.</p> <p>Default: 94608000 (3 years)</p>"""
    max_instance_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The maximum number of instances to filter when searching for offerings.</p> <p>Default: 20</p>"""
    min_duration: NotRequired["capo_ec2.types.long.Long"]
    """<p>The minimum duration (in seconds) to filter when searching for offerings.</p> <p>Default: 2592000 (1 month)</p>"""
    offering_class: NotRequired["capo_ec2.types.offering_class_type.OfferingClassType"]
    """<p>The offering class of the Reserved Instance. Can be <code>standard</code> or <code>convertible</code>.</p>"""
    product_description: NotRequired[
        "capo_ec2.types.ri_product_description.RIProductDescription"
    ]
    """<p>The Reserved Instance product platform description. Instances that include <code>(Amazon VPC)</code> in the description are for use with Amazon VPC.</p>"""
    reserved_instances_offering_ids: NotRequired[
        "capo_ec2.types.reserved_instances_offering_id_string_list.ReservedInstancesOfferingIdStringList"
    ]
    """<p>One or more Reserved Instances offering IDs.</p>"""
    availability_zone_id: NotRequired[
        "capo_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> can be specified, but not both.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>availability-zone</code> - The Availability Zone where the Reserved Instance can be used.</p> </li> <li> <p> <code>availability-zone-id</code> - The ID of the Availability Zone where the Reserved Instance can be used.</p> </li> <li> <p> <code>duration</code> - The duration of the Reserved Instance (for example, one year or three years), in seconds (<code>31536000</code> | <code>94608000</code>).</p> </li> <li> <p> <code>fixed-price</code> - The purchase price of the Reserved Instance (for example, 9800.0).</p> </li> <li> <p> <code>instance-type</code> - The instance type that is covered by the reservation.</p> </li> <li> <p> <code>marketplace</code> - Set to <code>true</code> to show only Reserved Instance Marketplace offerings. When this filter is not used, which is the default behavior, all offerings from both Amazon Web Services and the Reserved Instance Marketplace are listed.</p> </li> <li> <p> <code>product-description</code> - The Reserved Instance product platform description (<code>Linux/UNIX</code> | <code>Linux with SQL Server Standard</code> | <code>Linux with SQL Server Web</code> | <code>Linux with SQL Server Enterprise</code> | <code>SUSE Linux</code> | <code>Red Hat Enterprise Linux</code> | <code>Red Hat Enterprise Linux with HA</code> | <code>Windows</code> | <code>Windows with SQL Server Standard</code> | <code>Windows with SQL Server Web</code> | <code>Windows with SQL Server Enterprise</code>).</p> </li> <li> <p> <code>reserved-instances-offering-id</code> - The Reserved Instances offering ID.</p> </li> <li> <p> <code>scope</code> - The scope of the Reserved Instance (<code>Availability Zone</code> or <code>Region</code>).</p> </li> <li> <p> <code>usage-price</code> - The usage price of the Reserved Instance, per hour (for example, 0.84).</p> </li> </ul>"""
    instance_tenancy: NotRequired["capo_ec2.types.tenancy.Tenancy"]
    """<p>The tenancy of the instances covered by the reservation. A Reserved Instance with a tenancy of <code>dedicated</code> is applied to instances that run in a VPC on single-tenant hardware (i.e., Dedicated Instances).</p> <p> <b>Important:</b> The <code>host</code> value cannot be used with this parameter. Use the <code>default</code> or <code>dedicated</code> values only.</p> <p>Default: <code>default</code> </p>"""
    offering_type: NotRequired["capo_ec2.types.offering_type_values.OfferingTypeValues"]
    """<p>The Reserved Instance offering type. If you are using tools that predate the 2011-11-01 API version, you only have access to the <code>Medium Utilization</code> Reserved Instance offering type. </p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to retrieve the next page of results.</p>"""
    max_results: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The maximum number of results to return for the request in a single page. The remaining results of the initial request can be seen by sending another request with the returned <code>NextToken</code> value. The maximum is 100.</p> <p>Default: 100</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeReservedInstancesOfferingsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "include_marketplace" in value:
        pairs.append(
            (
                f"{key_prefix}IncludeMarketplace",
                "true" if value["include_marketplace"] else "false",
            )
        )
    if "instance_type" in value:
        import capo_ec2.types.instance_type

        capo_ec2.types.instance_type.serialize_ec2_query(
            value["instance_type"], pairs, f"{key_prefix}InstanceType"
        )
    if "max_duration" in value:
        pairs.append((f"{key_prefix}MaxDuration", str(value["max_duration"])))
    if "max_instance_count" in value:
        pairs.append(
            (f"{key_prefix}MaxInstanceCount", str(value["max_instance_count"]))
        )
    if "min_duration" in value:
        pairs.append((f"{key_prefix}MinDuration", str(value["min_duration"])))
    if "offering_class" in value:
        import capo_ec2.types.offering_class_type

        capo_ec2.types.offering_class_type.serialize_ec2_query(
            value["offering_class"], pairs, f"{key_prefix}OfferingClass"
        )
    if "product_description" in value:
        import capo_ec2.types.ri_product_description

        capo_ec2.types.ri_product_description.serialize_ec2_query(
            value["product_description"], pairs, f"{key_prefix}ProductDescription"
        )
    if "reserved_instances_offering_ids" in value:
        import capo_ec2.types.reserved_instances_offering_id_string_list

        capo_ec2.types.reserved_instances_offering_id_string_list.serialize_ec2_query(
            value["reserved_instances_offering_ids"],
            pairs,
            f"{key_prefix}ReservedInstancesOfferingId",
        )
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )
    if "instance_tenancy" in value:
        import capo_ec2.types.tenancy

        capo_ec2.types.tenancy.serialize_ec2_query(
            value["instance_tenancy"], pairs, f"{key_prefix}InstanceTenancy"
        )
    if "offering_type" in value:
        import capo_ec2.types.offering_type_values

        capo_ec2.types.offering_type_values.serialize_ec2_query(
            value["offering_type"], pairs, f"{key_prefix}OfferingType"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))


def deserialize_ec2_query(el: Element) -> DescribeReservedInstancesOfferingsRequest:
    out: DescribeReservedInstancesOfferingsRequest = {}  # type: ignore[typeddict-item]
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_include_marketplace = el.find("IncludeMarketplace")
    if child_include_marketplace is not None:
        out["include_marketplace"] = (
            child_include_marketplace.text or ""
        ).lower() == "true"
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        import capo_ec2.types.instance_type

        out["instance_type"] = capo_ec2.types.instance_type.deserialize_ec2_query(
            child_instance_type
        )
    child_max_duration = el.find("MaxDuration")
    if child_max_duration is not None:
        out["max_duration"] = int(child_max_duration.text or "")
    child_max_instance_count = el.find("MaxInstanceCount")
    if child_max_instance_count is not None:
        out["max_instance_count"] = int(child_max_instance_count.text or "")
    child_min_duration = el.find("MinDuration")
    if child_min_duration is not None:
        out["min_duration"] = int(child_min_duration.text or "")
    child_offering_class = el.find("OfferingClass")
    if child_offering_class is not None:
        import capo_ec2.types.offering_class_type

        out["offering_class"] = (
            capo_ec2.types.offering_class_type.deserialize_ec2_query(
                child_offering_class
            )
        )
    child_product_description = el.find("ProductDescription")
    if child_product_description is not None:
        import capo_ec2.types.ri_product_description

        out["product_description"] = (
            capo_ec2.types.ri_product_description.deserialize_ec2_query(
                child_product_description
            )
        )
    child_reserved_instances_offering_ids = el.find("ReservedInstancesOfferingId")
    if child_reserved_instances_offering_ids is not None:
        import capo_ec2.types.reserved_instances_offering_id_string_list

        out["reserved_instances_offering_ids"] = (
            capo_ec2.types.reserved_instances_offering_id_string_list.deserialize_ec2_query(
                child_reserved_instances_offering_ids
            )
        )
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    child_instance_tenancy = el.find("instanceTenancy")
    if child_instance_tenancy is not None:
        import capo_ec2.types.tenancy

        out["instance_tenancy"] = capo_ec2.types.tenancy.deserialize_ec2_query(
            child_instance_tenancy
        )
    child_offering_type = el.find("offeringType")
    if child_offering_type is not None:
        import capo_ec2.types.offering_type_values

        out["offering_type"] = (
            capo_ec2.types.offering_type_values.deserialize_ec2_query(
                child_offering_type
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("maxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    return out
