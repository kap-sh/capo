"""Generated from Smithy shape ``com.amazonaws.eventbridge#DescribeConnectionResourceParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eventbridge.types.resource_association_arn
    import capo_eventbridge.types.resource_configuration_arn


class DescribeConnectionResourceParameters(TypedDict, closed=True):
    resource_configuration_arn: (
        "capo_eventbridge.types.resource_configuration_arn.ResourceConfigurationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the resource configuration for the private API.</p>"""
    resource_association_arn: (
        "capo_eventbridge.types.resource_association_arn.ResourceAssociationArn"
    )
    """<p>For connections to private APIs, the Amazon Resource Name (ARN) of the resource association EventBridge created between the connection and the private API's resource configuration.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/connection-private.html#connection-private-snra"> Managing service network resource associations for connections</a> in the <i> <i>Amazon EventBridge User Guide</i> </i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConnectionResourceParameters) -> dict:
    out: dict = {}
    out["ResourceConfigurationArn"] = value["resource_configuration_arn"]
    out["ResourceAssociationArn"] = value["resource_association_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConnectionResourceParameters:
    out: DescribeConnectionResourceParameters = {}  # type: ignore[typeddict-item]
    if data.get("ResourceConfigurationArn") is not None:
        out["resource_configuration_arn"] = data["ResourceConfigurationArn"]
    else:
        raise DeserializationError(
            "DescribeConnectionResourceParameters.resource_configuration_arn required"
        )
    if data.get("ResourceAssociationArn") is not None:
        out["resource_association_arn"] = data["ResourceAssociationArn"]
    else:
        raise DeserializationError(
            "DescribeConnectionResourceParameters.resource_association_arn required"
        )
    return out
