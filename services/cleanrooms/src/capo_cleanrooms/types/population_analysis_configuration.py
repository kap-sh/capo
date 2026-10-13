"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PopulationAnalysisConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.population_analysis_sql_parameters


class _PopulationAnalysisConfiguration_sqlParameters(TypedDict, closed=True):
    sqlParameters: "capo_cleanrooms.types.population_analysis_sql_parameters.PopulationAnalysisSqlParameters"


PopulationAnalysisConfiguration: TypeAlias = (
    _PopulationAnalysisConfiguration_sqlParameters
)


# --- restJson1 ser/de ---
def serialize_json(value: PopulationAnalysisConfiguration) -> dict:
    if "sqlParameters" in value:
        import capo_cleanrooms.types.population_analysis_sql_parameters

        return {
            "sqlParameters": capo_cleanrooms.types.population_analysis_sql_parameters.serialize_json(
                value["sqlParameters"]
            )
        }
    else:
        raise SerializationError("PopulationAnalysisConfiguration: no variant present")


def deserialize_json(data: dict) -> PopulationAnalysisConfiguration:
    if data.get("sqlParameters") is not None:
        import capo_cleanrooms.types.population_analysis_sql_parameters

        return {
            "sqlParameters": capo_cleanrooms.types.population_analysis_sql_parameters.deserialize_json(
                data["sqlParameters"]
            )
        }
    else:
        raise DeserializationError(
            "PopulationAnalysisConfiguration: no recognized variant key"
        )


def redact_sensitive(value: PopulationAnalysisConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sqlParameters" in value:
        out["sqlParameters"] = "*** Sensitive Data Redacted ***"
    return out
