"""Generated from Smithy shape ``com.amazonaws.health#ConfigureTagsForOrganizationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_health.types.configure_tags_for_organization_tag_key_list


class ConfigureTagsForOrganizationRequest(TypedDict, closed=True):
    tag_keys: "capo_health.types.configure_tags_for_organization_tag_key_list.ConfigureTagsForOrganizationTagKeyList"
    """<p>The list of tag keys to configure for Health event tracking across the organization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigureTagsForOrganizationRequest) -> dict:
    out: dict = {}
    import capo_health.types.configure_tags_for_organization_tag_key_list

    out["tagKeys"] = (
        capo_health.types.configure_tags_for_organization_tag_key_list.serialize_aws_json_1_1(
            value["tag_keys"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfigureTagsForOrganizationRequest:
    out: ConfigureTagsForOrganizationRequest = {}  # type: ignore[typeddict-item]
    if data.get("tagKeys") is not None:
        import capo_health.types.configure_tags_for_organization_tag_key_list

        out["tag_keys"] = (
            capo_health.types.configure_tags_for_organization_tag_key_list.deserialize_aws_json_1_1(
                data["tagKeys"]
            )
        )
    else:
        out["tag_keys"] = []
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConfigureTagsForOrganizationRequest) -> dict:
    out: dict = {}
    import capo_health.types.configure_tags_for_organization_tag_key_list

    out["tagKeys"] = (
        capo_health.types.configure_tags_for_organization_tag_key_list.serialize_cbor(
            value["tag_keys"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> ConfigureTagsForOrganizationRequest:
    out: ConfigureTagsForOrganizationRequest = {}  # type: ignore[typeddict-item]
    if data.get("tagKeys") is not None:
        import capo_health.types.configure_tags_for_organization_tag_key_list

        out["tag_keys"] = (
            capo_health.types.configure_tags_for_organization_tag_key_list.deserialize_cbor(
                data["tagKeys"]
            )
        )
    else:
        out["tag_keys"] = []
    return out
