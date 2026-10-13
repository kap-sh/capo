"""Generated from Smithy shape ``com.amazonaws.customerprofiles#PutIntegrationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.event_trigger_names
    import capo_customer_profiles.types.flow_definition
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.object_type_names
    import capo_customer_profiles.types.role_arn
    import capo_customer_profiles.types.scope
    import capo_customer_profiles.types.string1_to255
    import capo_customer_profiles.types.tag_map
    import capo_customer_profiles.types.type_name


class PutIntegrationRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    uri: NotRequired["capo_customer_profiles.types.string1_to255.string1To255"]
    """<p>The URI of the S3 bucket or any other type of data source.</p>"""
    object_type_name: NotRequired["capo_customer_profiles.types.type_name.typeName"]
    """<p>The name of the profile object type.</p>"""
    object_type_names: NotRequired[
        "capo_customer_profiles.types.object_type_names.ObjectTypeNames"
    ]
    """<p>A map in which each key is an event type from an external application such as Segment or Shopify, and each value is an <code>ObjectTypeName</code> (template) used to ingest the event. It supports the following event types: <code>SegmentIdentify</code>, <code>ShopifyCreateCustomers</code>, <code>ShopifyUpdateCustomers</code>, <code>ShopifyCreateDraftOrders</code>, <code>ShopifyUpdateDraftOrders</code>, <code>ShopifyCreateOrders</code>, and <code>ShopifyUpdatedOrders</code>.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    flow_definition: NotRequired[
        "capo_customer_profiles.types.flow_definition.FlowDefinition"
    ]
    """<p>The configuration that controls how Customer Profiles retrieves data from the source.</p>"""
    role_arn: NotRequired["capo_customer_profiles.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role. The Integration uses this role to make Customer Profiles requests on your behalf.</p>"""
    event_trigger_names: NotRequired[
        "capo_customer_profiles.types.event_trigger_names.EventTriggerNames"
    ]
    """<p>A list of unique names for active event triggers associated with the integration.</p>"""
    scope: NotRequired["capo_customer_profiles.types.scope.Scope"]
    """<p>Specifies whether the integration applies to profile level data (associated with profiles) or domain level data (not associated with any specific profile). The default value is PROFILE.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutIntegrationRequest) -> dict:
    out: dict = {}
    if "uri" in value:
        out["Uri"] = value["uri"]
    if "object_type_name" in value:
        out["ObjectTypeName"] = value["object_type_name"]
    if "object_type_names" in value:
        import capo_customer_profiles.types.object_type_names

        out["ObjectTypeNames"] = (
            capo_customer_profiles.types.object_type_names.serialize_json(
                value["object_type_names"]
            )
        )
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    if "flow_definition" in value:
        import capo_customer_profiles.types.flow_definition

        out["FlowDefinition"] = (
            capo_customer_profiles.types.flow_definition.serialize_json(
                value["flow_definition"]
            )
        )
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


def deserialize_json(data: dict) -> PutIntegrationRequest:
    out: PutIntegrationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Uri") is not None:
        out["uri"] = data["Uri"]
    if data.get("ObjectTypeName") is not None:
        out["object_type_name"] = data["ObjectTypeName"]
    if data.get("ObjectTypeNames") is not None:
        import capo_customer_profiles.types.object_type_names

        out["object_type_names"] = (
            capo_customer_profiles.types.object_type_names.deserialize_json(
                data["ObjectTypeNames"]
            )
        )
    if data.get("Tags") is not None:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    if data.get("FlowDefinition") is not None:
        import capo_customer_profiles.types.flow_definition

        out["flow_definition"] = (
            capo_customer_profiles.types.flow_definition.deserialize_json(
                data["FlowDefinition"]
            )
        )
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


def redact_sensitive(value: PutIntegrationRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "flow_definition" in value:
        out["flow_definition"] = "*** Sensitive Data Redacted ***"
    return out
