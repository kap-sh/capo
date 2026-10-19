"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#AccountAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.account_attribute_name


class AccountAttribute(TypedDict, closed=True):
    name: "capo_pinpoint_sms_voice_v2.types.account_attribute_name.AccountAttributeName"
    """<p>The name of the account attribute.</p>"""
    value: "str"
    """<p>The value associated with the account attribute name.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountAttribute) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AccountAttribute:
    out: AccountAttribute = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
