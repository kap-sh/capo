"""Generated from Smithy shape ``com.amazonaws.ssm#UpdateServiceSettingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.service_setting_id
    import capo_ssm.types.service_setting_value


class UpdateServiceSettingRequest(TypedDict, closed=True):
    setting_id: "capo_ssm.types.service_setting_id.ServiceSettingId"
    """<p>The Amazon Resource Name (ARN) of the service setting to update. For example, <code>arn:aws:ssm:us-east-1:111122223333:servicesetting/ssm/parameter-store/high-throughput-enabled</code>. The setting ID can be one of the following.</p> <ul> <li> <p> <code>/ssm/appmanager/appmanager-enabled</code> </p> </li> <li> <p> <code>/ssm/automation/customer-script-log-destination</code> </p> </li> <li> <p> <code>/ssm/automation/customer-script-log-group-name</code> </p> </li> <li> <p>/ssm/automation/enable-adaptive-concurrency</p> </li> <li> <p> <code>/ssm/documents/console/public-sharing-permission</code> </p> </li> <li> <p> <code>/ssm/managed-instance/activation-tier</code> </p> </li> <li> <p> <code>/ssm/managed-instance/default-ec2-instance-management-role</code> </p> </li> <li> <p> <code>/ssm/opsinsights/opscenter</code> </p> </li> <li> <p> <code>/ssm/parameter-store/default-parameter-tier</code> </p> </li> <li> <p> <code>/ssm/parameter-store/high-throughput-enabled</code> </p> </li> </ul> <note> <p>Permissions to update the <code>/ssm/managed-instance/default-ec2-instance-management-role</code> setting should only be provided to administrators. Implement least privilege access when allowing individuals to configure or modify the Default Host Management Configuration.</p> </note>"""
    setting_value: "capo_ssm.types.service_setting_value.ServiceSettingValue"
    """<p>The new value to specify for the service setting. The following list specifies the available values for each setting.</p> <ul> <li> <p>For <code>/ssm/appmanager/appmanager-enabled</code>, enter <code>True</code> or <code>False</code>.</p> </li> <li> <p>For <code>/ssm/automation/customer-script-log-destination</code>, enter <code>CloudWatch</code>.</p> </li> <li> <p>For <code>/ssm/automation/customer-script-log-group-name</code>, enter the name of an Amazon CloudWatch Logs log group.</p> </li> <li> <p>For <code>/ssm/documents/console/public-sharing-permission</code>, enter <code>Enable</code> or <code>Disable</code>.</p> </li> <li> <p>For <code>/ssm/managed-instance/activation-tier</code>, enter <code>standard</code> or <code>advanced</code>.</p> </li> <li> <p>For <code>/ssm/managed-instance/default-ec2-instance-management-role</code>, enter the name of an IAM role. </p> </li> <li> <p> For <code>/ssm/opsinsights/opscenter</code>, enter <code>Enabled</code> or <code>Disabled</code>. </p> </li> <li> <p>For <code>/ssm/parameter-store/default-parameter-tier</code>, enter <code>Standard</code>, <code>Advanced</code>, or <code>Intelligent-Tiering</code> </p> </li> <li> <p>For <code>/ssm/parameter-store/high-throughput-enabled</code>, enter <code>true</code> or <code>false</code>.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateServiceSettingRequest) -> dict:
    out: dict = {}
    out["SettingId"] = value["setting_id"]
    out["SettingValue"] = value["setting_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateServiceSettingRequest:
    out: UpdateServiceSettingRequest = {}  # type: ignore[typeddict-item]
    if data.get("SettingId") is not None:
        out["setting_id"] = data["SettingId"]
    else:
        out["setting_id"] = ""
    if data.get("SettingValue") is not None:
        out["setting_value"] = data["SettingValue"]
    else:
        out["setting_value"] = ""
    return out
