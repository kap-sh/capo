"""Generated from Smithy shape ``com.amazonaws.securityagent#TrustedCaCertificateList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.trusted_ca_certificate

TrustedCaCertificateList: TypeAlias = list[
    "capo_securityagent.types.trusted_ca_certificate.TrustedCaCertificate"
]


# --- restJson1 ser/de ---
def serialize_json(value: TrustedCaCertificateList) -> list:
    import capo_securityagent.types.trusted_ca_certificate

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.trusted_ca_certificate.serialize_json(item))
    return out


def deserialize_json(data: list) -> TrustedCaCertificateList:
    import capo_securityagent.types.trusted_ca_certificate

    out: TrustedCaCertificateList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_securityagent.types.trusted_ca_certificate.deserialize_json(item)
        )
    return out


def redact_sensitive(value: TrustedCaCertificateList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
