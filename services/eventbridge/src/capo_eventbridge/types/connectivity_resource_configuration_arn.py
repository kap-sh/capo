"""Generated from Smithy shape ``com.amazonaws.eventbridge#ConnectivityResourceConfigurationArn``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.resource_configuration_arn


class ConnectivityResourceConfigurationArn(TypedDict, closed=True):
    resource_configuration_arn: (
        "capo_eventbridge.types.resource_configuration_arn.ResourceConfigurationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Amazon VPC Lattice resource configuration for the resource endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectivityResourceConfigurationArn) -> dict:
    out: dict = {}
    out["ResourceConfigurationArn"] = value["resource_configuration_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectivityResourceConfigurationArn:
    out: ConnectivityResourceConfigurationArn = {}  # type: ignore[typeddict-item]
    if data.get("ResourceConfigurationArn") is not None:
        out["resource_configuration_arn"] = data["ResourceConfigurationArn"]
    else:
        out["resource_configuration_arn"] = ""
    return out
