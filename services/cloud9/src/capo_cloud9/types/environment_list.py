"""Generated from Smithy shape ``com.amazonaws.cloud9#EnvironmentList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_cloud9.types.environment

EnvironmentList: TypeAlias = list["capo_cloud9.types.environment.Environment"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentList) -> list:
    import capo_cloud9.types.environment

    out: list = []
    for item in value:
        out.append(capo_cloud9.types.environment.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EnvironmentList:
    import capo_cloud9.types.environment

    out: EnvironmentList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloud9.types.environment.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: EnvironmentList) -> list[Any]:
    import capo_cloud9.types.environment

    return [capo_cloud9.types.environment.redact_sensitive(item) for item in value]
