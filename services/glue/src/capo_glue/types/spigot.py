"""Generated from Smithy shape ``com.amazonaws.glue#Spigot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.node_name
    import capo_glue.types.one_input
    import capo_glue.types.prob
    import capo_glue.types.topk


class Spigot(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the transform node.</p>"""
    inputs: "capo_glue.types.one_input.OneInput"
    """<p>The data inputs identified by their node names.</p>"""
    path: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>A path in Amazon S3 where the transform will write a subset of records from the dataset to a JSON file in an Amazon S3 bucket.</p>"""
    topk: NotRequired["capo_glue.types.topk.Topk"]
    """<p>Specifies a number of records to write starting from the beginning of the dataset.</p>"""
    prob: NotRequired["capo_glue.types.prob.Prob"]
    """<p>The probability (a decimal value with a maximum value of 1) of picking any given record. A value of 1 indicates that each row read from the dataset should be included in the sample output.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Spigot) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.one_input

    out["Inputs"] = capo_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    out["Path"] = value["path"]
    if "topk" in value:
        out["Topk"] = value["topk"]
    if "prob" in value:
        out["Prob"] = (
            "NaN"
            if value["prob"] != value["prob"]
            else "Infinity"
            if value["prob"] == float("inf")
            else "-Infinity"
            if value["prob"] == float("-inf")
            else value["prob"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Spigot:
    out: Spigot = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Inputs") is not None:
        import capo_glue.types.one_input

        out["inputs"] = capo_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        out["inputs"] = []
    if data.get("Path") is not None:
        out["path"] = data["Path"]
    else:
        out["path"] = ""
    if data.get("Topk") is not None:
        out["topk"] = data["Topk"]
    if data.get("Prob") is not None:
        out["prob"] = float(data["Prob"])
    return out
