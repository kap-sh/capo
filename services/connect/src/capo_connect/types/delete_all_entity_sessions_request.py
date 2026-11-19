"""Generated from Smithy shape ``com.amazonaws.connect#DeleteAllEntitySessionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.entity_id
    import capo_connect.types.instance_id
    import capo_connect.types.session_entity_type


class DeleteAllEntitySessionsRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    entity_id: "capo_connect.types.entity_id.EntityId"
    """<p>The identifier of the entity whose sessions you want to delete. For <code>USER</code>, use the user ID or the user ARN.</p>"""
    entity_type: "capo_connect.types.session_entity_type.SessionEntityType"
    """<p>The type of entity whose sessions you want to delete.</p> <note> <p>The only valid value is <code>USER</code>, which signs out a user in your Connect Customer instance.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAllEntitySessionsRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    out["EntityId"] = value["entity_id"]
    import capo_connect.types.session_entity_type

    out["EntityType"] = capo_connect.types.session_entity_type.serialize_json(
        value["entity_type"]
    )
    return out


def deserialize_json(data: dict) -> DeleteAllEntitySessionsRequest:
    out: DeleteAllEntitySessionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        out["instance_id"] = ""
    if data.get("EntityId") is not None:
        out["entity_id"] = data["EntityId"]
    else:
        out["entity_id"] = ""
    if data.get("EntityType") is not None:
        import capo_connect.types.session_entity_type

        out["entity_type"] = capo_connect.types.session_entity_type.deserialize_json(
            data["EntityType"]
        )
    else:
        import typing

        out["entity_type"] = typing.cast(
            "capo_connect.types.session_entity_type.SessionEntityType", ""
        )
    return out
