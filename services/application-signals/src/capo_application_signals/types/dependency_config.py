"""Generated from Smithy shape ``com.amazonaws.applicationsignals#DependencyConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.attributes
    import capo_application_signals.types.operation_name


class DependencyConfig(TypedDict, closed=True):
    dependency_key_attributes: "capo_application_signals.types.attributes.Attributes"
    """<p>This is a string-to-string map. It can include the following fields.</p> <ul> <li> <p> <code>Type</code> designates the type of object this is.</p> </li> <li> <p> <code>ResourceType</code> specifies the type of the resource. This field is used only when the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Name</code> specifies the name of the object. This is used only if the value of the <code>Type</code> field is <code>Service</code>, <code>RemoteService</code>, or <code>AWS::Service</code>.</p> </li> <li> <p> <code>Identifier</code> identifies the resource objects of this resource. This is used only if the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Environment</code> specifies the location where this object is hosted, or what it belongs to.</p> </li> </ul>"""
    dependency_operation_name: (
        "capo_application_signals.types.operation_name.OperationName"
    )
    """<p>The name of the called operation in the dependency.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DependencyConfig) -> dict:
    out: dict = {}
    import capo_application_signals.types.attributes

    out["DependencyKeyAttributes"] = (
        capo_application_signals.types.attributes.serialize_json(
            value["dependency_key_attributes"]
        )
    )
    out["DependencyOperationName"] = value["dependency_operation_name"]
    return out


def deserialize_json(data: dict) -> DependencyConfig:
    out: DependencyConfig = {}  # type: ignore[typeddict-item]
    if data.get("DependencyKeyAttributes") is not None:
        import capo_application_signals.types.attributes

        out["dependency_key_attributes"] = (
            capo_application_signals.types.attributes.deserialize_json(
                data["DependencyKeyAttributes"]
            )
        )
    else:
        out["dependency_key_attributes"] = {}
    if data.get("DependencyOperationName") is not None:
        out["dependency_operation_name"] = data["DependencyOperationName"]
    else:
        out["dependency_operation_name"] = ""
    return out
