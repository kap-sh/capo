"""Generated from Smithy shape ``com.amazonaws.connect#SearchResourceTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.instance_id_or_arn
    import capo_connect.types.max_result100
    import capo_connect.types.next_token2500
    import capo_connect.types.resource_tags_search_criteria
    import capo_connect.types.resource_type_list


class SearchResourceTagsRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id_or_arn.InstanceIdOrArn"
    """<p>The identifier of the Connect Customer instance. You can find the instanceId in the Amazon Resource Name (ARN) of the instance.</p>"""
    resource_types: NotRequired[
        "capo_connect.types.resource_type_list.ResourceTypeList"
    ]
    """<p>The list of resource types to be used to search tags from. If not provided or if any empty list is provided, this API will search from all supported resource types. Note that lowercase and - are required.</p> <p class="title"> <b>Supported resource types</b> </p> <ul> <li> <p>agent</p> </li> <li> <p>agent-state</p> </li> <li> <p>routing-profile</p> </li> <li> <p>standard-queue</p> </li> <li> <p>security-profile</p> </li> <li> <p>operating-hours</p> </li> <li> <p>prompt</p> </li> <li> <p>contact-flow</p> </li> <li> <p>flow- module</p> </li> <li> <p>transfer-destination (also known as quick connect)</p> </li> <li> <p>metric</p> </li> </ul>"""
    next_token: NotRequired["capo_connect.types.next_token2500.NextToken2500"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["capo_connect.types.max_result100.MaxResult100"]
    """<p>The maximum number of results to return per page.</p>"""
    search_criteria: NotRequired[
        "capo_connect.types.resource_tags_search_criteria.ResourceTagsSearchCriteria"
    ]
    """<p>The search criteria to be used to return tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchResourceTagsRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    if "resource_types" in value:
        import capo_connect.types.resource_type_list

        out["ResourceTypes"] = capo_connect.types.resource_type_list.serialize_json(
            value["resource_types"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "search_criteria" in value:
        import capo_connect.types.resource_tags_search_criteria

        out["SearchCriteria"] = (
            capo_connect.types.resource_tags_search_criteria.serialize_json(
                value["search_criteria"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchResourceTagsRequest:
    out: SearchResourceTagsRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("SearchResourceTagsRequest.instance_id required")
    if data.get("ResourceTypes") is not None:
        import capo_connect.types.resource_type_list

        out["resource_types"] = capo_connect.types.resource_type_list.deserialize_json(
            data["ResourceTypes"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("SearchCriteria") is not None:
        import capo_connect.types.resource_tags_search_criteria

        out["search_criteria"] = (
            capo_connect.types.resource_tags_search_criteria.deserialize_json(
                data["SearchCriteria"]
            )
        )
    return out
