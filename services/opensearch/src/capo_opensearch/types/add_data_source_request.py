"""Generated from Smithy shape ``com.amazonaws.opensearch#AddDataSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.data_source_description
    import capo_opensearch.types.data_source_name
    import capo_opensearch.types.data_source_type
    import capo_opensearch.types.domain_name


class AddDataSourceRequest(TypedDict, closed=True):
    domain_name: "capo_opensearch.types.domain_name.DomainName"
    """<p>The name of the domain to add the data source to.</p>"""
    name: "capo_opensearch.types.data_source_name.DataSourceName"
    """<p>A name for the data source.</p>"""
    data_source_type: "capo_opensearch.types.data_source_type.DataSourceType"
    """<p>The type of data source.</p>"""
    description: NotRequired[
        "capo_opensearch.types.data_source_description.DataSourceDescription"
    ]
    """<p>A description of the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddDataSourceRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_opensearch.types.data_source_type

    out["DataSourceType"] = capo_opensearch.types.data_source_type.serialize_json(
        value["data_source_type"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> AddDataSourceRequest:
    out: AddDataSourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("DataSourceType") is not None:
        import capo_opensearch.types.data_source_type

        out["data_source_type"] = (
            capo_opensearch.types.data_source_type.deserialize_json(
                data["DataSourceType"]
            )
        )
    else:
        import capo_opensearch.types._unknown

        out["data_source_type"] = capo_opensearch.types._unknown.UnknownUnionMember("")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
