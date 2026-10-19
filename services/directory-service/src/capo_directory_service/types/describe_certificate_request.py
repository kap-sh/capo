"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.certificate_id
    import capo_directory_service.types.directory_id


class DescribeCertificateRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>The identifier of the directory.</p>"""
    certificate_id: "capo_directory_service.types.certificate_id.CertificateId"
    """<p>The identifier of the certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCertificateRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    out["CertificateId"] = value["certificate_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCertificateRequest:
    out: DescribeCertificateRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    if data.get("CertificateId") is not None:
        out["certificate_id"] = data["CertificateId"]
    else:
        out["certificate_id"] = ""
    return out
