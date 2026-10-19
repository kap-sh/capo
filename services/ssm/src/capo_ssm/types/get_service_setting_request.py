"""Generated from Smithy shape ``com.amazonaws.ssm#GetServiceSettingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.service_setting_id


class GetServiceSettingRequest(TypedDict, closed=True):
    setting_id: "capo_ssm.types.service_setting_id.ServiceSettingId"
    """<p>The ID of the service setting to get. The setting ID can be one of the following.</p> <ul> <li> <p> <code>/ssm/appmanager/appmanager-enabled</code> </p> </li> <li> <p> <code>/ssm/automation/customer-script-log-destination</code> </p> </li> <li> <p> <code>/ssm/automation/customer-script-log-group-name</code> </p> </li> <li> <p>/ssm/automation/enable-adaptive-concurrency</p> </li> <li> <p> <code>/ssm/documents/console/public-sharing-permission</code> </p> </li> <li> <p> <code>/ssm/managed-instance/activation-tier</code> </p> </li> <li> <p> <code>/ssm/managed-instance/default-ec2-instance-management-role</code> </p> </li> <li> <p> <code>/ssm/opsinsights/opscenter</code> </p> </li> <li> <p> <code>/ssm/parameter-store/default-parameter-tier</code> </p> </li> <li> <p> <code>/ssm/parameter-store/high-throughput-enabled</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetServiceSettingRequest) -> dict:
    out: dict = {}
    out["SettingId"] = value["setting_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetServiceSettingRequest:
    out: GetServiceSettingRequest = {}  # type: ignore[typeddict-item]
    if data.get("SettingId") is not None:
        out["setting_id"] = data["SettingId"]
    else:
        out["setting_id"] = ""
    return out
