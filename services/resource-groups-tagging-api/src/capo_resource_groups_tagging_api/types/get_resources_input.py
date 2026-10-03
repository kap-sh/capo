"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#GetResourcesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.exclude_compliant_resources
    import capo_resource_groups_tagging_api.types.include_compliance_details
    import capo_resource_groups_tagging_api.types.pagination_token
    import capo_resource_groups_tagging_api.types.resource_arn_list_for_get
    import capo_resource_groups_tagging_api.types.resource_type_filter_list
    import capo_resource_groups_tagging_api.types.resources_per_page
    import capo_resource_groups_tagging_api.types.tag_filter_list
    import capo_resource_groups_tagging_api.types.tags_per_page


class GetResourcesInput(TypedDict, closed=True):
    pagination_token: NotRequired[
        "capo_resource_groups_tagging_api.types.pagination_token.PaginationToken"
    ]
    """<p>Specifies a <code>PaginationToken</code> response value from a previous request to indicate that you want the next page of results. Leave this parameter empty in your initial request.</p>"""
    tag_filters: NotRequired[
        "capo_resource_groups_tagging_api.types.tag_filter_list.TagFilterList"
    ]
    """<p>Specifies a list of TagFilters (keys and values) to restrict the output to only those resources that have tags with the specified keys and, if included, the specified values. Each <code>TagFilter</code> must contain a key with values optional. A request can include up to 50 keys, and each key can include up to 20 values. </p> <p>You can't specify both this parameter and the <code>ResourceArnList</code> parameter in the same request. If you do, you get an <code>Invalid Parameter</code> exception.</p> <p>Note the following when deciding how to use TagFilters:</p> <ul> <li> <p>If you <i>don't</i> specify a <code>TagFilter</code>, the response includes all resources that are currently tagged or ever had a tag. Resources that were previously tagged, <i>but do not currently</i> have tags, are shown with an empty tag set, like this: <code>"Tags": []</code>.</p> </li> <li> <p>If you specify more than one filter in a single request, the response returns only those resources that satisfy all filters.</p> </li> <li> <p>If you specify a filter that contains more than one value for a key, the response returns resources that match <i>any</i> of the specified values for that key.</p> </li> <li> <p>If you don't specify a value for a key, the response returns all resources that are tagged with that key, with any or no value.</p> <p>For example, for the following filters: <code>filter1= {key1,{value1}}</code>, <code>filter2={key2,{value2,value3,value4}}</code>, <code>filter3= {key3}</code>:</p> <ul> <li> <p> <code>GetResources({filter1})</code> returns resources tagged with <code>key1=value1</code> </p> </li> <li> <p> <code>GetResources({filter2})</code> returns resources tagged with <code>key2=value2</code> or <code>key2=value3</code> or <code>key2=value4</code> </p> </li> <li> <p> <code>GetResources({filter3})</code> returns resources tagged with any tag with the key <code>key3</code>, and with any or no value</p> </li> <li> <p> <code>GetResources({filter1,filter2,filter3})</code> returns resources tagged with <code>(key1=value1) and (key2=value2 or key2=value3 or key2=value4) and (key3, any or no value)</code> </p> </li> </ul> </li> </ul>"""
    resources_per_page: NotRequired[
        "capo_resource_groups_tagging_api.types.resources_per_page.ResourcesPerPage"
    ]
    """<p>Specifies the maximum number of results to be returned in each page. A query can return fewer than this maximum, even if there are more results still to return. You should always check the <code>PaginationToken</code> response value to see if there are more results. You can specify a minimum of 1 and a maximum value of 100.</p>"""
    tags_per_page: NotRequired[
        "capo_resource_groups_tagging_api.types.tags_per_page.TagsPerPage"
    ]
    """<p>Amazon Web Services recommends using <code>ResourcesPerPage</code> instead of this parameter.</p> <p>A limit that restricts the number of tags (key and value pairs) returned by <code>GetResources</code> in paginated output. A resource with no tags is counted as having one tag (one key and value pair).</p> <p> <code>GetResources</code> does not split a resource and its associated tags across pages. If the specified <code>TagsPerPage</code> would cause such a break, a <code>PaginationToken</code> is returned in place of the affected resource and its tags. Use that token in another request to get the remaining data. For example, if you specify a <code>TagsPerPage</code> of <code>100</code> and the account has 22 resources with 10 tags each (meaning that each resource has 10 key and value pairs), the output will consist of three pages. The first page displays the first 10 resources, each with its 10 tags. The second page displays the next 10 resources, each with its 10 tags. The third page displays the remaining 2 resources, each with its 10 tags.</p> <p>You can set <code>TagsPerPage</code> to a minimum of 100 items up to a maximum of 500 items.</p>"""
    resource_type_filters: NotRequired[
        "capo_resource_groups_tagging_api.types.resource_type_filter_list.ResourceTypeFilterList"
    ]
    """<p>Specifies the resource types that you want included in the response. The format of each resource type is <code>service[:resourceType]</code>. For example, specifying a service of <code>ec2</code> returns all Amazon EC2 resources (which includes EC2 instances). Specifying a resource type of <code>ec2:instance</code> returns only EC2 instances. </p> <p>You can't specify both this parameter and the <code>ResourceArnList</code> parameter in the same request. If you do, you get an <code>Invalid Parameter</code> exception.</p> <p>The string for each service name and resource type is the same as that embedded in a resource's Amazon Resource Name (ARN).</p> <note> <p>For the list of services whose resources you can tag using the Resource Groups Tagging API, see <a href="https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/supported-services.html">Services that support the Resource Groups Tagging API</a>. If an Amazon Web Services service isn't listed on that page, you might still be able to tag that service's resources by using that service's native tagging operations instead of using Resource Groups Tagging API operations. All tagged resources, whether the tagging used the Resource Groups Tagging API or not, are returned by the <code>Get*</code> operation.</p> </note> <p>You can specify multiple resource types by using an array. The array can include up to 100 items. Note that the length constraint requirement applies to each resource type filter. For example, the following string would limit the response to only Amazon EC2 instances, Amazon S3 buckets, or any Audit Manager resource:</p> <p> <code>ec2:instance,s3:bucket,auditmanager</code> </p>"""
    include_compliance_details: NotRequired[
        "capo_resource_groups_tagging_api.types.include_compliance_details.IncludeComplianceDetails"
    ]
    """<p>Specifies whether to include details regarding the compliance with the effective tag policy. Set this to <code>true</code> to determine whether resources are compliant with the tag policy and to get details.</p>"""
    exclude_compliant_resources: NotRequired[
        "capo_resource_groups_tagging_api.types.exclude_compliant_resources.ExcludeCompliantResources"
    ]
    """<p>Specifies whether to exclude resources that are compliant with the tag policy. Set this to <code>true</code> if you are interested in retrieving information on noncompliant resources only.</p> <p>You can use this parameter only if the <code>IncludeComplianceDetails</code> parameter is also set to <code>true</code>.</p>"""
    resource_arn_list: NotRequired[
        "capo_resource_groups_tagging_api.types.resource_arn_list_for_get.ResourceARNListForGet"
    ]
    """<p>Specifies a list of ARNs of resources for which you want to retrieve tag data.</p> <p>You can't specify both this parameter and the <code>ResourceTypeFilters</code> parameter in the same request. If you do, you get an <code>Invalid Parameter</code> exception.</p> <p>You can't specify both this parameter and the <code>TagFilters</code> parameter in the same request. If you do, you get an <code>Invalid Parameter</code> exception.</p> <p>You can't specify both this parameter and any of the pagination parameters (<code>ResourcesPerPage</code>, <code>TagsPerPage</code>, <code>PaginationToken</code>) in the same request. If you do, you get an <code>Invalid Parameter</code> exception.</p> <p>If a resource specified by this parameter doesn't exist, it doesn't generate an error; it simply isn't included in the response.</p> <p>An ARN (Amazon Resource Name) uniquely identifies a resource. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourcesInput) -> dict:
    out: dict = {}
    if "pagination_token" in value:
        out["PaginationToken"] = value["pagination_token"]
    if "tag_filters" in value:
        import capo_resource_groups_tagging_api.types.tag_filter_list

        out["TagFilters"] = (
            capo_resource_groups_tagging_api.types.tag_filter_list.serialize_aws_json_1_1(
                value["tag_filters"]
            )
        )
    if "resources_per_page" in value:
        out["ResourcesPerPage"] = value["resources_per_page"]
    if "tags_per_page" in value:
        out["TagsPerPage"] = value["tags_per_page"]
    if "resource_type_filters" in value:
        import capo_resource_groups_tagging_api.types.resource_type_filter_list

        out["ResourceTypeFilters"] = (
            capo_resource_groups_tagging_api.types.resource_type_filter_list.serialize_aws_json_1_1(
                value["resource_type_filters"]
            )
        )
    if "include_compliance_details" in value:
        out["IncludeComplianceDetails"] = value["include_compliance_details"]
    if "exclude_compliant_resources" in value:
        out["ExcludeCompliantResources"] = value["exclude_compliant_resources"]
    if "resource_arn_list" in value:
        import capo_resource_groups_tagging_api.types.resource_arn_list_for_get

        out["ResourceARNList"] = (
            capo_resource_groups_tagging_api.types.resource_arn_list_for_get.serialize_aws_json_1_1(
                value["resource_arn_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourcesInput:
    out: GetResourcesInput = {}  # type: ignore[typeddict-item]
    if data.get("PaginationToken") is not None:
        out["pagination_token"] = data["PaginationToken"]
    if data.get("TagFilters") is not None:
        import capo_resource_groups_tagging_api.types.tag_filter_list

        out["tag_filters"] = (
            capo_resource_groups_tagging_api.types.tag_filter_list.deserialize_aws_json_1_1(
                data["TagFilters"]
            )
        )
    if data.get("ResourcesPerPage") is not None:
        out["resources_per_page"] = data["ResourcesPerPage"]
    if data.get("TagsPerPage") is not None:
        out["tags_per_page"] = data["TagsPerPage"]
    if data.get("ResourceTypeFilters") is not None:
        import capo_resource_groups_tagging_api.types.resource_type_filter_list

        out["resource_type_filters"] = (
            capo_resource_groups_tagging_api.types.resource_type_filter_list.deserialize_aws_json_1_1(
                data["ResourceTypeFilters"]
            )
        )
    if data.get("IncludeComplianceDetails") is not None:
        out["include_compliance_details"] = data["IncludeComplianceDetails"]
    if data.get("ExcludeCompliantResources") is not None:
        out["exclude_compliant_resources"] = data["ExcludeCompliantResources"]
    if data.get("ResourceARNList") is not None:
        import capo_resource_groups_tagging_api.types.resource_arn_list_for_get

        out["resource_arn_list"] = (
            capo_resource_groups_tagging_api.types.resource_arn_list_for_get.deserialize_aws_json_1_1(
                data["ResourceARNList"]
            )
        )
    return out
