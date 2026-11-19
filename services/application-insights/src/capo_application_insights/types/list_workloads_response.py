"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ListWorkloadsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_insights.types.pagination_token
    import capo_application_insights.types.workload_list


class ListWorkloadsResponse(TypedDict, closed=True):
    workload_list: NotRequired[
        "capo_application_insights.types.workload_list.WorkloadList"
    ]
    """<p>The list of workloads.</p>"""
    next_token: NotRequired[
        "capo_application_insights.types.pagination_token.PaginationToken"
    ]
    """<p>The token to request the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListWorkloadsResponse) -> dict:
    out: dict = {}
    if "workload_list" in value:
        import capo_application_insights.types.workload_list

        out["WorkloadList"] = (
            capo_application_insights.types.workload_list.serialize_aws_json_1_1(
                value["workload_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListWorkloadsResponse:
    out: ListWorkloadsResponse = {}  # type: ignore[typeddict-item]
    if data.get("WorkloadList") is not None:
        import capo_application_insights.types.workload_list

        out["workload_list"] = (
            capo_application_insights.types.workload_list.deserialize_aws_json_1_1(
                data["WorkloadList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListWorkloadsResponse) -> dict:
    out: dict = {}
    if "workload_list" in value:
        import capo_application_insights.types.workload_list

        out["WorkloadList"] = (
            capo_application_insights.types.workload_list.serialize_cbor(
                value["workload_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListWorkloadsResponse:
    out: ListWorkloadsResponse = {}  # type: ignore[typeddict-item]
    if data.get("WorkloadList") is not None:
        import capo_application_insights.types.workload_list

        out["workload_list"] = (
            capo_application_insights.types.workload_list.deserialize_cbor(
                data["WorkloadList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
