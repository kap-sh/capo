"""Generated from Smithy shape ``com.amazonaws.devicefarm#DeviceSelectionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_device_farm.types.device_filters
    import capo_device_farm.types.integer


class DeviceSelectionConfiguration(TypedDict, closed=True):
    filters: "capo_device_farm.types.device_filters.DeviceFilters"
    """<p>Used to dynamically select a set of devices for a test run. A filter is made up of an attribute, an operator, and one or more values.</p> <ul> <li> <p> <b>Attribute</b> </p> <p>The aspect of a device such as platform or model used as the selection criteria in a device filter.</p> <p>Allowed values include:</p> <ul> <li> <p>ARN: The Amazon Resource Name (ARN) of the device (for example, <code>arn:aws:devicefarm:us-west-2::device:12345Example</code>).</p> </li> <li> <p>PLATFORM: The device platform. Valid values are ANDROID or IOS.</p> </li> <li> <p>OS_VERSION: The operating system version (for example, 10.3.2).</p> </li> <li> <p>MODEL: The device model (for example, iPad 5th Gen).</p> </li> <li> <p>AVAILABILITY: The current availability of the device. Valid values are AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.</p> </li> <li> <p>FORM_FACTOR: The device form factor. Valid values are PHONE or TABLET.</p> </li> <li> <p>MANUFACTURER: The device manufacturer (for example, Apple).</p> </li> <li> <p>REMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access. Valid values are TRUE or FALSE.</p> </li> <li> <p>REMOTE_DEBUG_ENABLED: Whether the device is enabled for remote debugging. Valid values are TRUE or FALSE. Because remote debugging is <a href="https://docs.aws.amazon.com/devicefarm/latest/developerguide/history.html">no longer supported</a>, this filter is ignored.</p> </li> <li> <p>INSTANCE_ARN: The Amazon Resource Name (ARN) of the device instance.</p> </li> <li> <p>INSTANCE_LABELS: The label of the device instance.</p> </li> <li> <p>FLEET_TYPE: The fleet type. Valid values are PUBLIC or PRIVATE.</p> </li> </ul> </li> <li> <p> <b>Operator</b> </p> <p>The filter operator.</p> <ul> <li> <p>The EQUALS operator is available for every attribute except INSTANCE_LABELS.</p> </li> <li> <p>The CONTAINS operator is available for the INSTANCE_LABELS and MODEL attributes.</p> </li> <li> <p>The IN and NOT_IN operators are available for the ARN, OS_VERSION, MODEL, MANUFACTURER, and INSTANCE_ARN attributes.</p> </li> <li> <p>The LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUALS, and GREATER_THAN_OR_EQUALS operators are also available for the OS_VERSION attribute.</p> </li> </ul> </li> <li> <p> <b>Values</b> </p> <p>An array of one or more filter values.</p> <p class="title"> <b>Operator Values</b> </p> <ul> <li> <p>The IN and NOT_IN operators can take a values array that has more than one element.</p> </li> <li> <p>The other operators require an array with a single element.</p> </li> </ul> <p class="title"> <b>Attribute Values</b> </p> <ul> <li> <p>The PLATFORM attribute can be set to ANDROID or IOS.</p> </li> <li> <p>The AVAILABILITY attribute can be set to AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.</p> </li> <li> <p>The FORM_FACTOR attribute can be set to PHONE or TABLET.</p> </li> <li> <p>The FLEET_TYPE attribute can be set to PUBLIC or PRIVATE.</p> </li> </ul> </li> </ul>"""
    max_devices: "capo_device_farm.types.integer.Integer"
    """<p>The maximum number of devices to be included in a test run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceSelectionConfiguration) -> dict:
    out: dict = {}
    import capo_device_farm.types.device_filters

    out["filters"] = capo_device_farm.types.device_filters.serialize_aws_json_1_1(
        value["filters"]
    )
    out["maxDevices"] = value["max_devices"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeviceSelectionConfiguration:
    out: DeviceSelectionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("filters") is not None:
        import capo_device_farm.types.device_filters

        out["filters"] = capo_device_farm.types.device_filters.deserialize_aws_json_1_1(
            data["filters"]
        )
    else:
        raise DeserializationError("DeviceSelectionConfiguration.filters required")
    if data.get("maxDevices") is not None:
        out["max_devices"] = data["maxDevices"]
    else:
        raise DeserializationError("DeviceSelectionConfiguration.max_devices required")
    return out
