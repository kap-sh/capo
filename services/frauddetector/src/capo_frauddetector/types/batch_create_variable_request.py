"""Generated from Smithy shape ``com.amazonaws.frauddetector#BatchCreateVariableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.tag_list
    import capo_frauddetector.types.variable_entry_list


class BatchCreateVariableRequest(TypedDict, closed=True):
    variable_entries: "capo_frauddetector.types.variable_entry_list.VariableEntryList"
    """<p>The list of variables for the batch create variable request.</p>"""
    tags: NotRequired["capo_frauddetector.types.tag_list.tagList"]
    """<p>A collection of key and value pairs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchCreateVariableRequest) -> dict:
    out: dict = {}
    import capo_frauddetector.types.variable_entry_list

    out["variableEntries"] = (
        capo_frauddetector.types.variable_entry_list.serialize_aws_json_1_1(
            value["variable_entries"]
        )
    )
    if "tags" in value:
        import capo_frauddetector.types.tag_list

        out["tags"] = capo_frauddetector.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchCreateVariableRequest:
    out: BatchCreateVariableRequest = {}  # type: ignore[typeddict-item]
    if data.get("variableEntries") is not None:
        import capo_frauddetector.types.variable_entry_list

        out["variable_entries"] = (
            capo_frauddetector.types.variable_entry_list.deserialize_aws_json_1_1(
                data["variableEntries"]
            )
        )
    else:
        out["variable_entries"] = []
    if data.get("tags") is not None:
        import capo_frauddetector.types.tag_list

        out["tags"] = capo_frauddetector.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
