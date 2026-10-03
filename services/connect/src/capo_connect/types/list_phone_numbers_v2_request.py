"""Generated from Smithy shape ``com.amazonaws.connect#ListPhoneNumbersV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.instance_id
    import capo_connect.types.large_next_token
    import capo_connect.types.max_result1000
    import capo_connect.types.phone_number_country_codes
    import capo_connect.types.phone_number_prefix
    import capo_connect.types.phone_number_types


class ListPhoneNumbersV2Request(TypedDict, closed=True):
    target_arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) for Connect Customer instances or traffic distribution groups that phone number inbound traffic is routed through. If both <code>TargetArn</code> and <code>InstanceId</code> input are not provided, this API lists numbers claimed to all the Connect Customer instances belonging to your account in the same Amazon Web Services Region as the request.</p>"""
    instance_id: NotRequired["capo_connect.types.instance_id.InstanceId"]
    """<p>The identifier of the Connect Customer instance that phone numbers are claimed to. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance. If both <code>TargetArn</code> and <code>InstanceId</code> are not provided, this API lists numbers claimed to all the Connect Customer instances belonging to your account in the same Amazon Web Services Region as the request.</p>"""
    max_results: NotRequired["capo_connect.types.max_result1000.MaxResult1000"]
    """<p>The maximum number of results to return per page.</p>"""
    next_token: NotRequired["capo_connect.types.large_next_token.LargeNextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    phone_number_country_codes: NotRequired[
        "capo_connect.types.phone_number_country_codes.PhoneNumberCountryCodes"
    ]
    """<p>The ISO country code.</p>"""
    phone_number_types: NotRequired[
        "capo_connect.types.phone_number_types.PhoneNumberTypes"
    ]
    """<p>The type of phone number.</p>"""
    phone_number_prefix: NotRequired[
        "capo_connect.types.phone_number_prefix.PhoneNumberPrefix"
    ]
    """<p>The prefix of the phone number. If provided, it must contain <code>+</code> as part of the country code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPhoneNumbersV2Request) -> dict:
    out: dict = {}
    if "target_arn" in value:
        out["TargetArn"] = value["target_arn"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "phone_number_country_codes" in value:
        import capo_connect.types.phone_number_country_codes

        out["PhoneNumberCountryCodes"] = (
            capo_connect.types.phone_number_country_codes.serialize_json(
                value["phone_number_country_codes"]
            )
        )
    if "phone_number_types" in value:
        import capo_connect.types.phone_number_types

        out["PhoneNumberTypes"] = capo_connect.types.phone_number_types.serialize_json(
            value["phone_number_types"]
        )
    if "phone_number_prefix" in value:
        out["PhoneNumberPrefix"] = value["phone_number_prefix"]
    return out


def deserialize_json(data: dict) -> ListPhoneNumbersV2Request:
    out: ListPhoneNumbersV2Request = {}  # type: ignore[typeddict-item]
    if data.get("TargetArn") is not None:
        out["target_arn"] = data["TargetArn"]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("PhoneNumberCountryCodes") is not None:
        import capo_connect.types.phone_number_country_codes

        out["phone_number_country_codes"] = (
            capo_connect.types.phone_number_country_codes.deserialize_json(
                data["PhoneNumberCountryCodes"]
            )
        )
    if data.get("PhoneNumberTypes") is not None:
        import capo_connect.types.phone_number_types

        out["phone_number_types"] = (
            capo_connect.types.phone_number_types.deserialize_json(
                data["PhoneNumberTypes"]
            )
        )
    if data.get("PhoneNumberPrefix") is not None:
        out["phone_number_prefix"] = data["PhoneNumberPrefix"]
    return out
