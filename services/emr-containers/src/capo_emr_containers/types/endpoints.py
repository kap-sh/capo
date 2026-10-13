"""Generated from Smithy shape ``com.amazonaws.emrcontainers#Endpoints``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_emr_containers.types.endpoint

Endpoints: TypeAlias = list["capo_emr_containers.types.endpoint.Endpoint"]


# --- restJson1 ser/de ---
def serialize_json(value: Endpoints) -> list:
    import capo_emr_containers.types.endpoint

    out: list = []
    for item in value:
        out.append(capo_emr_containers.types.endpoint.serialize_json(item))
    return out


def deserialize_json(data: list) -> Endpoints:
    import capo_emr_containers.types.endpoint

    out: Endpoints = []
    for item in data:
        if item is None:
            continue
        out.append(capo_emr_containers.types.endpoint.deserialize_json(item))
    return out


def redact_sensitive(value: Endpoints) -> list[Any]:
    import capo_emr_containers.types.endpoint

    return [capo_emr_containers.types.endpoint.redact_sensitive(item) for item in value]
