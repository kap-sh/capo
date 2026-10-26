"""Generated from Smithy shape ``com.amazonaws.opensearch#UpdateDataSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.data_source_description
    import capo_opensearch.types.data_source_name
    import capo_opensearch.types.data_source_status
    import capo_opensearch.types.data_source_type
    import capo_opensearch.types.domain_name


class UpdateDataSourceRequest(TypedDict, closed=True):
    domain_name: "capo_opensearch.types.domain_name.DomainName"
    """<p>The name of the domain.</p>"""
    name: "capo_opensearch.types.data_source_name.DataSourceName"
    """<p>The name of the data source to modify.</p>"""
    data_source_type: "capo_opensearch.types.data_source_type.DataSourceType"
    """<p>The type of data source.</p>"""
    description: NotRequired[
        "capo_opensearch.types.data_source_description.DataSourceDescription"
    ]
    """<p>A new description of the data source.</p>"""
    status: NotRequired["capo_opensearch.types.data_source_status.DataSourceStatus"]
    """<p>The status of the data source update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataSourceRequest) -> dict:
    out: dict = {}
    import capo_opensearch.types.data_source_type

    out["DataSourceType"] = capo_opensearch.types.data_source_type.serialize_json(
        value["data_source_type"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import capo_opensearch.types.data_source_status

        out["Status"] = capo_opensearch.types.data_source_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> UpdateDataSourceRequest:
    out: UpdateDataSourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("DataSourceType") is not None:
        import capo_opensearch.types.data_source_type

        out["data_source_type"] = (
            capo_opensearch.types.data_source_type.deserialize_json(
                data["DataSourceType"]
            )
        )
    else:
        out["data_source_type"] = {"$unknown": {"name": ""}}
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Status") is not None:
        import capo_opensearch.types.data_source_status

        out["status"] = capo_opensearch.types.data_source_status.deserialize_json(
            data["Status"]
        )
    return out
