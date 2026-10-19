"""Generated from Smithy shape ``com.amazonaws.frauddetector#UpdateListRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.description
    import capo_frauddetector.types.elements_list
    import capo_frauddetector.types.list_update_mode
    import capo_frauddetector.types.no_dash_identifier
    import capo_frauddetector.types.variable_type


class UpdateListRequest(TypedDict, closed=True):
    name: "capo_frauddetector.types.no_dash_identifier.noDashIdentifier"
    """<p> The name of the list to update. </p>"""
    elements: NotRequired["capo_frauddetector.types.elements_list.ElementsList"]
    """<p> One or more list elements to add or replace. If you are providing the elements, make sure to specify the <code>updateMode</code> to use. </p> <p>If you are deleting all elements from the list, use <code>REPLACE</code> for the <code>updateMode</code> and provide an empty list (0 elements).</p>"""
    description: NotRequired["capo_frauddetector.types.description.description"]
    """<p> The new description. </p>"""
    update_mode: NotRequired["capo_frauddetector.types.list_update_mode.ListUpdateMode"]
    """<p> The update mode (type). </p> <ul> <li> <p>Use <code>APPEND</code> if you are adding elements to the list.</p> </li> <li> <p>Use <code>REPLACE</code> if you replacing existing elements in the list.</p> </li> <li> <p>Use <code>REMOVE</code> if you are removing elements from the list.</p> </li> </ul>"""
    variable_type: NotRequired["capo_frauddetector.types.variable_type.variableType"]
    """<p> The variable type you want to assign to the list. </p> <note> <p>You cannot update a variable type of a list that already has a variable type assigned to it. You can assign a variable type to a list only if the list does not already have a variable type.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateListRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "elements" in value:
        import capo_frauddetector.types.elements_list

        out["elements"] = capo_frauddetector.types.elements_list.serialize_aws_json_1_1(
            value["elements"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "update_mode" in value:
        import capo_frauddetector.types.list_update_mode

        out["updateMode"] = (
            capo_frauddetector.types.list_update_mode.serialize_aws_json_1_1(
                value["update_mode"]
            )
        )
    if "variable_type" in value:
        out["variableType"] = value["variable_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateListRequest:
    out: UpdateListRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("elements") is not None:
        import capo_frauddetector.types.elements_list

        out["elements"] = (
            capo_frauddetector.types.elements_list.deserialize_aws_json_1_1(
                data["elements"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("updateMode") is not None:
        import capo_frauddetector.types.list_update_mode

        out["update_mode"] = (
            capo_frauddetector.types.list_update_mode.deserialize_aws_json_1_1(
                data["updateMode"]
            )
        )
    if data.get("variableType") is not None:
        out["variable_type"] = data["variableType"]
    return out


def redact_sensitive(value: UpdateListRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "elements" in value:
        import capo_frauddetector.types.elements_list

        out["elements"] = capo_frauddetector.types.elements_list.redact_sensitive(
            value["elements"]
        )
    return out
