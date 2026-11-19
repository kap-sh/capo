"""Generated from Smithy shape ``com.amazonaws.fms#ResourceSetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.base62_id
    import capo_fms.types.description
    import capo_fms.types.name
    import capo_fms.types.resource_set_status
    import capo_fms.types.time_stamp


class ResourceSetSummary(TypedDict, closed=True):
    id: NotRequired["capo_fms.types.base62_id.Base62Id"]
    """<p>A unique identifier for the resource set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.</p>"""
    name: NotRequired["capo_fms.types.name.Name"]
    """<p>The descriptive name of the resource set. You can't change the name of a resource set after you create it.</p>"""
    description: NotRequired["capo_fms.types.description.Description"]
    """<p>A description of the resource set.</p>"""
    last_update_time: NotRequired["capo_fms.types.time_stamp.TimeStamp"]
    """<p>The last time that the resource set was changed.</p>"""
    resource_set_status: NotRequired[
        "capo_fms.types.resource_set_status.ResourceSetStatus"
    ]
    """<p>Indicates whether the resource set is in or out of an admin's Region scope.</p> <ul> <li> <p> <code>ACTIVE</code> - The administrator can manage and delete the resource set.</p> </li> <li> <p> <code>OUT_OF_ADMIN_SCOPE</code> - The administrator can view the resource set, but they can't edit or delete the resource set. Existing protections stay in place. Any new resource that come into scope of the resource set won't be protected.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceSetSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
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


def deserialize_aws_json_1_1(data: dict) -> ResourceSetSummary:
    out: ResourceSetSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
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


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceSetSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "last_update_time" in value:
        import capo_fms.types.time_stamp

        out["LastUpdateTime"] = capo_fms.types.time_stamp.serialize_cbor(
            value["last_update_time"]
        )
    if "resource_set_status" in value:
        import capo_fms.types.resource_set_status

        out["ResourceSetStatus"] = capo_fms.types.resource_set_status.serialize_cbor(
            value["resource_set_status"]
        )
    return out


def deserialize_cbor(data: dict) -> ResourceSetSummary:
    out: ResourceSetSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("LastUpdateTime") is not None:
        import capo_fms.types.time_stamp

        out["last_update_time"] = capo_fms.types.time_stamp.deserialize_cbor(
            data["LastUpdateTime"]
        )
    if data.get("ResourceSetStatus") is not None:
        import capo_fms.types.resource_set_status

        out["resource_set_status"] = (
            capo_fms.types.resource_set_status.deserialize_cbor(
                data["ResourceSetStatus"]
            )
        )
    return out
