"""Generated from Smithy shape ``com.amazonaws.securityhub#ExportOutputSummary``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityhub.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_securityhub.types.findings_output_summary


class _ExportOutputSummary_Findings(TypedDict, closed=True):
    Findings: "capo_securityhub.types.findings_output_summary.FindingsOutputSummary"


ExportOutputSummary: TypeAlias = _ExportOutputSummary_Findings


# --- restJson1 ser/de ---
def serialize_json(value: ExportOutputSummary) -> dict:
    if "Findings" in value:
        import capo_securityhub.types.findings_output_summary

        return {
            "Findings": capo_securityhub.types.findings_output_summary.serialize_json(
                value["Findings"]
            )
        }
    else:
        raise SerializationError("ExportOutputSummary: no variant present")


def deserialize_json(data: dict) -> ExportOutputSummary:
    if data.get("Findings") is not None:
        import capo_securityhub.types.findings_output_summary

        return {
            "Findings": capo_securityhub.types.findings_output_summary.deserialize_json(
                data["Findings"]
            )
        }
    else:
        raise DeserializationError("ExportOutputSummary: no recognized variant key")
