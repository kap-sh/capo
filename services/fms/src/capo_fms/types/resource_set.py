"""Generated from Smithy shape ``com.amazonaws.fms#ResourceSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.base62_id
    import capo_fms.types.description
    import capo_fms.types.name
    import capo_fms.types.resource_set_status
    import capo_fms.types.resource_type_list
    import capo_fms.types.time_stamp
    import capo_fms.types.update_token


class ResourceSet(TypedDict, closed=True):
    id: NotRequired["capo_fms.types.base62_id.Base62Id"]
    """<p>A unique identifier for the resource set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.</p>"""
    name: "capo_fms.types.name.Name"
    """<p>The descriptive name of the resource set. You can't change the name of a resource set after you create it.</p>"""
    description: NotRequired["capo_fms.types.description.Description"]
    """<p>A description of the resource set.</p>"""
    update_token: NotRequired["capo_fms.types.update_token.UpdateToken"]
    """<p>An optional token that you can use for optimistic locking. Firewall Manager returns a token to your requests that access the resource set. The token marks the state of the resource set resource at the time of the request. Update tokens are not allowed when creating a resource set. After creation, each subsequent update call to the resource set requires the update token. </p> <p>To make an unconditional change to the resource set, omit the token in your update request. Without the token, Firewall Manager performs your updates regardless of whether the resource set has changed since you last retrieved it.</p> <p>To make a conditional change to the resource set, provide the token in your update request. Firewall Manager uses the token to ensure that the resource set hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the resource set again to get a current copy of it with a new token. Reapply your changes as needed, then try the operation again using the new token. </p>"""
    resource_type_list: "capo_fms.types.resource_type_list.ResourceTypeList"
    """<p>Determines the resources that can be associated to the resource set. Depending on your setting for max results and the number of resource sets, a single call might not return the full list.</p>"""
    last_update_time: NotRequired["capo_fms.types.time_stamp.TimeStamp"]
    """<p>The last time that the resource set was changed.</p>"""
    resource_set_status: NotRequired[
        "capo_fms.types.resource_set_status.ResourceSetStatus"
    ]
    """<p>Indicates whether the resource set is in or out of an admin's Region scope.</p> <ul> <li> <p> <code>ACTIVE</code> - The administrator can manage and delete the resource set.</p> </li> <li> <p> <code>OUT_OF_ADMIN_SCOPE</code> - The administrator can view the resource set, but they can't edit or delete the resource set. Existing protections stay in place. Any new resource that come into scope of the resource set won't be protected.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceSet) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "update_token" in value:
        out["UpdateToken"] = value["update_token"]
    import capo_fms.types.resource_type_list

    out["ResourceTypeList"] = capo_fms.types.resource_type_list.serialize_aws_json_1_1(
        value["resource_type_list"]
    )
    if "last_update_time" in value:
        import capo_fms.types.time_stamp

        out["LastUpdateTime"] = capo_fms.types.time_stamp.serialize_aws_json_1_1(
            value["last_update_time"]
        )
    if "resource_set_status" in value:
        import capo_fms.types.resource_set_status

        out["ResourceSetStatus"] = (
            capo_fms.types.resource_set_status.serialize_aws_json_1_1(
                value["resource_set_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceSet:
    out: ResourceSet = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("UpdateToken") is not None:
        out["update_token"] = data["UpdateToken"]
    if data.get("ResourceTypeList") is not None:
        import capo_fms.types.resource_type_list

        out["resource_type_list"] = (
            capo_fms.types.resource_type_list.deserialize_aws_json_1_1(
                data["ResourceTypeList"]
            )
        )
    else:
        out["resource_type_list"] = []
    if data.get("LastUpdateTime") is not None:
        import capo_fms.types.time_stamp

        out["last_update_time"] = capo_fms.types.time_stamp.deserialize_aws_json_1_1(
            data["LastUpdateTime"]
        )
    if data.get("ResourceSetStatus") is not None:
        import capo_fms.types.resource_set_status

        out["resource_set_status"] = (
            capo_fms.types.resource_set_status.deserialize_aws_json_1_1(
                data["ResourceSetStatus"]
            )
        )
    return out
