"""Generated from Smithy shape ``com.amazonaws.imagebuilder#CreateDistributionConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_imagebuilder.types.boolean
    import capo_imagebuilder.types.client_token
    import capo_imagebuilder.types.distribution_list
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.resource_name
    import capo_imagebuilder.types.tag_map


class CreateDistributionConfigurationRequest(TypedDict, closed=True):
    name: "capo_imagebuilder.types.resource_name.ResourceName"
    """<p>The name of the distribution configuration. Distribution configuration names must be unique to your account in each Amazon Web Services Region. Image Builder generates the distribution configuration ARN from a normalized form of the name, so names that differ only in case, spaces, or underscores count as the same name.</p>"""
    description: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The description of the distribution configuration.</p>"""
    distributions: "capo_imagebuilder.types.distribution_list.DistributionList"
    """<p>The distribution settings for the configuration. Each entry defines how output images are distributed in one target Amazon Web Services Region. A Region can appear at most once in the list.</p>"""
    tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>The tags of the distribution configuration.</p>"""
    client_token: "capo_imagebuilder.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""
    dry_run: "capo_imagebuilder.types.boolean.Boolean"
    """<p>Validates the required permissions and request parameters without performing the operation. If validation succeeds, the operation returns a <code>DryRunOperationException</code> error response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDistributionConfigurationRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_imagebuilder.types.distribution_list

    out["distributions"] = capo_imagebuilder.types.distribution_list.serialize_json(
        value["distributions"]
    )
    if "tags" in value:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.serialize_json(value["tags"])
    out["clientToken"] = value["client_token"]
    out["dryRun"] = value.get("dry_run", False)
    return out


def deserialize_json(data: dict) -> CreateDistributionConfigurationRequest:
    out: CreateDistributionConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "CreateDistributionConfigurationRequest.name required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("distributions") is not None:
        import capo_imagebuilder.types.distribution_list

        out["distributions"] = (
            capo_imagebuilder.types.distribution_list.deserialize_json(
                data["distributions"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDistributionConfigurationRequest.distributions required"
        )
    if data.get("tags") is not None:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError(
            "CreateDistributionConfigurationRequest.client_token required"
        )
    if data.get("dryRun") is not None:
        out["dry_run"] = data["dryRun"]
    else:
        out["dry_run"] = False
    return out
