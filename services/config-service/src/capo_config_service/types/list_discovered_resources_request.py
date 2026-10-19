"""Generated from Smithy shape ``com.amazonaws.configservice#ListDiscoveredResourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.boolean
    import capo_config_service.types.limit
    import capo_config_service.types.next_token
    import capo_config_service.types.resource_id_list
    import capo_config_service.types.resource_name
    import capo_config_service.types.resource_type


class ListDiscoveredResourcesRequest(TypedDict, closed=True):
    resource_type: "capo_config_service.types.resource_type.ResourceType"
    """<p>The type of resources that you want Config to list in the response.</p>"""
    resource_ids: NotRequired[
        "capo_config_service.types.resource_id_list.ResourceIdList"
    ]
    """<p>The IDs of only those resources that you want Config to list in the response. If you do not specify this parameter, Config lists all resources of the specified type that it has discovered. You can list a minimum of 1 resourceID and a maximum of 20 resourceIds.</p>"""
    resource_name: NotRequired["capo_config_service.types.resource_name.ResourceName"]
    """<p>The custom name of only those resources that you want Config to list in the response. If you do not specify this parameter, Config lists all resources of the specified type that it has discovered.</p>"""
    limit: NotRequired["capo_config_service.types.limit.Limit"]
    """<p>The maximum number of resource identifiers returned on each page. The default is 100. You cannot specify a number greater than 100. If you specify 0, Config uses the default.</p>"""
    include_deleted_resources: NotRequired["capo_config_service.types.boolean.Boolean"]
    """<p>Specifies whether Config includes deleted resources in the results. By default, deleted resources are not included.</p>"""
    next_token: NotRequired["capo_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDiscoveredResourcesRequest) -> dict:
    out: dict = {}
    import capo_config_service.types.resource_type

    out["resourceType"] = (
        capo_config_service.types.resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    )
    if "resource_ids" in value:
        import capo_config_service.types.resource_id_list

        out["resourceIds"] = (
            capo_config_service.types.resource_id_list.serialize_aws_json_1_1(
                value["resource_ids"]
            )
        )
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    if "limit" in value:
        out["limit"] = value["limit"]
    if "include_deleted_resources" in value:
        out["includeDeletedResources"] = value["include_deleted_resources"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDiscoveredResourcesRequest:
    out: ListDiscoveredResourcesRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceType") is not None:
        import capo_config_service.types.resource_type

        out["resource_type"] = (
            capo_config_service.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    else:
        import typing

        out["resource_type"] = typing.cast(
            "capo_config_service.types.resource_type.ResourceType", ""
        )
    if data.get("resourceIds") is not None:
        import capo_config_service.types.resource_id_list

        out["resource_ids"] = (
            capo_config_service.types.resource_id_list.deserialize_aws_json_1_1(
                data["resourceIds"]
            )
        )
    if data.get("resourceName") is not None:
        out["resource_name"] = data["resourceName"]
    if data.get("limit") is not None:
        out["limit"] = data["limit"]
    if data.get("includeDeletedResources") is not None:
        out["include_deleted_resources"] = data["includeDeletedResources"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
