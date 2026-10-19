"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.certificate_name
    import capo_lightsail.types.domain_name
    import capo_lightsail.types.subject_alternative_name_list
    import capo_lightsail.types.tag_list


class CreateCertificateRequest(TypedDict, closed=True):
    certificate_name: "capo_lightsail.types.certificate_name.CertificateName"
    """<p>The name for the certificate.</p>"""
    domain_name: "capo_lightsail.types.domain_name.DomainName"
    """<p>The domain name (<code>example.com</code>) for the certificate.</p>"""
    subject_alternative_names: NotRequired[
        "capo_lightsail.types.subject_alternative_name_list.SubjectAlternativeNameList"
    ]
    """<p>An array of strings that specify the alternate domains (<code>example2.com</code>) and subdomains (<code>blog.example.com</code>) for the certificate.</p> <p>You can specify a maximum of nine alternate domains (in addition to the primary domain name).</p> <p>Wildcard domain entries (<code>*.example.com</code>) are not supported.</p>"""
    tags: NotRequired["capo_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values to add to the certificate during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCertificateRequest) -> dict:
    out: dict = {}
    out["certificateName"] = value["certificate_name"]
    out["domainName"] = value["domain_name"]
    if "subject_alternative_names" in value:
        import capo_lightsail.types.subject_alternative_name_list

        out["subjectAlternativeNames"] = (
            capo_lightsail.types.subject_alternative_name_list.serialize_aws_json_1_1(
                value["subject_alternative_names"]
            )
        )
    if "tags" in value:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCertificateRequest:
    out: CreateCertificateRequest = {}  # type: ignore[typeddict-item]
    if data.get("certificateName") is not None:
        out["certificate_name"] = data["certificateName"]
    else:
        out["certificate_name"] = ""
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    else:
        out["domain_name"] = ""
    if data.get("subjectAlternativeNames") is not None:
        import capo_lightsail.types.subject_alternative_name_list

        out["subject_alternative_names"] = (
            capo_lightsail.types.subject_alternative_name_list.deserialize_aws_json_1_1(
                data["subjectAlternativeNames"]
            )
        )
    if data.get("tags") is not None:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
