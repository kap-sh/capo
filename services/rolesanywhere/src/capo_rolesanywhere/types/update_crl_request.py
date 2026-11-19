"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#UpdateCrlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rolesanywhere.types.alias_name
    import capo_rolesanywhere.types.crl_identifier
    import capo_rolesanywhere.types.resource_name


class UpdateCrlRequest(TypedDict, closed=True):
    crl_id: "capo_rolesanywhere.types.crl_identifier.CrlIdentifier"
    """<p>The certificate revocation list (CRL) to act on. You can specify one of the following:</p> <ul> <li> <p>The CRL ID.</p> </li> <li> <p>The CRL ARN.</p> </li> <li> <p>The alias ARN of the CRL.</p> </li> </ul> <p>An ARN must be for a CRL in your account and Region.</p>"""
    name: NotRequired["capo_rolesanywhere.types.resource_name.ResourceName"]
    """<p>The name of the Crl.</p>"""
    crl_data: NotRequired["bytes"]
    """<p>The x509 v3 specified certificate revocation list (CRL).</p>"""
    alias_name: NotRequired["capo_rolesanywhere.types.alias_name.AliasName"]
    """<p>The alias for the certificate revocation list (CRL).</p> <p>You can use this parameter in the following ways:</p> <ul> <li> <p>To set or change the alias, specify the new alias name. After the change, the previous alias ARN no longer identifies the resource. You can then assign the previous alias to another resource of the same type. A change can take a short time to take effect for requests that use an alias ARN.</p> </li> <li> <p>To remove the alias, specify an empty string.</p> </li> <li> <p>To keep the current alias, omit this parameter.</p> </li> </ul> <p>An alias name contains 1 to 256 characters. It must begin with a letter (A-Z or a-z). It can contain only letters (A-Z and a-z), numbers (0-9), underscores (_), hyphens (-), and forward slashes (/). A forward slash can appear only between two other characters, so an alias name can't end with a forward slash or contain two in a row. Alias names that begin with <code>aws/</code>, in any combination of uppercase and lowercase letters, are reserved. Alias names are case sensitive.</p> <p>The alias name must be unique among resources of the same type in your account and Region. If another resource of the same type already has the alias, the request fails with a <code>ValidationException</code>. An invalid or reserved alias name also causes a <code>ValidationException</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCrlRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "crl_data" in value:
        import capo_rolesanywhere.types._prelude.blob

        out["crlData"] = capo_rolesanywhere.types._prelude.blob.serialize_json(
            value["crl_data"]
        )
    if "alias_name" in value:
        out["aliasName"] = value["alias_name"]
    return out


def deserialize_json(data: dict) -> UpdateCrlRequest:
    out: UpdateCrlRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("crlData") is not None:
        import capo_rolesanywhere.types._prelude.blob

        out["crl_data"] = capo_rolesanywhere.types._prelude.blob.deserialize_json(
            data["crlData"]
        )
    if data.get("aliasName") is not None:
        out["alias_name"] = data["aliasName"]
    return out
