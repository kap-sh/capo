"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#Entity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.entity_attributes
    import capo_cloudwatch_logs.types.entity_key_attributes


class Entity(TypedDict, closed=True):
    key_attributes: NotRequired[
        "capo_cloudwatch_logs.types.entity_key_attributes.EntityKeyAttributes"
    ]
    """<p>The attributes of the entity which identify the specific entity, as a list of key-value pairs. Entities with the same <code>keyAttributes</code> are considered to be the same entity.</p> <p>There are five allowed attributes (key names): <code>Type</code>, <code>ResourceType</code>, <code>Identifier</code> <code>Name</code>, and <code>Environment</code>.</p> <p>For details about how to use the key attributes, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/adding-your-own-related-telemetry.html">How to add related information to telemetry</a> in the <i>CloudWatch User Guide</i>.</p>"""
    attributes: NotRequired[
        "capo_cloudwatch_logs.types.entity_attributes.EntityAttributes"
    ]
    """<p>Additional attributes of the entity that are not used to specify the identity of the entity. A list of key-value pairs.</p> <p>For details about how to use the attributes, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/adding-your-own-related-telemetry.html">How to add related information to telemetry</a> in the <i>CloudWatch User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Entity) -> dict:
    out: dict = {}
    if "key_attributes" in value:
        import capo_cloudwatch_logs.types.entity_key_attributes

        out["keyAttributes"] = (
            capo_cloudwatch_logs.types.entity_key_attributes.serialize_aws_json_1_1(
                value["key_attributes"]
            )
        )
    if "attributes" in value:
        import capo_cloudwatch_logs.types.entity_attributes

        out["attributes"] = (
            capo_cloudwatch_logs.types.entity_attributes.serialize_aws_json_1_1(
                value["attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Entity:
    out: Entity = {}  # type: ignore[typeddict-item]
    if data.get("keyAttributes") is not None:
        import capo_cloudwatch_logs.types.entity_key_attributes

        out["key_attributes"] = (
            capo_cloudwatch_logs.types.entity_key_attributes.deserialize_aws_json_1_1(
                data["keyAttributes"]
            )
        )
    if data.get("attributes") is not None:
        import capo_cloudwatch_logs.types.entity_attributes

        out["attributes"] = (
            capo_cloudwatch_logs.types.entity_attributes.deserialize_aws_json_1_1(
                data["attributes"]
            )
        )
    return out
