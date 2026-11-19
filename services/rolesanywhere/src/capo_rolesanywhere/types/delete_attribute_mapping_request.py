"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#DeleteAttributeMappingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rolesanywhere.types.certificate_field
    import capo_rolesanywhere.types.profile_identifier
    import capo_rolesanywhere.types.specifier_list


class DeleteAttributeMappingRequest(TypedDict, closed=True):
    profile_id: "capo_rolesanywhere.types.profile_identifier.ProfileIdentifier"
    """<p>The profile to act on. You can specify one of the following:</p> <ul> <li> <p>The profile ID.</p> </li> <li> <p>The profile ARN.</p> </li> <li> <p>The alias ARN of the profile.</p> </li> </ul> <p>An ARN must be for a profile in your account and Region.</p>"""
    certificate_field: "capo_rolesanywhere.types.certificate_field.CertificateField"
    """<p>Fields (x509Subject, x509Issuer and x509SAN) within X.509 certificates.</p>"""
    specifiers: NotRequired["capo_rolesanywhere.types.specifier_list.SpecifierList"]
    """<p>A list of specifiers of a certificate field; for example, CN, OU, UID from a Subject.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAttributeMappingRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAttributeMappingRequest:
    out: DeleteAttributeMappingRequest = {}  # type: ignore[typeddict-item]
    return out
