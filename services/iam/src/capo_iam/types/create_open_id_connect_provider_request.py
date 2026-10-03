"""Generated from Smithy shape ``com.amazonaws.iam#CreateOpenIDConnectProviderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.client_id_list_type
    import capo_iam.types.open_id_connect_provider_url_type
    import capo_iam.types.tag_list_type
    import capo_iam.types.thumbprint_list_type


class CreateOpenIDConnectProviderRequest(TypedDict, closed=True):
    url: "capo_iam.types.open_id_connect_provider_url_type.OpenIDConnectProviderUrlType"
    """<p>The URL of the identity provider. The URL must begin with <code>https://</code> and should correspond to the <code>iss</code> claim in the provider's OpenID Connect ID tokens. Per the OIDC standard, path components are allowed but query parameters are not. Typically the URL consists of only a hostname, like <code>https://server.example.org</code> or <code>https://example.com</code>. The URL should not contain a port number. </p> <p>You cannot register the same provider multiple times in a single Amazon Web Services account. If you try to submit a URL that has already been used for an OpenID Connect provider in the Amazon Web Services account, you will get an error.</p>"""
    client_id_list: NotRequired["capo_iam.types.client_id_list_type.clientIDListType"]
    """<p>Provides a list of client IDs, also known as audiences. When a mobile or web app registers with an OpenID Connect provider, they establish a value that identifies the application. This is the value that's sent as the <code>client_id</code> parameter on OAuth requests.</p> <p>You can register multiple client IDs with the same provider. For example, you might have multiple applications that use the same OIDC provider. You cannot register more than 100 client IDs with a single IAM OIDC provider.</p> <p>There is no defined format for a client ID. The <code>CreateOpenIDConnectProviderRequest</code> operation accepts client IDs up to 255 characters long.</p>"""
    thumbprint_list: NotRequired[
        "capo_iam.types.thumbprint_list_type.thumbprintListType"
    ]
    """<p>A list of server certificate thumbprints for the OpenID Connect (OIDC) identity provider's server certificates. Typically this list includes only one entry. However, IAM lets you have up to five thumbprints for an OIDC provider. This lets you maintain multiple thumbprints if the identity provider is rotating certificates.</p> <p>This parameter is optional. If it is not included, IAM will retrieve and use the top intermediate certificate authority (CA) thumbprint of the OpenID Connect identity provider server certificate.</p> <p>The server certificate thumbprint is the hex-encoded SHA-1 hash value of the X.509 certificate used by the domain where the OpenID Connect provider makes its keys available. It is always a 40-character string.</p> <p>For example, assume that the OIDC provider is <code>server.example.com</code> and the provider stores its keys at https://keys.server.example.com/openid-connect. In that case, the thumbprint string would be the hex-encoded SHA-1 hash value of the certificate used by <code>https://keys.server.example.com.</code> </p> <p>For more information about obtaining the OIDC provider thumbprint, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/identity-providers-oidc-obtain-thumbprint.html">Obtaining the thumbprint for an OpenID Connect provider</a> in the <i>IAM user Guide</i>.</p> <note> <p>If your OIDC provider's discovery endpoint and JWKS endpoint (<code>jwks_uri</code>) use different certificates or hosts, include the thumbprints for both endpoints in this list.</p> </note>"""
    tags: NotRequired["capo_iam.types.tag_list_type.tagListType"]
    """<p>A list of tags that you want to attach to the new IAM OpenID Connect (OIDC) provider. Each tag consists of a key name and an associated value. For more information about tagging, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html">Tagging IAM resources</a> in the <i>IAM User Guide</i>.</p> <note> <p>If any one of the tags is invalid or if you exceed the allowed maximum number of tags, then the entire request fails and the resource is not created.</p> </note>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateOpenIDConnectProviderRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Url", str(value["url"])))
    if "client_id_list" in value:
        import capo_iam.types.client_id_list_type

        capo_iam.types.client_id_list_type.serialize_query(
            value["client_id_list"], pairs, f"{key_prefix}ClientIDList"
        )
    if "thumbprint_list" in value:
        import capo_iam.types.thumbprint_list_type

        capo_iam.types.thumbprint_list_type.serialize_query(
            value["thumbprint_list"], pairs, f"{key_prefix}ThumbprintList"
        )
    if "tags" in value:
        import capo_iam.types.tag_list_type

        capo_iam.types.tag_list_type.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> CreateOpenIDConnectProviderRequest:
    out: CreateOpenIDConnectProviderRequest = {}  # type: ignore[typeddict-item]
    child_url = el.find("Url")
    if child_url is not None:
        out["url"] = str(child_url.text or "")
    else:
        raise DeserializationError("CreateOpenIDConnectProviderRequest.url required")
    child_client_id_list = el.find("ClientIDList")
    if child_client_id_list is not None:
        import capo_iam.types.client_id_list_type

        out["client_id_list"] = capo_iam.types.client_id_list_type.deserialize_query(
            child_client_id_list
        )
    child_thumbprint_list = el.find("ThumbprintList")
    if child_thumbprint_list is not None:
        import capo_iam.types.thumbprint_list_type

        out["thumbprint_list"] = capo_iam.types.thumbprint_list_type.deserialize_query(
            child_thumbprint_list
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_iam.types.tag_list_type

        out["tags"] = capo_iam.types.tag_list_type.deserialize_query(child_tags)
    return out
