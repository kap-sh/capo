"""Generated from Smithy shape ``com.amazonaws.datazone#RedshiftRunConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.redshift_credential_configuration
    import capo_datazone.types.redshift_storage
    import capo_datazone.types.relational_filter_configurations


class RedshiftRunConfigurationOutput(TypedDict, closed=True):
    account_id: NotRequired["str"]
    """<p>The ID of the Amazon Web Services account included in the configuration details of the Amazon Redshift data source.</p>"""
    region: NotRequired["str"]
    """<p>The Amazon Web Services region included in the configuration details of the Amazon Redshift data source.</p>"""
    data_access_role: NotRequired["str"]
    """<p>The data access role included in the configuration details of the Amazon Redshift data source.</p>"""
    relational_filter_configurations: "capo_datazone.types.relational_filter_configurations.RelationalFilterConfigurations"
    """<p>The relational filger configurations included in the configuration details of the Amazon Redshift data source.</p>"""
    redshift_credential_configuration: NotRequired[
        "capo_datazone.types.redshift_credential_configuration.RedshiftCredentialConfiguration"
    ]
    redshift_storage: "capo_datazone.types.redshift_storage.RedshiftStorage"


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftRunConfigurationOutput) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "region" in value:
        out["region"] = value["region"]
    if "data_access_role" in value:
        out["dataAccessRole"] = value["data_access_role"]
    import capo_datazone.types.relational_filter_configurations

    out["relationalFilterConfigurations"] = (
        capo_datazone.types.relational_filter_configurations.serialize_json(
            value["relational_filter_configurations"]
        )
    )
    if "redshift_credential_configuration" in value:
        import capo_datazone.types.redshift_credential_configuration

        out["redshiftCredentialConfiguration"] = (
            capo_datazone.types.redshift_credential_configuration.serialize_json(
                value["redshift_credential_configuration"]
            )
        )
    import capo_datazone.types.redshift_storage

    out["redshiftStorage"] = capo_datazone.types.redshift_storage.serialize_json(
        value["redshift_storage"]
    )
    return out


def deserialize_json(data: dict) -> RedshiftRunConfigurationOutput:
    out: RedshiftRunConfigurationOutput = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("dataAccessRole") is not None:
        out["data_access_role"] = data["dataAccessRole"]
    if data.get("relationalFilterConfigurations") is not None:
        import capo_datazone.types.relational_filter_configurations

        out["relational_filter_configurations"] = (
            capo_datazone.types.relational_filter_configurations.deserialize_json(
                data["relationalFilterConfigurations"]
            )
        )
    else:
        out["relational_filter_configurations"] = []
    if data.get("redshiftCredentialConfiguration") is not None:
        import capo_datazone.types.redshift_credential_configuration

        out["redshift_credential_configuration"] = (
            capo_datazone.types.redshift_credential_configuration.deserialize_json(
                data["redshiftCredentialConfiguration"]
            )
        )
    if data.get("redshiftStorage") is not None:
        import capo_datazone.types.redshift_storage

        out["redshift_storage"] = capo_datazone.types.redshift_storage.deserialize_json(
            data["redshiftStorage"]
        )
    else:
        import capo_datazone.types._unknown

        out["redshift_storage"] = capo_datazone.types._unknown.UnknownUnionMember("")
    return out
