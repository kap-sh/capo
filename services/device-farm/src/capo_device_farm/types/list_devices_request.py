"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListDevicesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.amazon_resource_name
    import capo_device_farm.types.device_filters
    import capo_device_farm.types.pagination_token


class ListDevicesRequest(TypedDict, closed=True):
    arn: NotRequired["capo_device_farm.types.amazon_resource_name.AmazonResourceName"]
    """<p>The Amazon Resource Name (ARN) of the project.</p>"""
    next_token: NotRequired["capo_device_farm.types.pagination_token.PaginationToken"]
    """<p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>"""
    filters: NotRequired["capo_device_farm.types.device_filters.DeviceFilters"]
    """<p>Used to select a set of devices. A filter is made up of an attribute, an operator, and one or more values.</p> <ul> <li> <p>Attribute: The aspect of a device such as platform or model used as the selection criteria in a device filter.</p> <p>Allowed values include:</p> <ul> <li> <p>ARN: The Amazon Resource Name (ARN) of the device (for example, <code>arn:aws:devicefarm:us-west-2::device:12345Example</code>).</p> </li> <li> <p>PLATFORM: The device platform. Valid values are ANDROID or IOS.</p> </li> <li> <p>OS_VERSION: The operating system version (for example, 10.3.2).</p> </li> <li> <p>MODEL: The device model (for example, iPad 5th Gen).</p> </li> <li> <p>AVAILABILITY: The current availability of the device. Valid values are AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.</p> </li> <li> <p>FORM_FACTOR: The device form factor. Valid values are PHONE or TABLET.</p> </li> <li> <p>MANUFACTURER: The device manufacturer (for example, Apple).</p> </li> <li> <p>REMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access. Valid values are TRUE or FALSE.</p> </li> <li> <p>REMOTE_DEBUG_ENABLED: Whether the device is enabled for remote debugging. Valid values are TRUE or FALSE. Because remote debugging is <a href="https://docs.aws.amazon.com/devicefarm/latest/developerguide/history.html">no longer supported</a>, this attribute is ignored.</p> </li> <li> <p>INSTANCE_ARN: The Amazon Resource Name (ARN) of the device instance.</p> </li> <li> <p>INSTANCE_LABELS: The label of the device instance.</p> </li> <li> <p>FLEET_TYPE: The fleet type. Valid values are PUBLIC or PRIVATE.</p> </li> </ul> </li> <li> <p>Operator: The filter operator.</p> <ul> <li> <p>The EQUALS operator is available for every attribute except INSTANCE_LABELS.</p> </li> <li> <p>The CONTAINS operator is available for the INSTANCE_LABELS and MODEL attributes.</p> </li> <li> <p>The IN and NOT_IN operators are available for the ARN, OS_VERSION, MODEL, MANUFACTURER, and INSTANCE_ARN attributes.</p> </li> <li> <p>The LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUALS, and GREATER_THAN_OR_EQUALS operators are also available for the OS_VERSION attribute.</p> </li> </ul> </li> <li> <p>Values: An array of one or more filter values.</p> <ul> <li> <p>The IN and NOT_IN operators take a values array that has one or more elements.</p> </li> <li> <p>The other operators require an array with a single element.</p> </li> <li> <p>In a request, the AVAILABILITY attribute takes the following values: AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.</p> </li> </ul> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDevicesRequest) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "filters" in value:
        import capo_device_farm.types.device_filters

        out["filters"] = capo_device_farm.types.device_filters.serialize_aws_json_1_1(
            value["filters"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDevicesRequest:
    out: ListDevicesRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("filters") is not None:
        import capo_device_farm.types.device_filters

        out["filters"] = capo_device_farm.types.device_filters.deserialize_aws_json_1_1(
            data["filters"]
        )
    return out
