"""Generated from Smithy shape ``com.amazonaws.ssm#InstanceInformationStringFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.instance_information_filter_value_set
    import capo_ssm.types.instance_information_string_filter_key


class InstanceInformationStringFilter(TypedDict, closed=True):
    key: "capo_ssm.types.instance_information_string_filter_key.InstanceInformationStringFilterKey"
    """<p>The filter key name to describe your managed nodes.</p> <p>Valid filter key values: ActivationIds | AgentVersion | AssociationStatus | IamRole | InstanceIds | PingStatus | PlatformTypes | ResourceType | SourceIds | SourceTypes | "tag-key" | "tag:<code>{keyname}</code> </p> <ul> <li> <p>Valid values for the <code>AssociationStatus</code> filter key: Success | Pending | Failed</p> </li> <li> <p>Valid values for the <code>PingStatus</code> filter key: Online | ConnectionLost | Inactive (deprecated)</p> </li> <li> <p>Valid values for the <code>PlatformTypes</code> filter key: Windows | Linux | MacOS</p> </li> <li> <p>Valid values for the <code>ResourceType</code> filter key: EC2Instance | ManagedInstance</p> </li> <li> <p>Valid values for the <code>SourceType</code> filter key: AWS::EC2::Instance | AWS::SSM::ManagedInstance | AWS::IoT::Thing | Microsoft.Compute/virtualMachines</p> </li> <li> <p>Valid tag examples: <code>Key=tag-key,Values=Purpose</code> | <code>Key=tag:Purpose,Values=Test</code>.</p> </li> </ul>"""
    values: "capo_ssm.types.instance_information_filter_value_set.InstanceInformationFilterValueSet"
    """<p>The filter values.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceInformationStringFilter) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    import capo_ssm.types.instance_information_filter_value_set

    out["Values"] = (
        capo_ssm.types.instance_information_filter_value_set.serialize_aws_json_1_1(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceInformationStringFilter:
    out: InstanceInformationStringFilter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("InstanceInformationStringFilter.key required")
    if data.get("Values") is not None:
        import capo_ssm.types.instance_information_filter_value_set

        out["values"] = (
            capo_ssm.types.instance_information_filter_value_set.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("InstanceInformationStringFilter.values required")
    return out
