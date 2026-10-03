"""Generated from Smithy shape ``com.amazonaws.translate#ImportTerminologyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_translate.errors import DeserializationError

if TYPE_CHECKING:
    import capo_translate.types.description
    import capo_translate.types.encryption_key
    import capo_translate.types.merge_strategy
    import capo_translate.types.resource_name
    import capo_translate.types.tag_list
    import capo_translate.types.terminology_data


class ImportTerminologyRequest(TypedDict, closed=True):
    name: "capo_translate.types.resource_name.ResourceName"
    """<p>The name of the custom terminology being imported.</p>"""
    merge_strategy: "capo_translate.types.merge_strategy.MergeStrategy"
    """<p>The merge strategy of the custom terminology being imported. Currently, only the OVERWRITE merge strategy is supported. In this case, the imported terminology will overwrite an existing terminology of the same name.</p>"""
    description: NotRequired["capo_translate.types.description.Description"]
    """<p>The description of the custom terminology being imported.</p>"""
    terminology_data: "capo_translate.types.terminology_data.TerminologyData"
    """<p>The terminology data for the custom terminology being imported.</p>"""
    encryption_key: NotRequired["capo_translate.types.encryption_key.EncryptionKey"]
    """<p>The encryption key for the custom terminology being imported.</p>"""
    tags: NotRequired["capo_translate.types.tag_list.TagList"]
    """<p>Tags to be associated with this resource. A tag is a key-value pair that adds metadata to a resource. Each tag key for the resource must be unique. For more information, see <a href="https://docs.aws.amazon.com/translate/latest/dg/tagging.html"> Tagging your resources</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportTerminologyRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_translate.types.merge_strategy

    out["MergeStrategy"] = capo_translate.types.merge_strategy.serialize_aws_json_1_1(
        value["merge_strategy"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    import capo_translate.types.terminology_data

    out["TerminologyData"] = (
        capo_translate.types.terminology_data.serialize_aws_json_1_1(
            value["terminology_data"]
        )
    )
    if "encryption_key" in value:
        import capo_translate.types.encryption_key

        out["EncryptionKey"] = (
            capo_translate.types.encryption_key.serialize_aws_json_1_1(
                value["encryption_key"]
            )
        )
    if "tags" in value:
        import capo_translate.types.tag_list

        out["Tags"] = capo_translate.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportTerminologyRequest:
    out: ImportTerminologyRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ImportTerminologyRequest.name required")
    if data.get("MergeStrategy") is not None:
        import capo_translate.types.merge_strategy

        out["merge_strategy"] = (
            capo_translate.types.merge_strategy.deserialize_aws_json_1_1(
                data["MergeStrategy"]
            )
        )
    else:
        raise DeserializationError("ImportTerminologyRequest.merge_strategy required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("TerminologyData") is not None:
        import capo_translate.types.terminology_data

        out["terminology_data"] = (
            capo_translate.types.terminology_data.deserialize_aws_json_1_1(
                data["TerminologyData"]
            )
        )
    else:
        raise DeserializationError("ImportTerminologyRequest.terminology_data required")
    if data.get("EncryptionKey") is not None:
        import capo_translate.types.encryption_key

        out["encryption_key"] = (
            capo_translate.types.encryption_key.deserialize_aws_json_1_1(
                data["EncryptionKey"]
            )
        )
    if data.get("Tags") is not None:
        import capo_translate.types.tag_list

        out["tags"] = capo_translate.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
