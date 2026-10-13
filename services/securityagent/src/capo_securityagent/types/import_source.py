"""Generated from Smithy shape ``com.amazonaws.securityagent#ImportSource``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_securityagent.types.security_requirement_artifact_list


class _ImportSource_documents(TypedDict, closed=True):
    documents: "capo_securityagent.types.security_requirement_artifact_list.SecurityRequirementArtifactList"


ImportSource: TypeAlias = _ImportSource_documents


# --- restJson1 ser/de ---
def serialize_json(value: ImportSource) -> dict:
    if "documents" in value:
        import capo_securityagent.types.security_requirement_artifact_list

        return {
            "documents": capo_securityagent.types.security_requirement_artifact_list.serialize_json(
                value["documents"]
            )
        }
    else:
        raise SerializationError("ImportSource: no variant present")


def deserialize_json(data: dict) -> ImportSource:
    if data.get("documents") is not None:
        import capo_securityagent.types.security_requirement_artifact_list

        return {
            "documents": capo_securityagent.types.security_requirement_artifact_list.deserialize_json(
                data["documents"]
            )
        }
    else:
        raise DeserializationError("ImportSource: no recognized variant key")


def redact_sensitive(value: ImportSource) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "documents" in value:
        import capo_securityagent.types.security_requirement_artifact_list

        out["documents"] = (
            capo_securityagent.types.security_requirement_artifact_list.redact_sensitive(
                value["documents"]
            )
        )
    return out
