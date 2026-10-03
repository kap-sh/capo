"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#GetComplianceSummaryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.group_by
    import capo_resource_groups_tagging_api.types.max_results_get_compliance_summary
    import capo_resource_groups_tagging_api.types.pagination_token
    import capo_resource_groups_tagging_api.types.region_filter_list
    import capo_resource_groups_tagging_api.types.resource_type_filter_list
    import capo_resource_groups_tagging_api.types.tag_key_filter_list
    import capo_resource_groups_tagging_api.types.target_id_filter_list


class GetComplianceSummaryInput(TypedDict, closed=True):
    target_id_filters: NotRequired[
        "capo_resource_groups_tagging_api.types.target_id_filter_list.TargetIdFilterList"
    ]
    """<p>Specifies target identifiers (usually, specific account IDs) to limit the output by. If you use this parameter, the count of returned noncompliant resources includes only resources with the specified target IDs.</p>"""
    region_filters: NotRequired[
        "capo_resource_groups_tagging_api.types.region_filter_list.RegionFilterList"
    ]
    """<p>Specifies a list of Amazon Web Services Regions to limit the output to. If you use this parameter, the count of returned noncompliant resources includes only resources in the specified Regions.</p>"""
    resource_type_filters: NotRequired[
        "capo_resource_groups_tagging_api.types.resource_type_filter_list.ResourceTypeFilterList"
    ]
    """<p>Specifies that you want the response to include information for only resources of the specified types. The format of each resource type is <code>service[:resourceType]</code>. For example, specifying a resource type of <code>ec2</code> returns all Amazon EC2 resources (which includes EC2 instances). Specifying a resource type of <code>ec2:instance</code> returns only EC2 instances.</p> <p>The string for each service name and resource type is the same as that embedded in a resource's Amazon Resource Name (ARN). Consult the <i> <a href="https://docs.aws.amazon.com/general/latest/gr/">Amazon Web Services General Reference</a> </i> for the following:</p> <ul> <li> <p>For a list of service name strings, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces">Amazon Web Services Service Namespaces</a>.</p> </li> <li> <p>For resource type strings, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arns-syntax">Example ARNs</a>.</p> </li> <li> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a>.</p> </li> </ul> <note> <p>For the list of services whose resources you can tag using the Resource Groups Tagging API, see <a href="https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/supported-services.html">Services that support the Resource Groups Tagging API</a>. If an Amazon Web Services service isn't listed on that page, you might still be able to tag that service's resources by using that service's native tagging operations instead of using Resource Groups Tagging API operations. All tagged resources, whether the tagging used the Resource Groups Tagging API or not, are returned by the <code>Get*</code> operation.</p> </note> <p>You can specify multiple resource types by using a comma separated array. The array can include up to 100 items. Note that the length constraint requirement applies to each resource type filter. </p>"""
    tag_key_filters: NotRequired[
        "capo_resource_groups_tagging_api.types.tag_key_filter_list.TagKeyFilterList"
    ]
    """<p>Specifies that you want the response to include information for only resources that have tags with the specified tag keys. If you use this parameter, the count of returned noncompliant resources includes only resources that have the specified tag keys.</p>"""
    group_by: NotRequired["capo_resource_groups_tagging_api.types.group_by.GroupBy"]
    """<p>Specifies a list of attributes to group the counts of noncompliant resources by. If supplied, the counts are sorted by those attributes.</p>"""
    max_results: NotRequired[
        "capo_resource_groups_tagging_api.types.max_results_get_compliance_summary.MaxResultsGetComplianceSummary"
    ]
    """<p>Specifies the maximum number of results to be returned in each page. A query can return fewer than this maximum, even if there are more results still to return. You should always check the <code>PaginationToken</code> response value to see if there are more results. You can specify a minimum of 1 and a maximum value of 100.</p>"""
    pagination_token: NotRequired[
        "capo_resource_groups_tagging_api.types.pagination_token.PaginationToken"
    ]
    """<p>Specifies a <code>PaginationToken</code> response value from a previous request to indicate that you want the next page of results. Leave this parameter empty in your initial request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetComplianceSummaryInput) -> dict:
    out: dict = {}
    if "target_id_filters" in value:
        import capo_resource_groups_tagging_api.types.target_id_filter_list

        out["TargetIdFilters"] = (
            capo_resource_groups_tagging_api.types.target_id_filter_list.serialize_aws_json_1_1(
                value["target_id_filters"]
            )
        )
    if "region_filters" in value:
        import capo_resource_groups_tagging_api.types.region_filter_list

        out["RegionFilters"] = (
            capo_resource_groups_tagging_api.types.region_filter_list.serialize_aws_json_1_1(
                value["region_filters"]
            )
        )
    if "resource_type_filters" in value:
        import capo_resource_groups_tagging_api.types.resource_type_filter_list

        out["ResourceTypeFilters"] = (
            capo_resource_groups_tagging_api.types.resource_type_filter_list.serialize_aws_json_1_1(
                value["resource_type_filters"]
            )
        )
    if "tag_key_filters" in value:
        import capo_resource_groups_tagging_api.types.tag_key_filter_list

        out["TagKeyFilters"] = (
            capo_resource_groups_tagging_api.types.tag_key_filter_list.serialize_aws_json_1_1(
                value["tag_key_filters"]
            )
        )
    if "group_by" in value:
        import capo_resource_groups_tagging_api.types.group_by

        out["GroupBy"] = (
            capo_resource_groups_tagging_api.types.group_by.serialize_aws_json_1_1(
                value["group_by"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "pagination_token" in value:
        out["PaginationToken"] = value["pagination_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetComplianceSummaryInput:
    out: GetComplianceSummaryInput = {}  # type: ignore[typeddict-item]
    if data.get("TargetIdFilters") is not None:
        import capo_resource_groups_tagging_api.types.target_id_filter_list

        out["target_id_filters"] = (
            capo_resource_groups_tagging_api.types.target_id_filter_list.deserialize_aws_json_1_1(
                data["TargetIdFilters"]
            )
        )
    if data.get("RegionFilters") is not None:
        import capo_resource_groups_tagging_api.types.region_filter_list

        out["region_filters"] = (
            capo_resource_groups_tagging_api.types.region_filter_list.deserialize_aws_json_1_1(
                data["RegionFilters"]
            )
        )
    if data.get("ResourceTypeFilters") is not None:
        import capo_resource_groups_tagging_api.types.resource_type_filter_list

        out["resource_type_filters"] = (
            capo_resource_groups_tagging_api.types.resource_type_filter_list.deserialize_aws_json_1_1(
                data["ResourceTypeFilters"]
            )
        )
    if data.get("TagKeyFilters") is not None:
        import capo_resource_groups_tagging_api.types.tag_key_filter_list

        out["tag_key_filters"] = (
            capo_resource_groups_tagging_api.types.tag_key_filter_list.deserialize_aws_json_1_1(
                data["TagKeyFilters"]
            )
        )
    if data.get("GroupBy") is not None:
        import capo_resource_groups_tagging_api.types.group_by

        out["group_by"] = (
            capo_resource_groups_tagging_api.types.group_by.deserialize_aws_json_1_1(
                data["GroupBy"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("PaginationToken") is not None:
        out["pagination_token"] = data["PaginationToken"]
    return out
