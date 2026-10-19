"""Generated from Smithy shape ``com.amazonaws.evs#AccountSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_evs.types.setting_name
    import capo_evs.types.setting_value


class AccountSetting(TypedDict, closed=True):
    name: "capo_evs.types.setting_name.SettingName"
    """<p>The name of the EVS setting. Valid values are:</p> <ul> <li> <p> <code>vcfPortedCoreCount</code> (type: numeric string) - The total number of VCF license cores ported to Amazon EVS for the account in that Region. The maximum value is 1,000,000 cores. This setting value is shared with Broadcom for record-keeping.</p> </li> </ul>"""
    value: "capo_evs.types.setting_value.SettingValue"
    """<p>The value of the EVS setting.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountSetting) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AccountSetting:
    out: AccountSetting = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
