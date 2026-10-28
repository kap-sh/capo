"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#SourceData``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_rolesanywhere.errors import DeserializationError, SerializationError
from capo_rolesanywhere.types._unknown import UnknownUnionMember


class SourceDataX509CertificateDataMember(TypedDict, closed=True):
    x509CertificateData: "str"


class SourceDataAcmPcaArnMember(TypedDict, closed=True):
    acmPcaArn: "str"


SourceData: TypeAlias = (
    SourceDataX509CertificateDataMember | SourceDataAcmPcaArnMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SourceData) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SourceData: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "x509CertificateData" in value:
        return {"x509CertificateData": value["x509CertificateData"]}
    elif "acmPcaArn" in value:
        return {"acmPcaArn": value["acmPcaArn"]}
    else:
        raise SerializationError("SourceData: no variant present")


def deserialize_json(data: dict) -> SourceData:
    if data.get("x509CertificateData") is not None:
        return {"x509CertificateData": data["x509CertificateData"]}
    elif data.get("acmPcaArn") is not None:
        return {"acmPcaArn": data["acmPcaArn"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("SourceData: no recognized variant key")
