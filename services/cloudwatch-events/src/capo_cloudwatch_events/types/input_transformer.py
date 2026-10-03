"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#InputTransformer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_events.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.transformer_input
    import capo_cloudwatch_events.types.transformer_paths


class InputTransformer(TypedDict, closed=True):
    input_paths_map: NotRequired[
        "capo_cloudwatch_events.types.transformer_paths.TransformerPaths"
    ]
    """<p>Map of JSON paths to be extracted from the event. You can then insert these in the template in <code>InputTemplate</code> to produce the output you want to be sent to the target.</p> <p> <code>InputPathsMap</code> is an array key-value pairs, where each value is a valid JSON path. You can have as many as 100 key-value pairs. You must use JSON dot notation, not bracket notation.</p> <p>The keys cannot start with "Amazon Web Services." </p>"""
    input_template: "capo_cloudwatch_events.types.transformer_input.TransformerInput"
    r"""<p>Input template where you specify placeholders that will be filled with the values of the keys from <code>InputPathsMap</code> to customize the data sent to the target. Enclose each <code>InputPathsMaps</code> value in brackets: <<i>value</i>> The InputTemplate must be valid JSON.</p> <p>If <code>InputTemplate</code> is a JSON object (surrounded by curly braces), the following restrictions apply:</p> <ul> <li> <p>The placeholder cannot be used as an object key.</p> </li> </ul> <p>The following example shows the syntax for using <code>InputPathsMap</code> and <code>InputTemplate</code>.</p> <p> <code> "InputTransformer":</code> </p> <p> <code>{</code> </p> <p> <code>"InputPathsMap": {"instance": "$.detail.instance","status": "$.detail.status"},</code> </p> <p> <code>"InputTemplate": "<instance> is in state <status>"</code> </p> <p> <code>}</code> </p> <p>To have the <code>InputTemplate</code> include quote marks within a JSON string, escape each quote marks with a slash, as in the following example:</p> <p> <code> "InputTransformer":</code> </p> <p> <code>{</code> </p> <p> <code>"InputPathsMap": {"instance": "$.detail.instance","status": "$.detail.status"},</code> </p> <p> <code>"InputTemplate": "<instance> is in state \"<status>\""</code> </p> <p> <code>}</code> </p> <p>The <code>InputTemplate</code> can also be valid JSON with varibles in quotes or out, as in the following example:</p> <p> <code> "InputTransformer":</code> </p> <p> <code>{</code> </p> <p> <code>"InputPathsMap": {"instance": "$.detail.instance","status": "$.detail.status"},</code> </p> <p> <code>"InputTemplate": '{"myInstance": <instance>,"myStatus": "<instance> is in state \"<status>\""}'</code> </p> <p> <code>}</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputTransformer) -> dict:
    out: dict = {}
    if "input_paths_map" in value:
        import capo_cloudwatch_events.types.transformer_paths

        out["InputPathsMap"] = (
            capo_cloudwatch_events.types.transformer_paths.serialize_aws_json_1_1(
                value["input_paths_map"]
            )
        )
    out["InputTemplate"] = value["input_template"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InputTransformer:
    out: InputTransformer = {}  # type: ignore[typeddict-item]
    if data.get("InputPathsMap") is not None:
        import capo_cloudwatch_events.types.transformer_paths

        out["input_paths_map"] = (
            capo_cloudwatch_events.types.transformer_paths.deserialize_aws_json_1_1(
                data["InputPathsMap"]
            )
        )
    if data.get("InputTemplate") is not None:
        out["input_template"] = data["InputTemplate"]
    else:
        raise DeserializationError("InputTransformer.input_template required")
    return out
