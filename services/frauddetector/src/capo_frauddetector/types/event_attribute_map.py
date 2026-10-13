"""Generated from Smithy shape ``com.amazonaws.frauddetector#EventAttributeMap``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.attribute_key
    import capo_frauddetector.types.attribute_value

EventAttributeMap: TypeAlias = dict[
    "capo_frauddetector.types.attribute_key.attributeKey",
    "capo_frauddetector.types.attribute_value.attributeValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: EventAttributeMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> EventAttributeMap:
    out: EventAttributeMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


def redact_sensitive(value: EventAttributeMap) -> dict[str, Any]:
    return dict.fromkeys(value, "*** Sensitive Data Redacted ***")
