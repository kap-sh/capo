"""Generated from Smithy shape ``com.amazonaws.frauddetector#BatchGetVariableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.name_list


class BatchGetVariableRequest(TypedDict, closed=True):
    names: "capo_frauddetector.types.name_list.NameList"
    """<p>The list of variable names to get.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetVariableRequest) -> dict:
    out: dict = {}
    import capo_frauddetector.types.name_list

    out["names"] = capo_frauddetector.types.name_list.serialize_aws_json_1_1(
        value["names"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetVariableRequest:
    out: BatchGetVariableRequest = {}  # type: ignore[typeddict-item]
    if data.get("names") is not None:
        import capo_frauddetector.types.name_list

        out["names"] = capo_frauddetector.types.name_list.deserialize_aws_json_1_1(
            data["names"]
        )
    else:
        out["names"] = []
    return out
