"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#StartTestSetGenerationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.description
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.role_arn
    import capo_lex_models_v2.types.tag_map
    import capo_lex_models_v2.types.test_set_generation_data_source
    import capo_lex_models_v2.types.test_set_storage_location


class StartTestSetGenerationRequest(TypedDict, closed=True):
    test_set_name: "capo_lex_models_v2.types.name.Name"
    """<p>The test set name for the test set generation request.</p>"""
    description: NotRequired["capo_lex_models_v2.types.description.Description"]
    """<p>The test set description for the test set generation request.</p>"""
    storage_location: (
        "capo_lex_models_v2.types.test_set_storage_location.TestSetStorageLocation"
    )
    """<p>The Amazon S3 storage location for the test set generation.</p>"""
    generation_data_source: "capo_lex_models_v2.types.test_set_generation_data_source.TestSetGenerationDataSource"
    """<p>The data source for the test set generation.</p>"""
    role_arn: "capo_lex_models_v2.types.role_arn.RoleArn"
    """<p>The roleARN used for any operation in the test set to access resources in the Amazon Web Services account.</p>"""
    test_set_tags: NotRequired["capo_lex_models_v2.types.tag_map.TagMap"]
    """<p>A list of tags to add to the test set. You can only add tags when you import/generate a new test set. You can't use the <code>UpdateTestSet</code> operation to update tags. To update tags, use the <code>TagResource</code> operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartTestSetGenerationRequest) -> dict:
    out: dict = {}
    out["testSetName"] = value["test_set_name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_lex_models_v2.types.test_set_storage_location

    out["storageLocation"] = (
        capo_lex_models_v2.types.test_set_storage_location.serialize_json(
            value["storage_location"]
        )
    )
    import capo_lex_models_v2.types.test_set_generation_data_source

    out["generationDataSource"] = (
        capo_lex_models_v2.types.test_set_generation_data_source.serialize_json(
            value["generation_data_source"]
        )
    )
    out["roleArn"] = value["role_arn"]
    if "test_set_tags" in value:
        import capo_lex_models_v2.types.tag_map

        out["testSetTags"] = capo_lex_models_v2.types.tag_map.serialize_json(
            value["test_set_tags"]
        )
    return out


def deserialize_json(data: dict) -> StartTestSetGenerationRequest:
    out: StartTestSetGenerationRequest = {}  # type: ignore[typeddict-item]
    if data.get("testSetName") is not None:
        out["test_set_name"] = data["testSetName"]
    else:
        out["test_set_name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("storageLocation") is not None:
        import capo_lex_models_v2.types.test_set_storage_location

        out["storage_location"] = (
            capo_lex_models_v2.types.test_set_storage_location.deserialize_json(
                data["storageLocation"]
            )
        )
    else:
        raise DeserializationError(
            "StartTestSetGenerationRequest.storage_location required"
        )
    if data.get("generationDataSource") is not None:
        import capo_lex_models_v2.types.test_set_generation_data_source

        out["generation_data_source"] = (
            capo_lex_models_v2.types.test_set_generation_data_source.deserialize_json(
                data["generationDataSource"]
            )
        )
    else:
        raise DeserializationError(
            "StartTestSetGenerationRequest.generation_data_source required"
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("testSetTags") is not None:
        import capo_lex_models_v2.types.tag_map

        out["test_set_tags"] = capo_lex_models_v2.types.tag_map.deserialize_json(
            data["testSetTags"]
        )
    return out
