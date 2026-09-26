"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ConfigurationIssue``."""

from typing_extensions import NotRequired, TypedDict


class ConfigurationIssue(TypedDict, closed=True):
    configuration_name: NotRequired["str"]
    """<p>The name of the configuration setting that is in conflict.</p>"""
    expected_value: NotRequired["str"]
    """<p>The configuration value that AWS Network Security Manager expected.</p>"""
    actual_value: NotRequired["str"]
    """<p>The configuration value that was found on the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationIssue) -> dict:
    out: dict = {}
    if "configuration_name" in value:
        out["configurationName"] = value["configuration_name"]
    if "expected_value" in value:
        out["expectedValue"] = value["expected_value"]
    if "actual_value" in value:
        out["actualValue"] = value["actual_value"]
    return out


def deserialize_json(data: dict) -> ConfigurationIssue:
    out: ConfigurationIssue = {}  # type: ignore[typeddict-item]
    if data.get("configurationName") is not None:
        out["configuration_name"] = data["configurationName"]
    if data.get("expectedValue") is not None:
        out["expected_value"] = data["expectedValue"]
    if data.get("actualValue") is not None:
        out["actual_value"] = data["actualValue"]
    return out
