"""Generated from Smithy shape ``com.amazonaws.devicefarm#AccountSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.aws_account_number
    import capo_device_farm.types.job_timeout_minutes
    import capo_device_farm.types.max_slot_map
    import capo_device_farm.types.purchased_devices_map
    import capo_device_farm.types.skip_app_resign
    import capo_device_farm.types.trial_minutes


class AccountSettings(TypedDict, closed=True):
    aws_account_number: NotRequired[
        "capo_device_farm.types.aws_account_number.AWSAccountNumber"
    ]
    """<p>The AWS account number specified in the <code>AccountSettings</code> container.</p>"""
    unmetered_devices: NotRequired[
        "capo_device_farm.types.purchased_devices_map.PurchasedDevicesMap"
    ]
    """<p>Returns the unmetered devices you have purchased or want to purchase.</p>"""
    unmetered_remote_access_devices: NotRequired[
        "capo_device_farm.types.purchased_devices_map.PurchasedDevicesMap"
    ]
    """<p>Returns the unmetered remote access devices you have purchased or want to purchase.</p>"""
    max_job_timeout_minutes: NotRequired[
        "capo_device_farm.types.job_timeout_minutes.JobTimeoutMinutes"
    ]
    """<p>The maximum number of minutes a test run executes before it times out.</p>"""
    trial_minutes: NotRequired["capo_device_farm.types.trial_minutes.TrialMinutes"]
    """<p>Information about an AWS account's usage of free trial device minutes.</p>"""
    max_slots: NotRequired["capo_device_farm.types.max_slot_map.MaxSlotMap"]
    """<p>The maximum number of device slots that the AWS account can purchase. Each maximum is expressed as an <code>offering-id:number</code> pair, where the <code>offering-id</code> represents one of the IDs returned by the <code>ListOfferings</code> command.</p>"""
    default_job_timeout_minutes: NotRequired[
        "capo_device_farm.types.job_timeout_minutes.JobTimeoutMinutes"
    ]
    """<p>The default number of minutes (at the account level) a test run executes before it times out. The default value is 150 minutes.</p>"""
    skip_app_resign: NotRequired["capo_device_farm.types.skip_app_resign.SkipAppResign"]
    """<p>When set to <code>true</code>, for private devices, Device Farm does not sign your app again. For public devices, Device Farm always signs your apps again.</p> <p>For more information about how Device Farm re-signs your apps, see <a href="http://aws.amazon.com/device-farm/faqs/">Do you modify my app?</a> in the <i>AWS Device Farm FAQs</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountSettings) -> dict:
    out: dict = {}
    if "aws_account_number" in value:
        out["awsAccountNumber"] = value["aws_account_number"]
    if "unmetered_devices" in value:
        import capo_device_farm.types.purchased_devices_map

        out["unmeteredDevices"] = (
            capo_device_farm.types.purchased_devices_map.serialize_aws_json_1_1(
                value["unmetered_devices"]
            )
        )
    if "unmetered_remote_access_devices" in value:
        import capo_device_farm.types.purchased_devices_map

        out["unmeteredRemoteAccessDevices"] = (
            capo_device_farm.types.purchased_devices_map.serialize_aws_json_1_1(
                value["unmetered_remote_access_devices"]
            )
        )
    if "max_job_timeout_minutes" in value:
        out["maxJobTimeoutMinutes"] = value["max_job_timeout_minutes"]
    if "trial_minutes" in value:
        import capo_device_farm.types.trial_minutes

        out["trialMinutes"] = (
            capo_device_farm.types.trial_minutes.serialize_aws_json_1_1(
                value["trial_minutes"]
            )
        )
    if "max_slots" in value:
        import capo_device_farm.types.max_slot_map

        out["maxSlots"] = capo_device_farm.types.max_slot_map.serialize_aws_json_1_1(
            value["max_slots"]
        )
    if "default_job_timeout_minutes" in value:
        out["defaultJobTimeoutMinutes"] = value["default_job_timeout_minutes"]
    if "skip_app_resign" in value:
        out["skipAppResign"] = value["skip_app_resign"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AccountSettings:
    out: AccountSettings = {}  # type: ignore[typeddict-item]
    if data.get("awsAccountNumber") is not None:
        out["aws_account_number"] = data["awsAccountNumber"]
    if data.get("unmeteredDevices") is not None:
        import capo_device_farm.types.purchased_devices_map

        out["unmetered_devices"] = (
            capo_device_farm.types.purchased_devices_map.deserialize_aws_json_1_1(
                data["unmeteredDevices"]
            )
        )
    if data.get("unmeteredRemoteAccessDevices") is not None:
        import capo_device_farm.types.purchased_devices_map

        out["unmetered_remote_access_devices"] = (
            capo_device_farm.types.purchased_devices_map.deserialize_aws_json_1_1(
                data["unmeteredRemoteAccessDevices"]
            )
        )
    if data.get("maxJobTimeoutMinutes") is not None:
        out["max_job_timeout_minutes"] = data["maxJobTimeoutMinutes"]
    if data.get("trialMinutes") is not None:
        import capo_device_farm.types.trial_minutes

        out["trial_minutes"] = (
            capo_device_farm.types.trial_minutes.deserialize_aws_json_1_1(
                data["trialMinutes"]
            )
        )
    if data.get("maxSlots") is not None:
        import capo_device_farm.types.max_slot_map

        out["max_slots"] = capo_device_farm.types.max_slot_map.deserialize_aws_json_1_1(
            data["maxSlots"]
        )
    if data.get("defaultJobTimeoutMinutes") is not None:
        out["default_job_timeout_minutes"] = data["defaultJobTimeoutMinutes"]
    if data.get("skipAppResign") is not None:
        out["skip_app_resign"] = data["skipAppResign"]
    return out
