"""Generated from Smithy shape ``com.amazonaws.appconfig#Validator``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_appconfig.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appconfig.types.string_with_length_between0_and32768
    import capo_appconfig.types.validator_type


class Validator(TypedDict, closed=True):
    type: "capo_appconfig.types.validator_type.ValidatorType"
    """<p>AppConfig supports validators of type <code>JSON_SCHEMA</code> and <code>LAMBDA</code> </p>"""
    content: "capo_appconfig.types.string_with_length_between0_and32768.StringWithLengthBetween0And32768"
    """<p>Either the JSON Schema content or the Amazon Resource Name (ARN) of an Lambda function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Validator) -> dict:
    out: dict = {}
    import capo_appconfig.types.validator_type

    out["Type"] = capo_appconfig.types.validator_type.serialize_json(value["type"])
    out["Content"] = value["content"]
    return out


def deserialize_json(data: dict) -> Validator:
    out: Validator = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_appconfig.types.validator_type

        out["type"] = capo_appconfig.types.validator_type.deserialize_json(data["Type"])
    else:
        raise DeserializationError("Validator.type required")
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    else:
        raise DeserializationError("Validator.content required")
    return out


def redact_sensitive(value: Validator) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        out["content"] = "*** Sensitive Data Redacted ***"
    return out
