"""Generated from Smithy shape ``com.amazonaws.frauddetector#listOfEntities``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.entity

listOfEntities: TypeAlias = list["capo_frauddetector.types.entity.Entity"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: listOfEntities) -> list:
    import capo_frauddetector.types.entity

    out: list = []
    for item in value:
        out.append(capo_frauddetector.types.entity.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> listOfEntities:
    import capo_frauddetector.types.entity

    out: listOfEntities = []
    for item in data:
        if item is None:
            continue
        out.append(capo_frauddetector.types.entity.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: listOfEntities) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
