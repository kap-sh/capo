"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DescribeConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.configuration_id_list


class DescribeConfigurationsRequest(TypedDict, closed=True):
    configuration_ids: "capo_application_discovery_service.types.configuration_id_list.ConfigurationIdList"
    """<p>One or more configuration IDs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConfigurationsRequest) -> dict:
    out: dict = {}
    import capo_application_discovery_service.types.configuration_id_list

    out["configurationIds"] = (
        capo_application_discovery_service.types.configuration_id_list.serialize_aws_json_1_1(
            value["configuration_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConfigurationsRequest:
    out: DescribeConfigurationsRequest = {}  # type: ignore[typeddict-item]
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
