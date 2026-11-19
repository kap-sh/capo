"""Generated from Smithy shape ``com.amazonaws.translate#ListParallelDataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_translate.types.next_token
    import capo_translate.types.parallel_data_properties_list


class ListParallelDataResponse(TypedDict, closed=True):
    parallel_data_properties_list: NotRequired[
        "capo_translate.types.parallel_data_properties_list.ParallelDataPropertiesList"
    ]
    """<p>The properties of the parallel data resources returned by this request.</p>"""
    next_token: NotRequired["capo_translate.types.next_token.NextToken"]
    """<p>The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListParallelDataResponse) -> dict:
    out: dict = {}
    if "parallel_data_properties_list" in value:
        import capo_translate.types.parallel_data_properties_list

        out["ParallelDataPropertiesList"] = (
            capo_translate.types.parallel_data_properties_list.serialize_aws_json_1_1(
                value["parallel_data_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListParallelDataResponse:
    out: ListParallelDataResponse = {}  # type: ignore[typeddict-item]
    if data.get("ParallelDataPropertiesList") is not None:
        import capo_translate.types.parallel_data_properties_list

        out["parallel_data_properties_list"] = (
            capo_translate.types.parallel_data_properties_list.deserialize_aws_json_1_1(
                data["ParallelDataPropertiesList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListParallelDataResponse) -> dict:
    out: dict = {}
    if "parallel_data_properties_list" in value:
        import capo_translate.types.parallel_data_properties_list

        out["ParallelDataPropertiesList"] = (
            capo_translate.types.parallel_data_properties_list.serialize_cbor(
                value["parallel_data_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListParallelDataResponse:
    out: ListParallelDataResponse = {}  # type: ignore[typeddict-item]
    if data.get("ParallelDataPropertiesList") is not None:
        import capo_translate.types.parallel_data_properties_list

        out["parallel_data_properties_list"] = (
            capo_translate.types.parallel_data_properties_list.deserialize_cbor(
                data["ParallelDataPropertiesList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
