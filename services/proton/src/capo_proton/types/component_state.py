"""Generated from Smithy shape ``com.amazonaws.proton#ComponentState``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.resource_name_or_empty
    import capo_proton.types.spec_contents
    import capo_proton.types.template_file_contents


class ComponentState(TypedDict, closed=True):
    service_name: NotRequired[
        "capo_proton.types.resource_name_or_empty.ResourceNameOrEmpty"
    ]
    """<p>The name of the service that <code>serviceInstanceName</code> is associated with. Provided when a component is attached to a service instance.</p>"""
    service_instance_name: NotRequired[
        "capo_proton.types.resource_name_or_empty.ResourceNameOrEmpty"
    ]
    """<p>The name of the service instance that this component is attached to. Provided when a component is attached to a service instance.</p>"""
    service_spec: NotRequired["capo_proton.types.spec_contents.SpecContents"]
    """<p>The service spec that the component uses to access service inputs. Provided when a component is attached to a service instance.</p>"""
    template_file: NotRequired[
        "capo_proton.types.template_file_contents.TemplateFileContents"
    ]
    """<p>The template file used.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ComponentState) -> dict:
    out: dict = {}
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "service_instance_name" in value:
        out["serviceInstanceName"] = value["service_instance_name"]
    if "service_spec" in value:
        out["serviceSpec"] = value["service_spec"]
    if "template_file" in value:
        out["templateFile"] = value["template_file"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ComponentState:
    out: ComponentState = {}  # type: ignore[typeddict-item]
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    if data.get("serviceInstanceName") is not None:
        out["service_instance_name"] = data["serviceInstanceName"]
    if data.get("serviceSpec") is not None:
        out["service_spec"] = data["serviceSpec"]
    if data.get("templateFile") is not None:
        out["template_file"] = data["templateFile"]
    return out


def redact_sensitive(value: ComponentState) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "service_spec" in value:
        out["service_spec"] = "*** Sensitive Data Redacted ***"
    if "template_file" in value:
        out["template_file"] = "*** Sensitive Data Redacted ***"
    return out
