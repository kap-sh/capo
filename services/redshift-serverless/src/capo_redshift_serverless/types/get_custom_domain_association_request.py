"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetCustomDomainAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.custom_domain_name
    import capo_redshift_serverless.types.workgroup_name


class GetCustomDomainAssociationRequest(TypedDict, closed=True):
    custom_domain_name: (
        "capo_redshift_serverless.types.custom_domain_name.CustomDomainName"
    )
    """<p>The custom domain name associated with the workgroup.</p>"""
    workgroup_name: "capo_redshift_serverless.types.workgroup_name.WorkgroupName"
    """<p>The name of the workgroup associated with the database.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCustomDomainAssociationRequest) -> dict:
    out: dict = {}
    out["customDomainName"] = value["custom_domain_name"]
    out["workgroupName"] = value["workgroup_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCustomDomainAssociationRequest:
    out: GetCustomDomainAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("customDomainName") is not None:
        out["custom_domain_name"] = data["customDomainName"]
    else:
        out["custom_domain_name"] = ""
    if data.get("workgroupName") is not None:
        out["workgroup_name"] = data["workgroupName"]
    else:
        out["workgroup_name"] = ""
    return out
