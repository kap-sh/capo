"""Generated from Smithy shape ``com.amazonaws.securityhub#ExportOutput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityhub.errors import DeserializationError, SerializationError
from capo_securityhub.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_securityhub.types.findings_output


class _ExportOutput_Findings(TypedDict, closed=True):
    Findings: "capo_securityhub.types.findings_output.FindingsOutput"


ExportOutput: TypeAlias = _ExportOutput_Findings | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: ExportOutput) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ExportOutput: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Findings" in value:
        import capo_securityhub.types.findings_output

        return {
            "Findings": capo_securityhub.types.findings_output.serialize_json(
                value["Findings"]
            )
        }
    else:
        raise SerializationError("ExportOutput: no variant present")


def deserialize_json(data: dict) -> ExportOutput:
    if data.get("Findings") is not None:
        import capo_securityhub.types.findings_output

        return {
            "Findings": capo_securityhub.types.findings_output.deserialize_json(
                data["Findings"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ExportOutput: no recognized variant key")
