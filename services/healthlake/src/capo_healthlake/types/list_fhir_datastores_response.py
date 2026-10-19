"""Generated from Smithy shape ``com.amazonaws.healthlake#ListFHIRDatastoresResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.datastore_properties_list
    import capo_healthlake.types.next_token


class ListFHIRDatastoresResponse(TypedDict, closed=True):
    datastore_properties_list: (
        "capo_healthlake.types.datastore_properties_list.DatastorePropertiesList"
    )
    """<p>The properties associated with all listed data stores.</p>"""
    next_token: NotRequired["capo_healthlake.types.next_token.NextToken"]
    """<p>The pagination token used to retrieve the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListFHIRDatastoresResponse) -> dict:
    out: dict = {}
    import capo_healthlake.types.datastore_properties_list

    out["DatastorePropertiesList"] = (
        capo_healthlake.types.datastore_properties_list.serialize_aws_json_1_0(
            value["datastore_properties_list"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListFHIRDatastoresResponse:
    out: ListFHIRDatastoresResponse = {}  # type: ignore[typeddict-item]
    if data.get("DatastorePropertiesList") is not None:
        import capo_healthlake.types.datastore_properties_list

        out["datastore_properties_list"] = (
            capo_healthlake.types.datastore_properties_list.deserialize_aws_json_1_0(
                data["DatastorePropertiesList"]
            )
        )
    else:
        out["datastore_properties_list"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
