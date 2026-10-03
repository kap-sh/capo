"""Generated from Smithy shape ``com.amazonaws.devicefarm#DeviceFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_device_farm.types.device_filter_attribute
    import capo_device_farm.types.device_filter_values
    import capo_device_farm.types.rule_operator


class DeviceFilter(TypedDict, closed=True):
    attribute: "capo_device_farm.types.device_filter_attribute.DeviceFilterAttribute"
    """<p>The aspect of a device such as platform or model used as the selection criteria in a device filter.</p> <p>The supported operators for each attribute are provided in the following list.</p> <dl> <dt>ARN</dt> <dd> <p>The Amazon Resource Name (ARN) of the device (for example, <code>arn:aws:devicefarm:us-west-2::device:12345Example</code>).</p> <p>Supported operators: <code>EQUALS</code>, <code>IN</code>, <code>NOT_IN</code> </p> </dd> <dt>PLATFORM</dt> <dd> <p>The device platform. Valid values are ANDROID or IOS.</p> <p>Supported operators: <code>EQUALS</code> </p> </dd> <dt>OS_VERSION</dt> <dd> <p>The operating system version (for example, 10.3.2).</p> <p>Supported operators: <code>EQUALS</code>, <code>GREATER_THAN</code>, <code>GREATER_THAN_OR_EQUALS</code>, <code>IN</code>, <code>LESS_THAN</code>, <code>LESS_THAN_OR_EQUALS</code>, <code>NOT_IN</code> </p> </dd> <dt>MODEL</dt> <dd> <p>The device model (for example, iPad 5th Gen).</p> <p>Supported operators: <code>CONTAINS</code>, <code>EQUALS</code>, <code>IN</code>, <code>NOT_IN</code> </p> </dd> <dt>AVAILABILITY</dt> <dd> <p>The current availability of the device. Valid values are AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.</p> <p>Supported operators: <code>EQUALS</code> </p> </dd> <dt>FORM_FACTOR</dt> <dd> <p>The device form factor. Valid values are PHONE or TABLET.</p> <p>Supported operators: <code>EQUALS</code> </p> </dd> <dt>MANUFACTURER</dt> <dd> <p>The device manufacturer (for example, Apple).</p> <p>Supported operators: <code>EQUALS</code>, <code>IN</code>, <code>NOT_IN</code> </p> </dd> <dt>REMOTE_ACCESS_ENABLED</dt> <dd> <p>Whether the device is enabled for remote access. Valid values are TRUE or FALSE.</p> <p>Supported operators: <code>EQUALS</code> </p> </dd> <dt>REMOTE_DEBUG_ENABLED</dt> <dd> <p>Whether the device is enabled for remote debugging. Valid values are TRUE or FALSE.</p> <p>Supported operators: <code>EQUALS</code> </p> <p>Because remote debugging is <a href="https://docs.aws.amazon.com/devicefarm/latest/developerguide/history.html">no longer supported</a>, this filter is ignored.</p> </dd> <dt>INSTANCE_ARN</dt> <dd> <p>The Amazon Resource Name (ARN) of the device instance.</p> <p>Supported operators: <code>EQUALS</code>, <code>IN</code>, <code>NOT_IN</code> </p> </dd> <dt>INSTANCE_LABELS</dt> <dd> <p>The label of the device instance.</p> <p>Supported operators: <code>CONTAINS</code> </p> </dd> <dt>FLEET_TYPE</dt> <dd> <p>The fleet type. Valid values are PUBLIC or PRIVATE.</p> <p>Supported operators: <code>EQUALS</code> </p> </dd> </dl>"""
    operator: "capo_device_farm.types.rule_operator.RuleOperator"
    """<p>Specifies how Device Farm compares the filter's attribute to the value. See the attribute descriptions.</p>"""
    values: "capo_device_farm.types.device_filter_values.DeviceFilterValues"
    """<p>An array of one or more filter values used in a device filter.</p> <p class="title"> <b>Operator Values</b> </p> <ul> <li> <p>The IN and NOT_IN operators can take a values array that has more than one element.</p> </li> <li> <p>The other operators require an array with a single element.</p> </li> </ul> <p class="title"> <b>Attribute Values</b> </p> <ul> <li> <p>The PLATFORM attribute can be set to ANDROID or IOS.</p> </li> <li> <p>The AVAILABILITY attribute can be set to AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.</p> </li> <li> <p>The FORM_FACTOR attribute can be set to PHONE or TABLET.</p> </li> <li> <p>The FLEET_TYPE attribute can be set to PUBLIC or PRIVATE.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceFilter) -> dict:
    out: dict = {}
    import capo_device_farm.types.device_filter_attribute

    out["attribute"] = (
        capo_device_farm.types.device_filter_attribute.serialize_aws_json_1_1(
            value["attribute"]
        )
    )
    import capo_device_farm.types.rule_operator

    out["operator"] = capo_device_farm.types.rule_operator.serialize_aws_json_1_1(
        value["operator"]
    )
    import capo_device_farm.types.device_filter_values

    out["values"] = capo_device_farm.types.device_filter_values.serialize_aws_json_1_1(
        value["values"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeviceFilter:
    out: DeviceFilter = {}  # type: ignore[typeddict-item]
    if data.get("attribute") is not None:
        import capo_device_farm.types.device_filter_attribute

        out["attribute"] = (
            capo_device_farm.types.device_filter_attribute.deserialize_aws_json_1_1(
                data["attribute"]
            )
        )
    else:
        raise DeserializationError("DeviceFilter.attribute required")
    if data.get("operator") is not None:
        import capo_device_farm.types.rule_operator

        out["operator"] = capo_device_farm.types.rule_operator.deserialize_aws_json_1_1(
            data["operator"]
        )
    else:
        raise DeserializationError("DeviceFilter.operator required")
    if data.get("values") is not None:
        import capo_device_farm.types.device_filter_values

        out["values"] = (
            capo_device_farm.types.device_filter_values.deserialize_aws_json_1_1(
                data["values"]
            )
        )
    else:
        raise DeserializationError("DeviceFilter.values required")
    return out
