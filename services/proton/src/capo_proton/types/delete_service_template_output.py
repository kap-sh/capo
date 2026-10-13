"""Generated from Smithy shape ``com.amazonaws.proton#DeleteServiceTemplateOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.service_template


class DeleteServiceTemplateOutput(TypedDict, closed=True):
    service_template: NotRequired["capo_proton.types.service_template.ServiceTemplate"]
    """<p>The detailed data of the service template being deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteServiceTemplateOutput) -> dict:
    out: dict = {}
    if "service_template" in value:
        import capo_proton.types.service_template

        out["serviceTemplate"] = (
            capo_proton.types.service_template.serialize_aws_json_1_0(
                value["service_template"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteServiceTemplateOutput:
    out: DeleteServiceTemplateOutput = {}  # type: ignore[typeddict-item]
    if data.get("serviceTemplate") is not None:
        import capo_proton.types.service_template

        out["service_template"] = (
            capo_proton.types.service_template.deserialize_aws_json_1_0(
                data["serviceTemplate"]
            )
        )
    return out


def redact_sensitive(value: DeleteServiceTemplateOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "service_template" in value:
        import capo_proton.types.service_template

        out["service_template"] = capo_proton.types.service_template.redact_sensitive(
            value["service_template"]
        )
    return out
