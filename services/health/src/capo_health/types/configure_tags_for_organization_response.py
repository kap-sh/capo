"""Generated from Smithy shape ``com.amazonaws.health#ConfigureTagsForOrganizationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.configure_tags_for_organization_response_tag_key_list


class ConfigureTagsForOrganizationResponse(TypedDict, closed=True):
    configured_tag_keys: NotRequired[
        "capo_health.types.configure_tags_for_organization_response_tag_key_list.ConfigureTagsForOrganizationResponseTagKeyList"
    ]
    """<p>The list of tag keys that were successfully configured for the organization, with the current status of each tag key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigureTagsForOrganizationResponse) -> dict:
    out: dict = {}
    if "configured_tag_keys" in value:
        import capo_health.types.configure_tags_for_organization_response_tag_key_list

        out["configuredTagKeys"] = (
            capo_health.types.configure_tags_for_organization_response_tag_key_list.serialize_aws_json_1_1(
                value["configured_tag_keys"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfigureTagsForOrganizationResponse:
    out: ConfigureTagsForOrganizationResponse = {}  # type: ignore[typeddict-item]
    if data.get("configuredTagKeys") is not None:
        import capo_health.types.configure_tags_for_organization_response_tag_key_list

        out["configured_tag_keys"] = (
            capo_health.types.configure_tags_for_organization_response_tag_key_list.deserialize_aws_json_1_1(
                data["configuredTagKeys"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConfigureTagsForOrganizationResponse) -> dict:
    out: dict = {}
    if "configured_tag_keys" in value:
        import capo_health.types.configure_tags_for_organization_response_tag_key_list

        out["configuredTagKeys"] = (
            capo_health.types.configure_tags_for_organization_response_tag_key_list.serialize_cbor(
                value["configured_tag_keys"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ConfigureTagsForOrganizationResponse:
    out: ConfigureTagsForOrganizationResponse = {}  # type: ignore[typeddict-item]
    if data.get("configuredTagKeys") is not None:
        import capo_health.types.configure_tags_for_organization_response_tag_key_list

        out["configured_tag_keys"] = (
            capo_health.types.configure_tags_for_organization_response_tag_key_list.deserialize_cbor(
                data["configuredTagKeys"]
            )
        )
    return out
