"""Generated from Smithy shape ``com.amazonaws.healthlake#ListFHIRImportJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.import_job_properties_list
    import capo_healthlake.types.next_token


class ListFHIRImportJobsResponse(TypedDict, closed=True):
    import_job_properties_list: (
        "capo_healthlake.types.import_job_properties_list.ImportJobPropertiesList"
    )
    """<p>The properties for listed import jobs.</p>"""
    next_token: NotRequired["capo_healthlake.types.next_token.NextToken"]
    """<p>The pagination token used to identify the next page of results to return.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListFHIRImportJobsResponse) -> dict:
    out: dict = {}
    import capo_healthlake.types.import_job_properties_list

    out["ImportJobPropertiesList"] = (
        capo_healthlake.types.import_job_properties_list.serialize_aws_json_1_0(
            value["import_job_properties_list"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListFHIRImportJobsResponse:
    out: ListFHIRImportJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ImportJobPropertiesList") is not None:
        import capo_healthlake.types.import_job_properties_list

        out["import_job_properties_list"] = (
            capo_healthlake.types.import_job_properties_list.deserialize_aws_json_1_0(
                data["ImportJobPropertiesList"]
            )
        )
    else:
        out["import_job_properties_list"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
