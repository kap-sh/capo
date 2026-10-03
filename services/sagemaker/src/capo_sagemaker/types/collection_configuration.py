"""Generated from Smithy shape ``com.amazonaws.sagemaker#CollectionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.collection_name
    import capo_sagemaker.types.collection_parameters


class CollectionConfiguration(TypedDict, closed=True):
    collection_name: NotRequired["capo_sagemaker.types.collection_name.CollectionName"]
    """<p>The name of the tensor collection. The name must be unique relative to other rule configuration names.</p>"""
    collection_parameters: NotRequired[
        "capo_sagemaker.types.collection_parameters.CollectionParameters"
    ]
    """<p>Parameter values for the tensor collection. The allowed parameters are <code>"name"</code>, <code>"include_regex"</code>, <code>"reduction_config"</code>, <code>"save_config"</code>, <code>"tensor_names"</code>, and <code>"save_histogram"</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CollectionConfiguration) -> dict:
    out: dict = {}
    if "collection_name" in value:
        out["CollectionName"] = value["collection_name"]
    if "collection_parameters" in value:
        import capo_sagemaker.types.collection_parameters

        out["CollectionParameters"] = (
            capo_sagemaker.types.collection_parameters.serialize_aws_json_1_1(
                value["collection_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CollectionConfiguration:
    out: CollectionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("CollectionName") is not None:
        out["collection_name"] = data["CollectionName"]
    if data.get("CollectionParameters") is not None:
        import capo_sagemaker.types.collection_parameters

        out["collection_parameters"] = (
            capo_sagemaker.types.collection_parameters.deserialize_aws_json_1_1(
                data["CollectionParameters"]
            )
        )
    return out
