"""Generated from Smithy shape ``com.amazonaws.iot#RegisterThingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.parameters
    import capo_iot.types.template_body


class RegisterThingRequest(TypedDict, closed=True):
    template_body: "capo_iot.types.template_body.TemplateBody"
    """<p>The provisioning template. See <a href="https://docs.aws.amazon.com/iot/latest/developerguide/provision-w-cert.html">Provisioning Devices That Have Device Certificates</a> for more information.</p>"""
    parameters: NotRequired["capo_iot.types.parameters.Parameters"]
    """<p>The parameters for provisioning a thing. See <a href="https://docs.aws.amazon.com/iot/latest/developerguide/provision-template.html">Provisioning Templates</a> for more information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterThingRequest) -> dict:
    out: dict = {}
    out["templateBody"] = value["template_body"]
    if "parameters" in value:
        import capo_iot.types.parameters

        out["parameters"] = capo_iot.types.parameters.serialize_json(
            value["parameters"]
        )
    return out


def deserialize_json(data: dict) -> RegisterThingRequest:
    out: RegisterThingRequest = {}  # type: ignore[typeddict-item]
    if data.get("templateBody") is not None:
        out["template_body"] = data["templateBody"]
    else:
        raise DeserializationError("RegisterThingRequest.template_body required")
    if data.get("parameters") is not None:
        import capo_iot.types.parameters

        out["parameters"] = capo_iot.types.parameters.deserialize_json(
            data["parameters"]
        )
    return out
