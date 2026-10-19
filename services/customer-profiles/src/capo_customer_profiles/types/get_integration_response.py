"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetIntegrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.event_trigger_names
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.object_type_names
    import capo_customer_profiles.types.optional_boolean
    import capo_customer_profiles.types.role_arn
    import capo_customer_profiles.types.scope
    import capo_customer_profiles.types.string1_to255
    import capo_customer_profiles.types.tag_map
    import capo_customer_profiles.types.timestamp
    import capo_customer_profiles.types.type_name


class GetIntegrationResponse(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    uri: "capo_customer_profiles.types.string1_to255.string1To255"
    """<p>The URI of the S3 bucket or any other type of data source.</p>"""
    object_type_name: NotRequired["capo_customer_profiles.types.type_name.typeName"]
    """<p>The name of the profile object type.</p>"""
    created_at: "capo_customer_profiles.types.timestamp.timestamp"
    """<p>The timestamp of when the domain was created.</p>"""
    last_updated_at: "capo_customer_profiles.types.timestamp.timestamp"
    """<p>The timestamp of when the domain was most recently edited.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    object_type_names: NotRequired[
        "capo_customer_profiles.types.object_type_names.ObjectTypeNames"
    ]
    """<p>A map in which each key is an event type from an external application such as Segment or Shopify, and each value is an <code>ObjectTypeName</code> (template) used to ingest the event. It supports the following event types: <code>SegmentIdentify</code>, <code>ShopifyCreateCustomers</code>, <code>ShopifyUpdateCustomers</code>, <code>ShopifyCreateDraftOrders</code>, <code>ShopifyUpdateDraftOrders</code>, <code>ShopifyCreateOrders</code>, and <code>ShopifyUpdatedOrders</code>.</p>"""
    workflow_id: NotRequired["capo_customer_profiles.types.string1_to255.string1To255"]
    """<p>Unique identifier for the workflow.</p>"""
    is_unstructured: NotRequired[
        "capo_customer_profiles.types.optional_boolean.optionalBoolean"
    ]
    """<p>Boolean that shows if the Flow that's associated with the Integration is created in Amazon Appflow, or with ObjectTypeName equals _unstructured via API/CLI in flowDefinition.</p>"""
    role_arn: NotRequired["capo_customer_profiles.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role. The Integration uses this role to make Customer Profiles requests on your behalf.</p>"""
    event_trigger_names: NotRequired[
        "capo_customer_profiles.types.event_trigger_names.EventTriggerNames"
    ]
    """<p>A list of unique names for active event triggers associated with the integration. This list would be empty if no Event Trigger is associated with the integration.</p>"""
    scope: NotRequired["capo_customer_profiles.types.scope.Scope"]
    """<p>Specifies whether the integration applies to profile level data (associated with profiles) or domain level data (not associated with any specific profile). The default value is PROFILE.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIntegrationResponse) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    out["Uri"] = value["uri"]
    if "object_type_name" in value:
        out["ObjectTypeName"] = value["object_type_name"]
    import capo_customer_profiles.types.timestamp

    out["CreatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_customer_profiles.types.timestamp

    out["LastUpdatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
        value["last_updated_at"]
    )
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    if "object_type_names" in value:
        import capo_customer_profiles.types.object_type_names

        out["ObjectTypeNames"] = (
            capo_customer_profiles.types.object_type_names.serialize_json(
                value["object_type_names"]
            )
        )
    if "workflow_id" in value:
        out["WorkflowId"] = value["workflow_id"]
    if "is_unstructured" in value:
        out["IsUnstructured"] = value["is_unstructured"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "event_trigger_names" in value:
        import capo_customer_profiles.types.event_trigger_names

        out["EventTriggerNames"] = (
            capo_customer_profiles.types.event_trigger_names.serialize_json(
                value["event_trigger_names"]
            )
        )
    if "scope" in value:
        import capo_customer_profiles.types.scope

        out["Scope"] = capo_customer_profiles.types.scope.serialize_json(value["scope"])
    return out


def deserialize_json(data: dict) -> GetIntegrationResponse:
    out: GetIntegrationResponse = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    if data.get("Uri") is not None:
        out["uri"] = data["Uri"]
    else:
        out["uri"] = ""
    if data.get("ObjectTypeName") is not None:
        out["object_type_name"] = data["ObjectTypeName"]
    if data.get("CreatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["created_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("LastUpdatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["last_updated_at"] = (
            capo_customer_profiles.types.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    else:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("Tags") is not None:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    if data.get("ObjectTypeNames") is not None:
        import capo_customer_profiles.types.object_type_names

        out["object_type_names"] = (
            capo_customer_profiles.types.object_type_names.deserialize_json(
                data["ObjectTypeNames"]
            )
        )
    if data.get("WorkflowId") is not None:
        out["workflow_id"] = data["WorkflowId"]
    if data.get("IsUnstructured") is not None:
        out["is_unstructured"] = data["IsUnstructured"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("EventTriggerNames") is not None:
        import capo_customer_profiles.types.event_trigger_names

        out["event_trigger_names"] = (
            capo_customer_profiles.types.event_trigger_names.deserialize_json(
                data["EventTriggerNames"]
            )
        )
    if data.get("Scope") is not None:
        import capo_customer_profiles.types.scope

        out["scope"] = capo_customer_profiles.types.scope.deserialize_json(
            data["Scope"]
        )
    return out
