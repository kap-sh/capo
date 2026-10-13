"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#RedundantIngestCredentials``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_ivs_realtime.types.redundant_ingest_credential

RedundantIngestCredentials: TypeAlias = list[
    "capo_ivs_realtime.types.redundant_ingest_credential.RedundantIngestCredential"
]


# --- restJson1 ser/de ---
def serialize_json(value: RedundantIngestCredentials) -> list:
    import capo_ivs_realtime.types.redundant_ingest_credential

    out: list = []
    for item in value:
        out.append(
            capo_ivs_realtime.types.redundant_ingest_credential.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RedundantIngestCredentials:
    import capo_ivs_realtime.types.redundant_ingest_credential

    out: RedundantIngestCredentials = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ivs_realtime.types.redundant_ingest_credential.deserialize_json(item)
        )
    return out


def redact_sensitive(value: RedundantIngestCredentials) -> list[Any]:
    import capo_ivs_realtime.types.redundant_ingest_credential

    return [
        capo_ivs_realtime.types.redundant_ingest_credential.redact_sensitive(item)
        for item in value
    ]
