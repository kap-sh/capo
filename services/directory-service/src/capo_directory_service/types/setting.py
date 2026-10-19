"""Generated from Smithy shape ``com.amazonaws.directoryservice#Setting``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.directory_configuration_setting_name
    import capo_directory_service.types.directory_configuration_setting_value


class Setting(TypedDict, closed=True):
    name: "capo_directory_service.types.directory_configuration_setting_name.DirectoryConfigurationSettingName"
    """<p>The name of the directory setting. For example:</p> <p> <code>TLS_1_0</code> </p>"""
    value: "capo_directory_service.types.directory_configuration_setting_value.DirectoryConfigurationSettingValue"
    """<p>The value of the directory setting for which to retrieve information. For example, for <code>TLS_1_0</code>, the valid values are: <code>Enable</code> and <code>Disable</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Setting) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Setting:
    out: Setting = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
