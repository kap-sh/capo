"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IntermediateTableVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.analysis_identifier
    import capo_cleanrooms.types.intermediate_table_identifier
    import capo_cleanrooms.types.intermediate_table_version_status
    import capo_cleanrooms.types.kms_key_arn
    import capo_cleanrooms.types.populate_intermediate_table_analysis_type
    import capo_cleanrooms.types.uuid


class IntermediateTableVersionSummary(TypedDict, closed=True):
    version_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the version.</p>"""
    table_id: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier"
    """<p>The unique identifier of the intermediate table that this version belongs to.</p>"""
    create_time: "datetime.datetime"
    """<p>The time the version was created.</p>"""
    analysis_id: "capo_cleanrooms.types.analysis_identifier.AnalysisIdentifier"
    """<p>The identifier of the protected query that created this version.</p>"""
    status: "capo_cleanrooms.types.intermediate_table_version_status.IntermediateTableVersionStatus"
    """<p>The status of the version.</p>"""
    analysis_type: "capo_cleanrooms.types.populate_intermediate_table_analysis_type.PopulateIntermediateTableAnalysisType"
    """<p>The type of analysis that created this version.</p>"""
    kms_key_arn: NotRequired["capo_cleanrooms.types.kms_key_arn.KMSKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt this version's data.</p>"""
    expiration_time: NotRequired["datetime.datetime"]
    """<p>The time when this version expires based on the retention period.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntermediateTableVersionSummary) -> dict:
    out: dict = {}
    out["versionId"] = value["version_id"]
    out["tableId"] = value["table_id"]
    import capo_cleanrooms.types._prelude.timestamp

    out["createTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    out["analysisId"] = value["analysis_id"]
    import capo_cleanrooms.types.intermediate_table_version_status

    out["status"] = (
        capo_cleanrooms.types.intermediate_table_version_status.serialize_json(
            value["status"]
        )
    )
    import capo_cleanrooms.types.populate_intermediate_table_analysis_type

    out["analysisType"] = (
        capo_cleanrooms.types.populate_intermediate_table_analysis_type.serialize_json(
            value["analysis_type"]
        )
    )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "expiration_time" in value:
        import capo_cleanrooms.types._prelude.timestamp

        out["expirationTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
            value["expiration_time"]
        )
    return out


def deserialize_json(data: dict) -> IntermediateTableVersionSummary:
    out: IntermediateTableVersionSummary = {}  # type: ignore[typeddict-item]
    if data.get("versionId") is not None:
        out["version_id"] = data["versionId"]
    else:
        out["version_id"] = ""
    if data.get("tableId") is not None:
        out["table_id"] = data["tableId"]
    else:
        out["table_id"] = ""
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
    if data.get("analysisId") is not None:
        out["analysis_id"] = data["analysisId"]
    else:
        out["analysis_id"] = ""
    if data.get("status") is not None:
        import capo_cleanrooms.types.intermediate_table_version_status

        out["status"] = (
            capo_cleanrooms.types.intermediate_table_version_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_cleanrooms.types.intermediate_table_version_status.IntermediateTableVersionStatus",
            "",
        )
    if data.get("analysisType") is not None:
        import capo_cleanrooms.types.populate_intermediate_table_analysis_type

        out["analysis_type"] = (
            capo_cleanrooms.types.populate_intermediate_table_analysis_type.deserialize_json(
                data["analysisType"]
            )
        )
    else:
        import typing

        out["analysis_type"] = typing.cast(
            "capo_cleanrooms.types.populate_intermediate_table_analysis_type.PopulateIntermediateTableAnalysisType",
            "",
        )
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("expirationTime") is not None:
        import capo_cleanrooms.types._prelude.timestamp

        out["expiration_time"] = (
            capo_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["expirationTime"]
            )
        )
    return out
