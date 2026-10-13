"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IntermediateTableActiveVersion``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.analysis_identifier
    import capo_cleanrooms.types.intermediate_table_inherited_constraints
    import capo_cleanrooms.types.kms_key_arn
    import capo_cleanrooms.types.parameter_map
    import capo_cleanrooms.types.populate_intermediate_table_analysis_type
    import capo_cleanrooms.types.uuid


class IntermediateTableActiveVersion(TypedDict, closed=True):
    version_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the active version.</p>"""
    analysis_id: "capo_cleanrooms.types.analysis_identifier.AnalysisIdentifier"
    """<p>The identifier of the protected query that created this version.</p>"""
    analysis_type: "capo_cleanrooms.types.populate_intermediate_table_analysis_type.PopulateIntermediateTableAnalysisType"
    """<p>The type of analysis that created this version.</p>"""
    kms_key_arn: NotRequired["capo_cleanrooms.types.kms_key_arn.KMSKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt this version's data.</p>"""
    parameters: NotRequired["capo_cleanrooms.types.parameter_map.ParameterMap"]
    """<p>The runtime parameters that were used when populating this version.</p>"""
    inherited_constraints: "capo_cleanrooms.types.intermediate_table_inherited_constraints.IntermediateTableInheritedConstraints"
    """<p>The privacy constraints inherited from parent tables at the time this version was populated.</p>"""
    expiration_time: NotRequired["datetime.datetime"]
    """<p>The time when this version expires based on the retention period.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntermediateTableActiveVersion) -> dict:
    out: dict = {}
    out["versionId"] = value["version_id"]
    out["analysisId"] = value["analysis_id"]
    import capo_cleanrooms.types.populate_intermediate_table_analysis_type

    out["analysisType"] = (
        capo_cleanrooms.types.populate_intermediate_table_analysis_type.serialize_json(
            value["analysis_type"]
        )
    )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "parameters" in value:
        import capo_cleanrooms.types.parameter_map

        out["parameters"] = capo_cleanrooms.types.parameter_map.serialize_json(
            value["parameters"]
        )
    import capo_cleanrooms.types.intermediate_table_inherited_constraints

    out["inheritedConstraints"] = (
        capo_cleanrooms.types.intermediate_table_inherited_constraints.serialize_json(
            value["inherited_constraints"]
        )
    )
    if "expiration_time" in value:
        import capo_cleanrooms.types._prelude.timestamp

        out["expirationTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
            value["expiration_time"]
        )
    return out


def deserialize_json(data: dict) -> IntermediateTableActiveVersion:
    out: IntermediateTableActiveVersion = {}  # type: ignore[typeddict-item]
    if data.get("versionId") is not None:
        out["version_id"] = data["versionId"]
    else:
        raise DeserializationError("IntermediateTableActiveVersion.version_id required")
    if data.get("analysisId") is not None:
        out["analysis_id"] = data["analysisId"]
    else:
        raise DeserializationError(
            "IntermediateTableActiveVersion.analysis_id required"
        )
    if data.get("analysisType") is not None:
        import capo_cleanrooms.types.populate_intermediate_table_analysis_type

        out["analysis_type"] = (
            capo_cleanrooms.types.populate_intermediate_table_analysis_type.deserialize_json(
                data["analysisType"]
            )
        )
    else:
        raise DeserializationError(
            "IntermediateTableActiveVersion.analysis_type required"
        )
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("parameters") is not None:
        import capo_cleanrooms.types.parameter_map

        out["parameters"] = capo_cleanrooms.types.parameter_map.deserialize_json(
            data["parameters"]
        )
    if data.get("inheritedConstraints") is not None:
        import capo_cleanrooms.types.intermediate_table_inherited_constraints

        out["inherited_constraints"] = (
            capo_cleanrooms.types.intermediate_table_inherited_constraints.deserialize_json(
                data["inheritedConstraints"]
            )
        )
    else:
        raise DeserializationError(
            "IntermediateTableActiveVersion.inherited_constraints required"
        )
    if data.get("expirationTime") is not None:
        import capo_cleanrooms.types._prelude.timestamp

        out["expiration_time"] = (
            capo_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["expirationTime"]
            )
        )
    return out


def redact_sensitive(value: IntermediateTableActiveVersion) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "parameters" in value:
        out["parameters"] = "*** Sensitive Data Redacted ***"
    return out
