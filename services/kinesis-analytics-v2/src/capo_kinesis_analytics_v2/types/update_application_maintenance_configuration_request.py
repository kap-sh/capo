"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#UpdateApplicationMaintenanceConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_maintenance_configuration_update
    import capo_kinesis_analytics_v2.types.application_name


class UpdateApplicationMaintenanceConfigurationRequest(TypedDict, closed=True):
    application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName"
    """<p>The name of the application for which you want to update the maintenance configuration.</p>"""
    application_maintenance_configuration_update: "capo_kinesis_analytics_v2.types.application_maintenance_configuration_update.ApplicationMaintenanceConfigurationUpdate"
    """<p>Describes the application maintenance configuration update.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: UpdateApplicationMaintenanceConfigurationRequest,
) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    import capo_kinesis_analytics_v2.types.application_maintenance_configuration_update

    out["ApplicationMaintenanceConfigurationUpdate"] = (
        capo_kinesis_analytics_v2.types.application_maintenance_configuration_update.serialize_aws_json_1_1(
            value["application_maintenance_configuration_update"]
        )
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> UpdateApplicationMaintenanceConfigurationRequest:
    out: UpdateApplicationMaintenanceConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationName") is not None:
        out["application_name"] = data["ApplicationName"]
    else:
        out["application_name"] = ""
    if data.get("ApplicationMaintenanceConfigurationUpdate") is not None:
        import capo_kinesis_analytics_v2.types.application_maintenance_configuration_update

        out["application_maintenance_configuration_update"] = (
            capo_kinesis_analytics_v2.types.application_maintenance_configuration_update.deserialize_aws_json_1_1(
                data["ApplicationMaintenanceConfigurationUpdate"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateApplicationMaintenanceConfigurationRequest.application_maintenance_configuration_update required"
        )
    return out
