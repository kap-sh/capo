"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#DissociateEntityFromThingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.entity_type
    import capo_iotthingsgraph.types.thing_name


class DissociateEntityFromThingRequest(TypedDict, closed=True):
    thing_name: "capo_iotthingsgraph.types.thing_name.ThingName"
    """<p>The name of the thing to disassociate.</p>"""
    entity_type: "capo_iotthingsgraph.types.entity_type.EntityType"
    """<p>The entity type from which to disassociate the thing.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DissociateEntityFromThingRequest) -> dict:
    out: dict = {}
    out["thingName"] = value["thing_name"]
    import capo_iotthingsgraph.types.entity_type

    out["entityType"] = capo_iotthingsgraph.types.entity_type.serialize_aws_json_1_1(
        value["entity_type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DissociateEntityFromThingRequest:
    out: DissociateEntityFromThingRequest = {}  # type: ignore[typeddict-item]
    if data.get("thingName") is not None:
        out["thing_name"] = data["thingName"]
    else:
        out["thing_name"] = ""
    if data.get("entityType") is not None:
        import capo_iotthingsgraph.types.entity_type

        out["entity_type"] = (
            capo_iotthingsgraph.types.entity_type.deserialize_aws_json_1_1(
                data["entityType"]
            )
        )
    else:
        import typing

        out["entity_type"] = typing.cast(
            "capo_iotthingsgraph.types.entity_type.EntityType", ""
        )
    return out
