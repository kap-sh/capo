"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestSetImportResourceSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.description
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.role_arn
    import capo_lex_models_v2.types.tag_map
    import capo_lex_models_v2.types.test_set_import_input_location
    import capo_lex_models_v2.types.test_set_modality
    import capo_lex_models_v2.types.test_set_storage_location


class TestSetImportResourceSpecification(TypedDict, closed=True):
    test_set_name: "capo_lex_models_v2.types.name.Name"
    """<p>The name of the test set.</p>"""
    description: NotRequired["capo_lex_models_v2.types.description.Description"]
    """<p>The description of the test set.</p>"""
    role_arn: "capo_lex_models_v2.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of an IAM role that has permission to access the test set.</p>"""
    storage_location: (
        "capo_lex_models_v2.types.test_set_storage_location.TestSetStorageLocation"
    )
    """<p>Contains information about the location that Amazon Lex uses to store the test-set.</p>"""
    import_input_location: "capo_lex_models_v2.types.test_set_import_input_location.TestSetImportInputLocation"
    """<p>Contains information about the input location from where test-set should be imported.</p>"""
    modality: "capo_lex_models_v2.types.test_set_modality.TestSetModality"
    """<p>Specifies whether the test-set being imported contains written or spoken data.</p>"""
    test_set_tags: NotRequired["capo_lex_models_v2.types.tag_map.TagMap"]
    """<p>A list of tags to add to the test set. You can only add tags when you import/generate a new test set. You can't use the <code>UpdateTestSet</code> operation to update tags. To update tags, use the <code>TagResource</code> operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestSetImportResourceSpecification) -> dict:
    out: dict = {}
    out["testSetName"] = value["test_set_name"]
    if "description" in value:
        out["description"] = value["description"]
    out["roleArn"] = value["role_arn"]
    import capo_lex_models_v2.types.test_set_storage_location

    out["storageLocation"] = (
        capo_lex_models_v2.types.test_set_storage_location.serialize_json(
            value["storage_location"]
        )
    )
    import capo_lex_models_v2.types.test_set_import_input_location

    out["importInputLocation"] = (
        capo_lex_models_v2.types.test_set_import_input_location.serialize_json(
            value["import_input_location"]
        )
    )
    import capo_lex_models_v2.types.test_set_modality

    out["modality"] = capo_lex_models_v2.types.test_set_modality.serialize_json(
        value["modality"]
    )
    if "test_set_tags" in value:
        import capo_lex_models_v2.types.tag_map

        out["testSetTags"] = capo_lex_models_v2.types.tag_map.serialize_json(
            value["test_set_tags"]
        )
    return out


def deserialize_json(data: dict) -> TestSetImportResourceSpecification:
    out: TestSetImportResourceSpecification = {}  # type: ignore[typeddict-item]
    if data.get("testSetName") is not None:
        out["test_set_name"] = data["testSetName"]
    else:
        out["test_set_name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("storageLocation") is not None:
        import capo_lex_models_v2.types.test_set_storage_location

        out["storage_location"] = (
            capo_lex_models_v2.types.test_set_storage_location.deserialize_json(
                data["storageLocation"]
            )
        )
    else:
        raise DeserializationError(
            "TestSetImportResourceSpecification.storage_location required"
        )
    if data.get("importInputLocation") is not None:
        import capo_lex_models_v2.types.test_set_import_input_location

        out["import_input_location"] = (
            capo_lex_models_v2.types.test_set_import_input_location.deserialize_json(
                data["importInputLocation"]
            )
        )
    else:
        raise DeserializationError(
            "TestSetImportResourceSpecification.import_input_location required"
        )
    if data.get("modality") is not None:
        import capo_lex_models_v2.types.test_set_modality

        out["modality"] = capo_lex_models_v2.types.test_set_modality.deserialize_json(
            data["modality"]
        )
    else:
        import typing

        out["modality"] = typing.cast(
            "capo_lex_models_v2.types.test_set_modality.TestSetModality", ""
        )
    if data.get("testSetTags") is not None:
        import capo_lex_models_v2.types.tag_map

        out["test_set_tags"] = capo_lex_models_v2.types.tag_map.deserialize_json(
            data["testSetTags"]
        )
    return out
