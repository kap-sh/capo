"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#DataPartitionUploadOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.event_expression
    import capo_iotfleetwise.types.language_version


class DataPartitionUploadOptions(TypedDict, closed=True):
    expression: "capo_iotfleetwise.types.event_expression.eventExpression"
    """<p>The logical expression used to recognize what data to collect. For example, <code>$variable.`Vehicle.OutsideAirTemperature` &gt;= 105.0</code>.</p>"""
    condition_language_version: NotRequired[
        "capo_iotfleetwise.types.language_version.languageVersion"
    ]
    """<p>The version of the condition language. Defaults to the most recent condition language version.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DataPartitionUploadOptions) -> dict:
    out: dict = {}
    out["expression"] = value["expression"]
    if "condition_language_version" in value:
        out["conditionLanguageVersion"] = value["condition_language_version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DataPartitionUploadOptions:
    out: DataPartitionUploadOptions = {}  # type: ignore[typeddict-item]
    if data.get("expression") is not None:
        out["expression"] = data["expression"]
    else:
        raise DeserializationError("DataPartitionUploadOptions.expression required")
    if data.get("conditionLanguageVersion") is not None:
        out["condition_language_version"] = data["conditionLanguageVersion"]
    return out


def redact_sensitive(value: DataPartitionUploadOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "expression" in value:
        out["expression"] = "*** Sensitive Data Redacted ***"
    return out
