"""Generated from Smithy shape ``com.amazonaws.acm#UpdateCertificateOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_acm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_acm.types.arn
    import capo_acm.types.certificate_options


class UpdateCertificateOptionsRequest(TypedDict, closed=True):
    certificate_arn: "capo_acm.types.arn.Arn"
    """<p>ARN of the requested certificate to update. This must be of the form:</p> <p> <code>arn:aws:acm:us-east-1:<i>account</i>:certificate/<i>12345678-1234-1234-1234-123456789012</i> </code> </p>"""
    options: "capo_acm.types.certificate_options.CertificateOptions"
    """<p>Use to update the options for your certificate. Currently, you can change the domain validation method or specify whether to export your certificate. For more information about migrating from email to DNS validation, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/email-to-dns-migration.html">Migrate from email to DNS validation</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCertificateOptionsRequest) -> dict:
    out: dict = {}
    out["CertificateArn"] = value["certificate_arn"]
    import capo_acm.types.certificate_options

    out["Options"] = capo_acm.types.certificate_options.serialize_aws_json_1_1(
        value["options"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCertificateOptionsRequest:
    out: UpdateCertificateOptionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("CertificateArn") is not None:
        out["certificate_arn"] = data["CertificateArn"]
    else:
        raise DeserializationError(
            "UpdateCertificateOptionsRequest.certificate_arn required"
        )
    if data.get("Options") is not None:
        import capo_acm.types.certificate_options

        out["options"] = capo_acm.types.certificate_options.deserialize_aws_json_1_1(
            data["Options"]
        )
    else:
        raise DeserializationError("UpdateCertificateOptionsRequest.options required")
    return out
