"""Generated from Smithy shape ``com.amazonaws.acm#CertificateAuthority``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_acm.errors import DeserializationError, SerializationError
from capo_acm.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_acm.types.public_certificate_authority


class _CertificateAuthority_PublicCertificateAuthority(TypedDict, closed=True):
    PublicCertificateAuthority: (
        "capo_acm.types.public_certificate_authority.PublicCertificateAuthority"
    )


CertificateAuthority: TypeAlias = (
    _CertificateAuthority_PublicCertificateAuthority | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateAuthority) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CertificateAuthority: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "PublicCertificateAuthority" in value:
        import capo_acm.types.public_certificate_authority

        return {
            "PublicCertificateAuthority": capo_acm.types.public_certificate_authority.serialize_aws_json_1_1(
                value["PublicCertificateAuthority"]
            )
        }
    else:
        raise SerializationError("CertificateAuthority: no variant present")


def deserialize_aws_json_1_1(data: dict) -> CertificateAuthority:
    if data.get("PublicCertificateAuthority") is not None:
        import capo_acm.types.public_certificate_authority

        return {
            "PublicCertificateAuthority": capo_acm.types.public_certificate_authority.deserialize_aws_json_1_1(
                data["PublicCertificateAuthority"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("CertificateAuthority: no recognized variant key")
