"""Generated from Smithy shape ``com.amazonaws.forecast#Tags``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_forecast.types.tag

Tags: TypeAlias = list["capo_forecast.types.tag.Tag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tags) -> list:
    import capo_forecast.types.tag

    out: list = []
    for item in value:
        out.append(capo_forecast.types.tag.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Tags:
    import capo_forecast.types.tag

    out: Tags = []
    for item in data:
        if item is None:
            continue
        out.append(capo_forecast.types.tag.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: Tags) -> list[Any]:
    import capo_forecast.types.tag

    return [capo_forecast.types.tag.redact_sensitive(item) for item in value]
