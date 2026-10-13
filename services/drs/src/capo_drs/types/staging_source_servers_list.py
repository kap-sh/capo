"""Generated from Smithy shape ``com.amazonaws.drs#StagingSourceServersList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_drs.types.staging_source_server

StagingSourceServersList: TypeAlias = list[
    "capo_drs.types.staging_source_server.StagingSourceServer"
]


# --- restJson1 ser/de ---
def serialize_json(value: StagingSourceServersList) -> list:
    import capo_drs.types.staging_source_server

    out: list = []
    for item in value:
        out.append(capo_drs.types.staging_source_server.serialize_json(item))
    return out


def deserialize_json(data: list) -> StagingSourceServersList:
    import capo_drs.types.staging_source_server

    out: StagingSourceServersList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_drs.types.staging_source_server.deserialize_json(item))
    return out


def redact_sensitive(value: StagingSourceServersList) -> list[Any]:
    import capo_drs.types.staging_source_server

    return [
        capo_drs.types.staging_source_server.redact_sensitive(item) for item in value
    ]
