"""Generated from Smithy shape ``com.amazonaws.appconfig#ListHostedConfigurationVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.long_name
    import capo_appconfig.types.max_results
    import capo_appconfig.types.name
    import capo_appconfig.types.next_token
    import capo_appconfig.types.query_name


class ListHostedConfigurationVersionsRequest(TypedDict, closed=True):
    application_id: "capo_appconfig.types.name.Name"
    """<p>The application ID.</p>"""
    configuration_profile_id: "capo_appconfig.types.long_name.LongName"
    """<p>The configuration profile ID.</p>"""
    max_results: NotRequired["capo_appconfig.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. If <code>MaxResults</code> is not provided in the call, AppConfig returns the maximum of 50. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["capo_appconfig.types.next_token.NextToken"]
    """<p>A token to start the list. Use this token to get the next set of results. </p>"""
    version_label: NotRequired["capo_appconfig.types.query_name.QueryName"]
    """<p>An optional filter that can be used to specify the version label of an AppConfig hosted configuration version. This parameter supports filtering by prefix using a wildcard, for example "v2*". If you don't specify an asterisk at the end of the value, only an exact match is returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListHostedConfigurationVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListHostedConfigurationVersionsRequest:
    out: ListHostedConfigurationVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
