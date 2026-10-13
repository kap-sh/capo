"""Generated from Smithy shape ``com.amazonaws.devicefarm#RemoteAccessEndpoints``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.sensitive_url


class RemoteAccessEndpoints(TypedDict, closed=True):
    remote_driver_endpoint: NotRequired[
        "capo_device_farm.types.sensitive_url.SensitiveURL"
    ]
    """<p>URL for controlling the device using WebDriver-compliant clients, like Appium, during the remote access session.</p>"""
    interactive_endpoint: NotRequired[
        "capo_device_farm.types.sensitive_url.SensitiveURL"
    ]
    """<p>URL for viewing and interacting with the device during the remote access session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoteAccessEndpoints) -> dict:
    out: dict = {}
    if "remote_driver_endpoint" in value:
        out["remoteDriverEndpoint"] = value["remote_driver_endpoint"]
    if "interactive_endpoint" in value:
        out["interactiveEndpoint"] = value["interactive_endpoint"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoteAccessEndpoints:
    out: RemoteAccessEndpoints = {}  # type: ignore[typeddict-item]
    if data.get("remoteDriverEndpoint") is not None:
        out["remote_driver_endpoint"] = data["remoteDriverEndpoint"]
    if data.get("interactiveEndpoint") is not None:
        out["interactive_endpoint"] = data["interactiveEndpoint"]
    return out


def redact_sensitive(value: RemoteAccessEndpoints) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "remote_driver_endpoint" in value:
        out["remote_driver_endpoint"] = "*** Sensitive Data Redacted ***"
    if "interactive_endpoint" in value:
        out["interactive_endpoint"] = "*** Sensitive Data Redacted ***"
    return out
