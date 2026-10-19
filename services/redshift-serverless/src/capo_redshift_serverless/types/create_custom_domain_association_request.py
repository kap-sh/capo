"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#CreateCustomDomainAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.custom_domain_certificate_arn_string
    import capo_redshift_serverless.types.custom_domain_name
    import capo_redshift_serverless.types.workgroup_name


class CreateCustomDomainAssociationRequest(TypedDict, closed=True):
    workgroup_name: "capo_redshift_serverless.types.workgroup_name.WorkgroupName"
    """<p>The name of the workgroup associated with the database.</p>"""
    custom_domain_name: (
        "capo_redshift_serverless.types.custom_domain_name.CustomDomainName"
    )
    """<p>The custom domain name to associate with the workgroup.</p>"""
    custom_domain_certificate_arn: "capo_redshift_serverless.types.custom_domain_certificate_arn_string.CustomDomainCertificateArnString"
    """<p>The custom domain name’s certificate Amazon resource name (ARN).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCustomDomainAssociationRequest) -> dict:
    out: dict = {}
    out["workgroupName"] = value["workgroup_name"]
    out["customDomainName"] = value["custom_domain_name"]
    out["customDomainCertificateArn"] = value["custom_domain_certificate_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCustomDomainAssociationRequest:
    out: CreateCustomDomainAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("workgroupName") is not None:
        out["workgroup_name"] = data["workgroupName"]
    else:
        out["workgroup_name"] = ""
    if data.get("customDomainName") is not None:
        out["custom_domain_name"] = data["customDomainName"]
    else:
        out["custom_domain_name"] = ""
    if data.get("customDomainCertificateArn") is not None:
        out["custom_domain_certificate_arn"] = data["customDomainCertificateArn"]
    else:
        out["custom_domain_certificate_arn"] = ""
    return out
