"""Generated from Smithy shape ``com.amazonaws.connect#TagContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.contact_id
    import capo_connect.types.contact_tag_map
    import capo_connect.types.instance_id


class TagContactRequest(TypedDict, closed=True):
    contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact in this instance of Connect Customer. </p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    tags: "capo_connect.types.contact_tag_map.ContactTagMap"
    """<p>The tags to be assigned to the contact resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p> <note> <p>Authorization is not supported by this tag.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagContactRequest) -> dict:
    out: dict = {}
    out["ContactId"] = value["contact_id"]
    out["InstanceId"] = value["instance_id"]
    import capo_connect.types.contact_tag_map

    out["Tags"] = capo_connect.types.contact_tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagContactRequest:
    out: TagContactRequest = {}  # type: ignore[typeddict-item]
    if data.get("ContactId") is not None:
        out["contact_id"] = data["ContactId"]
    else:
        raise DeserializationError("TagContactRequest.contact_id required")
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("TagContactRequest.instance_id required")
    if data.get("Tags") is not None:
        import capo_connect.types.contact_tag_map

        out["tags"] = capo_connect.types.contact_tag_map.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("TagContactRequest.tags required")
    return out
