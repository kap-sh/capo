"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ModifyingProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.property_value_type
    import capo_elasticsearch_service.types.string


class ModifyingProperties(TypedDict, closed=True):
    name: NotRequired["capo_elasticsearch_service.types.string.String"]
    """<p>The name of the property that is currently being modified.</p>"""
    active_value: NotRequired["capo_elasticsearch_service.types.string.String"]
    """<p>The current value of the domain property that is being modified.</p>"""
    pending_value: NotRequired["capo_elasticsearch_service.types.string.String"]
    """<p>The value that the property that is currently being modified will eventually have.</p>"""
    value_type: NotRequired[
        "capo_elasticsearch_service.types.property_value_type.PropertyValueType"
    ]
    """<p>The type of value that is currently being modified. Properties can have two types:</p> <ul> <li><b>PLAIN_TEXT</b>: Contain direct values such as "1", "True", or "c5.large.search".</li> <li><b>STRINGIFIED_JSON</b>: Contain content in JSON format, such as {"Enabled":"True"}".</li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModifyingProperties) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "active_value" in value:
        out["ActiveValue"] = value["active_value"]
    if "pending_value" in value:
        out["PendingValue"] = value["pending_value"]
    if "value_type" in value:
        import capo_elasticsearch_service.types.property_value_type

        out["ValueType"] = (
            capo_elasticsearch_service.types.property_value_type.serialize_json(
                value["value_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> ModifyingProperties:
    out: ModifyingProperties = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ActiveValue") is not None:
        out["active_value"] = data["ActiveValue"]
    if data.get("PendingValue") is not None:
        out["pending_value"] = data["PendingValue"]
    if data.get("ValueType") is not None:
        import capo_elasticsearch_service.types.property_value_type

        out["value_type"] = (
            capo_elasticsearch_service.types.property_value_type.deserialize_json(
                data["ValueType"]
            )
        )
    return out
