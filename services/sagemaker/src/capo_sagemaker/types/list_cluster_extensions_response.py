"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListClusterExtensionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.extension_summaries
    import capo_sagemaker.types.next_token


class ListClusterExtensionsResponse(TypedDict, closed=True):
    extensions: NotRequired[
        "capo_sagemaker.types.extension_summaries.ExtensionSummaries"
    ]
    """<p>The list of extensions installed on the cluster.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>The next token specified for listing extensions on a SageMaker HyperPod cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListClusterExtensionsResponse) -> dict:
    out: dict = {}
    if "extensions" in value:
        import capo_sagemaker.types.extension_summaries

        out["Extensions"] = (
            capo_sagemaker.types.extension_summaries.serialize_aws_json_1_1(
                value["extensions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListClusterExtensionsResponse:
    out: ListClusterExtensionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Extensions") is not None:
        import capo_sagemaker.types.extension_summaries

        out["extensions"] = (
            capo_sagemaker.types.extension_summaries.deserialize_aws_json_1_1(
                data["Extensions"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
