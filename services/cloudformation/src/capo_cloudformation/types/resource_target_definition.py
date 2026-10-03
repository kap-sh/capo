"""Generated from Smithy shape ``com.amazonaws.cloudformation#ResourceTargetDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.after_value
    import capo_cloudformation.types.after_value_from
    import capo_cloudformation.types.attribute_change_type
    import capo_cloudformation.types.before_value
    import capo_cloudformation.types.before_value_from
    import capo_cloudformation.types.live_resource_drift
    import capo_cloudformation.types.property_name
    import capo_cloudformation.types.requires_recreation
    import capo_cloudformation.types.resource_attribute
    import capo_cloudformation.types.resource_property_path


class ResourceTargetDefinition(TypedDict, closed=True):
    attribute: NotRequired[
        "capo_cloudformation.types.resource_attribute.ResourceAttribute"
    ]
    """<p>Indicates which resource attribute is triggering this update, such as a change in the resource attribute's <code>Metadata</code>, <code>Properties</code>, or <code>Tags</code>.</p>"""
    name: NotRequired["capo_cloudformation.types.property_name.PropertyName"]
    """<p>If the <code>Attribute</code> value is <code>Properties</code>, the name of the property. For all other attributes, the value is null.</p>"""
    requires_recreation: NotRequired[
        "capo_cloudformation.types.requires_recreation.RequiresRecreation"
    ]
    """<p>If the <code>Attribute</code> value is <code>Properties</code>, indicates whether a change to this property causes the resource to be recreated. The value can be <code>Never</code>, <code>Always</code>, or <code>Conditionally</code>. To determine the conditions for a <code>Conditionally</code> recreation, see the update behavior for that property in the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html">Amazon Web Services resource and property types reference</a> in the <i>CloudFormation User Guide</i>.</p>"""
    path: NotRequired[
        "capo_cloudformation.types.resource_property_path.ResourcePropertyPath"
    ]
    """<p>The property path of the property.</p>"""
    before_value: NotRequired["capo_cloudformation.types.before_value.BeforeValue"]
    """<p>The value of the property before the change is executed. Large values can be truncated.</p>"""
    after_value: NotRequired["capo_cloudformation.types.after_value.AfterValue"]
    """<p>The value of the property after the change is executed. Large values can be truncated.</p>"""
    before_value_from: NotRequired[
        "capo_cloudformation.types.before_value_from.BeforeValueFrom"
    ]
    """<p>Indicates the source of the before value. Valid values:</p> <ul> <li> <p> <code>ACTUAL_STATE</code> – The before value represents current actual state.</p> </li> <li> <p> <code>PREVIOUS_DEPLOYMENT_STATE</code> – The before value represents the previous CloudFormation deployment state.</p> </li> </ul> <p>Only present for drift-aware change sets.</p>"""
    after_value_from: NotRequired[
        "capo_cloudformation.types.after_value_from.AfterValueFrom"
    ]
    """<p>Indicates the source of the after value. Valid value:</p> <ul> <li> <p> <code>TEMPLATE</code> – The after value comes from the new template.</p> </li> </ul> <p>Only present for drift-aware change sets.</p>"""
    drift: NotRequired[
        "capo_cloudformation.types.live_resource_drift.LiveResourceDrift"
    ]
    """<p>Detailed drift information for the resource property, including actual values, previous deployment values, and drift detection timestamps.</p>"""
    attribute_change_type: NotRequired[
        "capo_cloudformation.types.attribute_change_type.AttributeChangeType"
    ]
    """<p>The type of change to be made to the property if the change is executed.</p> <ul> <li> <p> <code>Add</code> The item will be added.</p> </li> <li> <p> <code>Remove</code> The item will be removed.</p> </li> <li> <p> <code>Modify</code> The item will be modified.</p> </li> <li> <p> <code>SyncWithActual</code> The drift status of this item will be reset but the item will not be modified.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourceTargetDefinition, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "attribute" in value:
        import capo_cloudformation.types.resource_attribute

        capo_cloudformation.types.resource_attribute.serialize_query(
            value["attribute"], pairs, f"{key_prefix}Attribute"
        )
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "requires_recreation" in value:
        import capo_cloudformation.types.requires_recreation

        capo_cloudformation.types.requires_recreation.serialize_query(
            value["requires_recreation"], pairs, f"{key_prefix}RequiresRecreation"
        )
    if "path" in value:
        pairs.append((f"{key_prefix}Path", str(value["path"])))
    if "before_value" in value:
        pairs.append((f"{key_prefix}BeforeValue", str(value["before_value"])))
    if "after_value" in value:
        pairs.append((f"{key_prefix}AfterValue", str(value["after_value"])))
    if "before_value_from" in value:
        import capo_cloudformation.types.before_value_from

        capo_cloudformation.types.before_value_from.serialize_query(
            value["before_value_from"], pairs, f"{key_prefix}BeforeValueFrom"
        )
    if "after_value_from" in value:
        import capo_cloudformation.types.after_value_from

        capo_cloudformation.types.after_value_from.serialize_query(
            value["after_value_from"], pairs, f"{key_prefix}AfterValueFrom"
        )
    if "drift" in value:
        import capo_cloudformation.types.live_resource_drift

        capo_cloudformation.types.live_resource_drift.serialize_query(
            value["drift"], pairs, f"{key_prefix}Drift"
        )
    if "attribute_change_type" in value:
        import capo_cloudformation.types.attribute_change_type

        capo_cloudformation.types.attribute_change_type.serialize_query(
            value["attribute_change_type"], pairs, f"{key_prefix}AttributeChangeType"
        )


def deserialize_query(el: Element) -> ResourceTargetDefinition:
    out: ResourceTargetDefinition = {}  # type: ignore[typeddict-item]
    child_attribute = el.find("Attribute")
    if child_attribute is not None:
        import capo_cloudformation.types.resource_attribute

        out["attribute"] = (
            capo_cloudformation.types.resource_attribute.deserialize_query(
                child_attribute
            )
        )
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_requires_recreation = el.find("RequiresRecreation")
    if child_requires_recreation is not None:
        import capo_cloudformation.types.requires_recreation

        out["requires_recreation"] = (
            capo_cloudformation.types.requires_recreation.deserialize_query(
                child_requires_recreation
            )
        )
    child_path = el.find("Path")
    if child_path is not None:
        out["path"] = str(child_path.text or "")
    child_before_value = el.find("BeforeValue")
    if child_before_value is not None:
        out["before_value"] = str(child_before_value.text or "")
    child_after_value = el.find("AfterValue")
    if child_after_value is not None:
        out["after_value"] = str(child_after_value.text or "")
    child_before_value_from = el.find("BeforeValueFrom")
    if child_before_value_from is not None:
        import capo_cloudformation.types.before_value_from

        out["before_value_from"] = (
            capo_cloudformation.types.before_value_from.deserialize_query(
                child_before_value_from
            )
        )
    child_after_value_from = el.find("AfterValueFrom")
    if child_after_value_from is not None:
        import capo_cloudformation.types.after_value_from

        out["after_value_from"] = (
            capo_cloudformation.types.after_value_from.deserialize_query(
                child_after_value_from
            )
        )
    child_drift = el.find("Drift")
    if child_drift is not None:
        import capo_cloudformation.types.live_resource_drift

        out["drift"] = capo_cloudformation.types.live_resource_drift.deserialize_query(
            child_drift
        )
    child_attribute_change_type = el.find("AttributeChangeType")
    if child_attribute_change_type is not None:
        import capo_cloudformation.types.attribute_change_type

        out["attribute_change_type"] = (
            capo_cloudformation.types.attribute_change_type.deserialize_query(
                child_attribute_change_type
            )
        )
    return out
