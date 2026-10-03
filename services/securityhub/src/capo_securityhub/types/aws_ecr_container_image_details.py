"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcrContainerImageDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.non_empty_string_list


class AwsEcrContainerImageDetails(TypedDict, closed=True):
    registry_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Web Services account identifier that is associated with the registry that the image belongs to.</p>"""
    repository_name: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the repository that the image belongs to.</p>"""
    architecture: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The architecture of the image. Valid values are as follows:</p> <ul> <li> <p> <code>arm64</code> </p> </li> <li> <p> <code>i386</code> </p> </li> <li> <p> <code>x86_64</code> </p> </li> </ul>"""
    image_digest: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The sha256 digest of the image manifest.</p>"""
    image_tags: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The list of tags that are associated with the image.</p>"""
    image_published_at: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The date and time when the image was pushed to the repository.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcrContainerImageDetails) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["RegistryId"] = value["registry_id"]
    if "repository_name" in value:
        out["RepositoryName"] = value["repository_name"]
    if "architecture" in value:
        out["Architecture"] = value["architecture"]
    if "image_digest" in value:
        out["ImageDigest"] = value["image_digest"]
    if "image_tags" in value:
        import capo_securityhub.types.non_empty_string_list

        out["ImageTags"] = capo_securityhub.types.non_empty_string_list.serialize_json(
            value["image_tags"]
        )
    if "image_published_at" in value:
        out["ImagePublishedAt"] = value["image_published_at"]
    return out


def deserialize_json(data: dict) -> AwsEcrContainerImageDetails:
    out: AwsEcrContainerImageDetails = {}  # type: ignore[typeddict-item]
    if data.get("RegistryId") is not None:
        out["registry_id"] = data["RegistryId"]
    if data.get("RepositoryName") is not None:
        out["repository_name"] = data["RepositoryName"]
    if data.get("Architecture") is not None:
        out["architecture"] = data["Architecture"]
    if data.get("ImageDigest") is not None:
        out["image_digest"] = data["ImageDigest"]
    if data.get("ImageTags") is not None:
        import capo_securityhub.types.non_empty_string_list

        out["image_tags"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["ImageTags"]
            )
        )
    if data.get("ImagePublishedAt") is not None:
        out["image_published_at"] = data["ImagePublishedAt"]
    return out
