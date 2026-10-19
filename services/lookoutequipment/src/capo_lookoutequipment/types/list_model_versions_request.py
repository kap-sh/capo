"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ListModelVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.max_results
    import capo_lookoutequipment.types.model_name
    import capo_lookoutequipment.types.model_version
    import capo_lookoutequipment.types.model_version_source_type
    import capo_lookoutequipment.types.model_version_status
    import capo_lookoutequipment.types.next_token
    import capo_lookoutequipment.types.timestamp


class ListModelVersionsRequest(TypedDict, closed=True):
    model_name: "capo_lookoutequipment.types.model_name.ModelName"
    """<p>Then name of the machine learning model for which the model versions are to be listed.</p>"""
    next_token: NotRequired["capo_lookoutequipment.types.next_token.NextToken"]
    """<p>If the total number of results exceeds the limit that the response can display, the response returns an opaque pagination token indicating where to continue the listing of machine learning model versions. Use this token in the <code>NextToken</code> field in the request to list the next page of results.</p>"""
    max_results: NotRequired["capo_lookoutequipment.types.max_results.MaxResults"]
    """<p>Specifies the maximum number of machine learning model versions to list.</p>"""
    status: NotRequired[
        "capo_lookoutequipment.types.model_version_status.ModelVersionStatus"
    ]
    """<p>Filter the results based on the current status of the model version.</p>"""
    source_type: NotRequired[
        "capo_lookoutequipment.types.model_version_source_type.ModelVersionSourceType"
    ]
    """<p>Filter the results based on the way the model version was generated.</p>"""
    created_at_end_time: NotRequired["capo_lookoutequipment.types.timestamp.Timestamp"]
    """<p>Filter results to return all the model versions created before this time.</p>"""
    created_at_start_time: NotRequired[
        "capo_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>Filter results to return all the model versions created after this time.</p>"""
    max_model_version: NotRequired[
        "capo_lookoutequipment.types.model_version.ModelVersion"
    ]
    """<p>Specifies the highest version of the model to return in the list.</p>"""
    min_model_version: NotRequired[
        "capo_lookoutequipment.types.model_version.ModelVersion"
    ]
    """<p>Specifies the lowest version of the model to return in the list.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListModelVersionsRequest) -> dict:
    out: dict = {}
    out["ModelName"] = value["model_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "status" in value:
        import capo_lookoutequipment.types.model_version_status

        out["Status"] = (
            capo_lookoutequipment.types.model_version_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "source_type" in value:
        import capo_lookoutequipment.types.model_version_source_type

        out["SourceType"] = (
            capo_lookoutequipment.types.model_version_source_type.serialize_aws_json_1_0(
                value["source_type"]
            )
        )
    if "created_at_end_time" in value:
        import capo_lookoutequipment.types.timestamp

        out["CreatedAtEndTime"] = (
            capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["created_at_end_time"]
            )
        )
    if "created_at_start_time" in value:
        import capo_lookoutequipment.types.timestamp

        out["CreatedAtStartTime"] = (
            capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["created_at_start_time"]
            )
        )
    if "max_model_version" in value:
        out["MaxModelVersion"] = value["max_model_version"]
    if "min_model_version" in value:
        out["MinModelVersion"] = value["min_model_version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListModelVersionsRequest:
    out: ListModelVersionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ModelName") is not None:
        out["model_name"] = data["ModelName"]
    else:
        out["model_name"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("Status") is not None:
        import capo_lookoutequipment.types.model_version_status

        out["status"] = (
            capo_lookoutequipment.types.model_version_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if data.get("SourceType") is not None:
        import capo_lookoutequipment.types.model_version_source_type

        out["source_type"] = (
            capo_lookoutequipment.types.model_version_source_type.deserialize_aws_json_1_0(
                data["SourceType"]
            )
        )
    if data.get("CreatedAtEndTime") is not None:
        import capo_lookoutequipment.types.timestamp

        out["created_at_end_time"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["CreatedAtEndTime"]
            )
        )
    if data.get("CreatedAtStartTime") is not None:
        import capo_lookoutequipment.types.timestamp

        out["created_at_start_time"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["CreatedAtStartTime"]
            )
        )
    if data.get("MaxModelVersion") is not None:
        out["max_model_version"] = data["MaxModelVersion"]
    if data.get("MinModelVersion") is not None:
        out["min_model_version"] = data["MinModelVersion"]
    return out
