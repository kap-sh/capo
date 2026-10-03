"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCertificateManagerCertificateRenewalSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_certificate_manager_certificate_domain_validation_options
    import capo_securityhub.types.non_empty_string


class AwsCertificateManagerCertificateRenewalSummary(TypedDict, closed=True):
    domain_validation_options: NotRequired[
        "capo_securityhub.types.aws_certificate_manager_certificate_domain_validation_options.AwsCertificateManagerCertificateDomainValidationOptions"
    ]
    """<p>Information about the validation of each domain name in the certificate, as it pertains to Certificate Manager managed renewal. Provided only when the certificate type is <code>AMAZON_ISSUED</code>.</p>"""
    renewal_status: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The status of the Certificate Manager managed renewal of the certificate.</p> <p>Valid values: <code>PENDING_AUTO_RENEWAL</code> | <code>PENDING_VALIDATION</code> | <code>SUCCESS</code> | <code>FAILED</code> </p>"""
    renewal_status_reason: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The reason that a renewal request was unsuccessful. This attribute is used only when <code>RenewalStatus</code> is <code>FAILED</code>.</p> <p>Valid values: <code>NO_AVAILABLE_CONTACTS</code> | <code>ADDITIONAL_VERIFICATION_REQUIRED</code> | <code>DOMAIN_NOT_ALLOWED</code> | <code>INVALID_PUBLIC_DOMAIN</code> | <code>DOMAIN_VALIDATION_DENIED</code> | <code>CAA_ERROR</code> | <code>PCA_LIMIT_EXCEEDED</code> | <code>PCA_INVALID_ARN</code> | <code>PCA_INVALID_STATE</code> | <code>PCA_REQUEST_FAILED</code> | <code>PCA_NAME_CONSTRAINTS_VALIDATION</code> | <code>PCA_RESOURCE_NOT_FOUND</code> | <code>PCA_INVALID_ARGS</code> | <code>PCA_INVALID_DURATION</code> | <code>PCA_ACCESS_DENIED</code> | <code>SLR_NOT_FOUND</code> | <code>OTHER</code> </p>"""
    updated_at: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Indicates when the renewal summary was last updated.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCertificateManagerCertificateRenewalSummary) -> dict:
    out: dict = {}
    if "domain_validation_options" in value:
        import capo_securityhub.types.aws_certificate_manager_certificate_domain_validation_options

        out["DomainValidationOptions"] = (
            capo_securityhub.types.aws_certificate_manager_certificate_domain_validation_options.serialize_json(
                value["domain_validation_options"]
            )
        )
    if "renewal_status" in value:
        out["RenewalStatus"] = value["renewal_status"]
    if "renewal_status_reason" in value:
        out["RenewalStatusReason"] = value["renewal_status_reason"]
    if "updated_at" in value:
        out["UpdatedAt"] = value["updated_at"]
    return out


def deserialize_json(data: dict) -> AwsCertificateManagerCertificateRenewalSummary:
    out: AwsCertificateManagerCertificateRenewalSummary = {}  # type: ignore[typeddict-item]
    if data.get("DomainValidationOptions") is not None:
        import capo_securityhub.types.aws_certificate_manager_certificate_domain_validation_options

        out["domain_validation_options"] = (
            capo_securityhub.types.aws_certificate_manager_certificate_domain_validation_options.deserialize_json(
                data["DomainValidationOptions"]
            )
        )
    if data.get("RenewalStatus") is not None:
        out["renewal_status"] = data["RenewalStatus"]
    if data.get("RenewalStatusReason") is not None:
        out["renewal_status_reason"] = data["RenewalStatusReason"]
    if data.get("UpdatedAt") is not None:
        out["updated_at"] = data["UpdatedAt"]
    return out
