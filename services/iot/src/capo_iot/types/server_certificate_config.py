"""Generated from Smithy shape ``com.amazonaws.iot#ServerCertificateConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.acm_certificate_arn
    import capo_iot.types.enable_ocsp_check
    import capo_iot.types.ocsp_lambda_arn


class ServerCertificateConfig(TypedDict, closed=True):
    enable_ocsp_check: NotRequired["capo_iot.types.enable_ocsp_check.EnableOCSPCheck"]
    """<p>A Boolean value that indicates whether Online Certificate Status Protocol (OCSP) server certificate check is enabled or not.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot/latest/developerguide/iot-custom-endpoints-cert-config.html"> Server certificate configuration for OCSP stapling</a> from Amazon Web Services IoT Core Developer Guide.</p>"""
    ocsp_lambda_arn: NotRequired["capo_iot.types.ocsp_lambda_arn.OCSPLambdaArn"]
    """<p>The Amazon Resource Name (ARN) for a Lambda function that acts as a Request for Comments (RFC) 6960-compliant Online Certificate Status Protocol (OCSP) responder, supporting basic OCSP responses. The Lambda function accepts a base64-encoding of the OCSP request in the Distinguished Encoding Rules (DER) format. The Lambda function's response is also a base64-encoded OCSP response in the DER format. The response size must not exceed 4 kilobytes (KiB). The Lambda function must be in the same Amazon Web Services account and region as the domain configuration. For more information, see <a href="https://docs.aws.amazon.com/iot/latest/developerguide/iot-custom-endpoints-cert-config.html#iot-custom-endpoints-cert-config-ocsp-private-endpoint.html">Configuring server certificate OCSP for private endpoints in Amazon Web Services IoT Core</a> from the Amazon Web Services IoT Core developer guide.</p>"""
    ocsp_authorized_responder_arn: NotRequired[
        "capo_iot.types.acm_certificate_arn.AcmCertificateArn"
    ]
    """<p>The Amazon Resource Name (ARN) for an X.509 certificate stored in Amazon Web Services Certificate Manager (ACM). If provided, Amazon Web Services IoT Core will use this certificate to validate the signature of the received OCSP response. The OCSP responder must sign responses using either this authorized responder certificate or the issuing certificate, depending on whether the ARN is provided or not. The certificate must be in the same Amazon Web Services account and region as the domain configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServerCertificateConfig) -> dict:
    out: dict = {}
    if "enable_ocsp_check" in value:
        out["enableOCSPCheck"] = value["enable_ocsp_check"]
    if "ocsp_lambda_arn" in value:
        out["ocspLambdaArn"] = value["ocsp_lambda_arn"]
    if "ocsp_authorized_responder_arn" in value:
        out["ocspAuthorizedResponderArn"] = value["ocsp_authorized_responder_arn"]
    return out


def deserialize_json(data: dict) -> ServerCertificateConfig:
    out: ServerCertificateConfig = {}  # type: ignore[typeddict-item]
    if data.get("enableOCSPCheck") is not None:
        out["enable_ocsp_check"] = data["enableOCSPCheck"]
    if data.get("ocspLambdaArn") is not None:
        out["ocsp_lambda_arn"] = data["ocspLambdaArn"]
    if data.get("ocspAuthorizedResponderArn") is not None:
        out["ocsp_authorized_responder_arn"] = data["ocspAuthorizedResponderArn"]
    return out
