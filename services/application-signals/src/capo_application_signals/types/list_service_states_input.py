"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ListServiceStatesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_application_signals.types.attribute_filters
    import capo_application_signals.types.aws_account_id
    import capo_application_signals.types.list_service_states_max_results
    import capo_application_signals.types.next_token


class ListServiceStatesInput(TypedDict, closed=True):
    start_time: "datetime.datetime"
    """<p>The start of the time period to retrieve service state information for. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example, <code>1698778057</code>.</p>"""
    end_time: "datetime.datetime"
    """<p>The end of the time period to retrieve service state information for. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example, <code>1698778057</code>.</p>"""
    max_results: NotRequired[
        "capo_application_signals.types.list_service_states_max_results.ListServiceStatesMaxResults"
    ]
    """<p>The maximum number of service states to return in one operation. If you omit this parameter, the default of 20 is used.</p>"""
    next_token: NotRequired["capo_application_signals.types.next_token.NextToken"]
    """<p>Include this value, if it was returned by the previous operation, to get the next set of service states.</p>"""
    include_linked_accounts: NotRequired["bool"]
    """<p>If you are using this operation in a monitoring account, specify <code>true</code> to include service states from source accounts in the returned data.</p>"""
    aws_account_id: NotRequired[
        "capo_application_signals.types.aws_account_id.AwsAccountId"
    ]
    """<p>The Amazon Web Services account ID to filter service states by. Use this to limit results to services from a specific account.</p>"""
    attribute_filters: NotRequired[
        "capo_application_signals.types.attribute_filters.AttributeFilters"
    ]
    """<p>A list of attribute filters to narrow down the services. You can filter by platform, environment, or other service attributes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceStatesInput) -> dict:
    out: dict = {}
    import capo_application_signals.types._prelude.timestamp

    out["StartTime"] = capo_application_signals.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    import capo_application_signals.types._prelude.timestamp

    out["EndTime"] = capo_application_signals.types._prelude.timestamp.serialize_json(
        value["end_time"]
    )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "include_linked_accounts" in value:
        out["IncludeLinkedAccounts"] = value["include_linked_accounts"]
    if "aws_account_id" in value:
        out["AwsAccountId"] = value["aws_account_id"]
    if "attribute_filters" in value:
        import capo_application_signals.types.attribute_filters

        out["AttributeFilters"] = (
            capo_application_signals.types.attribute_filters.serialize_json(
                value["attribute_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListServiceStatesInput:
    out: ListServiceStatesInput = {}  # type: ignore[typeddict-item]
    if data.get("StartTime") is not None:
        import capo_application_signals.types._prelude.timestamp

        out["start_time"] = (
            capo_application_signals.types._prelude.timestamp.deserialize_json(
                data["StartTime"]
            )
        )
    else:
        raise DeserializationError("ListServiceStatesInput.start_time required")
    if data.get("EndTime") is not None:
        import capo_application_signals.types._prelude.timestamp

        out["end_time"] = (
            capo_application_signals.types._prelude.timestamp.deserialize_json(
                data["EndTime"]
            )
        )
    else:
        raise DeserializationError("ListServiceStatesInput.end_time required")
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("IncludeLinkedAccounts") is not None:
        out["include_linked_accounts"] = data["IncludeLinkedAccounts"]
    if data.get("AwsAccountId") is not None:
        out["aws_account_id"] = data["AwsAccountId"]
    if data.get("AttributeFilters") is not None:
        import capo_application_signals.types.attribute_filters

        out["attribute_filters"] = (
            capo_application_signals.types.attribute_filters.deserialize_json(
                data["AttributeFilters"]
            )
        )
    return out
