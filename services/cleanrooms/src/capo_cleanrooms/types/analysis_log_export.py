"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisLogExport``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.analysis_log_export_error
    import capo_cleanrooms.types.analysis_log_export_identifier
    import capo_cleanrooms.types.analysis_log_export_result_configuration
    import capo_cleanrooms.types.analysis_log_export_status
    import capo_cleanrooms.types.log_export_analysis_type
    import capo_cleanrooms.types.uuid


class AnalysisLogExport(TypedDict, closed=True):
    analysis_log_export_id: "capo_cleanrooms.types.analysis_log_export_identifier.AnalysisLogExportIdentifier"
    """<p>The unique identifier of the analysis log export.</p>"""
    analysis_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the protected query that the analysis logs were exported for.</p>"""
    analysis_type: (
        "capo_cleanrooms.types.log_export_analysis_type.LogExportAnalysisType"
    )
    """<p>The type of analysis that the logs were exported for. Currently, only <code>PROTECTED_QUERY</code> is supported.</p>"""
    membership_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the membership that the analysis log export belongs to.</p>"""
    status: "capo_cleanrooms.types.analysis_log_export_status.AnalysisLogExportStatus"
    """<p>The status of the analysis log export. Possible values are:</p> <ul> <li> <p> <code>IN_PROGRESS</code> – The export is currently running.</p> </li> <li> <p> <code>SUCCESS</code> – The export completed successfully.</p> </li> <li> <p> <code>FAILED</code> – The export failed. See the <code>error</code> field for details.</p> </li> </ul>"""
    result_configuration: "capo_cleanrooms.types.analysis_log_export_result_configuration.AnalysisLogExportResultConfiguration"
    """<p>Contains the details needed to write the exported analysis logs.</p>"""
    create_time: "datetime.datetime"
    """<p>The time the analysis log export was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The time the analysis log export was last updated.</p>"""
    error: NotRequired[
        "capo_cleanrooms.types.analysis_log_export_error.AnalysisLogExportError"
    ]
    """<p>The analysis log export error. This is present only when the export <code>status</code> is <code>FAILED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisLogExport) -> dict:
    out: dict = {}
    out["analysisLogExportId"] = value["analysis_log_export_id"]
    out["analysisId"] = value["analysis_id"]
    import capo_cleanrooms.types.log_export_analysis_type

    out["analysisType"] = capo_cleanrooms.types.log_export_analysis_type.serialize_json(
        value["analysis_type"]
    )
    out["membershipId"] = value["membership_id"]
    import capo_cleanrooms.types.analysis_log_export_status

    out["status"] = capo_cleanrooms.types.analysis_log_export_status.serialize_json(
        value["status"]
    )
    import capo_cleanrooms.types.analysis_log_export_result_configuration

    out["resultConfiguration"] = (
        capo_cleanrooms.types.analysis_log_export_result_configuration.serialize_json(
            value["result_configuration"]
        )
    )
    import capo_cleanrooms.types._prelude.timestamp

    out["createTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_cleanrooms.types._prelude.timestamp

    out["updateTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    if "error" in value:
        import capo_cleanrooms.types.analysis_log_export_error

        out["error"] = capo_cleanrooms.types.analysis_log_export_error.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> AnalysisLogExport:
    out: AnalysisLogExport = {}  # type: ignore[typeddict-item]
    if data.get("analysisLogExportId") is not None:
        out["analysis_log_export_id"] = data["analysisLogExportId"]
    else:
        out["analysis_log_export_id"] = ""
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
    if data.get("membershipId") is not None:
        out["membership_id"] = data["membershipId"]
    else:
        out["membership_id"] = ""
    if data.get("status") is not None:
        import capo_cleanrooms.types.analysis_log_export_status

        out["status"] = (
            capo_cleanrooms.types.analysis_log_export_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_cleanrooms.types.analysis_log_export_status.AnalysisLogExportStatus",
            "",
        )
    if data.get("resultConfiguration") is not None:
        import capo_cleanrooms.types.analysis_log_export_result_configuration

        out["result_configuration"] = (
            capo_cleanrooms.types.analysis_log_export_result_configuration.deserialize_json(
                data["resultConfiguration"]
            )
        )
    else:
        raise DeserializationError("AnalysisLogExport.result_configuration required")
    if data.get("createTime") is not None:
        import capo_cleanrooms.types._prelude.timestamp

        out["create_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["createTime"]
        )
    else:
        import datetime

        out["create_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("updateTime") is not None:
        import capo_cleanrooms.types._prelude.timestamp

        out["update_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["updateTime"]
        )
    else:
        import datetime

        out["update_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("error") is not None:
        import capo_cleanrooms.types.analysis_log_export_error

        out["error"] = capo_cleanrooms.types.analysis_log_export_error.deserialize_json(
            data["error"]
        )
    return out
