"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CustomDomainConfigType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.arn_type
    import capo_cognito_identity_provider.types.security_policy_type


class CustomDomainConfigType(TypedDict, closed=True):
    certificate_arn: "capo_cognito_identity_provider.types.arn_type.ArnType"
    """<p>The Amazon Resource Name (ARN) of an Certificate Manager SSL certificate. You use this certificate for the subdomain of your custom domain.</p>"""
    security_policy: NotRequired[
        "capo_cognito_identity_provider.types.security_policy_type.SecurityPolicyType"
    ]
    """<p>The security policy for the custom domain. Defines the minimum TLS version and cipher suites that Amazon CloudFront supports when communicating with clients. For specific guidance, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html">Supported protocols and ciphers between viewers and CloudFront</a>. Valid values are as follows:</p> <ul> <li> <p> <code>TLS_V1_3_2025</code> (strictest): A post-quantum-ready policy requiring TLS 1.3. It provides the strongest security posture and is ideal for workloads where all clients and browsers are updated to the latest versions. <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html">Supported protocols and ciphers for TLSv1.3_2025</a>.</p> </li> <li> <p> <code>TLS_V1_2_2021</code> (recommended): A post-quantum-ready policy which prefers TLS 1.3 but allows fallback to TLS 1.2 to accommodate older clients. It is the recommended minimum for typical commercial-grade consumer applications. <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html">Supported protocols and ciphers for TLSv1.2_2021</a>.</p> </li> <li> <p> <code>TLS_V1</code> (strongly discouraged): Permits fallback to TLS 1.0. It offers the broadest compatibility, including support for legacy clients that are more than a decade old. This compatibility comes at the expense of allowing TLS versions and cryptographic algorithms that are no longer considered safe for commercial use. <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html">Supported protocols and ciphers for TLSv1</a>.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomDomainConfigType) -> dict:
    out: dict = {}
    out["CertificateArn"] = value["certificate_arn"]
    if "security_policy" in value:
        import capo_cognito_identity_provider.types.security_policy_type

        out["SecurityPolicy"] = (
            capo_cognito_identity_provider.types.security_policy_type.serialize_aws_json_1_1(
                value["security_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomDomainConfigType:
    out: CustomDomainConfigType = {}  # type: ignore[typeddict-item]
    if data.get("CertificateArn") is not None:
        out["certificate_arn"] = data["CertificateArn"]
    else:
        raise DeserializationError("CustomDomainConfigType.certificate_arn required")
    if data.get("SecurityPolicy") is not None:
        import capo_cognito_identity_provider.types.security_policy_type

        out["security_policy"] = (
            capo_cognito_identity_provider.types.security_policy_type.deserialize_aws_json_1_1(
                data["SecurityPolicy"]
            )
        )
    return out
