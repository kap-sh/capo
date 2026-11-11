"""Generated from Smithy shape ``com.amazonaws.devicefarm#ArtifactType``."""

from typing import Literal, TypeAlias, cast

ArtifactType: TypeAlias = Literal[
    "UNKNOWN",
    "SCREENSHOT",
    "DEVICE_LOG",
    "MESSAGE_LOG",
    "VIDEO_LOG",
    "RESULT_LOG",
    "SERVICE_LOG",
    "WEBKIT_LOG",
    "INSTRUMENTATION_OUTPUT",
    "EXERCISER_MONKEY_OUTPUT",
    "CALABASH_JSON_OUTPUT",
    "CALABASH_PRETTY_OUTPUT",
    "CALABASH_STANDARD_OUTPUT",
    "CALABASH_JAVA_XML_OUTPUT",
    "AUTOMATION_OUTPUT",
    "APPIUM_SERVER_OUTPUT",
    "APPIUM_JAVA_OUTPUT",
    "APPIUM_JAVA_XML_OUTPUT",
    "APPIUM_PYTHON_OUTPUT",
    "APPIUM_PYTHON_XML_OUTPUT",
    "EXPLORER_EVENT_LOG",
    "EXPLORER_SUMMARY_LOG",
    "APPLICATION_CRASH_REPORT",
    "XCTEST_LOG",
    "VIDEO",
    "CUSTOMER_ARTIFACT",
    "CUSTOMER_ARTIFACT_LOG",
    "TESTSPEC_OUTPUT",
    "DEVICE_CONNECT_COMMAND_LOG",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArtifactType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ArtifactType:
    return cast(ArtifactType, data)
