"""Generated from Smithy shape ``com.amazonaws.configservice#AssociateResourceTypesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.amazon_resource_name
    import capo_config_service.types.resource_type_list


class AssociateResourceTypesRequest(TypedDict, closed=True):
    configuration_recorder_arn: (
        "capo_config_service.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The Amazon Resource Name (ARN) of the specified configuration recorder.</p>"""
    resource_types: "capo_config_service.types.resource_type_list.ResourceTypeList"
    """<p>The list of resource types you want to add to the recording group of the specified configuration recorder.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateResourceTypesRequest) -> dict:
    out: dict = {}
    out["ConfigurationRecorderArn"] = value["configuration_recorder_arn"]
    import capo_config_service.types.resource_type_list

    out["ResourceTypes"] = (
        capo_config_service.types.resource_type_list.serialize_aws_json_1_1(
            value["resource_types"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateResourceTypesRequest:
    out: AssociateResourceTypesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConfigurationRecorderArn") is not None:
        out["configuration_recorder_arn"] = data["ConfigurationRecorderArn"]
    else:
        out["configuration_recorder_arn"] = ""
    if data.get("ResourceTypes") is not None:
        import capo_config_service.types.resource_type_list

        out["resource_types"] = (
            capo_config_service.types.resource_type_list.deserialize_aws_json_1_1(
                data["ResourceTypes"]
            )
        )
    else:
        out["resource_types"] = []
    return out
