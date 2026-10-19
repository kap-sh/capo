"""Generated from Smithy shape ``com.amazonaws.kendra#EntityConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.entity_id
    import capo_kendra.types.entity_type


class EntityConfiguration(TypedDict, closed=True):
    entity_id: "capo_kendra.types.entity_id.EntityId"
    """<p>The identifier of a user or group in your IAM Identity Center identity source. For example, a user ID could be an email.</p>"""
    entity_type: "capo_kendra.types.entity_type.EntityType"
    """<p>Specifies whether you are configuring a <code>User</code> or a <code>Group</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityConfiguration) -> dict:
    out: dict = {}
    out["EntityId"] = value["entity_id"]
    import capo_kendra.types.entity_type

    out["EntityType"] = capo_kendra.types.entity_type.serialize_aws_json_1_1(
        value["entity_type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityConfiguration:
    out: EntityConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("EntityId") is not None:
        out["entity_id"] = data["EntityId"]
    else:
        out["entity_id"] = ""
    if data.get("EntityType") is not None:
        import capo_kendra.types.entity_type

        out["entity_type"] = capo_kendra.types.entity_type.deserialize_aws_json_1_1(
            data["EntityType"]
        )
    else:
        import typing

        out["entity_type"] = typing.cast("capo_kendra.types.entity_type.EntityType", "")
    return out
