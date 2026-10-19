"""Generated from Smithy shape ``com.amazonaws.proton#ListServiceInstanceOutputsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.empty_next_token
    import capo_proton.types.outputs_list


class ListServiceInstanceOutputsOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_proton.types.empty_next_token.EmptyNextToken"]
    """<p>A token that indicates the location of the next output in the array of outputs, after the current requested list of outputs.</p>"""
    outputs: "capo_proton.types.outputs_list.OutputsList"
    """<p>An array of service instance Infrastructure as Code (IaC) outputs.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListServiceInstanceOutputsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_proton.types.outputs_list

    out["outputs"] = capo_proton.types.outputs_list.serialize_aws_json_1_0(
        value["outputs"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListServiceInstanceOutputsOutput:
    out: ListServiceInstanceOutputsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("outputs") is not None:
        import capo_proton.types.outputs_list

        out["outputs"] = capo_proton.types.outputs_list.deserialize_aws_json_1_0(
            data["outputs"]
        )
    else:
        out["outputs"] = []
    return out


def redact_sensitive(value: ListServiceInstanceOutputsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "outputs" in value:
        import capo_proton.types.outputs_list

        out["outputs"] = capo_proton.types.outputs_list.redact_sensitive(
            value["outputs"]
        )
    return out
