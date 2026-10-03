"""Generated from Smithy shape ``com.amazonaws.resourcegroups#StartTagSyncTaskInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resource_groups.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resource_groups.types.group_string_v2
    import capo_resource_groups.types.resource_query
    import capo_resource_groups.types.role_arn
    import capo_resource_groups.types.tag_key
    import capo_resource_groups.types.tag_value


class StartTagSyncTaskInput(TypedDict, closed=True):
    group: "capo_resource_groups.types.group_string_v2.GroupStringV2"
    """<p>The Amazon resource name (ARN) or name of the application group for which you want to create a tag-sync task. </p>"""
    tag_key: NotRequired["capo_resource_groups.types.tag_key.TagKey"]
    """<p>The tag key. Resources tagged with this tag key-value pair will be added to the application. If a resource with this tag is later untagged, the tag-sync task removes the resource from the application. </p> <p>When using the <code>TagKey</code> parameter, you must also specify the <code>TagValue</code> parameter. If you specify a tag key-value pair, you can't use the <code>ResourceQuery</code> parameter. </p>"""
    tag_value: NotRequired["capo_resource_groups.types.tag_value.TagValue"]
    """<p>The tag value. Resources tagged with this tag key-value pair will be added to the application. If a resource with this tag is later untagged, the tag-sync task removes the resource from the application. </p> <p>When using the <code>TagValue</code> parameter, you must also specify the <code>TagKey</code> parameter. If you specify a tag key-value pair, you can't use the <code>ResourceQuery</code> parameter. </p>"""
    resource_query: NotRequired[
        "capo_resource_groups.types.resource_query.ResourceQuery"
    ]
    r"""<p>The query you can use to create the tag-sync task. With this method, all resources matching the query are added to the specified application group. A <code>ResourceQuery</code> specifies both a query <code>Type</code> and a <code>Query</code> string as JSON string objects. For more information on defining a resource query for a tag-sync task, see the tag-based query type in <a href="https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-query.html#getting_started-query_types"> Types of resource group queries</a> in <i>Resource Groups User Guide</i>. </p> <p>When using the <code>ResourceQuery</code> parameter, you cannot use the <code>TagKey</code> and <code>TagValue</code> parameters. </p> <p>When you combine all of the elements together into a single string, any double quotes that are embedded inside another double quote pair must be escaped by preceding the embedded double quote with a backslash character (\). For example, a complete <code>ResourceQuery</code> parameter must be formatted like the following CLI parameter example:</p> <p> <code>--resource-query '{"Type":"TAG_FILTERS_1_0","Query":"{\"ResourceTypeFilters\":[\"AWS::AllSupported\"],\"TagFilters\":[{\"Key\":\"Stage\",\"Values\":[\"Test\"]}]}"}'</code> </p> <p>In the preceding example, all of the double quote characters in the value part of the <code>Query</code> element must be escaped because the value itself is surrounded by double quotes. For more information, see <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html">Quoting strings</a> in the <i>Command Line Interface User Guide</i>.</p> <p>For the complete list of resource types that you can use in the array value for <code>ResourceTypeFilters</code>, see <a href="https://docs.aws.amazon.com/ARG/latest/userguide/supported-resources.html">Resources you can use with Resource Groups and Tag Editor</a> in the <i>Resource Groups User Guide</i>. For example:</p> <p> <code>"ResourceTypeFilters":["AWS::S3::Bucket", "AWS::EC2::Instance"]</code> </p>"""
    role_arn: "capo_resource_groups.types.role_arn.RoleArn"
    """<p>The Amazon resource name (ARN) of the role assumed by the service to tag and untag resources on your behalf.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartTagSyncTaskInput) -> dict:
    out: dict = {}
    out["Group"] = value["group"]
    if "tag_key" in value:
        out["TagKey"] = value["tag_key"]
    if "tag_value" in value:
        out["TagValue"] = value["tag_value"]
    if "resource_query" in value:
        import capo_resource_groups.types.resource_query

        out["ResourceQuery"] = capo_resource_groups.types.resource_query.serialize_json(
            value["resource_query"]
        )
    out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> StartTagSyncTaskInput:
    out: StartTagSyncTaskInput = {}  # type: ignore[typeddict-item]
    if data.get("Group") is not None:
        out["group"] = data["Group"]
    else:
        raise DeserializationError("StartTagSyncTaskInput.group required")
    if data.get("TagKey") is not None:
        out["tag_key"] = data["TagKey"]
    if data.get("TagValue") is not None:
        out["tag_value"] = data["TagValue"]
    if data.get("ResourceQuery") is not None:
        import capo_resource_groups.types.resource_query

        out["resource_query"] = (
            capo_resource_groups.types.resource_query.deserialize_json(
                data["ResourceQuery"]
            )
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("StartTagSyncTaskInput.role_arn required")
    return out
