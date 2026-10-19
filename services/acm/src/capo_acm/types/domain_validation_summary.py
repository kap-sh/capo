"""Generated from Smithy shape ``com.amazonaws.acm#DomainValidationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.domain_name_string
    import capo_acm.types.validation_configuration


class DomainValidationSummary(TypedDict, closed=True):
    domain_name: "capo_acm.types.domain_name_string.DomainNameString"
    """<p>The fully qualified domain name (FQDN) in the certificate for which this validation summary applies.</p>"""
    active_validation_configuration: NotRequired[
        "capo_acm.types.validation_configuration.ValidationConfiguration"
    ]
    """<p>The validation configuration currently in effect for this domain. This reflects the validation method that ACM is currently using to validate domain ownership (for example, email or DNS).</p>"""
    requested_validation_configuration: NotRequired[
        "capo_acm.types.validation_configuration.ValidationConfiguration"
    ]
    """<p>The validation configuration for a pending validation method migration. This field is present only when a migration is in progress (for example, from email to DNS validation). It contains the target validation method, the current validation status, and the validation challenge details (such as the CNAME record to add to your DNS configuration).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainValidationSummary) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    if "active_validation_configuration" in value:
        import capo_acm.types.validation_configuration

        out["ActiveValidationConfiguration"] = (
            capo_acm.types.validation_configuration.serialize_aws_json_1_1(
                value["active_validation_configuration"]
            )
        )
    if "requested_validation_configuration" in value:
        import capo_acm.types.validation_configuration

        out["RequestedValidationConfiguration"] = (
            capo_acm.types.validation_configuration.serialize_aws_json_1_1(
                value["requested_validation_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DomainValidationSummary:
    out: DomainValidationSummary = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    if data.get("ActiveValidationConfiguration") is not None:
        import capo_acm.types.validation_configuration

        out["active_validation_configuration"] = (
            capo_acm.types.validation_configuration.deserialize_aws_json_1_1(
                data["ActiveValidationConfiguration"]
            )
        )
    if data.get("RequestedValidationConfiguration") is not None:
        import capo_acm.types.validation_configuration

        out["requested_validation_configuration"] = (
            capo_acm.types.validation_configuration.deserialize_aws_json_1_1(
                data["RequestedValidationConfiguration"]
            )
        )
    return out
