"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityTypesListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.entity_type_name


class EntityTypesListItem(TypedDict, closed=True):
    type: "capo_comprehend.types.entity_type_name.EntityTypeName"
    r"""<p>An entity type within a labeled training dataset that Amazon Comprehend uses to train a custom entity recognizer.</p> <p>Entity types must not contain the following invalid characters: \n (line break), \\n (escaped line break, \r (carriage return), \\r (escaped carriage return), \t (tab), \\t (escaped tab), and , (comma).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityTypesListItem) -> dict:
    out: dict = {}
    out["Type"] = value["type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityTypesListItem:
    out: EntityTypesListItem = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    else:
        out["type"] = ""
    return out
