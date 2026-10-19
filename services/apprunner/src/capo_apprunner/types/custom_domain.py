"""Generated from Smithy shape ``com.amazonaws.apprunner#CustomDomain``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.certificate_validation_record_list
    import capo_apprunner.types.custom_domain_association_status
    import capo_apprunner.types.domain_name
    import capo_apprunner.types.nullable_boolean


class CustomDomain(TypedDict, closed=True):
    domain_name: "capo_apprunner.types.domain_name.DomainName"
    """<p>An associated custom domain endpoint. It can be a root domain (for example, <code>example.com</code>), a subdomain (for example, <code>login.example.com</code> or <code>admin.login.example.com</code>), or a wildcard (for example, <code>*.example.com</code>).</p>"""
    enable_www_subdomain: "capo_apprunner.types.nullable_boolean.NullableBoolean"
    """<p>When <code>true</code>, the subdomain <code>www.<i>DomainName</i> </code> is associated with the App Runner service in addition to the base domain.</p>"""
    certificate_validation_records: NotRequired[
        "capo_apprunner.types.certificate_validation_record_list.CertificateValidationRecordList"
    ]
    """<p>A list of certificate CNAME records that's used for this domain name.</p>"""
    status: "capo_apprunner.types.custom_domain_association_status.CustomDomainAssociationStatus"
    """<p>The current state of the domain name association.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CustomDomain) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    out["EnableWWWSubdomain"] = value["enable_www_subdomain"]
    if "certificate_validation_records" in value:
        import capo_apprunner.types.certificate_validation_record_list

        out["CertificateValidationRecords"] = (
            capo_apprunner.types.certificate_validation_record_list.serialize_aws_json_1_0(
                value["certificate_validation_records"]
            )
        )
    import capo_apprunner.types.custom_domain_association_status

    out["Status"] = (
        capo_apprunner.types.custom_domain_association_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CustomDomain:
    out: CustomDomain = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    if data.get("EnableWWWSubdomain") is not None:
        out["enable_www_subdomain"] = data["EnableWWWSubdomain"]
    else:
        out["enable_www_subdomain"] = False
    if data.get("CertificateValidationRecords") is not None:
        import capo_apprunner.types.certificate_validation_record_list

        out["certificate_validation_records"] = (
            capo_apprunner.types.certificate_validation_record_list.deserialize_aws_json_1_0(
                data["CertificateValidationRecords"]
            )
        )
    if data.get("Status") is not None:
        import capo_apprunner.types.custom_domain_association_status

        out["status"] = (
            capo_apprunner.types.custom_domain_association_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_apprunner.types.custom_domain_association_status.CustomDomainAssociationStatus",
            "",
        )
    return out
