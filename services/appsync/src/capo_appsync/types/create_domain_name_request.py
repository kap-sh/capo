"""Generated from Smithy shape ``com.amazonaws.appsync#CreateDomainNameRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.certificate_arn
    import capo_appsync.types.description
    import capo_appsync.types.domain_name
    import capo_appsync.types.tag_map


class CreateDomainNameRequest(TypedDict, closed=True):
    domain_name: "capo_appsync.types.domain_name.DomainName"
    """<p>The domain name.</p>"""
    certificate_arn: "capo_appsync.types.certificate_arn.CertificateArn"
    """<p>The Amazon Resource Name (ARN) of the certificate. This can be an Certificate Manager (ACM) certificate or an Identity and Access Management (IAM) server certificate.</p>"""
    description: NotRequired["capo_appsync.types.description.Description"]
    """<p>A description of the <code>DomainName</code>.</p>"""
    tags: NotRequired["capo_appsync.types.tag_map.TagMap"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateDomainNameRequest) -> dict:
    out: dict = {}
    out["domainName"] = value["domain_name"]
    out["certificateArn"] = value["certificate_arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_appsync.types.tag_map

        out["tags"] = capo_appsync.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateDomainNameRequest:
    out: CreateDomainNameRequest = {}  # type: ignore[typeddict-item]
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    else:
        out["domain_name"] = ""
    if data.get("certificateArn") is not None:
        out["certificate_arn"] = data["certificateArn"]
    else:
        out["certificate_arn"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_appsync.types.tag_map

        out["tags"] = capo_appsync.types.tag_map.deserialize_json(data["tags"])
    return out
