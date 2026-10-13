"""Generated from Smithy shape ``com.amazonaws.datazone#ListDataSourcesInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.data_source_status
    import capo_datazone.types.data_source_type
    import capo_datazone.types.domain_id
    import capo_datazone.types.max_results
    import capo_datazone.types.name
    import capo_datazone.types.pagination_token


class ListDataSourcesInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which to list the data sources.</p>"""
    project_identifier: "str"
    """<p>The identifier of the project in which to list data sources.</p>"""
    environment_identifier: NotRequired["str"]
    """<p>The identifier of the environment in which to list the data sources.</p>"""
    connection_identifier: NotRequired["str"]
    """<p>The ID of the connection.</p>"""
    type: NotRequired["capo_datazone.types.data_source_type.DataSourceType"]
    """<p>The type of the data source.</p>"""
    status: NotRequired["capo_datazone.types.data_source_status.DataSourceStatus"]
    """<p>The status of the data source.</p>"""
    name: NotRequired["capo_datazone.types.name.Name"]
    """<p>The name of the data source.</p>"""
    next_token: NotRequired["capo_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of data sources is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of data sources, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListDataSources</code> to list the next set of data sources.</p>"""
    max_results: NotRequired["capo_datazone.types.max_results.MaxResults"]
    """<p>The maximum number of data sources to return in a single call to <code>ListDataSources</code>. When the number of data sources to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListDataSources</code> to list the next set of data sources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataSourcesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDataSourcesInput:
    out: ListDataSourcesInput = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: ListDataSourcesInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
