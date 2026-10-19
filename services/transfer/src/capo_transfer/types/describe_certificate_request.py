"""Generated from Smithy shape ``com.amazonaws.transfer#DescribeCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.certificate_id


class DescribeCertificateRequest(TypedDict, closed=True):
    certificate_id: "capo_transfer.types.certificate_id.CertificateId"
    """<p>An array of identifiers for the imported certificates. You use this identifier for working with profiles and partner profiles.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCertificateRequest) -> dict:
    out: dict = {}
    out["CertificateId"] = value["certificate_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCertificateRequest:
    out: DescribeCertificateRequest = {}  # type: ignore[typeddict-item]
    if data.get("CertificateId") is not None:
        out["certificate_id"] = data["CertificateId"]
    else:
        out["certificate_id"] = ""
    return out
