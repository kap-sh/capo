"""Generated from Smithy shape ``com.amazonaws.appmesh#ListenerTlsAcmCertificate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.arn


class ListenerTlsAcmCertificate(TypedDict, closed=True):
    certificate_arn: "capo_app_mesh.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for the certificate. The certificate must meet specific requirements and you must have proxy authorization enabled. For more information, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/tls.html#virtual-node-tls-prerequisites">Transport Layer Security (TLS)</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListenerTlsAcmCertificate) -> dict:
    out: dict = {}
    out["certificateArn"] = value["certificate_arn"]
    return out


def deserialize_json(data: dict) -> ListenerTlsAcmCertificate:
    out: ListenerTlsAcmCertificate = {}  # type: ignore[typeddict-item]
    if data.get("certificateArn") is not None:
        out["certificate_arn"] = data["certificateArn"]
    else:
        raise DeserializationError("ListenerTlsAcmCertificate.certificate_arn required")
    return out
