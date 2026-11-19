"""Generated from Smithy shape ``com.amazonaws.health#ConfigureTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_health.types.configure_tags_request_tag_key_list


class ConfigureTagsRequest(TypedDict, closed=True):
    tag_keys: "capo_health.types.configure_tags_request_tag_key_list.ConfigureTagsRequestTagKeyList"
    """<p>The list of resource tag keys to configure for Health event tracking.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigureTagsRequest) -> dict:
    out: dict = {}
    import capo_health.types.configure_tags_request_tag_key_list

    out["tagKeys"] = (
        capo_health.types.configure_tags_request_tag_key_list.serialize_aws_json_1_1(
            value["tag_keys"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfigureTagsRequest:
    out: ConfigureTagsRequest = {}  # type: ignore[typeddict-item]
    if data.get("tagKeys") is not None:
        import capo_health.types.configure_tags_request_tag_key_list

        out["tag_keys"] = (
            capo_health.types.configure_tags_request_tag_key_list.deserialize_aws_json_1_1(
                data["tagKeys"]
            )
        )
    else:
        out["tag_keys"] = []
    return out
