"""Generated from Smithy shape ``com.amazonaws.directoryservice#SettingEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.directory_configuration_setting_allowed_values
    import capo_directory_service.types.directory_configuration_setting_data_type
    import capo_directory_service.types.directory_configuration_setting_last_requested_date_time
    import capo_directory_service.types.directory_configuration_setting_last_updated_date_time
    import capo_directory_service.types.directory_configuration_setting_name
    import capo_directory_service.types.directory_configuration_setting_request_detailed_status
    import capo_directory_service.types.directory_configuration_setting_request_status_message
    import capo_directory_service.types.directory_configuration_setting_type
    import capo_directory_service.types.directory_configuration_setting_value
    import capo_directory_service.types.directory_configuration_status


class SettingEntry(TypedDict, closed=True):
    type: NotRequired[
        "capo_directory_service.types.directory_configuration_setting_type.DirectoryConfigurationSettingType"
    ]
    """<p>The type, or category, of a directory setting. Similar settings have the same type. For example, <code>Protocol</code>, <code>Cipher</code>, or <code>Certificate-Based Authentication</code>.</p>"""
    name: NotRequired[
        "capo_directory_service.types.directory_configuration_setting_name.DirectoryConfigurationSettingName"
    ]
    """<p>The name of the directory setting. For example:</p> <p> <code>TLS_1_0</code> </p>"""
    allowed_values: NotRequired[
        "capo_directory_service.types.directory_configuration_setting_allowed_values.DirectoryConfigurationSettingAllowedValues"
    ]
    """<p>The valid range of values for the directory setting. These values depend on the <code>DataType</code> of your directory.</p>"""
    applied_value: NotRequired[
        "capo_directory_service.types.directory_configuration_setting_value.DirectoryConfigurationSettingValue"
    ]
    """<p>The value of the directory setting that is applied to the directory.</p>"""
    requested_value: NotRequired[
        "capo_directory_service.types.directory_configuration_setting_value.DirectoryConfigurationSettingValue"
    ]
    """<p>The value that was last requested for the directory setting.</p>"""
    request_status: NotRequired[
        "capo_directory_service.types.directory_configuration_status.DirectoryConfigurationStatus"
    ]
    """<p>The overall status of the request to update the directory setting request. If the directory setting is deployed in more than one region, and the request fails in any region, the overall status is <code>Failed</code>.</p>"""
    request_detailed_status: NotRequired[
        "capo_directory_service.types.directory_configuration_setting_request_detailed_status.DirectoryConfigurationSettingRequestDetailedStatus"
    ]
    """<p>Details about the status of the request to update the directory setting. If the directory setting is deployed in more than one region, status is returned for the request in each region where the setting is deployed.</p>"""
    request_status_message: NotRequired[
        "capo_directory_service.types.directory_configuration_setting_request_status_message.DirectoryConfigurationSettingRequestStatusMessage"
    ]
    """<p>The last status message for the directory status request.</p>"""
    last_updated_date_time: NotRequired[
        "capo_directory_service.types.directory_configuration_setting_last_updated_date_time.DirectoryConfigurationSettingLastUpdatedDateTime"
    ]
    """<p>The date and time when the directory setting was last updated.</p>"""
    last_requested_date_time: NotRequired[
        "capo_directory_service.types.directory_configuration_setting_last_requested_date_time.DirectoryConfigurationSettingLastRequestedDateTime"
    ]
    """<p>The date and time when the request to update a directory setting was last submitted.</p>"""
    data_type: NotRequired[
        "capo_directory_service.types.directory_configuration_setting_data_type.DirectoryConfigurationSettingDataType"
    ]
    """<p>The data type of a directory setting. This is used to define the <code>AllowedValues</code> of a setting. For example a data type can be <code>Boolean</code>, <code>DurationInSeconds</code>, or <code>Enum</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SettingEntry) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "name" in value:
        out["Name"] = value["name"]
    if "allowed_values" in value:
        out["AllowedValues"] = value["allowed_values"]
    if "applied_value" in value:
        out["AppliedValue"] = value["applied_value"]
    if "requested_value" in value:
        out["RequestedValue"] = value["requested_value"]
    if "request_status" in value:
        import capo_directory_service.types.directory_configuration_status

        out["RequestStatus"] = (
            capo_directory_service.types.directory_configuration_status.serialize_aws_json_1_1(
                value["request_status"]
            )
        )
    if "request_detailed_status" in value:
        import capo_directory_service.types.directory_configuration_setting_request_detailed_status

        out["RequestDetailedStatus"] = (
            capo_directory_service.types.directory_configuration_setting_request_detailed_status.serialize_aws_json_1_1(
                value["request_detailed_status"]
            )
        )
    if "request_status_message" in value:
        out["RequestStatusMessage"] = value["request_status_message"]
    if "last_updated_date_time" in value:
        import capo_directory_service.types.directory_configuration_setting_last_updated_date_time

        out["LastUpdatedDateTime"] = (
            capo_directory_service.types.directory_configuration_setting_last_updated_date_time.serialize_aws_json_1_1(
                value["last_updated_date_time"]
            )
        )
    if "last_requested_date_time" in value:
        import capo_directory_service.types.directory_configuration_setting_last_requested_date_time

        out["LastRequestedDateTime"] = (
            capo_directory_service.types.directory_configuration_setting_last_requested_date_time.serialize_aws_json_1_1(
                value["last_requested_date_time"]
            )
        )
    if "data_type" in value:
        out["DataType"] = value["data_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SettingEntry:
    out: SettingEntry = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("AllowedValues") is not None:
        out["allowed_values"] = data["AllowedValues"]
    if data.get("AppliedValue") is not None:
        out["applied_value"] = data["AppliedValue"]
    if data.get("RequestedValue") is not None:
        out["requested_value"] = data["RequestedValue"]
    if data.get("RequestStatus") is not None:
        import capo_directory_service.types.directory_configuration_status

        out["request_status"] = (
            capo_directory_service.types.directory_configuration_status.deserialize_aws_json_1_1(
                data["RequestStatus"]
            )
        )
    if data.get("RequestDetailedStatus") is not None:
        import capo_directory_service.types.directory_configuration_setting_request_detailed_status

        out["request_detailed_status"] = (
            capo_directory_service.types.directory_configuration_setting_request_detailed_status.deserialize_aws_json_1_1(
                data["RequestDetailedStatus"]
            )
        )
    if data.get("RequestStatusMessage") is not None:
        out["request_status_message"] = data["RequestStatusMessage"]
    if data.get("LastUpdatedDateTime") is not None:
        import capo_directory_service.types.directory_configuration_setting_last_updated_date_time

        out["last_updated_date_time"] = (
            capo_directory_service.types.directory_configuration_setting_last_updated_date_time.deserialize_aws_json_1_1(
                data["LastUpdatedDateTime"]
            )
        )
    if data.get("LastRequestedDateTime") is not None:
        import capo_directory_service.types.directory_configuration_setting_last_requested_date_time

        out["last_requested_date_time"] = (
            capo_directory_service.types.directory_configuration_setting_last_requested_date_time.deserialize_aws_json_1_1(
                data["LastRequestedDateTime"]
            )
        )
    if data.get("DataType") is not None:
        out["data_type"] = data["DataType"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SettingEntry) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "name" in value:
        out["Name"] = value["name"]
    if "allowed_values" in value:
        out["AllowedValues"] = value["allowed_values"]
    if "applied_value" in value:
        out["AppliedValue"] = value["applied_value"]
    if "requested_value" in value:
        out["RequestedValue"] = value["requested_value"]
    if "request_status" in value:
        import capo_directory_service.types.directory_configuration_status

        out["RequestStatus"] = (
            capo_directory_service.types.directory_configuration_status.serialize_cbor(
                value["request_status"]
            )
        )
    if "request_detailed_status" in value:
        import capo_directory_service.types.directory_configuration_setting_request_detailed_status

        out["RequestDetailedStatus"] = (
            capo_directory_service.types.directory_configuration_setting_request_detailed_status.serialize_cbor(
                value["request_detailed_status"]
            )
        )
    if "request_status_message" in value:
        out["RequestStatusMessage"] = value["request_status_message"]
    if "last_updated_date_time" in value:
        import capo_directory_service.types.directory_configuration_setting_last_updated_date_time

        out["LastUpdatedDateTime"] = (
            capo_directory_service.types.directory_configuration_setting_last_updated_date_time.serialize_cbor(
                value["last_updated_date_time"]
            )
        )
    if "last_requested_date_time" in value:
        import capo_directory_service.types.directory_configuration_setting_last_requested_date_time

        out["LastRequestedDateTime"] = (
            capo_directory_service.types.directory_configuration_setting_last_requested_date_time.serialize_cbor(
                value["last_requested_date_time"]
            )
        )
    if "data_type" in value:
        out["DataType"] = value["data_type"]
    return out


def deserialize_cbor(data: dict) -> SettingEntry:
    out: SettingEntry = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("AllowedValues") is not None:
        out["allowed_values"] = data["AllowedValues"]
    if data.get("AppliedValue") is not None:
        out["applied_value"] = data["AppliedValue"]
    if data.get("RequestedValue") is not None:
        out["requested_value"] = data["RequestedValue"]
    if data.get("RequestStatus") is not None:
        import capo_directory_service.types.directory_configuration_status

        out["request_status"] = (
            capo_directory_service.types.directory_configuration_status.deserialize_cbor(
                data["RequestStatus"]
            )
        )
    if data.get("RequestDetailedStatus") is not None:
        import capo_directory_service.types.directory_configuration_setting_request_detailed_status

        out["request_detailed_status"] = (
            capo_directory_service.types.directory_configuration_setting_request_detailed_status.deserialize_cbor(
                data["RequestDetailedStatus"]
            )
        )
    if data.get("RequestStatusMessage") is not None:
        out["request_status_message"] = data["RequestStatusMessage"]
    if data.get("LastUpdatedDateTime") is not None:
        import capo_directory_service.types.directory_configuration_setting_last_updated_date_time

        out["last_updated_date_time"] = (
            capo_directory_service.types.directory_configuration_setting_last_updated_date_time.deserialize_cbor(
                data["LastUpdatedDateTime"]
            )
        )
    if data.get("LastRequestedDateTime") is not None:
        import capo_directory_service.types.directory_configuration_setting_last_requested_date_time

        out["last_requested_date_time"] = (
            capo_directory_service.types.directory_configuration_setting_last_requested_date_time.deserialize_cbor(
                data["LastRequestedDateTime"]
            )
        )
    if data.get("DataType") is not None:
        out["data_type"] = data["DataType"]
    return out
