"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#AssociateConfigurationItemsToApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.application_id
    import capo_application_discovery_service.types.configuration_id_list


class AssociateConfigurationItemsToApplicationRequest(TypedDict, closed=True):
    application_configuration_id: (
        "capo_application_discovery_service.types.application_id.ApplicationId"
    )
    """<p>The configuration ID of an application with which items are to be associated.</p>"""
    configuration_ids: "capo_application_discovery_service.types.configuration_id_list.ConfigurationIdList"
    """<p>The ID of each configuration item to be associated with an application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: AssociateConfigurationItemsToApplicationRequest,
) -> dict:
    out: dict = {}
    out["applicationConfigurationId"] = value["application_configuration_id"]
    import capo_application_discovery_service.types.configuration_id_list

    out["configurationIds"] = (
        capo_application_discovery_service.types.configuration_id_list.serialize_aws_json_1_1(
            value["configuration_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> AssociateConfigurationItemsToApplicationRequest:
    out: AssociateConfigurationItemsToApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("applicationConfigurationId") is not None:
        out["application_configuration_id"] = data["applicationConfigurationId"]
    else:
        out["application_configuration_id"] = ""
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
