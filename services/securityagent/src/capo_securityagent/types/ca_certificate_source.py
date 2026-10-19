"""Generated from Smithy shape ``com.amazonaws.securityagent#CaCertificateSource``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError, SerializationError
from capo_securityagent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_securityagent.types.ca_certificate_pem


class _CaCertificateSource_inlinePem(TypedDict, closed=True):
    inlinePem: "capo_securityagent.types.ca_certificate_pem.CaCertificatePem"


class _CaCertificateSource_artifactId(TypedDict, closed=True):
    artifactId: "str"


class _CaCertificateSource_s3Location(TypedDict, closed=True):
    s3Location: "str"


CaCertificateSource: TypeAlias = (
    _CaCertificateSource_inlinePem
    | _CaCertificateSource_artifactId
    | _CaCertificateSource_s3Location
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CaCertificateSource) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"CaCertificateSource: cannot serialize unknown variant {value.name!r}"
        )
    elif "inlinePem" in value:
        return {"inlinePem": value["inlinePem"]}
    elif "artifactId" in value:
        return {"artifactId": value["artifactId"]}
    elif "s3Location" in value:
        return {"s3Location": value["s3Location"]}
    else:
        raise SerializationError("CaCertificateSource: no variant present")


def deserialize_json(data: dict) -> CaCertificateSource:
    if data.get("inlinePem") is not None:
        return {"inlinePem": data["inlinePem"]}
    elif data.get("artifactId") is not None:
        return {"artifactId": data["artifactId"]}
    elif data.get("s3Location") is not None:
        return {"s3Location": data["s3Location"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("CaCertificateSource: no recognized variant key")


def redact_sensitive(value: CaCertificateSource) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "inlinePem" in value:
        out["inlinePem"] = "*** Sensitive Data Redacted ***"
    return out
