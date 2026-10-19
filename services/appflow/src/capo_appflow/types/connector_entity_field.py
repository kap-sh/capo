"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorEntityField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.boolean
    import capo_appflow.types.custom_properties
    import capo_appflow.types.description
    import capo_appflow.types.destination_field_properties
    import capo_appflow.types.identifier
    import capo_appflow.types.label
    import capo_appflow.types.source_field_properties
    import capo_appflow.types.string
    import capo_appflow.types.supported_field_type_details


class ConnectorEntityField(TypedDict, closed=True):
    identifier: "capo_appflow.types.identifier.Identifier"
    """<p> The unique identifier of the connector field. </p>"""
    parent_identifier: NotRequired["capo_appflow.types.identifier.Identifier"]
    """<p>The parent identifier of the connector field.</p>"""
    label: NotRequired["capo_appflow.types.label.Label"]
    """<p> The label applied to a connector entity field. </p>"""
    is_primary_key: "capo_appflow.types.boolean.Boolean"
    """<p>Booelan value that indicates whether this field can be used as a primary key.</p>"""
    default_value: NotRequired["capo_appflow.types.string.String"]
    """<p>Default value that can be assigned to this field.</p>"""
    is_deprecated: "capo_appflow.types.boolean.Boolean"
    """<p>Booelan value that indicates whether this field is deprecated or not.</p>"""
    supported_field_type_details: NotRequired[
        "capo_appflow.types.supported_field_type_details.SupportedFieldTypeDetails"
    ]
    """<p> Contains details regarding the supported <code>FieldType</code>, including the corresponding <code>filterOperators</code> and <code>supportedValues</code>. </p>"""
    description: NotRequired["capo_appflow.types.description.Description"]
    """<p> A description of the connector entity field. </p>"""
    source_properties: NotRequired[
        "capo_appflow.types.source_field_properties.SourceFieldProperties"
    ]
    """<p> The properties that can be applied to a field when the connector is being used as a source. </p>"""
    destination_properties: NotRequired[
        "capo_appflow.types.destination_field_properties.DestinationFieldProperties"
    ]
    """<p> The properties applied to a field when the connector is being used as a destination. </p>"""
    custom_properties: NotRequired[
        "capo_appflow.types.custom_properties.CustomProperties"
    ]
    """<p>A map that has specific properties related to the ConnectorEntityField.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorEntityField) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    if "parent_identifier" in value:
        out["parentIdentifier"] = value["parent_identifier"]
    if "label" in value:
        out["label"] = value["label"]
    out["isPrimaryKey"] = value.get("is_primary_key", False)
    if "default_value" in value:
        out["defaultValue"] = value["default_value"]
    out["isDeprecated"] = value.get("is_deprecated", False)
    if "supported_field_type_details" in value:
        import capo_appflow.types.supported_field_type_details

        out["supportedFieldTypeDetails"] = (
            capo_appflow.types.supported_field_type_details.serialize_json(
                value["supported_field_type_details"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "source_properties" in value:
        import capo_appflow.types.source_field_properties

        out["sourceProperties"] = (
            capo_appflow.types.source_field_properties.serialize_json(
                value["source_properties"]
            )
        )
    if "destination_properties" in value:
        import capo_appflow.types.destination_field_properties

        out["destinationProperties"] = (
            capo_appflow.types.destination_field_properties.serialize_json(
                value["destination_properties"]
            )
        )
    if "custom_properties" in value:
        import capo_appflow.types.custom_properties

        out["customProperties"] = capo_appflow.types.custom_properties.serialize_json(
            value["custom_properties"]
        )
    return out


def deserialize_json(data: dict) -> ConnectorEntityField:
    out: ConnectorEntityField = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    if data.get("parentIdentifier") is not None:
        out["parent_identifier"] = data["parentIdentifier"]
    if data.get("label") is not None:
        out["label"] = data["label"]
    if data.get("isPrimaryKey") is not None:
        out["is_primary_key"] = data["isPrimaryKey"]
    else:
        out["is_primary_key"] = False
    if data.get("defaultValue") is not None:
        out["default_value"] = data["defaultValue"]
    if data.get("isDeprecated") is not None:
        out["is_deprecated"] = data["isDeprecated"]
    else:
        out["is_deprecated"] = False
    if data.get("supportedFieldTypeDetails") is not None:
        import capo_appflow.types.supported_field_type_details

        out["supported_field_type_details"] = (
            capo_appflow.types.supported_field_type_details.deserialize_json(
                data["supportedFieldTypeDetails"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("sourceProperties") is not None:
        import capo_appflow.types.source_field_properties

        out["source_properties"] = (
            capo_appflow.types.source_field_properties.deserialize_json(
                data["sourceProperties"]
            )
        )
    if data.get("destinationProperties") is not None:
        import capo_appflow.types.destination_field_properties

        out["destination_properties"] = (
            capo_appflow.types.destination_field_properties.deserialize_json(
                data["destinationProperties"]
            )
        )
    if data.get("customProperties") is not None:
        import capo_appflow.types.custom_properties

        out["custom_properties"] = (
            capo_appflow.types.custom_properties.deserialize_json(
                data["customProperties"]
            )
        )
    return out
