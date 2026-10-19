"""Generated from Smithy shape ``com.amazonaws.cleanrooms#StartAnalysisLogExportInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_log_export_result_configuration
    import capo_cleanrooms.types.log_export_analysis_type
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.uuid


class StartAnalysisLogExportInput(TypedDict, closed=True):
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>A unique identifier for the membership to export the analysis logs for. Currently accepts a membership ID.</p>"""
    analysis_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the protected query that you want to export the analysis logs for.</p>"""
    analysis_type: (
        "capo_cleanrooms.types.log_export_analysis_type.LogExportAnalysisType"
    )
    """<p>The type of analysis that the logs are exported for. Currently, only <code>PROTECTED_QUERY</code> is supported.</p>"""
    result_configuration: "capo_cleanrooms.types.analysis_log_export_result_configuration.AnalysisLogExportResultConfiguration"
    """<p>The details needed to write the exported analysis logs.</p> <p>You don't need to create an IAM role for log export. Clean Rooms writes the exported logs using your own identity, so Clean Rooms writes the exported logs only where your existing permissions allow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAnalysisLogExportInput) -> dict:
    out: dict = {}
    out["analysisId"] = value["analysis_id"]
    import capo_cleanrooms.types.log_export_analysis_type

    out["analysisType"] = capo_cleanrooms.types.log_export_analysis_type.serialize_json(
        value["analysis_type"]
    )
    import capo_cleanrooms.types.analysis_log_export_result_configuration

    out["resultConfiguration"] = (
        capo_cleanrooms.types.analysis_log_export_result_configuration.serialize_json(
            value["result_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> StartAnalysisLogExportInput:
    out: StartAnalysisLogExportInput = {}  # type: ignore[typeddict-item]
    if data.get("analysisId") is not None:
        out["analysis_id"] = data["analysisId"]
    else:
        out["analysis_id"] = ""
    if data.get("analysisType") is not None:
        import capo_cleanrooms.types.log_export_analysis_type

        out["analysis_type"] = (
            capo_cleanrooms.types.log_export_analysis_type.deserialize_json(
                data["analysisType"]
            )
        )
    else:
        import typing

        out["analysis_type"] = typing.cast(
            "capo_cleanrooms.types.log_export_analysis_type.LogExportAnalysisType", ""
        )
    if data.get("resultConfiguration") is not None:
        import capo_cleanrooms.types.analysis_log_export_result_configuration

        out["result_configuration"] = (
            capo_cleanrooms.types.analysis_log_export_result_configuration.deserialize_json(
                data["resultConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "StartAnalysisLogExportInput.result_configuration required"
        )
    return out
