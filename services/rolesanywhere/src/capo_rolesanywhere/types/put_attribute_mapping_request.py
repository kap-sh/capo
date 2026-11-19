"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#PutAttributeMappingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rolesanywhere.types.certificate_field
    import capo_rolesanywhere.types.mapping_rules
    import capo_rolesanywhere.types.profile_identifier


class PutAttributeMappingRequest(TypedDict, closed=True):
    profile_id: "capo_rolesanywhere.types.profile_identifier.ProfileIdentifier"
    """<p>The profile to act on. You can specify one of the following:</p> <ul> <li> <p>The profile ID.</p> </li> <li> <p>The profile ARN.</p> </li> <li> <p>The alias ARN of the profile.</p> </li> </ul> <p>An ARN must be for a profile in your account and Region.</p>"""
    certificate_field: "capo_rolesanywhere.types.certificate_field.CertificateField"
    """<p>Fields (x509Subject, x509Issuer and x509SAN) within X.509 certificates.</p>"""
    mapping_rules: "capo_rolesanywhere.types.mapping_rules.MappingRules"
    """<p>A list of mapping entries for every supported specifier or sub-field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAttributeMappingRequest) -> dict:
    out: dict = {}
    out["certificateField"] = value["certificate_field"]
    import capo_rolesanywhere.types.mapping_rules

    out["mappingRules"] = capo_rolesanywhere.types.mapping_rules.serialize_json(
        value["mapping_rules"]
    )
    return out


def deserialize_json(data: dict) -> PutAttributeMappingRequest:
    out: PutAttributeMappingRequest = {}  # type: ignore[typeddict-item]
    if data.get("certificateField") is not None:
        out["certificate_field"] = data["certificateField"]
    else:
        out["certificate_field"] = ""
    if data.get("mappingRules") is not None:
        import capo_rolesanywhere.types.mapping_rules

        out["mapping_rules"] = capo_rolesanywhere.types.mapping_rules.deserialize_json(
            data["mappingRules"]
        )
    else:
        out["mapping_rules"] = []
    return out
