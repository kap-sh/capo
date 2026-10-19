"""Generated from Smithy shape ``com.amazonaws.securityagent#SecurityRequirementArtifact``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.security_requirement_artifact_format
    import capo_securityagent.types.security_requirement_artifact_name
    import capo_securityagent.types.security_requirement_document_content


class SecurityRequirementArtifact(TypedDict, closed=True):
    name: "capo_securityagent.types.security_requirement_artifact_name.SecurityRequirementArtifactName"
    """<p>The file name of the document.</p>"""
    format: "capo_securityagent.types.security_requirement_artifact_format.SecurityRequirementArtifactFormat"
    """<p>The format of the document. Valid values are MD, PDF, TXT, DOCX, and DOC.</p>"""
    content: "capo_securityagent.types.security_requirement_document_content.SecurityRequirementDocumentContent"
    """<p>The binary content of the document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityRequirementArtifact) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_securityagent.types.security_requirement_artifact_format

    out["format"] = (
        capo_securityagent.types.security_requirement_artifact_format.serialize_json(
            value["format"]
        )
    )
    import capo_securityagent.types.security_requirement_document_content

    out["content"] = (
        capo_securityagent.types.security_requirement_document_content.serialize_json(
            value["content"]
        )
    )
    return out


def deserialize_json(data: dict) -> SecurityRequirementArtifact:
    out: SecurityRequirementArtifact = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("format") is not None:
        import capo_securityagent.types.security_requirement_artifact_format

        out["format"] = (
            capo_securityagent.types.security_requirement_artifact_format.deserialize_json(
                data["format"]
            )
        )
    else:
        import typing

        out["format"] = typing.cast(
            "capo_securityagent.types.security_requirement_artifact_format.SecurityRequirementArtifactFormat",
            "",
        )
    if data.get("content") is not None:
        import capo_securityagent.types.security_requirement_document_content

        out["content"] = (
            capo_securityagent.types.security_requirement_document_content.deserialize_json(
                data["content"]
            )
        )
    else:
        out["content"] = b""
    return out


def redact_sensitive(value: SecurityRequirementArtifact) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        out["content"] = "*** Sensitive Data Redacted ***"
    return out
