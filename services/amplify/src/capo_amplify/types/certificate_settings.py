"""Generated from Smithy shape ``com.amazonaws.amplify#CertificateSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplify.types.certificate_arn
    import capo_amplify.types.certificate_type


class CertificateSettings(TypedDict, closed=True):
    type: "capo_amplify.types.certificate_type.CertificateType"
    """<p>The certificate type.</p> <p>Specify <code>AMPLIFY_MANAGED</code> to use the default certificate that Amplify provisions for you.</p> <p>Specify <code>CUSTOM</code> to use your own certificate that you have already added to Certificate Manager in your Amazon Web Services account. Make sure you request (or import) the certificate in the US East (N. Virginia) Region (us-east-1). For more information about using ACM, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html">Importing certificates into Certificate Manager</a> in the <i>ACM User guide</i>.</p>"""
    custom_certificate_arn: NotRequired[
        "capo_amplify.types.certificate_arn.CertificateArn"
    ]
    """<p>The Amazon resource name (ARN) for the custom certificate that you have already added to Certificate Manager in your Amazon Web Services account.</p> <p>This field is required only when the certificate type is <code>CUSTOM</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CertificateSettings) -> dict:
    out: dict = {}
    import capo_amplify.types.certificate_type

    out["type"] = capo_amplify.types.certificate_type.serialize_json(value["type"])
    if "custom_certificate_arn" in value:
        out["customCertificateArn"] = value["custom_certificate_arn"]
    return out


def deserialize_json(data: dict) -> CertificateSettings:
    out: CertificateSettings = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_amplify.types.certificate_type

        out["type"] = capo_amplify.types.certificate_type.deserialize_json(data["type"])
    else:
        raise DeserializationError("CertificateSettings.type required")
    if data.get("customCertificateArn") is not None:
        out["custom_certificate_arn"] = data["customCertificateArn"]
    return out
