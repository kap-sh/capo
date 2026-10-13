"""Generated from Smithy shape ``com.amazonaws.emrserverless#ConfigurationList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_emr_serverless.types.configuration

ConfigurationList: TypeAlias = list[
    "capo_emr_serverless.types.configuration.Configuration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationList) -> list:
    import capo_emr_serverless.types.configuration

    out: list = []
    for item in value:
        out.append(capo_emr_serverless.types.configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConfigurationList:
    import capo_emr_serverless.types.configuration

    out: ConfigurationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_emr_serverless.types.configuration.deserialize_json(item))
    return out


def redact_sensitive(value: ConfigurationList) -> list[Any]:
    import capo_emr_serverless.types.configuration

    return [
        capo_emr_serverless.types.configuration.redact_sensitive(item) for item in value
    ]
