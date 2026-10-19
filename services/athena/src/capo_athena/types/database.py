"""Generated from Smithy shape ``com.amazonaws.athena#Database``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.description_string
    import capo_athena.types.name_string
    import capo_athena.types.parameters_map


class Database(TypedDict, closed=True):
    name: "capo_athena.types.name_string.NameString"
    """<p>The name of the database.</p>"""
    description: NotRequired["capo_athena.types.description_string.DescriptionString"]
    """<p>An optional description of the database.</p>"""
    parameters: NotRequired["capo_athena.types.parameters_map.ParametersMap"]
    """<p>A set of custom key/value pairs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Database) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "parameters" in value:
        import capo_athena.types.parameters_map

        out["Parameters"] = capo_athena.types.parameters_map.serialize_aws_json_1_1(
            value["parameters"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Database:
    out: Database = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Parameters") is not None:
        import capo_athena.types.parameters_map

        out["parameters"] = capo_athena.types.parameters_map.deserialize_aws_json_1_1(
            data["Parameters"]
        )
    return out
