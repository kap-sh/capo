"""Generated from Smithy shape ``com.amazonaws.elementalinference#CreateQuestionSetVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.choose_one_question_list
    import capo_elementalinference.types.feed_references
    import capo_elementalinference.types.question_set_arn
    import capo_elementalinference.types.question_set_id
    import capo_elementalinference.types.question_set_sha256
    import capo_elementalinference.types.question_set_version
    import capo_elementalinference.types.question_set_version_description
    import capo_elementalinference.types.resource_name
    import capo_elementalinference.types.tag_map
    import capo_elementalinference.types.yes_no_per_option_question_list
    import capo_elementalinference.types.yes_no_question_list


class CreateQuestionSetVersionResponse(TypedDict, closed=True):
    yes_no: NotRequired[
        "capo_elementalinference.types.yes_no_question_list.YesNoQuestionList"
    ]
    """<p>The yesNo questions in this version. Elemental Inference doesn't return this property if the version has no yesNo questions. </p>"""
    yes_no_per_option: NotRequired[
        "capo_elementalinference.types.yes_no_per_option_question_list.YesNoPerOptionQuestionList"
    ]
    """<p>The yesNoPerOption questions in this version. Elemental Inference doesn't return this property if the version has no yesNoPerOption questions. </p>"""
    choose_one: NotRequired[
        "capo_elementalinference.types.choose_one_question_list.ChooseOneQuestionList"
    ]
    """<p>The chooseOne questions in this version. Elemental Inference doesn't return this property if the version has no chooseOne questions. </p>"""
    arn: "capo_elementalinference.types.question_set_arn.QuestionSetArn"
    """<p>The ARN of the question set.</p>"""
    id: "capo_elementalinference.types.question_set_id.QuestionSetId"
    """<p>The ID of the question set.</p>"""
    name: "capo_elementalinference.types.resource_name.ResourceName"
    """<p>The name of the question set at this version.</p>"""
    version: "capo_elementalinference.types.question_set_version.QuestionSetVersion"
    """<p>The number of the version that Elemental Inference published. If DRAFT hadn't changed since the latest version, this is the number of that existing version. </p>"""
    description: NotRequired[
        "capo_elementalinference.types.question_set_version_description.QuestionSetVersionDescription"
    ]
    """<p>The description of the version. For a new version, this is the description that you specified in the request. If DRAFT hadn't changed since the latest version, this is the description of that existing version. Elemental Inference doesn't return this property if the version has no description. </p>"""
    latest_version: NotRequired[
        "capo_elementalinference.types.question_set_version.QuestionSetVersion"
    ]
    """<p>The number of the highest version that you have published for this question set. It's the same as version. </p>"""
    sha256: "capo_elementalinference.types.question_set_sha256.QuestionSetSha256"
    """<p>The SHA-256 hash of the version, as 64 lowercase hexadecimal characters. It's the same as the hash of the DRAFT version that Elemental Inference published. </p>"""
    references: NotRequired[
        "capo_elementalinference.types.feed_references.FeedReferences"
    ]
    """<p>A list of feed IDs that reference this version of the question set. For a new version, the list is empty. </p>"""
    tags: NotRequired["capo_elementalinference.types.tag_map.TagMap"]
    """<p>Any tags associated with the question set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateQuestionSetVersionResponse) -> dict:
    out: dict = {}
    if "yes_no" in value:
        import capo_elementalinference.types.yes_no_question_list

        out["yesNo"] = (
            capo_elementalinference.types.yes_no_question_list.serialize_json(
                value["yes_no"]
            )
        )
    if "yes_no_per_option" in value:
        import capo_elementalinference.types.yes_no_per_option_question_list

        out["yesNoPerOption"] = (
            capo_elementalinference.types.yes_no_per_option_question_list.serialize_json(
                value["yes_no_per_option"]
            )
        )
    if "choose_one" in value:
        import capo_elementalinference.types.choose_one_question_list

        out["chooseOne"] = (
            capo_elementalinference.types.choose_one_question_list.serialize_json(
                value["choose_one"]
            )
        )
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["version"] = value["version"]
    if "description" in value:
        out["description"] = value["description"]
    if "latest_version" in value:
        out["latestVersion"] = value["latest_version"]
    out["sha256"] = value["sha256"]
    if "references" in value:
        import capo_elementalinference.types.feed_references

        out["references"] = (
            capo_elementalinference.types.feed_references.serialize_json(
                value["references"]
            )
        )
    if "tags" in value:
        import capo_elementalinference.types.tag_map

        out["tags"] = capo_elementalinference.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateQuestionSetVersionResponse:
    out: CreateQuestionSetVersionResponse = {}  # type: ignore[typeddict-item]
    if data.get("yesNo") is not None:
        import capo_elementalinference.types.yes_no_question_list

        out["yes_no"] = (
            capo_elementalinference.types.yes_no_question_list.deserialize_json(
                data["yesNo"]
            )
        )
    if data.get("yesNoPerOption") is not None:
        import capo_elementalinference.types.yes_no_per_option_question_list

        out["yes_no_per_option"] = (
            capo_elementalinference.types.yes_no_per_option_question_list.deserialize_json(
                data["yesNoPerOption"]
            )
        )
    if data.get("chooseOne") is not None:
        import capo_elementalinference.types.choose_one_question_list

        out["choose_one"] = (
            capo_elementalinference.types.choose_one_question_list.deserialize_json(
                data["chooseOne"]
            )
        )
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("latestVersion") is not None:
        out["latest_version"] = data["latestVersion"]
    if data.get("sha256") is not None:
        out["sha256"] = data["sha256"]
    else:
        out["sha256"] = ""
    if data.get("references") is not None:
        import capo_elementalinference.types.feed_references

        out["references"] = (
            capo_elementalinference.types.feed_references.deserialize_json(
                data["references"]
            )
        )
    if data.get("tags") is not None:
        import capo_elementalinference.types.tag_map

        out["tags"] = capo_elementalinference.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
