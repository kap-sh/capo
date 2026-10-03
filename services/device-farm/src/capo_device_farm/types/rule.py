"""Generated from Smithy shape ``com.amazonaws.devicefarm#Rule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.device_attribute
    import capo_device_farm.types.rule_operator
    import capo_device_farm.types.string


class Rule(TypedDict, closed=True):
    attribute: NotRequired["capo_device_farm.types.device_attribute.DeviceAttribute"]
    r"""<p>The rule's stringified attribute. For example, specify the value as <code>"\"abc\""</code>.</p> <p>The supported operators for each attribute are provided in the following list.</p> <dl> <dt>APPIUM_VERSION</dt> <dd> <p>The Appium version for the test.</p> <p>Supported operators: <code>CONTAINS</code> </p> </dd> <dt>ARN</dt> <dd> <p>The Amazon Resource Name (ARN) of the device (for example, <code>arn:aws:devicefarm:us-west-2::device:12345Example</code>.</p> <p>Supported operators: <code>EQUALS</code>, <code>IN</code>, <code>NOT_IN</code> </p> </dd> <dt>AVAILABILITY</dt> <dd> <p>The current availability of the device. Valid values are AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.</p> <p>Supported operators: <code>EQUALS</code> </p> </dd> <dt>FLEET_TYPE</dt> <dd> <p>The fleet type. Valid values are PUBLIC or PRIVATE.</p> <p>Supported operators: <code>EQUALS</code> </p> </dd> <dt>FORM_FACTOR</dt> <dd> <p>The device form factor. Valid values are PHONE or TABLET.</p> <p>Supported operators: <code>EQUALS</code>, <code>IN</code>, <code>NOT_IN</code> </p> </dd> <dt>INSTANCE_ARN</dt> <dd> <p>The Amazon Resource Name (ARN) of the device instance.</p> <p>Supported operators: <code>IN</code>, <code>NOT_IN</code> </p> </dd> <dt>INSTANCE_LABELS</dt> <dd> <p>The label of the device instance.</p> <p>Supported operators: <code>CONTAINS</code> </p> </dd> <dt>MANUFACTURER</dt> <dd> <p>The device manufacturer (for example, Apple).</p> <p>Supported operators: <code>EQUALS</code>, <code>IN</code>, <code>NOT_IN</code> </p> </dd> <dt>MODEL</dt> <dd> <p>The device model, such as Apple iPad Air 2 or Google Pixel.</p> <p>Supported operators: <code>CONTAINS</code>, <code>EQUALS</code>, <code>IN</code>, <code>NOT_IN</code> </p> </dd> <dt>OS_VERSION</dt> <dd> <p>The operating system version (for example, 10.3.2).</p> <p>Supported operators: <code>EQUALS</code>, <code>GREATER_THAN</code>, <code>GREATER_THAN_OR_EQUALS</code>, <code>IN</code>, <code>LESS_THAN</code>, <code>LESS_THAN_OR_EQUALS</code>, <code>NOT_IN</code> </p> </dd> <dt>PLATFORM</dt> <dd> <p>The device platform. Valid values are ANDROID or IOS.</p> <p>Supported operators: <code>EQUALS</code>, <code>IN</code>, <code>NOT_IN</code> </p> </dd> <dt>REMOTE_ACCESS_ENABLED</dt> <dd> <p>Whether the device is enabled for remote access. Valid values are TRUE or FALSE.</p> <p>Supported operators: <code>EQUALS</code> </p> </dd> <dt>REMOTE_DEBUG_ENABLED</dt> <dd> <p>Whether the device is enabled for remote debugging. Valid values are TRUE or FALSE.</p> <p>Supported operators: <code>EQUALS</code> </p> <p>Because remote debugging is <a href="https://docs.aws.amazon.com/devicefarm/latest/developerguide/history.html">no longer supported</a>, this filter is ignored.</p> </dd> </dl>"""
    operator: NotRequired["capo_device_farm.types.rule_operator.RuleOperator"]
    """<p>Specifies how Device Farm compares the rule's attribute to the value. For the operators that are supported by each attribute, see the attribute descriptions.</p>"""
    value: NotRequired["capo_device_farm.types.string.String"]
    """<p>The rule's value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Rule) -> dict:
    out: dict = {}
    if "attribute" in value:
        import capo_device_farm.types.device_attribute

        out["attribute"] = (
            capo_device_farm.types.device_attribute.serialize_aws_json_1_1(
                value["attribute"]
            )
        )
    if "operator" in value:
        import capo_device_farm.types.rule_operator

        out["operator"] = capo_device_farm.types.rule_operator.serialize_aws_json_1_1(
            value["operator"]
        )
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Rule:
    out: Rule = {}  # type: ignore[typeddict-item]
    if data.get("attribute") is not None:
        import capo_device_farm.types.device_attribute

        out["attribute"] = (
            capo_device_farm.types.device_attribute.deserialize_aws_json_1_1(
                data["attribute"]
            )
        )
    if data.get("operator") is not None:
        import capo_device_farm.types.rule_operator

        out["operator"] = capo_device_farm.types.rule_operator.deserialize_aws_json_1_1(
            data["operator"]
        )
    if data.get("value") is not None:
        out["value"] = data["value"]
    return out
