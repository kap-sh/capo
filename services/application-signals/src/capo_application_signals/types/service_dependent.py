"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceDependent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.attributes
    import capo_application_signals.types.metric_references
    import capo_application_signals.types.operation_name


class ServiceDependent(TypedDict, closed=True):
    operation_name: NotRequired[
        "capo_application_signals.types.operation_name.OperationName"
    ]
    """<p>If the invoked entity is an operation on an entity, the name of that dependent operation is displayed here.</p>"""
    dependent_key_attributes: "capo_application_signals.types.attributes.Attributes"
    """<p>This is a string-to-string map. It can include the following fields.</p> <ul> <li> <p> <code>Type</code> designates the type of object this is.</p> </li> <li> <p> <code>ResourceType</code> specifies the type of the resource. This field is used only when the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Name</code> specifies the name of the object. This is used only if the value of the <code>Type</code> field is <code>Service</code>, <code>RemoteService</code>, or <code>AWS::Service</code>.</p> </li> <li> <p> <code>Identifier</code> identifies the resource objects of this resource. This is used only if the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Environment</code> specifies the location where this object is hosted, or what it belongs to.</p> </li> </ul>"""
    dependent_operation_name: NotRequired[
        "capo_application_signals.types.operation_name.OperationName"
    ]
    """<p>If the dependent invoker was a service that invoked it from an operation, the name of that dependent operation is displayed here.</p>"""
    metric_references: (
        "capo_application_signals.types.metric_references.MetricReferences"
    )
    """<p>An array of structures that each contain information about one metric associated with this service dependent that was discovered by Application Signals.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceDependent) -> dict:
    out: dict = {}
    if "operation_name" in value:
        out["OperationName"] = value["operation_name"]
    import capo_application_signals.types.attributes

    out["DependentKeyAttributes"] = (
        capo_application_signals.types.attributes.serialize_json(
            value["dependent_key_attributes"]
        )
    )
    if "dependent_operation_name" in value:
        out["DependentOperationName"] = value["dependent_operation_name"]
    import capo_application_signals.types.metric_references

    out["MetricReferences"] = (
        capo_application_signals.types.metric_references.serialize_json(
            value["metric_references"]
        )
    )
    return out


def deserialize_json(data: dict) -> ServiceDependent:
    out: ServiceDependent = {}  # type: ignore[typeddict-item]
    if data.get("OperationName") is not None:
        out["operation_name"] = data["OperationName"]
    if data.get("DependentKeyAttributes") is not None:
        import capo_application_signals.types.attributes

        out["dependent_key_attributes"] = (
            capo_application_signals.types.attributes.deserialize_json(
                data["DependentKeyAttributes"]
            )
        )
    else:
        out["dependent_key_attributes"] = {}
    if data.get("DependentOperationName") is not None:
        out["dependent_operation_name"] = data["DependentOperationName"]
    if data.get("MetricReferences") is not None:
        import capo_application_signals.types.metric_references

        out["metric_references"] = (
            capo_application_signals.types.metric_references.deserialize_json(
                data["MetricReferences"]
            )
        )
    else:
        out["metric_references"] = []
    return out
