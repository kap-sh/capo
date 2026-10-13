"""Generated from Smithy shape ``com.amazonaws.panorama#TemplateParametersMap``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_panorama.types.template_key
    import capo_panorama.types.template_value

TemplateParametersMap: TypeAlias = dict[
    "capo_panorama.types.template_key.TemplateKey",
    "capo_panorama.types.template_value.TemplateValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TemplateParametersMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> TemplateParametersMap:
    out: TemplateParametersMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


def redact_sensitive(value: TemplateParametersMap) -> dict[str, Any]:
    return dict.fromkeys(value, "*** Sensitive Data Redacted ***")
