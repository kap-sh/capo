"""Generated from Smithy shape ``com.amazonaws.gamelift#CertificateConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.certificate_type


class CertificateConfiguration(TypedDict, closed=True):
    certificate_type: NotRequired[
        "capo_gamelift.types.certificate_type.CertificateType"
    ]
    """<p>Indicates whether a TLS/SSL certificate is generated for a fleet. </p> <p>Valid values include: </p> <ul> <li> <p> <b>GENERATED</b> - Generate a TLS/SSL certificate for this fleet.</p> </li> <li> <p> <b>DISABLED</b> - (default) Do not generate a TLS/SSL certificate for this fleet. </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateConfiguration) -> dict:
    out: dict = {}
    if "certificate_type" in value:
        import capo_gamelift.types.certificate_type

        out["CertificateType"] = (
            capo_gamelift.types.certificate_type.serialize_aws_json_1_1(
                value["certificate_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CertificateConfiguration:
    out: CertificateConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("CertificateType") is not None:
        import capo_gamelift.types.certificate_type

        out["certificate_type"] = (
            capo_gamelift.types.certificate_type.deserialize_aws_json_1_1(
                data["CertificateType"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CertificateConfiguration) -> dict:
    out: dict = {}
    if "certificate_type" in value:
        import capo_gamelift.types.certificate_type

        out["CertificateType"] = capo_gamelift.types.certificate_type.serialize_cbor(
            value["certificate_type"]
        )
    return out


def deserialize_cbor(data: dict) -> CertificateConfiguration:
    out: CertificateConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("CertificateType") is not None:
        import capo_gamelift.types.certificate_type

        out["certificate_type"] = capo_gamelift.types.certificate_type.deserialize_cbor(
            data["CertificateType"]
        )
    return out
