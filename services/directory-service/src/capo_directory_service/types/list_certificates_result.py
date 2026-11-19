"""Generated from Smithy shape ``com.amazonaws.directoryservice#ListCertificatesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.certificates_info
    import capo_directory_service.types.next_token


class ListCertificatesResult(TypedDict, closed=True):
    next_token: NotRequired["capo_directory_service.types.next_token.NextToken"]
    """<p>Indicates whether another page of certificates is available when the number of available certificates exceeds the page limit.</p>"""
    certificates_info: NotRequired[
        "capo_directory_service.types.certificates_info.CertificatesInfo"
    ]
    """<p>A list of certificates with basic details including certificate ID, certificate common name, certificate state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCertificatesResult) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "certificates_info" in value:
        import capo_directory_service.types.certificates_info

        out["CertificatesInfo"] = (
            capo_directory_service.types.certificates_info.serialize_aws_json_1_1(
                value["certificates_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCertificatesResult:
    out: ListCertificatesResult = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("CertificatesInfo") is not None:
        import capo_directory_service.types.certificates_info

        out["certificates_info"] = (
            capo_directory_service.types.certificates_info.deserialize_aws_json_1_1(
                data["CertificatesInfo"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListCertificatesResult) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "certificates_info" in value:
        import capo_directory_service.types.certificates_info

        out["CertificatesInfo"] = (
            capo_directory_service.types.certificates_info.serialize_cbor(
                value["certificates_info"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ListCertificatesResult:
    out: ListCertificatesResult = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("CertificatesInfo") is not None:
        import capo_directory_service.types.certificates_info

        out["certificates_info"] = (
            capo_directory_service.types.certificates_info.deserialize_cbor(
                data["CertificatesInfo"]
            )
        )
    return out
