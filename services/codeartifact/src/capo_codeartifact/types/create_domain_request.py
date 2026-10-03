"""Generated from Smithy shape ``com.amazonaws.codeartifact#CreateDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.arn
    import capo_codeartifact.types.domain_name
    import capo_codeartifact.types.tag_list


class CreateDomainRequest(TypedDict, closed=True):
    domain: "capo_codeartifact.types.domain_name.DomainName"
    """<p> The name of the domain to create. All domain names in an Amazon Web Services Region that are in the same Amazon Web Services account must be unique. The domain name is used as the prefix in DNS hostnames. Do not use sensitive information in a domain name because it is publicly discoverable. </p>"""
    encryption_key: NotRequired["capo_codeartifact.types.arn.Arn"]
    """<p> The encryption key for the domain. This is used to encrypt content stored in a domain. An encryption key can be a key ID, a key Amazon Resource Name (ARN), a key alias, or a key alias ARN. To specify an <code>encryptionKey</code>, your IAM role must have <code>kms:DescribeKey</code> and <code>kms:CreateGrant</code> permissions on the encryption key that is used. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestSyntax">DescribeKey</a> in the <i>Key Management Service API Reference</i> and <a href="https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html">Key Management Service API Permissions Reference</a> in the <i>Key Management Service Developer Guide</i>. </p> <important> <p> CodeArtifact supports only symmetric CMKs. Do not associate an asymmetric CMK with your domain. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html">Using symmetric and asymmetric keys</a> in the <i>Key Management Service Developer Guide</i>. </p> </important>"""
    tags: NotRequired["capo_codeartifact.types.tag_list.TagList"]
    """<p>One or more tag key-value pairs for the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDomainRequest) -> dict:
    out: dict = {}
    if "encryption_key" in value:
        out["encryptionKey"] = value["encryption_key"]
    if "tags" in value:
        import capo_codeartifact.types.tag_list

        out["tags"] = capo_codeartifact.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateDomainRequest:
    out: CreateDomainRequest = {}  # type: ignore[typeddict-item]
    if data.get("encryptionKey") is not None:
        out["encryption_key"] = data["encryptionKey"]
    if data.get("tags") is not None:
        import capo_codeartifact.types.tag_list

        out["tags"] = capo_codeartifact.types.tag_list.deserialize_json(data["tags"])
    return out
