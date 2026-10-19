"""Generated from Smithy shape ``com.amazonaws.securityagent#ImportSecurityRequirementsInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.import_source
    import capo_securityagent.types.security_requirement_pack_id


class ImportSecurityRequirementsInput(TypedDict, closed=True):
    pack_id: "capo_securityagent.types.security_requirement_pack_id.SecurityRequirementPackId"
    """<p>The unique identifier of the security requirement pack to import requirements into.</p>"""
    input: "capo_securityagent.types.import_source.ImportSource"
    """<p>The import source containing the documents to extract security requirements from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportSecurityRequirementsInput) -> dict:
    out: dict = {}
    out["packId"] = value["pack_id"]
    import capo_securityagent.types.import_source

    out["input"] = capo_securityagent.types.import_source.serialize_json(value["input"])
    return out


def deserialize_json(data: dict) -> ImportSecurityRequirementsInput:
    out: ImportSecurityRequirementsInput = {}  # type: ignore[typeddict-item]
    if data.get("packId") is not None:
        out["pack_id"] = data["packId"]
    else:
        out["pack_id"] = ""
    if data.get("input") is not None:
        import capo_securityagent.types.import_source

        out["input"] = capo_securityagent.types.import_source.deserialize_json(
            data["input"]
        )
    else:
        import capo_securityagent.types._unknown

        out["input"] = capo_securityagent.types._unknown.UnknownUnionMember("")
    return out


def redact_sensitive(value: ImportSecurityRequirementsInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input" in value:
        import capo_securityagent.types.import_source

        out["input"] = capo_securityagent.types.import_source.redact_sensitive(
            value["input"]
        )
    return out
