"""Generated from Smithy shape ``com.amazonaws.resourcegroups#ResourceQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resource_groups.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resource_groups.types.query
    import capo_resource_groups.types.query_type


class ResourceQuery(TypedDict, closed=True):
    type: "capo_resource_groups.types.query_type.QueryType"
    """<p>The type of the query to perform. This can have one of two values:</p> <ul> <li> <p> <i> <code>CLOUDFORMATION_STACK_1_0:</code> </i> Specifies that you want the group to contain the members of an CloudFormation stack. The <code>Query</code> contains a <code>StackIdentifier</code> element with an Amazon resource name (ARN) for a CloudFormation stack.</p> </li> <li> <p> <i> <code>TAG_FILTERS_1_0:</code> </i> Specifies that you want the group to include resource that have tags that match the query. </p> </li> </ul>"""
    query: "capo_resource_groups.types.query.Query"
    """<p>The query that defines a group or a search. The contents depends on the value of the <code>Type</code> element.</p> <ul> <li> <p> <code>ResourceTypeFilters</code> – Applies to all <code>ResourceQuery</code> objects of either <code>Type</code>. This element contains one of the following two items:</p> <ul> <li> <p>The value <code>AWS::AllSupported</code>. This causes the ResourceQuery to match resources of any resource type that also match the query.</p> </li> <li> <p>A list (a JSON array) of resource type identifiers that limit the query to only resources of the specified types. For the complete list of resource types that you can use in the array value for <code>ResourceTypeFilters</code>, see <a href="https://docs.aws.amazon.com/ARG/latest/userguide/supported-resources.html">Resources you can use with Resource Groups and Tag Editor</a> in the <i>Resource Groups User Guide</i>.</p> </li> </ul> <p>Example: <code>"ResourceTypeFilters": ["AWS::AllSupported"]</code> or <code>"ResourceTypeFilters": ["AWS::EC2::Instance", "AWS::S3::Bucket"]</code> </p> </li> <li> <p> <code>TagFilters</code> – applicable only if <code>Type</code> = <code>TAG_FILTERS_1_0</code>. The <code>Query</code> contains a JSON string that represents a collection of simple tag filters. The JSON string uses a syntax similar to the <code> <a href="https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html">GetResources</a> </code> operation, but uses only the <code> <a href="https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html#resourcegrouptagging-GetResources-request-ResourceTypeFilters"> ResourceTypeFilters</a> </code> and <code> <a href="https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html#resourcegrouptagging-GetResources-request-TagFiltersTagFilters">TagFilters</a> </code> fields. If you specify more than one tag key, only resources that match all tag keys, and at least one value of each specified tag key, are returned in your query. If you specify more than one value for a tag key, a resource matches the filter if it has a tag key value that matches <i>any</i> of the specified values.</p> <p>For example, consider the following sample query for resources that have two tags, <code>Stage</code> and <code>Version</code>, with two values each:</p> <p> <code>[{"Stage":["Test","Deploy"]},{"Version":["1","2"]}]</code> </p> <p>The results of this resource query could include the following.</p> <ul> <li> <p>An Amazon EC2 instance that has the following two tags: <code>{"Stage":"Deploy"}</code>, and <code>{"Version":"2"}</code> </p> </li> <li> <p>An S3 bucket that has the following two tags: <code>{"Stage":"Test"}</code>, and <code>{"Version":"1"}</code> </p> </li> </ul> <p>The resource query results would <i>not</i> include the following items in the results, however. </p> <ul> <li> <p>An Amazon EC2 instance that has only the following tag: <code>{"Stage":"Deploy"}</code>.</p> <p>The instance does not have <b>all</b> of the tag keys specified in the filter, so it is excluded from the results.</p> </li> <li> <p>An RDS database that has the following two tags: <code>{"Stage":"Archived"}</code> and <code>{"Version":"4"}</code> </p> <p>The database has all of the tag keys, but none of those keys has an associated value that matches at least one of the specified values in the filter.</p> </li> </ul> <p>Example: <code>"TagFilters": [ { "Key": "Stage", "Values": [ "Gamma", "Beta" ] }</code> </p> </li> <li> <p> <code>StackIdentifier</code> – applicable only if <code>Type</code> = <code>CLOUDFORMATION_STACK_1_0</code>. The value of this parameter is the Amazon Resource Name (ARN) of the CloudFormation stack whose resources you want included in the group.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceQuery) -> dict:
    out: dict = {}
    import capo_resource_groups.types.query_type

    out["Type"] = capo_resource_groups.types.query_type.serialize_json(value["type"])
    out["Query"] = value["query"]
    return out


def deserialize_json(data: dict) -> ResourceQuery:
    out: ResourceQuery = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_resource_groups.types.query_type

        out["type"] = capo_resource_groups.types.query_type.deserialize_json(
            data["Type"]
        )
    else:
        raise DeserializationError("ResourceQuery.type required")
    if data.get("Query") is not None:
        out["query"] = data["Query"]
    else:
        raise DeserializationError("ResourceQuery.query required")
    return out
