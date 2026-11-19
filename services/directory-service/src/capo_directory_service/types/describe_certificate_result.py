"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeCertificateResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.certificate


class DescribeCertificateResult(TypedDict, closed=True):
    certificate: NotRequired["capo_directory_service.types.certificate.Certificate"]
    """<p>Information about the certificate, including registered date time, certificate state, the reason for the state, expiration date time, and certificate common name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCertificateResult) -> dict:
    out: dict = {}
    if "certificate" in value:
        import capo_directory_service.types.certificate

        out["Certificate"] = (
            capo_directory_service.types.certificate.serialize_aws_json_1_1(
                value["certificate"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCertificateResult:
    out: DescribeCertificateResult = {}  # type: ignore[typeddict-item]
    if data.get("Certificate") is not None:
        import capo_directory_service.types.certificate

        out["certificate"] = (
            capo_directory_service.types.certificate.deserialize_aws_json_1_1(
                data["Certificate"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeCertificateResult) -> dict:
    out: dict = {}
    if "certificate" in value:
        import capo_directory_service.types.certificate

        out["Certificate"] = capo_directory_service.types.certificate.serialize_cbor(
            value["certificate"]
        )
    return out


def deserialize_cbor(data: dict) -> DescribeCertificateResult:
    out: DescribeCertificateResult = {}  # type: ignore[typeddict-item]
    if data.get("Certificate") is not None:
        import capo_directory_service.types.certificate

        out["certificate"] = capo_directory_service.types.certificate.deserialize_cbor(
            data["Certificate"]
        )
    return out
