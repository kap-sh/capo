"""Generated from Smithy shape ``com.amazonaws.connect#SearchAvailablePhoneNumbersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.instance_id
    import capo_connect.types.large_next_token
    import capo_connect.types.max_result10
    import capo_connect.types.phone_number_country_code
    import capo_connect.types.phone_number_prefix
    import capo_connect.types.phone_number_type


class SearchAvailablePhoneNumbersRequest(TypedDict, closed=True):
    target_arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) for Connect Customer instances or traffic distribution groups that phone number inbound traffic is routed through. You must enter <code>InstanceId</code> or <code>TargetArn</code>. </p>"""
    instance_id: NotRequired["capo_connect.types.instance_id.InstanceId"]
    """<p>The identifier of the Connect Customer instance that phone numbers are claimed to. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance. You must enter <code>InstanceId</code> or <code>TargetArn</code>. </p>"""
    phone_number_country_code: (
        "capo_connect.types.phone_number_country_code.PhoneNumberCountryCode"
    )
    """<p>The ISO country code.</p>"""
    phone_number_type: "capo_connect.types.phone_number_type.PhoneNumberType"
    """<p>The type of phone number.</p>"""
    phone_number_prefix: NotRequired[
        "capo_connect.types.phone_number_prefix.PhoneNumberPrefix"
    ]
    """<p>The prefix of the phone number. If provided, it must contain <code>+</code> as part of the country code.</p>"""
    max_results: NotRequired["capo_connect.types.max_result10.MaxResult10"]
    """<p>The maximum number of results to return per page.</p>"""
    next_token: NotRequired["capo_connect.types.large_next_token.LargeNextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchAvailablePhoneNumbersRequest) -> dict:
    out: dict = {}
    if "target_arn" in value:
        out["TargetArn"] = value["target_arn"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    import capo_connect.types.phone_number_country_code

    out["PhoneNumberCountryCode"] = (
        capo_connect.types.phone_number_country_code.serialize_json(
            value["phone_number_country_code"]
        )
    )
    import capo_connect.types.phone_number_type

    out["PhoneNumberType"] = capo_connect.types.phone_number_type.serialize_json(
        value["phone_number_type"]
    )
    if "phone_number_prefix" in value:
        out["PhoneNumberPrefix"] = value["phone_number_prefix"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchAvailablePhoneNumbersRequest:
    out: SearchAvailablePhoneNumbersRequest = {}  # type: ignore[typeddict-item]
    if data.get("TargetArn") is not None:
        out["target_arn"] = data["TargetArn"]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    if data.get("PhoneNumberCountryCode") is not None:
        import capo_connect.types.phone_number_country_code

        out["phone_number_country_code"] = (
            capo_connect.types.phone_number_country_code.deserialize_json(
                data["PhoneNumberCountryCode"]
            )
        )
    else:
        raise DeserializationError(
            "SearchAvailablePhoneNumbersRequest.phone_number_country_code required"
        )
    if data.get("PhoneNumberType") is not None:
        import capo_connect.types.phone_number_type

        out["phone_number_type"] = (
            capo_connect.types.phone_number_type.deserialize_json(
                data["PhoneNumberType"]
            )
        )
    else:
        raise DeserializationError(
            "SearchAvailablePhoneNumbersRequest.phone_number_type required"
        )
    if data.get("PhoneNumberPrefix") is not None:
        out["phone_number_prefix"] = data["PhoneNumberPrefix"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
