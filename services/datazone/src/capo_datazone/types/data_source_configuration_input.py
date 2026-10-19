"""Generated from Smithy shape ``com.amazonaws.datazone#DataSourceConfigurationInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.glue_run_configuration_input
    import capo_datazone.types.redshift_run_configuration_input
    import capo_datazone.types.sage_maker_run_configuration_input


class _DataSourceConfigurationInput_glueRunConfiguration(TypedDict, closed=True):
    glueRunConfiguration: (
        "capo_datazone.types.glue_run_configuration_input.GlueRunConfigurationInput"
    )


class _DataSourceConfigurationInput_redshiftRunConfiguration(TypedDict, closed=True):
    redshiftRunConfiguration: "capo_datazone.types.redshift_run_configuration_input.RedshiftRunConfigurationInput"


class _DataSourceConfigurationInput_sageMakerRunConfiguration(TypedDict, closed=True):
    sageMakerRunConfiguration: "capo_datazone.types.sage_maker_run_configuration_input.SageMakerRunConfigurationInput"


DataSourceConfigurationInput: TypeAlias = (
    _DataSourceConfigurationInput_glueRunConfiguration
    | _DataSourceConfigurationInput_redshiftRunConfiguration
    | _DataSourceConfigurationInput_sageMakerRunConfiguration
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceConfigurationInput) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"DataSourceConfigurationInput: cannot serialize unknown variant {value.name!r}"
        )
    elif "glueRunConfiguration" in value:
        import capo_datazone.types.glue_run_configuration_input

        return {
            "glueRunConfiguration": capo_datazone.types.glue_run_configuration_input.serialize_json(
                value["glueRunConfiguration"]
            )
        }
    elif "redshiftRunConfiguration" in value:
        import capo_datazone.types.redshift_run_configuration_input

        return {
            "redshiftRunConfiguration": capo_datazone.types.redshift_run_configuration_input.serialize_json(
                value["redshiftRunConfiguration"]
            )
        }
    elif "sageMakerRunConfiguration" in value:
        import capo_datazone.types.sage_maker_run_configuration_input

        return {
            "sageMakerRunConfiguration": capo_datazone.types.sage_maker_run_configuration_input.serialize_json(
                value["sageMakerRunConfiguration"]
            )
        }
    else:
        raise SerializationError("DataSourceConfigurationInput: no variant present")


def deserialize_json(data: dict) -> DataSourceConfigurationInput:
    if data.get("glueRunConfiguration") is not None:
        import capo_datazone.types.glue_run_configuration_input

        return {
            "glueRunConfiguration": capo_datazone.types.glue_run_configuration_input.deserialize_json(
                data["glueRunConfiguration"]
            )
        }
    elif data.get("redshiftRunConfiguration") is not None:
        import capo_datazone.types.redshift_run_configuration_input

        return {
            "redshiftRunConfiguration": capo_datazone.types.redshift_run_configuration_input.deserialize_json(
                data["redshiftRunConfiguration"]
            )
        }
    elif data.get("sageMakerRunConfiguration") is not None:
        import capo_datazone.types.sage_maker_run_configuration_input

        return {
            "sageMakerRunConfiguration": capo_datazone.types.sage_maker_run_configuration_input.deserialize_json(
                data["sageMakerRunConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "DataSourceConfigurationInput: no recognized variant key"
        )
