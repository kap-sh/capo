"""Generated from Smithy shape ``com.amazonaws.lightsail#Sessions``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.session

Sessions: TypeAlias = list["capo_lightsail.types.session.Session"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Sessions) -> list:
    import capo_lightsail.types.session

    out: list = []
    for item in value:
        out.append(capo_lightsail.types.session.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Sessions:
    import capo_lightsail.types.session

    out: Sessions = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lightsail.types.session.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: Sessions) -> list[Any]:
    import capo_lightsail.types.session

    return [capo_lightsail.types.session.redact_sensitive(item) for item in value]
