"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#AssociateOriginationIdentityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.client_token
    import capo_pinpoint_sms_voice_v2.types.iso_country_code
    import capo_pinpoint_sms_voice_v2.types.phone_or_sender_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.pool_id_or_arn


class AssociateOriginationIdentityRequest(TypedDict, closed=True):
    pool_id: "capo_pinpoint_sms_voice_v2.types.pool_id_or_arn.PoolIdOrArn"
    """<p>The pool to update with the new Identity. This value can be either the PoolId or PoolArn, and you can find these values using <a href="https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribePools.html">DescribePools</a>.</p> <important> <p>If you are using a shared End User Messaging SMS; resource then you must use the full Amazon Resource Name(ARN).</p> </important>"""
    origination_identity: "capo_pinpoint_sms_voice_v2.types.phone_or_sender_id_or_arn.PhoneOrSenderIdOrArn"
    """<p>The origination identity to use, such as PhoneNumberId, PhoneNumberArn, SenderId, or SenderIdArn. You can use <a>DescribePhoneNumbers</a> to find the values for PhoneNumberId and PhoneNumberArn, while <a>DescribeSenderIds</a> can be used to get the values for SenderId and SenderIdArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>"""
    iso_country_code: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode"
    ]
    """<p>The new two-character code, in ISO 3166-1 alpha-2 format, for the country or region of the origination identity. This field is optional and is not required for origination identity types that are not country-specific, such as RCS agents.</p>"""
    client_token: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateOriginationIdentityRequest) -> dict:
    out: dict = {}
    out["PoolId"] = value["pool_id"]
    out["OriginationIdentity"] = value["origination_identity"]
    if "iso_country_code" in value:
        out["IsoCountryCode"] = value["iso_country_code"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateOriginationIdentityRequest:
    out: AssociateOriginationIdentityRequest = {}  # type: ignore[typeddict-item]
    if data.get("PoolId") is not None:
        out["pool_id"] = data["PoolId"]
    else:
        raise DeserializationError(
            "AssociateOriginationIdentityRequest.pool_id required"
        )
    if data.get("OriginationIdentity") is not None:
        out["origination_identity"] = data["OriginationIdentity"]
    else:
        raise DeserializationError(
            "AssociateOriginationIdentityRequest.origination_identity required"
        )
    if data.get("IsoCountryCode") is not None:
        out["iso_country_code"] = data["IsoCountryCode"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
