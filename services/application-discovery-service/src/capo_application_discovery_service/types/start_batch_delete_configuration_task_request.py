"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#StartBatchDeleteConfigurationTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.configuration_id_list
    import capo_application_discovery_service.types.deletion_configuration_item_type


class StartBatchDeleteConfigurationTaskRequest(TypedDict, closed=True):
    configuration_type: "capo_application_discovery_service.types.deletion_configuration_item_type.DeletionConfigurationItemType"
    """<p> The type of configuration item to delete. Supported types are: SERVER. </p>"""
    configuration_ids: "capo_application_discovery_service.types.configuration_id_list.ConfigurationIdList"
    """<p> The list of configuration IDs that will be deleted by the task. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartBatchDeleteConfigurationTaskRequest) -> dict:
    out: dict = {}
    import capo_application_discovery_service.types.deletion_configuration_item_type

    out["configurationType"] = (
        capo_application_discovery_service.types.deletion_configuration_item_type.serialize_aws_json_1_1(
            value["configuration_type"]
        )
    )
    import capo_application_discovery_service.types.configuration_id_list

    out["configurationIds"] = (
        capo_application_discovery_service.types.configuration_id_list.serialize_aws_json_1_1(
            value["configuration_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartBatchDeleteConfigurationTaskRequest:
    out: StartBatchDeleteConfigurationTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("configurationType") is not None:
        import capo_application_discovery_service.types.deletion_configuration_item_type

        out["configuration_type"] = (
            capo_application_discovery_service.types.deletion_configuration_item_type.deserialize_aws_json_1_1(
                data["configurationType"]
            )
        )
    else:
        import typing

        out["configuration_type"] = typing.cast(
            "capo_application_discovery_service.types.deletion_configuration_item_type.DeletionConfigurationItemType",
            "",
        )
    if data.get("configurationIds") is not None:
        import capo_application_discovery_service.types.configuration_id_list

        out["configuration_ids"] = (
            capo_application_discovery_service.types.configuration_id_list.deserialize_aws_json_1_1(
                data["configurationIds"]
            )
        )
    else:
        out["configuration_ids"] = []
    return out
