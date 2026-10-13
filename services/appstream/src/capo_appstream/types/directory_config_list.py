"""Generated from Smithy shape ``com.amazonaws.appstream#DirectoryConfigList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.directory_config

DirectoryConfigList: TypeAlias = list[
    "capo_appstream.types.directory_config.DirectoryConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectoryConfigList) -> list:
    import capo_appstream.types.directory_config

    out: list = []
    for item in value:
        out.append(capo_appstream.types.directory_config.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DirectoryConfigList:
    import capo_appstream.types.directory_config

    out: DirectoryConfigList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appstream.types.directory_config.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: DirectoryConfigList) -> list[Any]:
    import capo_appstream.types.directory_config

    return [
        capo_appstream.types.directory_config.redact_sensitive(item) for item in value
    ]
