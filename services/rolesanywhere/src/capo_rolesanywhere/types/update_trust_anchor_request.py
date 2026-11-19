"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#UpdateTrustAnchorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rolesanywhere.types.alias_name
    import capo_rolesanywhere.types.resource_name
    import capo_rolesanywhere.types.source
    import capo_rolesanywhere.types.trust_anchor_identifier


class UpdateTrustAnchorRequest(TypedDict, closed=True):
    trust_anchor_id: (
        "capo_rolesanywhere.types.trust_anchor_identifier.TrustAnchorIdentifier"
    )
    """<p>The trust anchor to act on. You can specify one of the following:</p> <ul> <li> <p>The trust anchor ID.</p> </li> <li> <p>The trust anchor ARN.</p> </li> <li> <p>The alias ARN of the trust anchor.</p> </li> </ul> <p>An ARN must be for a trust anchor in your account and Region.</p>"""
    name: NotRequired["capo_rolesanywhere.types.resource_name.ResourceName"]
    """<p>The name of the trust anchor.</p>"""
    source: NotRequired["capo_rolesanywhere.types.source.Source"]
    """<p>The trust anchor type and its related certificate data.</p>"""
    crl_dp_revocation_enabled: NotRequired["bool"]
    """<p>Specifies whether the trust anchor checks certificate revocation status against CRL distribution points.</p>"""
    alias_name: NotRequired["capo_rolesanywhere.types.alias_name.AliasName"]
    """<p>The alias for the trust anchor.</p> <p>You can use this parameter in the following ways:</p> <ul> <li> <p>To set or change the alias, specify the new alias name. After the change, the previous alias ARN no longer identifies the resource. You can then assign the previous alias to another resource of the same type. A change can take a short time to take effect for requests that use an alias ARN.</p> </li> <li> <p>To remove the alias, specify an empty string.</p> </li> <li> <p>To keep the current alias, omit this parameter.</p> </li> </ul> <p>An alias name contains 1 to 256 characters. It must begin with a letter (A-Z or a-z). It can contain only letters (A-Z and a-z), numbers (0-9), underscores (_), hyphens (-), and forward slashes (/). A forward slash can appear only between two other characters, so an alias name can't end with a forward slash or contain two in a row. Alias names that begin with <code>aws/</code>, in any combination of uppercase and lowercase letters, are reserved. Alias names are case sensitive.</p> <p>The alias name must be unique among resources of the same type in your account and Region. If another resource of the same type already has the alias, the request fails with a <code>ValidationException</code>. An invalid or reserved alias name also causes a <code>ValidationException</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTrustAnchorRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "source" in value:
        import capo_rolesanywhere.types.source

        out["source"] = capo_rolesanywhere.types.source.serialize_json(value["source"])
    if "crl_dp_revocation_enabled" in value:
        out["crlDpRevocationEnabled"] = value["crl_dp_revocation_enabled"]
    if "alias_name" in value:
        out["aliasName"] = value["alias_name"]
    return out


def deserialize_json(data: dict) -> UpdateTrustAnchorRequest:
    out: UpdateTrustAnchorRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("source") is not None:
        import capo_rolesanywhere.types.source

        out["source"] = capo_rolesanywhere.types.source.deserialize_json(data["source"])
    if data.get("crlDpRevocationEnabled") is not None:
        out["crl_dp_revocation_enabled"] = data["crlDpRevocationEnabled"]
    if data.get("aliasName") is not None:
        out["alias_name"] = data["aliasName"]
    return out
