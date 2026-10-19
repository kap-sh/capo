"""Generated from Smithy shape ``com.amazonaws.lightsail#DeleteCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.certificate_name


class DeleteCertificateRequest(TypedDict, closed=True):
    certificate_name: "capo_lightsail.types.certificate_name.CertificateName"
    """<p>The name of the certificate to delete.</p> <p>Use the <code>GetCertificates</code> action to get a list of certificate names that you can specify.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCertificateRequest) -> dict:
    out: dict = {}
    out["certificateName"] = value["certificate_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCertificateRequest:
    out: DeleteCertificateRequest = {}  # type: ignore[typeddict-item]
    if data.get("certificateName") is not None:
        out["certificate_name"] = data["certificateName"]
    else:
        out["certificate_name"] = ""
    return out
