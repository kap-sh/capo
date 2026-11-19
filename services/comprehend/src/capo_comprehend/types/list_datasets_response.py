"""Generated from Smithy shape ``com.amazonaws.comprehend#ListDatasetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.dataset_properties_list
    import capo_comprehend.types.string


class ListDatasetsResponse(TypedDict, closed=True):
    dataset_properties_list: NotRequired[
        "capo_comprehend.types.dataset_properties_list.DatasetPropertiesList"
    ]
    """<p>The dataset properties list.</p>"""
    next_token: NotRequired["capo_comprehend.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDatasetsResponse) -> dict:
    out: dict = {}
    if "dataset_properties_list" in value:
        import capo_comprehend.types.dataset_properties_list

        out["DatasetPropertiesList"] = (
            capo_comprehend.types.dataset_properties_list.serialize_aws_json_1_1(
                value["dataset_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDatasetsResponse:
    out: ListDatasetsResponse = {}  # type: ignore[typeddict-item]
    if data.get("DatasetPropertiesList") is not None:
        import capo_comprehend.types.dataset_properties_list

        out["dataset_properties_list"] = (
            capo_comprehend.types.dataset_properties_list.deserialize_aws_json_1_1(
                data["DatasetPropertiesList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListDatasetsResponse) -> dict:
    out: dict = {}
    if "dataset_properties_list" in value:
        import capo_comprehend.types.dataset_properties_list

        out["DatasetPropertiesList"] = (
            capo_comprehend.types.dataset_properties_list.serialize_cbor(
                value["dataset_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListDatasetsResponse:
    out: ListDatasetsResponse = {}  # type: ignore[typeddict-item]
    if data.get("DatasetPropertiesList") is not None:
        import capo_comprehend.types.dataset_properties_list

        out["dataset_properties_list"] = (
            capo_comprehend.types.dataset_properties_list.deserialize_cbor(
                data["DatasetPropertiesList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
