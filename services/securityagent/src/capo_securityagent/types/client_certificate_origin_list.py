"""Generated from Smithy shape ``com.amazonaws.securityagent#ClientCertificateOriginList``."""

from typing import TypeAlias

ClientCertificateOriginList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ClientCertificateOriginList) -> list:
    return list(value)


def deserialize_json(data: list) -> ClientCertificateOriginList:
    return [item for item in data if item is not None]
