"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ProtectedQueryInputParameters``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanroomsml.types.compute_configuration
    import capo_cleanroomsml.types.protected_query_sql_parameters
    import capo_cleanroomsml.types.result_format


class ProtectedQueryInputParameters(TypedDict, closed=True):
    sql_parameters: "capo_cleanroomsml.types.protected_query_sql_parameters.ProtectedQuerySQLParameters"
    compute_configuration: NotRequired[
        "capo_cleanroomsml.types.compute_configuration.ComputeConfiguration"
    ]
    """<p>Provides configuration information for the workers that will perform the protected query.</p>"""
    result_format: "capo_cleanroomsml.types.result_format.ResultFormat"
    """<p>The format in which the query results should be returned. If not specified, defaults to <code>CSV</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedQueryInputParameters) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types.protected_query_sql_parameters

    out["sqlParameters"] = (
        capo_cleanroomsml.types.protected_query_sql_parameters.serialize_json(
            value["sql_parameters"]
        )
    )
    if "compute_configuration" in value:
        import capo_cleanroomsml.types.compute_configuration

        out["computeConfiguration"] = (
            capo_cleanroomsml.types.compute_configuration.serialize_json(
                value["compute_configuration"]
            )
        )
    import capo_cleanroomsml.types.result_format

    out["resultFormat"] = capo_cleanroomsml.types.result_format.serialize_json(
        value.get("result_format", "CSV")
    )
    return out


def deserialize_json(data: dict) -> ProtectedQueryInputParameters:
    out: ProtectedQueryInputParameters = {}  # type: ignore[typeddict-item]
    if data.get("sqlParameters") is not None:
        import capo_cleanroomsml.types.protected_query_sql_parameters

        out["sql_parameters"] = (
            capo_cleanroomsml.types.protected_query_sql_parameters.deserialize_json(
                data["sqlParameters"]
            )
        )
    else:
        raise DeserializationError(
            "ProtectedQueryInputParameters.sql_parameters required"
        )
    if data.get("computeConfiguration") is not None:
        import capo_cleanroomsml.types.compute_configuration

        out["compute_configuration"] = (
            capo_cleanroomsml.types.compute_configuration.deserialize_json(
                data["computeConfiguration"]
            )
        )
    if data.get("resultFormat") is not None:
        import capo_cleanroomsml.types.result_format

        out["result_format"] = capo_cleanroomsml.types.result_format.deserialize_json(
            data["resultFormat"]
        )
    else:
        out["result_format"] = "CSV"
    return out


def redact_sensitive(value: ProtectedQueryInputParameters) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sql_parameters" in value:
        out["sql_parameters"] = "*** Sensitive Data Redacted ***"
    return out
