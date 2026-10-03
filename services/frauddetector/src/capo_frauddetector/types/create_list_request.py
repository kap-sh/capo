"""Generated from Smithy shape ``com.amazonaws.frauddetector#CreateListRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_frauddetector.types.description
    import capo_frauddetector.types.elements_list
    import capo_frauddetector.types.no_dash_identifier
    import capo_frauddetector.types.tag_list
    import capo_frauddetector.types.variable_type


class CreateListRequest(TypedDict, closed=True):
    name: "capo_frauddetector.types.no_dash_identifier.noDashIdentifier"
    """<p> The name of the list. </p>"""
    elements: NotRequired["capo_frauddetector.types.elements_list.ElementsList"]
    """<p> The names of the elements, if providing. You can also create an empty list and add elements later using the <a href="https://docs.aws.amazon.com/frauddetector/latest/api/API_Updatelist.html">UpdateList</a> API. </p>"""
    variable_type: NotRequired["capo_frauddetector.types.variable_type.variableType"]
    """<p> The variable type of the list. You can only assign the variable type with String data type. For more information, see <a href="https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types">Variable types</a>. </p>"""
    description: NotRequired["capo_frauddetector.types.description.description"]
    """<p> The description of the list. </p>"""
    tags: NotRequired["capo_frauddetector.types.tag_list.tagList"]
    """<p> A collection of the key and value pairs. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateListRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "elements" in value:
        import capo_frauddetector.types.elements_list

        out["elements"] = capo_frauddetector.types.elements_list.serialize_aws_json_1_1(
            value["elements"]
        )
    if "variable_type" in value:
        out["variableType"] = value["variable_type"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_frauddetector.types.tag_list

        out["tags"] = capo_frauddetector.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateListRequest:
    out: CreateListRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateListRequest.name required")
    if data.get("elements") is not None:
        import capo_frauddetector.types.elements_list

        out["elements"] = (
            capo_frauddetector.types.elements_list.deserialize_aws_json_1_1(
                data["elements"]
            )
        )
    if data.get("variableType") is not None:
        out["variable_type"] = data["variableType"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_frauddetector.types.tag_list

        out["tags"] = capo_frauddetector.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
