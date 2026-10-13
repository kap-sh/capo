"""Generated from Smithy shape ``com.amazonaws.securityagent#SecurityRequirementArtifactList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.security_requirement_artifact

SecurityRequirementArtifactList: TypeAlias = list[
    "capo_securityagent.types.security_requirement_artifact.SecurityRequirementArtifact"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityRequirementArtifactList) -> list:
    import capo_securityagent.types.security_requirement_artifact

    out: list = []
    for item in value:
        out.append(
            capo_securityagent.types.security_requirement_artifact.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SecurityRequirementArtifactList:
    import capo_securityagent.types.security_requirement_artifact

    out: SecurityRequirementArtifactList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_securityagent.types.security_requirement_artifact.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: SecurityRequirementArtifactList) -> list[Any]:
    import capo_securityagent.types.security_requirement_artifact

    return [
        capo_securityagent.types.security_requirement_artifact.redact_sensitive(item)
        for item in value
    ]
