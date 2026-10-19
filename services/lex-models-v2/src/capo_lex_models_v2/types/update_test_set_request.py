"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UpdateTestSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.description
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.name


class UpdateTestSetRequest(TypedDict, closed=True):
    test_set_id: "capo_lex_models_v2.types.id.Id"
    """<p>The test set Id for which update test operation to be performed.</p>"""
    test_set_name: "capo_lex_models_v2.types.name.Name"
    """<p>The new test set name.</p>"""
    description: NotRequired["capo_lex_models_v2.types.description.Description"]
    """<p>The new test set description.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTestSetRequest) -> dict:
    out: dict = {}
    out["testSetName"] = value["test_set_name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateTestSetRequest:
    out: UpdateTestSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("testSetName") is not None:
        out["test_set_name"] = data["testSetName"]
    else:
        out["test_set_name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
