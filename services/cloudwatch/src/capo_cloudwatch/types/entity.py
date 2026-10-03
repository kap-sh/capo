"""Generated from Smithy shape ``com.amazonaws.cloudwatch#Entity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.entity_attributes_map
    import capo_cloudwatch.types.entity_key_attributes_map


class Entity(TypedDict, closed=True):
    key_attributes: NotRequired[
        "capo_cloudwatch.types.entity_key_attributes_map.EntityKeyAttributesMap"
    ]
    """<p>The attributes of the entity which identify the specific entity, as a list of key-value pairs. Entities with the same <code>KeyAttributes</code> are considered to be the same entity. For an entity to be valid, the <code>KeyAttributes</code> must exist and be formatted correctly.</p> <p>There are five allowed attributes (key names): <code>Type</code>, <code>ResourceType</code>, <code>Identifier</code>, <code>Name</code>, and <code>Environment</code>.</p> <p>For details about how to use the key attributes to specify an entity, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/adding-your-own-related-telemetry.html">How to add related information to telemetry</a> in the <i>CloudWatch User Guide</i>.</p>"""
    attributes: NotRequired[
        "capo_cloudwatch.types.entity_attributes_map.EntityAttributesMap"
    ]
    """<p>Additional attributes of the entity that are not used to specify the identity of the entity. A list of key-value pairs.</p> <p>For details about how to use the attributes, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/adding-your-own-related-telemetry.html">How to add related information to telemetry</a> in the <i>CloudWatch User Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Entity) -> dict:
    out: dict = {}
    if "key_attributes" in value:
        import capo_cloudwatch.types.entity_key_attributes_map

        out["KeyAttributes"] = (
            capo_cloudwatch.types.entity_key_attributes_map.serialize_aws_json_1_0(
                value["key_attributes"]
            )
        )
    if "attributes" in value:
        import capo_cloudwatch.types.entity_attributes_map

        out["Attributes"] = (
            capo_cloudwatch.types.entity_attributes_map.serialize_aws_json_1_0(
                value["attributes"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Entity:
    out: Entity = {}  # type: ignore[typeddict-item]
    if data.get("KeyAttributes") is not None:
        import capo_cloudwatch.types.entity_key_attributes_map

        out["key_attributes"] = (
            capo_cloudwatch.types.entity_key_attributes_map.deserialize_aws_json_1_0(
                data["KeyAttributes"]
            )
        )
    if data.get("Attributes") is not None:
        import capo_cloudwatch.types.entity_attributes_map

        out["attributes"] = (
            capo_cloudwatch.types.entity_attributes_map.deserialize_aws_json_1_0(
                data["Attributes"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(value: Entity, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "key_attributes" in value:
        import capo_cloudwatch.types.entity_key_attributes_map

        capo_cloudwatch.types.entity_key_attributes_map.serialize_query(
            value["key_attributes"], pairs, f"{key_prefix}KeyAttributes"
        )
    if "attributes" in value:
        import capo_cloudwatch.types.entity_attributes_map

        capo_cloudwatch.types.entity_attributes_map.serialize_query(
            value["attributes"], pairs, f"{key_prefix}Attributes"
        )


def deserialize_query(el: Element) -> Entity:
    out: Entity = {}  # type: ignore[typeddict-item]
    child_key_attributes = el.find("KeyAttributes")
    if child_key_attributes is not None:
        import capo_cloudwatch.types.entity_key_attributes_map

        out["key_attributes"] = (
            capo_cloudwatch.types.entity_key_attributes_map.deserialize_query(
                child_key_attributes
            )
        )
    child_attributes = el.find("Attributes")
    if child_attributes is not None:
        import capo_cloudwatch.types.entity_attributes_map

        out["attributes"] = (
            capo_cloudwatch.types.entity_attributes_map.deserialize_query(
                child_attributes
            )
        )
    return out
