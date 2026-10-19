"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ListServicesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_application_signals.types.aws_account_id
    import capo_application_signals.types.list_services_max_results
    import capo_application_signals.types.next_token


class ListServicesInput(TypedDict, closed=True):
    start_time: "datetime.datetime"
    """<p>The start of the time period to retrieve information about. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>Your requested start time will be rounded to the nearest hour.</p>"""
    end_time: "datetime.datetime"
    """<p>The end of the time period to retrieve information about. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>Your requested start time will be rounded to the nearest hour.</p>"""
    max_results: NotRequired[
        "capo_application_signals.types.list_services_max_results.ListServicesMaxResults"
    ]
    """<p> The maximum number of results to return in one operation. If you omit this parameter, the default of 50 is used. </p>"""
    next_token: NotRequired["capo_application_signals.types.next_token.NextToken"]
    """<p>Include this value, if it was returned by the previous operation, to get the next set of services.</p>"""
    include_linked_accounts: NotRequired["bool"]
    """<p>If you are using this operation in a monitoring account, specify <code>true</code> to include services from source accounts in the returned data. </p>"""
    aws_account_id: NotRequired[
        "capo_application_signals.types.aws_account_id.AwsAccountId"
    ]
    """<p>Amazon Web Services Account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServicesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListServicesInput:
    out: ListServicesInput = {}  # type: ignore[typeddict-item]
    return out
