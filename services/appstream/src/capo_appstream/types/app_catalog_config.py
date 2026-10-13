"""Generated from Smithy shape ``com.amazonaws.appstream#AppCatalogConfig``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.application_config

AppCatalogConfig: TypeAlias = list[
    "capo_appstream.types.application_config.ApplicationConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppCatalogConfig) -> list:
    import capo_appstream.types.application_config

    out: list = []
    for item in value:
        out.append(capo_appstream.types.application_config.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AppCatalogConfig:
    import capo_appstream.types.application_config

    out: AppCatalogConfig = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_appstream.types.application_config.deserialize_aws_json_1_1(item)
        )
    return out


def redact_sensitive(value: AppCatalogConfig) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
