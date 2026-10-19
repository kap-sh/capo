"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RequestPhoneNumberRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.client_token
    import capo_pinpoint_sms_voice_v2.types.iso_country_code
    import capo_pinpoint_sms_voice_v2.types.message_type
    import capo_pinpoint_sms_voice_v2.types.number_capability_list
    import capo_pinpoint_sms_voice_v2.types.number_preference_list
    import capo_pinpoint_sms_voice_v2.types.opt_out_list_name_or_arn
    import capo_pinpoint_sms_voice_v2.types.pool_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.registration_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.requestable_number_type
    import capo_pinpoint_sms_voice_v2.types.tag_list


class RequestPhoneNumberRequest(TypedDict, closed=True):
    iso_country_code: "capo_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode"
    """<p>The two-character code, in ISO 3166-1 alpha-2 format, for the country or region. </p>"""
    message_type: "capo_pinpoint_sms_voice_v2.types.message_type.MessageType"
    """<p>The type of message. Valid values are <code>TRANSACTIONAL</code> for messages that are critical or time-sensitive and <code>PROMOTIONAL</code> for messages that aren't critical or time-sensitive.</p>"""
    number_capabilities: (
        "capo_pinpoint_sms_voice_v2.types.number_capability_list.NumberCapabilityList"
    )
    """<p>Indicates if the phone number will be used for text messages, voice messages, or both. </p>"""
    number_type: (
        "capo_pinpoint_sms_voice_v2.types.requestable_number_type.RequestableNumberType"
    )
    """<p>The type of phone number to request.</p> <p>When you request a <code>SIMULATOR</code> phone number, you must set <b>MessageType</b> as <code>TRANSACTIONAL</code>. </p>"""
    opt_out_list_name: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.opt_out_list_name_or_arn.OptOutListNameOrArn"
    ]
    """<p>The name of the OptOutList to associate with the phone number. You can use the OptOutListName or OptOutListArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>"""
    pool_id: NotRequired["capo_pinpoint_sms_voice_v2.types.pool_id_or_arn.PoolIdOrArn"]
    """<p>The pool to associated with the phone number. You can use the PoolId or PoolArn. </p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>"""
    registration_id: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.registration_id_or_arn.RegistrationIdOrArn"
    ]
    """<p>Use this field to attach your phone number for an external registration process.</p>"""
    number_preference: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.number_preference_list.NumberPreferenceList"
    ]
    """<p>An optional selection preference used to request a specific phone number, such as a number that starts with, ends with, or contains a particular digit pattern. You can specify at most one preference. Number preferences apply only to <code>TEN_DLC</code> requests in the <code>US</code>.</p>"""
    international_sending_enabled: NotRequired["bool"]
    """<p>By default this is set to false. When set to true the international sending of phone number is Enabled. </p>"""
    deletion_protection_enabled: NotRequired["bool"]
    """<p>By default this is set to false. When set to true the phone number can't be deleted.</p>"""
    tags: NotRequired["capo_pinpoint_sms_voice_v2.types.tag_list.TagList"]
    """<p>An array of tags (key and value pairs) to associate with the requested phone number. </p>"""
    client_token: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RequestPhoneNumberRequest) -> dict:
    out: dict = {}
    out["IsoCountryCode"] = value["iso_country_code"]
    out["MessageType"] = value["message_type"]
    import capo_pinpoint_sms_voice_v2.types.number_capability_list

    out["NumberCapabilities"] = (
        capo_pinpoint_sms_voice_v2.types.number_capability_list.serialize_aws_json_1_0(
            value["number_capabilities"]
        )
    )
    out["NumberType"] = value["number_type"]
    if "opt_out_list_name" in value:
        out["OptOutListName"] = value["opt_out_list_name"]
    if "pool_id" in value:
        out["PoolId"] = value["pool_id"]
    if "registration_id" in value:
        out["RegistrationId"] = value["registration_id"]
    if "number_preference" in value:
        import capo_pinpoint_sms_voice_v2.types.number_preference_list

        out["NumberPreference"] = (
            capo_pinpoint_sms_voice_v2.types.number_preference_list.serialize_aws_json_1_0(
                value["number_preference"]
            )
        )
    if "international_sending_enabled" in value:
        out["InternationalSendingEnabled"] = value["international_sending_enabled"]
    if "deletion_protection_enabled" in value:
        out["DeletionProtectionEnabled"] = value["deletion_protection_enabled"]
    if "tags" in value:
        import capo_pinpoint_sms_voice_v2.types.tag_list

        out["Tags"] = capo_pinpoint_sms_voice_v2.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RequestPhoneNumberRequest:
    out: RequestPhoneNumberRequest = {}  # type: ignore[typeddict-item]
    if data.get("IsoCountryCode") is not None:
        out["iso_country_code"] = data["IsoCountryCode"]
    else:
        out["iso_country_code"] = ""
    if data.get("MessageType") is not None:
        out["message_type"] = data["MessageType"]
    else:
        out["message_type"] = ""
    if data.get("NumberCapabilities") is not None:
        import capo_pinpoint_sms_voice_v2.types.number_capability_list

        out["number_capabilities"] = (
            capo_pinpoint_sms_voice_v2.types.number_capability_list.deserialize_aws_json_1_0(
                data["NumberCapabilities"]
            )
        )
    else:
        out["number_capabilities"] = []
    if data.get("NumberType") is not None:
        out["number_type"] = data["NumberType"]
    else:
        out["number_type"] = ""
    if data.get("OptOutListName") is not None:
        out["opt_out_list_name"] = data["OptOutListName"]
    if data.get("PoolId") is not None:
        out["pool_id"] = data["PoolId"]
    if data.get("RegistrationId") is not None:
        out["registration_id"] = data["RegistrationId"]
    if data.get("NumberPreference") is not None:
        import capo_pinpoint_sms_voice_v2.types.number_preference_list

        out["number_preference"] = (
            capo_pinpoint_sms_voice_v2.types.number_preference_list.deserialize_aws_json_1_0(
                data["NumberPreference"]
            )
        )
    if data.get("InternationalSendingEnabled") is not None:
        out["international_sending_enabled"] = data["InternationalSendingEnabled"]
    if data.get("DeletionProtectionEnabled") is not None:
        out["deletion_protection_enabled"] = data["DeletionProtectionEnabled"]
    if data.get("Tags") is not None:
        import capo_pinpoint_sms_voice_v2.types.tag_list

        out["tags"] = (
            capo_pinpoint_sms_voice_v2.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
