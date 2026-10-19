"""Generated from Smithy shape ``com.amazonaws.ecr#GetAccountSettingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.account_setting_name


class GetAccountSettingRequest(TypedDict, closed=True):
    name: "capo_ecr.types.account_setting_name.AccountSettingName"
    """<p>The name of the account setting, such as <code>BASIC_SCAN_TYPE_VERSION</code>, <code>REGISTRY_POLICY_SCOPE</code>, or <code>BLOB_MOUNTING</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAccountSettingRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAccountSettingRequest:
    out: GetAccountSettingRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
