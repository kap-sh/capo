"""Generated from Smithy shape ``com.amazonaws.securityagent#ClientCertificateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.client_certificate

ClientCertificateList: TypeAlias = list[
    "capo_securityagent.types.client_certificate.ClientCertificate"
]


# --- restJson1 ser/de ---
def serialize_json(value: ClientCertificateList) -> list:
    import capo_securityagent.types.client_certificate

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.client_certificate.serialize_json(item))
    return out


def deserialize_json(data: list) -> ClientCertificateList:
    import capo_securityagent.types.client_certificate

    out: ClientCertificateList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_securityagent.types.client_certificate.deserialize_json(item))
    return out
