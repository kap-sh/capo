"""Generated from Smithy shape ``com.amazonaws.connect#ListPhoneNumbersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.max_result1000
    import capo_connect.types.next_token
    import capo_connect.types.phone_number_country_codes
    import capo_connect.types.phone_number_types


class ListPhoneNumbersRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    phone_number_types: NotRequired[
        "capo_connect.types.phone_number_types.PhoneNumberTypes"
    ]
    """<p>The type of phone number.</p> <note> <p>We recommend using <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_ListPhoneNumbersV2.html">ListPhoneNumbersV2</a> to return phone number types. While ListPhoneNumbers returns number types <code>UIFN</code>, <code>SHARED</code>, <code>THIRD_PARTY_TF</code>, and <code>THIRD_PARTY_DID</code>, it incorrectly lists them as <code>TOLL_FREE</code> or <code>DID</code>. </p> </note>"""
    phone_number_country_codes: NotRequired[
        "capo_connect.types.phone_number_country_codes.PhoneNumberCountryCodes"
    ]
    """<p>The ISO country code.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["capo_connect.types.max_result1000.MaxResult1000"]
    """<p>The maximum number of results to return per page. The default MaxResult size is 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPhoneNumbersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPhoneNumbersRequest:
    out: ListPhoneNumbersRequest = {}  # type: ignore[typeddict-item]
    return out
