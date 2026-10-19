"""Generated from Smithy shape ``com.amazonaws.devicefarm#GetDevicePoolCompatibilityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.amazon_resource_name
    import capo_device_farm.types.schedule_run_configuration
    import capo_device_farm.types.schedule_run_test
    import capo_device_farm.types.test_type


class GetDevicePoolCompatibilityRequest(TypedDict, closed=True):
    device_pool_arn: "capo_device_farm.types.amazon_resource_name.AmazonResourceName"
    """<p>The device pool's ARN.</p>"""
    app_arn: NotRequired[
        "capo_device_farm.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the app that is associated with the specified device pool.</p>"""
    test_type: NotRequired["capo_device_farm.types.test_type.TestType"]
    """<p>The test type for the specified device pool.</p> <p>Allowed values include the following:</p> <ul> <li> <p>BUILTIN_FUZZ.</p> </li> <li> <p>APPIUM_JAVA_JUNIT.</p> </li> <li> <p>APPIUM_JAVA_TESTNG.</p> </li> <li> <p>APPIUM_PYTHON.</p> </li> <li> <p>APPIUM_NODE.</p> </li> <li> <p>APPIUM_RUBY.</p> </li> <li> <p>APPIUM_WEB_JAVA_JUNIT.</p> </li> <li> <p>APPIUM_WEB_JAVA_TESTNG.</p> </li> <li> <p>APPIUM_WEB_PYTHON.</p> </li> <li> <p>APPIUM_WEB_NODE.</p> </li> <li> <p>APPIUM_WEB_RUBY.</p> </li> <li> <p>INSTRUMENTATION.</p> </li> <li> <p>XCTEST.</p> </li> <li> <p>XCTEST_UI.</p> </li> </ul>"""
    test: NotRequired["capo_device_farm.types.schedule_run_test.ScheduleRunTest"]
    """<p>Information about the uploaded test to be run against the device pool.</p>"""
    configuration: NotRequired[
        "capo_device_farm.types.schedule_run_configuration.ScheduleRunConfiguration"
    ]
    """<p>An object that contains information about the settings for a run.</p>"""
    project_arn: NotRequired[
        "capo_device_farm.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the project for which you want to check device pool compatibility.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDevicePoolCompatibilityRequest) -> dict:
    out: dict = {}
    out["devicePoolArn"] = value["device_pool_arn"]
    if "app_arn" in value:
        out["appArn"] = value["app_arn"]
    if "test_type" in value:
        import capo_device_farm.types.test_type

        out["testType"] = capo_device_farm.types.test_type.serialize_aws_json_1_1(
            value["test_type"]
        )
    if "test" in value:
        import capo_device_farm.types.schedule_run_test

        out["test"] = capo_device_farm.types.schedule_run_test.serialize_aws_json_1_1(
            value["test"]
        )
    if "configuration" in value:
        import capo_device_farm.types.schedule_run_configuration

        out["configuration"] = (
            capo_device_farm.types.schedule_run_configuration.serialize_aws_json_1_1(
                value["configuration"]
            )
        )
    if "project_arn" in value:
        out["projectArn"] = value["project_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDevicePoolCompatibilityRequest:
    out: GetDevicePoolCompatibilityRequest = {}  # type: ignore[typeddict-item]
    if data.get("devicePoolArn") is not None:
        out["device_pool_arn"] = data["devicePoolArn"]
    else:
        out["device_pool_arn"] = ""
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    if data.get("testType") is not None:
        import capo_device_farm.types.test_type

        out["test_type"] = capo_device_farm.types.test_type.deserialize_aws_json_1_1(
            data["testType"]
        )
    if data.get("test") is not None:
        import capo_device_farm.types.schedule_run_test

        out["test"] = capo_device_farm.types.schedule_run_test.deserialize_aws_json_1_1(
            data["test"]
        )
    if data.get("configuration") is not None:
        import capo_device_farm.types.schedule_run_configuration

        out["configuration"] = (
            capo_device_farm.types.schedule_run_configuration.deserialize_aws_json_1_1(
                data["configuration"]
            )
        )
    if data.get("projectArn") is not None:
        out["project_arn"] = data["projectArn"]
    return out
