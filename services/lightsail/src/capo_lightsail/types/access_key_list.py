"""Generated from Smithy shape ``com.amazonaws.lightsail#AccessKeyList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.access_key

AccessKeyList: TypeAlias = list["capo_lightsail.types.access_key.AccessKey"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessKeyList) -> list:
    import capo_lightsail.types.access_key

    out: list = []
    for item in value:
        out.append(capo_lightsail.types.access_key.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AccessKeyList:
    import capo_lightsail.types.access_key

    out: AccessKeyList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lightsail.types.access_key.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: AccessKeyList) -> list[Any]:
    import capo_lightsail.types.access_key

    return [capo_lightsail.types.access_key.redact_sensitive(item) for item in value]
