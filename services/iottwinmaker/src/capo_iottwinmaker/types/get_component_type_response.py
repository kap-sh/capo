"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#GetComponentTypeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.boolean
    import capo_iottwinmaker.types.component_type_id
    import capo_iottwinmaker.types.component_type_name
    import capo_iottwinmaker.types.composite_component_types_response
    import capo_iottwinmaker.types.description
    import capo_iottwinmaker.types.extends_from
    import capo_iottwinmaker.types.functions_response
    import capo_iottwinmaker.types.id
    import capo_iottwinmaker.types.property_definitions_response
    import capo_iottwinmaker.types.property_groups_response
    import capo_iottwinmaker.types.status
    import capo_iottwinmaker.types.sync_source
    import capo_iottwinmaker.types.timestamp
    import capo_iottwinmaker.types.twin_maker_arn


class GetComponentTypeResponse(TypedDict, closed=True):
    workspace_id: "capo_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace that contains the component type.</p>"""
    is_singleton: NotRequired["capo_iottwinmaker.types.boolean.Boolean"]
    """<p>A Boolean value that specifies whether an entity can have more than one component of this type.</p>"""
    component_type_id: "capo_iottwinmaker.types.component_type_id.ComponentTypeId"
    """<p>The ID of the component type.</p>"""
    description: NotRequired["capo_iottwinmaker.types.description.Description"]
    """<p>The description of the component type.</p>"""
    property_definitions: NotRequired[
        "capo_iottwinmaker.types.property_definitions_response.PropertyDefinitionsResponse"
    ]
    """<p>An object that maps strings to the property definitions in the component type. Each string in the mapping must be unique to this object.</p>"""
    extends_from: NotRequired["capo_iottwinmaker.types.extends_from.ExtendsFrom"]
    """<p>The name of the parent component type that this component type extends.</p>"""
    functions: NotRequired[
        "capo_iottwinmaker.types.functions_response.FunctionsResponse"
    ]
    """<p>An object that maps strings to the functions in the component type. Each string in the mapping must be unique to this object.</p>"""
    creation_date_time: "capo_iottwinmaker.types.timestamp.Timestamp"
    """<p>The date and time when the component type was created.</p>"""
    update_date_time: "capo_iottwinmaker.types.timestamp.Timestamp"
    """<p>The date and time when the component was last updated.</p>"""
    arn: "capo_iottwinmaker.types.twin_maker_arn.TwinMakerArn"
    """<p>The ARN of the component type.</p>"""
    is_abstract: NotRequired["capo_iottwinmaker.types.boolean.Boolean"]
    """<p>A Boolean value that specifies whether the component type is abstract.</p>"""
    is_schema_initialized: NotRequired["capo_iottwinmaker.types.boolean.Boolean"]
    """<p>A Boolean value that specifies whether the component type has a schema initializer and that the schema initializer has run.</p>"""
    status: NotRequired["capo_iottwinmaker.types.status.Status"]
    """<p>The current status of the component type.</p>"""
    property_groups: NotRequired[
        "capo_iottwinmaker.types.property_groups_response.PropertyGroupsResponse"
    ]
    """<p>The maximum number of results to return at one time. The default is 25.</p> <p>Valid Range: Minimum value of 1. Maximum value of 250.</p>"""
    sync_source: NotRequired["capo_iottwinmaker.types.sync_source.SyncSource"]
    """<p>The syncSource of the SyncJob, if this entity was created by a SyncJob.</p>"""
    component_type_name: NotRequired[
        "capo_iottwinmaker.types.component_type_name.ComponentTypeName"
    ]
    """<p>The component type name.</p>"""
    composite_component_types: NotRequired[
        "capo_iottwinmaker.types.composite_component_types_response.CompositeComponentTypesResponse"
    ]
    """<p>This is an object that maps strings to <code>compositeComponentTypes</code> of the <code>componentType</code>. <code>CompositeComponentType</code> is referenced by <code>componentTypeId</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetComponentTypeResponse) -> dict:
    out: dict = {}
    out["workspaceId"] = value["workspace_id"]
    if "is_singleton" in value:
        out["isSingleton"] = value["is_singleton"]
    out["componentTypeId"] = value["component_type_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "property_definitions" in value:
        import capo_iottwinmaker.types.property_definitions_response

        out["propertyDefinitions"] = (
            capo_iottwinmaker.types.property_definitions_response.serialize_json(
                value["property_definitions"]
            )
        )
    if "extends_from" in value:
        import capo_iottwinmaker.types.extends_from

        out["extendsFrom"] = capo_iottwinmaker.types.extends_from.serialize_json(
            value["extends_from"]
        )
    if "functions" in value:
        import capo_iottwinmaker.types.functions_response

        out["functions"] = capo_iottwinmaker.types.functions_response.serialize_json(
            value["functions"]
        )
    import capo_iottwinmaker.types.timestamp

    out["creationDateTime"] = capo_iottwinmaker.types.timestamp.serialize_json(
        value["creation_date_time"]
    )
    import capo_iottwinmaker.types.timestamp

    out["updateDateTime"] = capo_iottwinmaker.types.timestamp.serialize_json(
        value["update_date_time"]
    )
    out["arn"] = value["arn"]
    if "is_abstract" in value:
        out["isAbstract"] = value["is_abstract"]
    if "is_schema_initialized" in value:
        out["isSchemaInitialized"] = value["is_schema_initialized"]
    if "status" in value:
        import capo_iottwinmaker.types.status

        out["status"] = capo_iottwinmaker.types.status.serialize_json(value["status"])
    if "property_groups" in value:
        import capo_iottwinmaker.types.property_groups_response

        out["propertyGroups"] = (
            capo_iottwinmaker.types.property_groups_response.serialize_json(
                value["property_groups"]
            )
        )
    if "sync_source" in value:
        out["syncSource"] = value["sync_source"]
    if "component_type_name" in value:
        out["componentTypeName"] = value["component_type_name"]
    if "composite_component_types" in value:
        import capo_iottwinmaker.types.composite_component_types_response

        out["compositeComponentTypes"] = (
            capo_iottwinmaker.types.composite_component_types_response.serialize_json(
                value["composite_component_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetComponentTypeResponse:
    out: GetComponentTypeResponse = {}  # type: ignore[typeddict-item]
    if data.get("workspaceId") is not None:
        out["workspace_id"] = data["workspaceId"]
    else:
        out["workspace_id"] = ""
    if data.get("isSingleton") is not None:
        out["is_singleton"] = data["isSingleton"]
    if data.get("componentTypeId") is not None:
        out["component_type_id"] = data["componentTypeId"]
    else:
        out["component_type_id"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("propertyDefinitions") is not None:
        import capo_iottwinmaker.types.property_definitions_response

        out["property_definitions"] = (
            capo_iottwinmaker.types.property_definitions_response.deserialize_json(
                data["propertyDefinitions"]
            )
        )
    if data.get("extendsFrom") is not None:
        import capo_iottwinmaker.types.extends_from

        out["extends_from"] = capo_iottwinmaker.types.extends_from.deserialize_json(
            data["extendsFrom"]
        )
    if data.get("functions") is not None:
        import capo_iottwinmaker.types.functions_response

        out["functions"] = capo_iottwinmaker.types.functions_response.deserialize_json(
            data["functions"]
        )
    if data.get("creationDateTime") is not None:
        import capo_iottwinmaker.types.timestamp

        out["creation_date_time"] = capo_iottwinmaker.types.timestamp.deserialize_json(
            data["creationDateTime"]
        )
    else:
        import datetime

        out["creation_date_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("updateDateTime") is not None:
        import capo_iottwinmaker.types.timestamp

        out["update_date_time"] = capo_iottwinmaker.types.timestamp.deserialize_json(
            data["updateDateTime"]
        )
    else:
        import datetime

        out["update_date_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("isAbstract") is not None:
        out["is_abstract"] = data["isAbstract"]
    if data.get("isSchemaInitialized") is not None:
        out["is_schema_initialized"] = data["isSchemaInitialized"]
    if data.get("status") is not None:
        import capo_iottwinmaker.types.status

        out["status"] = capo_iottwinmaker.types.status.deserialize_json(data["status"])
    if data.get("propertyGroups") is not None:
        import capo_iottwinmaker.types.property_groups_response

        out["property_groups"] = (
            capo_iottwinmaker.types.property_groups_response.deserialize_json(
                data["propertyGroups"]
            )
        )
    if data.get("syncSource") is not None:
        out["sync_source"] = data["syncSource"]
    if data.get("componentTypeName") is not None:
        out["component_type_name"] = data["componentTypeName"]
    if data.get("compositeComponentTypes") is not None:
        import capo_iottwinmaker.types.composite_component_types_response

        out["composite_component_types"] = (
            capo_iottwinmaker.types.composite_component_types_response.deserialize_json(
                data["compositeComponentTypes"]
            )
        )
    return out
