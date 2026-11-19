"""Generated from Smithy shape ``com.amazonaws.directoryservice#LDAPSSettingInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.last_updated_date_time
    import capo_directory_service.types.ldaps_status
    import capo_directory_service.types.ldaps_status_reason


class LDAPSSettingInfo(TypedDict, closed=True):
    ldaps_status: NotRequired["capo_directory_service.types.ldaps_status.LDAPSStatus"]
    """<p>The state of the LDAPS settings.</p>"""
    ldaps_status_reason: NotRequired[
        "capo_directory_service.types.ldaps_status_reason.LDAPSStatusReason"
    ]
    """<p>Describes a state change for LDAPS.</p>"""
    last_updated_date_time: NotRequired[
        "capo_directory_service.types.last_updated_date_time.LastUpdatedDateTime"
    ]
    """<p>The date and time when the LDAPS settings were last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LDAPSSettingInfo) -> dict:
    out: dict = {}
    if "ldaps_status" in value:
        import capo_directory_service.types.ldaps_status

        out["LDAPSStatus"] = (
            capo_directory_service.types.ldaps_status.serialize_aws_json_1_1(
                value["ldaps_status"]
            )
        )
    if "ldaps_status_reason" in value:
        out["LDAPSStatusReason"] = value["ldaps_status_reason"]
    if "last_updated_date_time" in value:
        import capo_directory_service.types.last_updated_date_time

        out["LastUpdatedDateTime"] = (
            capo_directory_service.types.last_updated_date_time.serialize_aws_json_1_1(
                value["last_updated_date_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LDAPSSettingInfo:
    out: LDAPSSettingInfo = {}  # type: ignore[typeddict-item]
    if data.get("LDAPSStatus") is not None:
        import capo_directory_service.types.ldaps_status

        out["ldaps_status"] = (
            capo_directory_service.types.ldaps_status.deserialize_aws_json_1_1(
                data["LDAPSStatus"]
            )
        )
    if data.get("LDAPSStatusReason") is not None:
        out["ldaps_status_reason"] = data["LDAPSStatusReason"]
    if data.get("LastUpdatedDateTime") is not None:
        import capo_directory_service.types.last_updated_date_time

        out["last_updated_date_time"] = (
            capo_directory_service.types.last_updated_date_time.deserialize_aws_json_1_1(
                data["LastUpdatedDateTime"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LDAPSSettingInfo) -> dict:
    out: dict = {}
    if "ldaps_status" in value:
        import capo_directory_service.types.ldaps_status

        out["LDAPSStatus"] = capo_directory_service.types.ldaps_status.serialize_cbor(
            value["ldaps_status"]
        )
    if "ldaps_status_reason" in value:
        out["LDAPSStatusReason"] = value["ldaps_status_reason"]
    if "last_updated_date_time" in value:
        import capo_directory_service.types.last_updated_date_time

        out["LastUpdatedDateTime"] = (
            capo_directory_service.types.last_updated_date_time.serialize_cbor(
                value["last_updated_date_time"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> LDAPSSettingInfo:
    out: LDAPSSettingInfo = {}  # type: ignore[typeddict-item]
    if data.get("LDAPSStatus") is not None:
        import capo_directory_service.types.ldaps_status

        out["ldaps_status"] = (
            capo_directory_service.types.ldaps_status.deserialize_cbor(
                data["LDAPSStatus"]
            )
        )
    if data.get("LDAPSStatusReason") is not None:
        out["ldaps_status_reason"] = data["LDAPSStatusReason"]
    if data.get("LastUpdatedDateTime") is not None:
        import capo_directory_service.types.last_updated_date_time

        out["last_updated_date_time"] = (
            capo_directory_service.types.last_updated_date_time.deserialize_cbor(
                data["LastUpdatedDateTime"]
            )
        )
    return out
