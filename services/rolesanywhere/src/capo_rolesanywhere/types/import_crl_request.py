"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#ImportCrlRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rolesanywhere.types.alias_name
    import capo_rolesanywhere.types.resource_name
    import capo_rolesanywhere.types.tag_list
    import capo_rolesanywhere.types.trust_anchor_identifier_arn


class ImportCrlRequest(TypedDict, closed=True):
    name: "capo_rolesanywhere.types.resource_name.ResourceName"
    """<p>The name of the certificate revocation list (CRL).</p>"""
    crl_data: "bytes"
    """<p>The x509 v3 specified certificate revocation list (CRL).</p>"""
    enabled: NotRequired["bool"]
    """<p>Specifies whether the certificate revocation list (CRL) is enabled.</p>"""
    tags: NotRequired["capo_rolesanywhere.types.tag_list.TagList"]
    """<p>A list of tags to attach to the certificate revocation list (CRL).</p>"""
    trust_anchor_arn: (
        "capo_rolesanywhere.types.trust_anchor_identifier_arn.TrustAnchorIdentifierArn"
    )
    """<p>The ARN of the trust anchor that the certificate revocation list (CRL) provides revocation for. Specify the trust anchor ARN that contains the trust anchor ID. This parameter doesn't support alias ARNs. If you specify an alias ARN, the request fails with <code>ResourceNotFoundException</code>.</p>"""
    alias_name: NotRequired["capo_rolesanywhere.types.alias_name.AliasName"]
    """<p>An alias for the certificate revocation list (CRL). When you set an alias, the response includes the alias ARN of the CRL in <code>aliasArn</code>.</p> <p>An alias name contains 1 to 256 characters. It must begin with a letter (A-Z or a-z). It can contain only letters (A-Z and a-z), numbers (0-9), underscores (_), hyphens (-), and forward slashes (/). A forward slash can appear only between two other characters, so an alias name can't end with a forward slash or contain two in a row. Alias names that begin with <code>aws/</code>, in any combination of uppercase and lowercase letters, are reserved. Alias names are case sensitive.</p> <p>The alias name must be unique among resources of the same type in your account and Region. If another resource of the same type already has the alias, the request fails with a <code>ValidationException</code>. An invalid or reserved alias name also causes a <code>ValidationException</code>.</p> <p>If you omit this parameter or specify an empty string, the resource is created without an alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportCrlRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_rolesanywhere.types._prelude.blob

    out["crlData"] = capo_rolesanywhere.types._prelude.blob.serialize_json(
        value["crl_data"]
    )
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "tags" in value:
        import capo_rolesanywhere.types.tag_list

        out["tags"] = capo_rolesanywhere.types.tag_list.serialize_json(value["tags"])
    out["trustAnchorArn"] = value["trust_anchor_arn"]
    if "alias_name" in value:
        out["aliasName"] = value["alias_name"]
    return out


def deserialize_json(data: dict) -> ImportCrlRequest:
    out: ImportCrlRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("crlData") is not None:
        import capo_rolesanywhere.types._prelude.blob

        out["crl_data"] = capo_rolesanywhere.types._prelude.blob.deserialize_json(
            data["crlData"]
        )
    else:
        out["crl_data"] = b""
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    if data.get("tags") is not None:
        import capo_rolesanywhere.types.tag_list

        out["tags"] = capo_rolesanywhere.types.tag_list.deserialize_json(data["tags"])
    if data.get("trustAnchorArn") is not None:
        out["trust_anchor_arn"] = data["trustAnchorArn"]
    else:
        out["trust_anchor_arn"] = ""
    if data.get("aliasName") is not None:
        out["alias_name"] = data["aliasName"]
    return out


def redact_sensitive(value: ImportCrlRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        import capo_rolesanywhere.types.tag_list

        out["tags"] = capo_rolesanywhere.types.tag_list.redact_sensitive(value["tags"])
    return out
