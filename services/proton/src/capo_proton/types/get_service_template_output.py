"""Generated from Smithy shape ``com.amazonaws.proton#GetServiceTemplateOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.service_template


class GetServiceTemplateOutput(TypedDict, closed=True):
    service_template: "capo_proton.types.service_template.ServiceTemplate"
    """<p>The detailed data of the requested service template.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetServiceTemplateOutput) -> dict:
    out: dict = {}
    import capo_proton.types.service_template

    out["serviceTemplate"] = capo_proton.types.service_template.serialize_aws_json_1_0(
        value["service_template"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetServiceTemplateOutput:
    out: GetServiceTemplateOutput = {}  # type: ignore[typeddict-item]
    if data.get("serviceTemplate") is not None:
        import capo_proton.types.service_template

        out["service_template"] = (
            capo_proton.types.service_template.deserialize_aws_json_1_0(
                data["serviceTemplate"]
            )
        )
    else:
        raise DeserializationError("GetServiceTemplateOutput.service_template required")
    return out


def redact_sensitive(value: GetServiceTemplateOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "service_template" in value:
        import capo_proton.types.service_template

        out["service_template"] = capo_proton.types.service_template.redact_sensitive(
            value["service_template"]
        )
    return out
