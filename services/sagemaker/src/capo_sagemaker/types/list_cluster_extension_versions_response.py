"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListClusterExtensionVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.extension_version_summaries
    import capo_sagemaker.types.next_token


class ListClusterExtensionVersionsResponse(TypedDict, closed=True):
    extension_versions: NotRequired[
        "capo_sagemaker.types.extension_version_summaries.ExtensionVersionSummaries"
    ]
    """<p>The versions of the extension that you can install, from the highest version to the lowest.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, a token that you can use in the next request to retrieve the next set of versions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListClusterExtensionVersionsResponse) -> dict:
    out: dict = {}
    if "extension_versions" in value:
        import capo_sagemaker.types.extension_version_summaries

        out["ExtensionVersions"] = (
            capo_sagemaker.types.extension_version_summaries.serialize_aws_json_1_1(
                value["extension_versions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListClusterExtensionVersionsResponse:
    out: ListClusterExtensionVersionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ExtensionVersions") is not None:
        import capo_sagemaker.types.extension_version_summaries

        out["extension_versions"] = (
            capo_sagemaker.types.extension_version_summaries.deserialize_aws_json_1_1(
                data["ExtensionVersions"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
