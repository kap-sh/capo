"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#SipMediaApplication``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.iso8601_timestamp
    import capo_chime_sdk_voice.types.non_empty_string
    import capo_chime_sdk_voice.types.sip_media_application_endpoint_list
    import capo_chime_sdk_voice.types.sip_media_application_name
    import capo_chime_sdk_voice.types.string


class SipMediaApplication(TypedDict, closed=True):
    sip_media_application_id: NotRequired[
        "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    ]
    """<p>A SIP media application's ID.</p>"""
    aws_region: NotRequired["capo_chime_sdk_voice.types.string.String"]
    """<p>The AWS Region in which the SIP media application is created.</p>"""
    name: NotRequired[
        "capo_chime_sdk_voice.types.sip_media_application_name.SipMediaApplicationName"
    ]
    """<p>The SIP media application's name.</p>"""
    endpoints: NotRequired[
        "capo_chime_sdk_voice.types.sip_media_application_endpoint_list.SipMediaApplicationEndpointList"
    ]
    """<p>List of endpoints for a SIP media application. Currently, only one endpoint per SIP media application is permitted.</p>"""
    created_timestamp: NotRequired[
        "capo_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The SIP media application creation timestamp, in ISO 8601 format.</p>"""
    updated_timestamp: NotRequired[
        "capo_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which the SIP media application was updated.</p>"""
    sip_media_application_arn: NotRequired[
        "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the SIP media application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SipMediaApplication) -> dict:
    out: dict = {}
    if "sip_media_application_id" in value:
        out["SipMediaApplicationId"] = value["sip_media_application_id"]
    if "aws_region" in value:
        out["AwsRegion"] = value["aws_region"]
    if "name" in value:
        out["Name"] = value["name"]
    if "endpoints" in value:
        import capo_chime_sdk_voice.types.sip_media_application_endpoint_list

        out["Endpoints"] = (
            capo_chime_sdk_voice.types.sip_media_application_endpoint_list.serialize_json(
                value["endpoints"]
            )
        )
    if "created_timestamp" in value:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["CreatedTimestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "updated_timestamp" in value:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["UpdatedTimestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["updated_timestamp"]
            )
        )
    if "sip_media_application_arn" in value:
        out["SipMediaApplicationArn"] = value["sip_media_application_arn"]
    return out


def deserialize_json(data: dict) -> SipMediaApplication:
    out: SipMediaApplication = {}  # type: ignore[typeddict-item]
    if data.get("SipMediaApplicationId") is not None:
        out["sip_media_application_id"] = data["SipMediaApplicationId"]
    if data.get("AwsRegion") is not None:
        out["aws_region"] = data["AwsRegion"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Endpoints") is not None:
        import capo_chime_sdk_voice.types.sip_media_application_endpoint_list

        out["endpoints"] = (
            capo_chime_sdk_voice.types.sip_media_application_endpoint_list.deserialize_json(
                data["Endpoints"]
            )
        )
    if data.get("CreatedTimestamp") is not None:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["created_timestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if data.get("UpdatedTimestamp") is not None:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["updated_timestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["UpdatedTimestamp"]
            )
        )
    if data.get("SipMediaApplicationArn") is not None:
        out["sip_media_application_arn"] = data["SipMediaApplicationArn"]
    return out


def redact_sensitive(value: SipMediaApplication) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "endpoints" in value:
        import capo_chime_sdk_voice.types.sip_media_application_endpoint_list

        out["endpoints"] = (
            capo_chime_sdk_voice.types.sip_media_application_endpoint_list.redact_sensitive(
                value["endpoints"]
            )
        )
    return out
